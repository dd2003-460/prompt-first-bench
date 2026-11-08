#!/usr/bin/env python3
"""S5: 完整 pfb 多步管道臂 — 分解 → 逐节点[搜索→逻辑校验→外部核验] loop → 封闭推理。

设计 (2026-11-08 成璐指令): "pfb本来就应该完整跑，直接在无泄漏状态跑" +
"分解的时候也查-逻辑-外信息逐个校验" + "全查-校验-再查这样loop循环，
最后验证好事实之后的分解和封闭推理才是有效的"。

与现有臂的区别:
  S0/A3/A4/S3 = 单轮 one-shot (S3 的"交叉核验"是 prompt 指令, 模型自说自话)
  S5          = 真·多步管道: harness 层真实执行检索 (research_hook/ego-browser),
                每个关键事实节点独立发起 LLM 调用做逻辑校验+外部核验,
                未通过校验的节点回炉重查 (≤K 轮), 全部收敛后才做封闭推理。
                这是生产 stage 外包模式的 pfb 化: 文件接口改成 JSON 记录,
                每步留痕可审计。

无泄漏: 各阶段 prompt 只喂题面+上一阶段产物, judge/gold 不进任何生成 prompt;
最终打分用 s8b_pilot.judge (gold 要点覆盖), 与 S0-A4 同一口径可比。

管道 (per rep):
  P1 decompose : 拆出 ≤N 个关键事实/前提节点 (编号 N1..NK), 每个附支撑它的结论
  P2 search    : 对每个节点调 research_hook(节点查询词) → 来源包 (arXiv API via ego-browser)
  P3 verify    : 每节点一次 LLM 调用: 逻辑自洽检查 + 对照来源核验 → status ∈ {verified, degraded, failed}
                 failed → 重查 (换查询词, ≤K 轮); 仍失败 → [待核验] 降级
  P4 synthesize: 基于已验证事实集做封闭推理, 输出最终答案 (未验证节点显式标注)
  J  judge     : gold 要点覆盖打分 (与 S0-A4 同口径)

Usage:
    python3 s5_pipeline.py --qs nat,soc --reps 2 --out runs-s5 --dry-run
    python3 s5_pipeline.py --qs nat --reps 1 --out runs-s5   # 冒烟
    python3 s5_pipeline.py --qs nat,soc --reps 500 --out runs-prod-s5  # 量产 (接在主 run 后)
"""
import argparse, json, os, random, re, sys, time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ablation_harness import call_llm, LLM_MODEL
from s8b_pilot import build_prompt, judge, QUESTIONS
from judge_v2_depth import score_run
from research_hook import research_hook, ResearchHookUnavailable

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_NODES = 8      # 每 rep 最多核验的关键事实节点数
MAX_ROUNDS = 2     # 每节点最大重查轮数 (含首轮)
SEARCH_PER_NODE = 4  # 每节点注入的来源上限

# ── 阶段 prompt ────────────────────────────────────────────────────────
P1_DECOMPOSE = (
    "你是严谨的研究员。下面是一道待解问题。你的任务不是回答问题本身，而是把它拆解成"
    "回答所依赖的关键事实/前提节点。\n\n"
    "要求：\n"
    "1. 列出回答该问题必须成立或必须取值的 3-8 个关键事实/前提（如物理常数、经验规律、"
    "统计分布性质、工程惯例、理论公式适用条件）；\n"
    "2. 每个节点给一个编号（N1, N2, ...）、一句话陈述、以及它支撑问题的哪个子问（a/b/c）；\n"
    "3. 为每个节点写一条英文检索词（用于后续联网核验，具体到该事实本身，不要写成整道题）；\n"
    "4. 不要把「计算步骤」当节点——节点是事实/前提，不是推导过程；\n"
    "5. 只输出 JSON，格式：{{\"nodes\": [{{\"id\": \"N1\", \"claim\": \"...\", \"supports\": \"a\",\n"
    "    \"search_query\": \"english query for this specific fact\"}}, ...]}}\n\n"
    "【问题】\n{question}\n"
)

P3_VERIFY = (
    "你是事实核验员。针对下面这个关键事实节点，执行两步检查：\n\n"
    "【第一步 — 逻辑校验】该陈述在逻辑上是否自洽？量纲/量级是否合理？"
    "是否存在内部矛盾或明显违背基本物理/经济直觉的地方？\n\n"
    "【第二步 — 外部核验】先判断参考来源与该事实是否相关（主题/领域是否匹配），再在相关性成立时判断是否有明确支持。"
    "支持强度：直接支持 / 间接支持 / 无关 / 矛盾。注意：若全部来源均与该事实主题无关，外部核验记为「无可用外部证据」——"
    "此时只能依据第一步逻辑校验判定，不得因来源不相关而判 failed，也不得把「来源无关」写成「来源支持」。\n\n"
    "【判定规则】\n"
    "- verified: 逻辑自洽，且（至少一个来源直接支持，或该事实可从第一性原理/题面条件推出且无来源与之矛盾）；\n"
    "- degraded: 逻辑自洽但只有间接支持、无法定量确认 → 保留但降级为定性表述；\n"
    "- failed: 仅当该陈述与参考来源明确矛盾，或存在硬逻辑错误（量纲错/内部矛盾）时才判 failed。\n"
    "注意：来源未覆盖 ≠ 错误。数学性质、统计规律这类可从第一性原理推出的事实，"
    "若逻辑校验通过且无来源与之矛盾，应判 verified 并在 evidence 里注明「逻辑推导成立，来源未直接覆盖」；"
    "不要仅因检索结果不相关就判 failed。\n\n"
    "【关键事实节点】\n{node_id}: {claim}\n\n"
    "【参考来源】\n{sources_block}\n\n"
    "只输出 JSON：{{\"status\": \"verified|degraded|failed\", \"logic_ok\": true/false,\n"
    "\"evidence\": \"一句话说明依据（引用来源编号）\", \"corrected_claim\": \"若 failed/degraded，给出修正后的表述；否则空字符串\"}}"
)

P4_SYNTHESIZE = (
    "你是严谨的研究员。下面是一道问题和一组已经过核验的事实节点表。"
    "请基于这些事实做封闭推理，给出最终答案。\n\n"
    "要求：\n"
    "1. 只使用事实表中 status 为 verified 的节点作为定量依据；degraded 节点只能定性引用并说明局限；\n"
    "2. failed 或缺失的节点不得假设其值——显式写出「缺 X 导致 Y 无法定量」，给出区间而非点估计；\n"
    "3. 先给结论，再给因果链，不跳步；每个数字写出量纲和口径；\n"
    "4. 区分「凭记忆的」和「刚查到的」：在正文中每出现一个关键数字/事实，紧跟其后用括号标注其状态——"
    "（已核验：来自 verified 节点或来源直接支持）/（推导：由题面条件+verified 节点推出）/（凭记忆：模型先验，未获外部验证）。"
    "要求：正文中至少出现 3 处此类括号标注；凡标注为（凭记忆）的数值必须降置信表述（如「约」「估计」）。\n"
    "5. 最后单独一节「事实核验摘要」：列出你实际使用了哪些节点、各自状态、哪些结论因此受限。\n\n"
    "【问题】\n{question}\n\n"
    "【已核验事实节点表】\n{fact_table}\n"
)


def _perturb():
    return "".join(random.choice(["\u200b", "\u200c", " ", "\u200d"]) for _ in range(4))


def _extract_json(text):
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


def decompose(question):
    """P1: 拆出关键事实节点。返回 nodes 列表。"""
    prompt = P1_DECOMPOSE.format(question=question) + _perturb()
    out, _ = call_llm(prompt, max_tokens=2500, temperature=0.7, top_p=0.95)
    d = _extract_json(out or "") or {}
    nodes = d.get("nodes") or []
    nodes = [n for n in nodes if isinstance(n, dict) and n.get("claim")]
    for i, n in enumerate(nodes[:MAX_NODES], 1):
        n.setdefault("id", f"N{i}")
    return nodes[:MAX_NODES], out


def search_node(node):
    """P2: 对该节点做真实联网检索 (arXiv API via ego-browser)。失败降级为空。"""
    q = node.get("search_query") or node["claim"]
    try:
        srcs = research_hook("s5-node", q, max_results=SEARCH_PER_NODE)
        return srcs, None
    except ResearchHookUnavailable as e:
        return [], str(e)
    except Exception as e:
        return [], str(e)


def sources_block(srcs):
    if not srcs:
        return "(本轮检索无可用来源 — 全部通道失败)"
    lines = []
    for i, s in enumerate(srcs, 1):
        lines.append(f"[{i}] {s.get('title','?')}\n    URL: {s.get('url','?')}\n    摘要: {s.get('snippet','')[:400]}")
    return "\n".join(lines)


def verify_node(node, srcs):
    """P3: 单节点逻辑+外部核验。返回 (status, evidence, corrected_claim)。"""
    prompt = P3_VERIFY.format(
        node_id=node["id"], claim=node["claim"],
        sources_block=sources_block(srcs)) + _perturb()
    out, _ = call_llm(prompt, max_tokens=1200, temperature=0.7, top_p=0.95)
    d = _extract_json(out or "") or {}
    status = d.get("status")
    if status not in ("verified", "degraded", "failed"):
        status = "degraded"  # 解析失败按保守档处理
    return status, d.get("evidence", ""), d.get("corrected_claim", ""), out


def run_one(qid, rep, dry_run=False):
    tag = f"S5-{qid}-r{rep}"
    question = QUESTIONS[qid]
    rec = {"tag": tag, "arm": "S5", "qid": qid, "rep": rep,
           "model": LLM_MODEL, "ts": datetime.now(timezone.utc).isoformat(),
           "stages": {}}
    if dry_run:
        print(f"[dry] {tag}: pipeline ready (P1 decompose → P2 search×N → P3 verify×N → P4 synthesize)")
        return rec
    t0 = time.time()
    # P1
    nodes, p1_raw = decompose(question)
    rec["stages"]["p1_decompose"] = {"nodes": len(nodes), "raw": p1_raw[:3000]}
    print(f"  [{tag}] P1: {len(nodes)} nodes", flush=True)
    if not nodes:
        rec["error"] = "decompose returned no nodes"
        return rec
    # P2+P3 per node (with re-search loop)
    facts = []
    for node in nodes:
        node_rec = {"id": node["id"], "claim": node["claim"],
                    "search_query": node.get("search_query", "")}
        rounds = []
        for rnd in range(1, MAX_ROUNDS + 1):
            srcs, err = search_node(node)
            status, evidence, corrected, raw = verify_node(node, srcs)
            rounds.append({"round": rnd, "n_sources": len(srcs), "search_err": err,
                           "status": status, "evidence": evidence})
            node_rec.update(status=status, evidence=evidence,
                            corrected_claim=corrected or node["claim"])
            if status != "failed":
                break
            # failed → 用核验员给出的修正表述重查 (corrected_claim 是核验员对错误的具体定位,
            # 比拼接关键词更接近事实本身; 空则退回原 claim)
            new_q = corrected.strip() or node["claim"]
            node["search_query"] = new_q[:150]
            print(f"  [{tag}] {node['id']} round {rnd} FAILED → re-search with corrected claim", flush=True)
        node_rec["rounds"] = rounds
        if node_rec["status"] == "failed":
            node_rec["status"] = "unverified"  # 重查耗尽 → 降级 [待核验]
        facts.append(node_rec)
    rec["stages"]["p2p3_nodes"] = facts
    n_v = sum(1 for f in facts if f["status"] == "verified")
    print(f"  [{tag}] P2/P3 done: {n_v}/{len(facts)} verified ({time.time()-t0:.0f}s)", flush=True)
    # P4
    table = "\n".join(
        f"{f['id']}: {f['corrected_claim']}  [status={f['status']}; evidence: {f['evidence'][:120]}]"
        for f in facts)
    prompt = P4_SYNTHESIZE.format(question=question, fact_table=table) + _perturb()
    answer, usage = call_llm(prompt, max_tokens=8000, temperature=0.7, top_p=0.95)
    rec["answer"] = answer or ""
    rec["usage"] = usage
    rec["wall_s"] = round(time.time() - t0, 1)
    rec["n_verified"] = n_v
    rec["n_nodes"] = len(facts)
    # Judge (binary coverage, same rubric as S0-A4 — comparable across arms)
    j = judge(qid, answer)
    rec["judge"] = j
    cov = round(j.get("coverage") or 0, 3)
    # Depth-continuous score (judge_v2_depth, k·ln(k+1) weighting) — finer resolution
    try:
        dv = score_run(qid, answer)
        rec["depth_score"] = dv.get("overall")
    except Exception as e:
        rec["depth_score"] = None
        print(f"  [{tag}] depth-score failed: {e}", flush=True)
    print(f"  [{tag}] P4+J: cov={cov} depth={rec['depth_score']} unverified={j.get('unverified_count')} wall={rec['wall_s']}s", flush=True)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--qs", default="nat,soc")
    ap.add_argument("--reps", type=int, default=2)
    ap.add_argument("--out", default="runs-s5")
    ap.add_argument("--start-rep", type=int, default=1)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    qs = args.qs.split(",")
    os.makedirs(args.out, exist_ok=True)
    out_f = open(f"{args.out}/run.log", "a")
    t0 = time.time()
    total = len(qs) * max(0, args.reps - args.start_rep + 1)
    done = 0
    for qid in qs:
        for rep in range(args.start_rep, args.reps + 1):
            tag = f"S5-{qid}-r{rep}"
            fp = f"{args.out}/{tag}.json"
            if os.path.exists(fp):
                done += 1
                continue
            r = run_one(qid, rep, args.dry_run)
            with open(fp, "w") as f:
                json.dump(r, f, ensure_ascii=False, indent=1)
            done += 1
            line = {"tag": tag, "ok": "error" not in r,
                    "cov": round((r.get("judge") or {}).get("coverage") or 0, 3),
                    "depth": r.get("depth_score"),
                    "n_verified": r.get("n_verified"), "wall_s": r.get("wall_s")}
            print(f"[{done}/{total}] {line} ({time.time()-t0:.0f}s)", flush=True)
            out_f.write(json.dumps(line, ensure_ascii=False) + "\n"); out_f.flush()
    print("S5 PIPELINE DONE", flush=True)


if __name__ == "__main__":
    random.seed()
    main()