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
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ablation_harness import call_llm, LLM_MODEL
from s8b_pilot import build_prompt, judge, QUESTIONS
from judge_v2_depth import score_run
from research_hook import research_hook, ResearchHookUnavailable

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_NODES = 25      # 每 rep 最多核验的关键事实节点数
MAX_ROUNDS = 2     # 每节点最大重查轮数 (含首轮)
SEARCH_PER_NODE = 4  # 每节点注入的来源上限

# ── 阶段 prompt ────────────────────────────────────────────────────────
P1_DECOMPOSE = (
    "你是严谨的研究员。下面是一道待解问题。你的任务不是回答问题本身，而是把它逐层拆解成"
    "回答所依赖的完整决策树。\n\n"
    "【逐层展开规则】\n"
    "1. 先识别顶层决策公式或目标函数（如成本公式、约束条件、评分标准），这是第 1 层；\n"
    "2. 对第 1 层的每个因子/参数，展开为第 2 层子节点——具体到需要查什么数字、什么公式、什么经验值；\n"
    "3. 对第 2 层中涉及复合量或可分解量的节点，继续展开为第 3 层（如 TCO → 摊销+电费+故障损耗；"
    "吞吐量 → prefill 算力瓶颈 + decode 带宽瓶颈）；\n"
    "4. 如果某节点的取值会影响其他节点的判断（交互效应），单独列出 SHARED 节点说明耦合关系；\n"
    "5. 不要停在'这个因素很重要'——必须拆到可以直接检索验证的具体事实（一个数字、一个公式、一个阈值）。\n\n"
    "【节点数量】\n"
    "- 简单问题：8-15 个节点\n"
    "- 复杂多因子问题（如选卡、架构设计、成本分析）：15-25 个节点\n"
    "- 宁多勿少：漏掉的节点 = 答案里缺的维度，比多查几个无用节点代价大得多\n\n"
    "【格式要求】\n"
    "每个节点给：编号（N1, N2, ...）、一句话陈述（具体到可检索的事实）、层级标记（L1/L2/L3）、"
    "它支撑问题的哪个子问、一条英文检索词（具体到该事实本身）。\n"
    "只输出 JSON，格式：{{\"nodes\": [{{\"id\": \"N1\", \"claim\": \"...\", \"level\": \"L1\", "
    "\"supports\": \"a\", \"search_query\": \"english query\"}}, ...]}}\n\n"
    "【问题】\n{question}\n"
)

P15A_DIMENSIONS = (
    "你是研究问题分解专家。下面是一道待解问题。"
    "你的唯一任务是：从问题文本本身出发，列出回答它必须覆盖的所有顶层维度。\n\n"
    "【规则】\n"
    "- 只看问题文本，不参考任何外部框架或常识性检查清单；\n"
    "- 每个维度用一句话描述（只陈述该维度是什么，不举具体例子）；\n"
    "- 维度之间必须正交——一个维度的信息不能由其他维度推出；\n"
    "- 通常 4-8 个维度，宁少勿多。\n\n"
    "【格式要求】只输出 JSON：{{\"dimensions\": [\"...\", ...]}}\n\n"
    "【问题】\n{question}\n"
)

P15B_GAP_FILL = (
    "你是研究覆盖度审查员。下面是一道问题、一组顶层维度、和一份已生成的事实节点列表。"
    "对照维度列表，找出哪些维度没有被节点充分覆盖，为缺失维度生成补充节点。\n\n"
    "【判断标准】\n"
    "- 某维度有 ≥2 个具体可检索的节点 → 视为已覆盖；\n"
    "- 某维度只有 0-1 个节点且停留在定性层面 → 视为缺失，需补 L2/L3 节点；\n"
    "- 补充节点必须具体到可检索的事实（一个数字、一个公式、一个阈值），带英文检索词。\n\n"
    "【规则】\n"
    "- 只补缺失维度，不重复已有节点；\n"
    "- 如果所有维度都已充分覆盖，new_nodes 输出空列表；\n"
    "- 补充节点数量通常 3-10 个。\n\n"
    "【格式要求】只输出 JSON：{{\"missing_dimensions\": [\"...\", ...], \"new_nodes\": "
    "[{{\"id\": \"NXX\", \"claim\": \"...\", \"level\": \"L2|L3\", "
    "\"supports\": \"...\", \"search_query\": \"english query\"}}, ...]}}\n\n"
    "【问题】\n{question}\n\n"
    "【顶层维度】\n{dimensions}\n\n"
    "【已有节点】\n{existing_nodes}\n"
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
    "4. 溯源标注（硬性格式要求）：正文中每个关键数字/事实，紧跟其后加一个方括号标签，只允许三种写法：[已核验]、[推导]、[凭记忆]。"
"例如：LRU 字节命中率约为 78% [推导]；典型 CDN 缓存容量约 10TB [凭记忆]。自检：数一下正文里带百分号/倍数/容量单位的数字共几个，"
"标签总数不得少于该数字个数的三分之一；标 [凭记忆] 的数值必须配降置信词（约/估计/通常）。禁止只在末尾摘要表写状态而不给正文数字打标签。\n"
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


def decompose(question, max_retries=2):
    """P1: 拆出关键事实节点。返回 nodes 列表。JSON 解析失败时 retry。"""
    last_raw = ""
    for attempt in range(max_retries + 1):
        prompt = P1_DECOMPOSE.format(question=question) + _perturb()
        out, _ = call_llm(prompt, max_tokens=4096, temperature=0.7, top_p=0.95)
        last_raw = out or ""
        d = _extract_json(last_raw) or {}
        nodes = d.get("nodes") or []
        nodes = [n for n in nodes if isinstance(n, dict) and n.get("claim")]
        if nodes:
            for i, n in enumerate(nodes[:MAX_NODES], 1):
                n.setdefault("id", f"N{i}")
            return nodes[:MAX_NODES], last_raw
        print(f"  [decompose] attempt {attempt+1}: no nodes parsed, retrying...", flush=True)
    return [], last_raw


def gap_check(question, existing_nodes):
    """P1.5: 两轮覆盖度审查。A=独立列维度（不看已有节点），B=对照补缺。"""
    # P15A: 独立识别顶层维度（不受已有节点锚定）
    prompt_a = P15A_DIMENSIONS.format(question=question) + _perturb()
    try:
        out_a, _ = call_llm(prompt_a, max_tokens=2048, temperature=0.7, top_p=0.95)
        d_a = _extract_json(out_a or "") or {}
        dimensions = d_a.get("dimensions") or []
    except Exception as e:
        print(f"  [gap_check A] error: {e}", flush=True)
        return [], [], ""
    if not dimensions:
        print(f"  [gap_check A] no dimensions identified", flush=True)
        return [], [], out_a or ""
    print(f"  [gap_check A] {len(dimensions)} dimensions: {' | '.join(d[:30] for d in dimensions[:5])}...", flush=True)

    # P15B: 对照维度列表补缺失节点
    node_lines = "\n".join(
        f"{n['id']} [{n.get('level','?')}]: {n['claim']}" for n in existing_nodes)
    dim_lines = "\n".join(f"- {d}" for d in dimensions)
    prompt_b = P15B_GAP_FILL.format(
        question=question, dimensions=dim_lines, existing_nodes=node_lines) + _perturb()
    try:
        out_b, _ = call_llm(prompt_b, max_tokens=4096, temperature=0.7, top_p=0.95)
        d_b = _extract_json(out_b or "") or {}
        new_nodes = [n for n in (d_b.get("new_nodes") or [])
                     if isinstance(n, dict) and n.get("claim")]
        missing = d_b.get("missing_dimensions") or []
        return new_nodes, missing, out_b
    except Exception as e:
        print(f"  [gap_check B] error: {e}", flush=True)
        return [], [], ""


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


_LABELS = ("[已核验]", "[推导]", "[凭记忆]")


def _label_stats(ans):
    """正文溯源标注统计：标签数 / 关键数字数 / 覆盖率。"""
    n_labels = sum(ans.count(p) for p in _LABELS)
    import re as _re
    n_nums = len(_re.findall(r'\d+\.?\d*\s*(%|个百分点|百分点|倍|ms|MB|GB|TB)', ans))
    return {"n_labels": n_labels, "n_numeric_claims": n_nums,
            "label_coverage": round(n_labels / max(n_nums, 1), 2)}


def _run_p1p2p3(rec, tag, question):
    """P1 decompose + P2 search + P3 verify. Sets stages.p2p3_nodes, n_verified, n_nodes."""
    t0 = time.time()
    # P1
    nodes, p1_raw = decompose(question)
    rec["stages"]["p1_decompose"] = {"nodes": len(nodes), "raw": p1_raw[:3000]}
    print(f"  [{tag}] P1: {len(nodes)} nodes", flush=True)
    if not nodes:
        rec["error"] = "decompose returned no nodes"
        rec["n_nodes"], rec["n_verified"] = 0, 0
        rec["stages"]["p2p3_nodes"] = []
        return rec
    # P1.5: gap check — 覆盖度审查，补缺失维度
    new_nodes, missing_dims, p15_raw = gap_check(question, nodes)
    if new_nodes:
        start_id = len(nodes) + 1
        for i, n in enumerate(new_nodes):
            n.setdefault("id", f"N{start_id + i}")
        nodes.extend(new_nodes[:MAX_NODES - len(nodes)])
        print(f"  [{tag}] P1.5: +{len(new_nodes)} nodes (missing: {', '.join(missing_dims[:4])}) → total {len(nodes)}", flush=True)
    else:
        print(f"  [{tag}] P1.5: no gaps found", flush=True)
    rec["stages"]["p15_gap_check"] = {"added": len(new_nodes), "missing": missing_dims, "raw": p15_raw[:2000]}
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
    rec["n_nodes"], rec["n_verified"] = len(facts), n_v
    print(f"  [{tag}] P2/P3 done: {n_v}/{len(facts)} verified", flush=True)


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
    if rec.get("_fact_table_override") is not None:
        facts = rec["_fact_table_override"]
        n_v = sum(1 for f in facts if f["status"] == "verified")
        rec["stages"]["p2p3_nodes"] = facts
        rec["n_nodes"], rec["n_verified"] = len(facts), n_v
        print(f"  [{tag}] using pre-built fact table ({len(facts)} nodes, {n_v} verified)", flush=True)
    else:
        _run_p1p2p3(rec, tag, question)
        facts = rec["stages"]["p2p3_nodes"]
        n_v = rec["n_verified"]
    # P4
    table = "\n".join(
        f"{f['id']}: {f['corrected_claim']}  [status={f['status']}; evidence: {f['evidence'][:120]}]"
        for f in facts)
    prompt = P4_SYNTHESIZE.format(question=question, fact_table=table) + _perturb()
    answer, usage = call_llm(prompt, max_tokens=8000, temperature=0.7, top_p=0.95)
    rec["answer"] = answer or ""
    rec["label_stats"] = _label_stats(answer or "")
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
    print(f"  [{tag}] P4+J: cov={cov} depth={rec['depth_score']} labels={rec['label_stats']['n_labels']}/{rec['label_stats']['n_numeric_claims']} nums unverified={j.get('unverified_count')} wall={rec['wall_s']}s", flush=True)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--qs", default="nat,soc")
    ap.add_argument("--reps", type=int, default=2)
    ap.add_argument("--out", default="runs-s5")
    ap.add_argument("--start-rep", type=int, default=1)
    ap.add_argument("--workers", type=int, default=1,
                    help="concurrent workers (default 1; use 2-3 for parallel)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    qs = args.qs.split(",")
    os.makedirs(args.out, exist_ok=True)
    out_f = open(f"{args.out}/run.log", "a")
    t0 = time.time()

    # Build work list: (qid, rep, tag, fp)
    tasks = []
    for qid in qs:
        for rep in range(args.start_rep, args.reps + 1):
            tag = f"S5-{qid}-r{rep}"
            fp = f"{args.out}/{tag}.json"
            if os.path.exists(fp):
                continue  # skip completed
            tasks.append((qid, rep, tag, fp))

    total = len(tasks)
    print(f"S5 PIPELINE: {total} tasks, {args.workers} workers, qs={qs}", flush=True)
    if total == 0:
        print("S5 PIPELINE DONE (all cached)", flush=True)
        return

    done = 0
    lock = __import__("threading").Lock()

    def _worker(qid, rep, tag, fp):
        nonlocal done
        r = run_one(qid, rep, args.dry_run)
        with open(fp, "w") as f:
            json.dump(r, f, ensure_ascii=False, indent=1)
        with lock:
            done += 1
            line = {"tag": tag, "ok": "error" not in r,
                    "cov": round((r.get("judge") or {}).get("coverage") or 0, 3),
                    "depth": r.get("depth_score"),
                    "n_verified": r.get("n_verified"), "wall_s": r.get("wall_s")}
            print(f"[{done}/{total}] {line} ({time.time()-t0:.0f}s)", flush=True)
            out_f.write(json.dumps(line, ensure_ascii=False) + "\n"); out_f.flush()

    if args.workers <= 1:
        # serial path (original behavior)
        for qid, rep, tag, fp in tasks:
            _worker(qid, rep, tag, fp)
    else:
        # parallel path
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = {pool.submit(_worker, qid, rep, tag, fp): tag
                       for qid, rep, tag, fp in tasks}
            for fut in as_completed(futures):
                try:
                    fut.result()
                except Exception as e:
                    tag = futures[fut]
                    print(f"ERROR {tag}: {e}", flush=True)
                    with lock:
                        done += 1
    print("S5 PIPELINE DONE", flush=True)


if __name__ == "__main__":
    random.seed()
    main()