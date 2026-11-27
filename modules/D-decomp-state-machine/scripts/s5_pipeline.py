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
import argparse, json, math, os, random, re, sys, time
from prompts import P1_L1_SKELETON, P1_DECOMPOSE, P15A_DIMENSIONS, P15B_GAP_FILL, P3_VERIFY, P4_SYNTHESIZE, P1_L1_TEXT, P1_L1_MINIMAL, P1_L1_METHOD, P1_L1_METHOD_CHALLENGE, P1H_INDEX
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ablation_harness import call_llm, LLM_MODEL
from s8b_pilot import build_prompt, judge, QUESTIONS
from judge_v2_depth import score_run
from research_hook import research_hook, ResearchHookUnavailable

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_NODES = 60  # safety valve only — real stopping rule is the objective function, not this cap
# BUDGET_RETRIEVAL removed 2026-11-08 (user: no cap on search). _budget_used is now a pure counter for diagnostics.
# breadth-vs-depth trade-off weight in the decomposition objective:
#   S_alpha(T) = sum_n [ n*ln(k_n) + alpha * k_n*ln(n) ]
# alpha=0 -> pure depth-mining; alpha=1 -> symmetric depth/breadth; default 0.5
ALPHA_BREADTH = 0.5
_budget_used = {"n": 0}

def _budget_reset():
    _budget_used["n"] = 0

def _budget_take():
    """Count retrieval calls (diagnostic only); NEVER blocks — user directive 2026-11-08: no budget cap on search/ego-browser."""
    _budget_used["n"] += 1
    return True
MAX_ROUNDS = 2     # 每节点最大重查轮数 (含首轮)
SEARCH_PER_NODE = 4  # 每节点注入的来源上限

# ── 阶段 prompt ────────────────────────────────────────────────────────


def _perturb():
    return "".join(random.choice(["\u200b", "\u200c", " ", "\u200d"]) for _ in range(4))


def _extract_json(text):
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None
    s = m.group(0)
    # 从前往后找第一个能解析成功的 { ... } 区间。
    # 旧实现只试一次全量贪婪匹配：模型输出被 max_tokens 截断时 JSON 尾部残缺，
    # 整个 parse 失败 → decompose 返回 0 节点（v13 r5 事故）。
    # 这里退而求其次：截取到最后一个完整对象（以 "}" 结尾且前面是 "," 或 "[" 的边界），
    # 把残缺尾部的半截 node 丢弃，保住已完整的 nodes。
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        pass
    # 截断修复：找到最后一个完整闭合的对象边界，补上缺失的 "]}"
    for end in range(len(s), max(0, len(s) - 2000), -1):
        if s[end - 1] == "}":
            candidate = s[:end].rstrip().rstrip(",") + "\n  ]\n}"
            try:
                return json.loads(candidate)
            except json.JSONDecodeError:
                continue
    return None


def decompose(question, max_retries=3, unlimited=False):
    """P1: 拆出关键事实节点。返回 nodes 列表。JSON 解析失败时 retry（降温度）。

    v2 (2026-11-09): r5 事故根因不是 max_tokens 截断（usage out=2128 < 8000），
    是模型在 ~2100 token 处主动停笔、JSON 停在半截 node。旧实现 parse 失败直接
    放弃整份输出（丢掉已完整的 N1-N10）。现在：_extract_json 有截断兜底，
    只要解出 ≥1 个完整 node 就接受；全空才 retry（retry 用更低温度减少跑飞）。
    """
    last_raw = ""
    for attempt in range(max_retries + 1):
        temp = 0.7 if attempt == 0 else 0.3
        prompt = P1_DECOMPOSE.format(question=question, alpha=ALPHA_BREADTH) + _perturb()
        out, _ = call_llm(prompt, max_tokens=8000, temperature=temp, top_p=0.95)
        last_raw = out or ""
        d = _extract_json(last_raw) or {}
        nodes = d.get("nodes") or []
        nodes = [n for n in nodes if isinstance(n, dict) and n.get("claim")]
        if nodes:
            for i, n in enumerate(nodes[:MAX_NODES], 1):
                n.setdefault("id", f"N{i}")
                n.setdefault("source", "search")
            from collections import Counter as _C
            sc = _C(n.get("source", "?") for n in nodes)
            print(f"  [decompose] source mix: {dict(sc)}", flush=True)
            cap = len(nodes) if unlimited else MAX_NODES
            return nodes[:cap], last_raw
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


def search_node(node, qid="gpu"):
    """P2: 对该节点做真实联网检索 (arXiv API via ego-browser)。失败降级为空。
    given/knowledge 节点不触发检索（逻辑核验即可）；search 节点全部真实联网（无预算上限）。

    local_corpus 通道按题域启用：_LOCAL_CORPUS_DIRS 目前只有 D1-gpu-research 语料，
    对 nat/soc 题 grep 出的"命中"全是无关 GPU 文档，会污染 P3 核验（nat 100 reps
    evidence 里大量出现"参考来源[1]为GPU硬件规格...与该节点无关"）。
    2026-11-09: 非 gpu 题禁用该通道，其余通道不受影响。"""
    if node.get("source", "search") in ("given", "knowledge"):
        return [], None  # no retrieval needed — logic verification only
    _budget_take()  # counter only, never blocks
    q = node.get("search_query") or node["claim"]
    claim = node["claim"]
    # 2026-11-15: 中文 claim 优先用中文 query 查（英文 search_query 查 wiki
    # 返回英文条目，与中文 claim 完全无关——soc 106 节点 retrieval_sources 全空
    # 的根因）。DDG 中文实测能出好结果（搜狐/今日头条/知乎，含央行/CHFS 数据）。
    # 策略：claim 含中文 → 先用中文 claim 查；否则用原 query。
    # 两组都查，取结果更好的那组（数量多 + 来源类型多）。
    import re as _re
    has_chinese = bool(_re.search(r'[\u4e00-\u9fff]', claim))
    if has_chinese and q != claim:
        # 中文 claim：优先用中文来源（英文 wiki 条目与中文 claim 无关，
        # 数量多不代表质量好——soc 106 节点全空的根因）。
        # 中文来源为空时才用英文兜底。
        try:
            srcs_cn = research_hook("s5-node", claim, max_results=SEARCH_PER_NODE,
                                    enable_local=(qid == "gpu"))
        except Exception:
            srcs_cn = []
        if srcs_cn:
            return srcs_cn, None
        # 中文全空 → 英文兜底
        try:
            srcs_en = research_hook("s5-node", q, max_results=SEARCH_PER_NODE,
                                    enable_local=(qid == "gpu"))
            return srcs_en, None
        except Exception:
            return [], None
    else:
        try:
            srcs = research_hook("s5-node", q, max_results=SEARCH_PER_NODE,
                                 enable_local=(qid == "gpu"))
            return srcs, None
        except ResearchHookUnavailable as e:
            if has_chinese and q != claim:
                try:
                    srcs = research_hook("s5-node", claim, max_results=SEARCH_PER_NODE,
                                         enable_local=(qid == "gpu"))
                    return srcs, None
                except Exception:
                    pass
            return [], str(e)
        except Exception as e:
            if has_chinese and q != claim:
                try:
                    srcs = research_hook("s5-node", claim, max_results=SEARCH_PER_NODE,
                                         enable_local=(qid == "gpu"))
                    return srcs, None
                except Exception:
                    pass
            return [], str(e)


def sources_block(srcs):
    if not srcs:
        return "(本轮检索无可用来源 — 全部通道失败)"
    lines = []
    for i, s in enumerate(srcs, 1):
        lines.append(f"[{i}] {s.get('title','?')}\n    URL: {s.get('url','?')}\n    摘要: {s.get('snippet','')[:800]}")
    return "\n".join(lines)


def verify_node(node, srcs):
    """P3: 单节点逻辑+外部核验。返回 (status, evidence, corrected_claim)。

    D-质询（2026-11-16）：prompt 第一步改为反方质询，模型必须先把最强攻击点
    写进 challenge 字段再判定——攻击点成立且无法排除时降档。challenge 随
    evidence 落盘（前缀 [质询]），verify 记录可审计。"""
    prompt = P3_VERIFY.format(
        node_id=node["id"], claim=node["claim"],
        source=node.get("source", "search"),
        sources_block=sources_block(srcs)) + _perturb()
    # verify 是短结构化任务（JSON 输出），不需要内部推理——thinking 会把
    # budget 烧在 reasoning_content 上导致 content 为空。关掉后单请求 ~3s vs 20s+。
    out, _ = call_llm(prompt, max_tokens=1200, temperature=0, top_p=1.0, enable_thinking=False)
    d = _extract_json(out or "") or {}
    status = d.get("status")
    if status not in ("verified", "degraded", "failed"):
        status = "degraded"  # 解析失败按保守档处理
    ev = d.get("evidence", "")
    ch = d.get("challenge", "")
    if ch and ch != "无可信攻击点":
        ev = f"[质询]{ch} | {ev}"
    return status, ev, d.get("corrected_claim", ""), out


_LABELS = ("[已核验]", "[推导]", "[凭记忆]")


def _label_stats(ans):
    """正文溯源标注统计：标签数 / 关键数字数 / 覆盖率。"""
    n_labels = sum(ans.count(p) for p in _LABELS)
    import re as _re
    n_nums = len(_re.findall(r'\d+\.?\d*\s*(%|个百分点|百分点|倍|ms|MB|GB|TB)', ans))
    return {"n_labels": n_labels, "n_numeric_claims": n_nums,
            "label_coverage": round(n_labels / max(n_nums, 1), 2)}


# #31 消融臂 B（文字版目标函数）：与 P1_L1_SKELETON 唯一差异是第一步的表述形式——
# 公式版要求"可测要素 + 组合方式（乘积/加权和/比值）"，文字版只要求"用一段话说明
# 好答案的标准"。两臂其余约束（维度正交性、三边分类、禁下钻、JSON 格式）完全一致，
# 保证单变量对照。指标 = verified 率 + quotient 率 + gain 序列（n≥3 同题）。


# #31 消融臂 C（M 臂 · minimal，2026-11-13）：与 P1_L1_TEXT 唯一差异是第一步——
# M 臂不给任何要素提示（不要求写 80 字标准段），只给"完整、详尽、准确"三个字，
# 直接让模型导出顶层正交维度。其余约束（2b 三边分类、禁下钻、JSON 格式）与 F/T 完全一致。
# 意义：F→T 只测公式化程度；M 把信息量也降下来，才能分离形式效应 vs 信息量效应
# （见 tasks/B-pipeline-ablation/TASK-B08-t53-objective-form-ablation.md §3）。


# #31 消融臂 D（M1 · method persona，2026-11-15）：在 P1_L1_MINIMAL 基础上加一句
# 元规则——"遇到任何论断都会质疑"。不展开成 7 条，保持核心信号不被稀释。
# 来源：成璐原话"其实我的习惯是遇到任何论断都会质疑"。

# #31 消融臂 E（M2 · method + 反方质询，2026-11-15）：M1 的一句元规则 + 一个结构步骤——
# 拆完维度后先列出"这个分解可能错在哪"（反方质询），再输出最终 JSON。


def _sa_tree(nodes):
    """S_α 树形得分（与 P1 prompt 中同一公式，harness 侧实现）：
    S = Σₙ [ n·ln(kₙ) + α·kₙ·ln(n) ]，kₙ = 第 n 层节点数。
    同时返回每层 kₙ 供状态机日志用。"""
    from collections import Counter as _C
    lv = _C(int((n.get("level") or "L?").lstrip("L")) for n in nodes
            if str(n.get("level") or "").startswith("L") and str(n.get("level")).lstrip("L").isdigit())
    s = 0.0
    per_layer = {}
    for n, k in sorted(lv.items()):
        contrib = n * math.log(k) + ALPHA_BREADTH * k * math.log(n)
        s += contrib
        per_layer[n] = {"k": k, "contrib": round(contrib, 3)}
    return round(s, 4), per_layer


def decompose_explore(question, max_rounds=8, budget_nodes=40, per_layer_cap=6, qid="gpu"):
    """P1e: 探索式分解 — 状态机主循环（无限回退，目标函数驱动停止）。

    每轮：decompose(整题 + 已确认事实) → gap_check(补广度) → 对未核验的 search
    节点做一轮 P2/P3 核验 → verified/degraded 节点作为【已确认事实】注入下一轮。
    回退是无限的——没有固定轮数上限；停止判据全部来自边际收益/行为证据：
      R1 饱和：本轮新增节点 = 0（模型找不到新东西可拆 = 定义级粒度自然停）
      R2 预算：累计节点 ≥ budget_nodes —— **软约束，不停止**。
         触发"该做层级压缩"信号（把深层叶子折叠成中间层摘要），树继续长。
         general 超级工程拆到定义级粒度节点数可达千级，硬上限会砍掉合法深度。
      R3 停滞：连续 2 轮 S_α 无增长（拆出来的都是同义复述）
    **层内限流（per-layer cap）**：每层每轮最多吸收 per_layer_cap 个新节点，
    超出的留到下一轮——防止深层同层数量爆炸导致单轮 token 溢出 / 注意力稀释。
    被截断的层会在日志里标记 capped=True，下一轮继续消化。
    返回 (nodes_all, rounds_log)，rounds_log 含每轮的 S_α、新增节点、停止原因。
    """
    confirmed = []          # [(id, claim, status)] 注入下一轮的已确认事实
    nodes_all = []
    seen_ids = set()
    rounds_log = []
    prev_sa = None
    stagnant = 0            # 连续无增长计数
    stop = None             # 停止原因（R1/R3/R4），循环内设置
    rnd = 0
    while True:
        rnd += 1
        # 防御性硬上限（v16.3 bug #5 修复）：R2 改软约束后循环真的无限了，
        # gpu 域 R1 迟迟不触发导致单 rep 失控。max_rounds 管"别失控"，
        # budget_nodes/compress_flag 管"该压缩了"，两者语义正交。
        if max_rounds and rnd > max_rounds:
            stop = "R4-max-rounds"
            break
        q_ext = question
        if confirmed:
            block = "\n".join(f"- {i}: {c} [{s}]" for i, c, s in confirmed[-budget_nodes:])
            q_ext += ("\n\n【已确认事实（前几轮分解+核验的结果，直接作为 given/knowledge 使用，"
                      "不要重复拆解它们；你的任务是找出尚未覆盖的维度并继续向深层展开）】\n" + block)
        nodes, raw = decompose(q_ext)
        new_nodes = [n for n in nodes if n["id"] not in seen_ids]
        seen_ids.update(n["id"] for n in nodes)
        # 广度审查只对新增部分跑（已有节点在上一轮已被审过）；无新增则跳过，省两次调用
        if new_nodes:
            new_nodes2, missing, _ = gap_check(question, new_nodes)
            candidates = new_nodes + new_nodes2[:max(0, MAX_NODES - len(nodes_all))]
        else:
            candidates, missing = [], []
        # 层内限流：每层每轮最多吸收 per_layer_cap 个新节点，超出的留到下一轮。
        # 深层同层数量大时（如 L3 一次出 15 个），单轮全吃下会导致 token 溢出
        # 和注意力稀释；截断后下一轮模型看到已确认事实块会继续消化剩余维度。
        from collections import Counter as _C2
        layer_counts = _C2(int(str(n.get("level") or "L?").lstrip("L")) for n in nodes_all
                           if str(n.get("level") or "").startswith("L") and str(n.get("level")).lstrip("L").isdigit())
        added, capped_layers = [], set()
        for n in candidates:
            lv = int(str(n.get("level") or "L?").lstrip("L")) if str(n.get("level") or "").startswith("L") and str(n.get("level")).lstrip("L").isdigit() else 0
            if lv > 0 and layer_counts[lv] >= per_layer_cap:
                capped_layers.add(lv)
                continue
            added.append(n)
            layer_counts[lv] += 1
        nodes_all.extend(added)
        sa, per_layer = _sa_tree(nodes_all)
        # 一轮 P2/P3 核验：只查 source=search 且未核验过的节点
        to_verify = [n for n in nodes_all if n.get("source", "search") == "search"
                     and n["id"] not in {c[0] for c in confirmed}]
        verified_now = []
        for node in to_verify[:12]:   # 每轮最多核验 12 个，控制 wall time
            srcs, err = search_node(node, qid=qid)
            if err:
                status, evidence, corrected, _raw = ("degraded", f"检索失败: {err}", node["claim"], "")
            else:
                status, evidence, corrected, _raw = verify_node(node, srcs)
            verified_now.append((node["id"], corrected or node["claim"], status))
        confirmed.extend(verified_now)
        stop = None
        # R1 饱和：本轮无任何新增节点（模型找不到新东西可拆 = 定义级粒度自然停）。
        # 注意口径是"所有层合计"——某一层被限流截断不算饱和，剩余维度下一轮继续消化；
        # 只有整棵树都长不出新节点才是真饱和。
        if len(added) == 0:
            stop = "R1-saturation"
        else:
            # R3 停滞：连续 2 轮 S_α 无增长（新增节点都是同义复述）
            if prev_sa is not None and sa <= prev_sa + 1e-6:
                stagnant += 1
            else:
                stagnant = 0
            if stagnant >= 2:
                stop = "R3-stagnant"
        # R2 预算阀：软约束，不停止循环。超过 budget_nodes 后在日志里标记
        # compress_triggered=True（提示该做层级压缩：把深层叶子折叠成中间层摘要），
        # 树继续长——general 超级工程拆到定义级粒度节点数可达千级，硬上限会砍掉合法深度。
        compress_flag = len(nodes_all) >= budget_nodes
        prev_sa = sa
        rounds_log.append({"round": rnd, "n_new": len(added), "n_total": len(nodes_all),
                           "S_alpha": sa, "per_layer": per_layer,
                           "capped_layers": sorted(capped_layers),
                           "compress_triggered": compress_flag,
                           "n_verified_this_round": len(verified_now), "stop": stop})
        print(f"  [state-machine] r{rnd}: +{len(added)} nodes (total {len(nodes_all)}), "
              f"S_α={sa}, verified +{len(verified_now)}, stop={stop}", flush=True)
        if stop:
            break
    return nodes_all, rounds_log


def _run_p1p2p3(rec, tag, question, qid="gpu"):
    """P1 decompose + P2 search + P3 verify. Sets stages.p2p3_nodes, n_verified, n_nodes."""
    t0 = time.time()
    # P1
    nodes, p1_raw = decompose(question)
    rec["stages"]["p1_decompose"] = {"nodes": len(nodes), "levels": {str(k): int(v) for k, v in Counter(n.get("level") or "?" for n in nodes).items()}, "raw": p1_raw}
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
                    "level": node.get("level", "?"),
                    "source": node.get("source", "search"),
                    "search_query": node.get("search_query", "")}
        rounds = []
        for rnd in range(1, MAX_ROUNDS + 1):
            srcs, err = search_node(node, qid=qid)
            if err:
                status, evidence, corrected, raw = ("degraded", f"检索失败: {err}；claim 保留待后续补查", node["claim"], "")
            else:
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
    rec["budget_used"] = _budget_used["n"]
    print(f"  [{tag}] P2/P3 done: {n_v}/{len(facts)} verified", flush=True)


def run_one(qid, rep, dry_run=False, rec_override=None):
    tag = f"S5-{qid}-r{rep}"
    question = QUESTIONS[qid]
    rec = rec_override or {"tag": tag, "arm": "S5", "qid": qid, "rep": rep,
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
        rec["budget_used"] = 0
        print(f"  [{tag}] using pre-built fact table ({len(facts)} nodes, {n_v} verified)", flush=True)
    else:
        _budget_reset()
        if rec.get("_use_hierarchy"):
            # v17: 层级目录臂 — 逐层 INDEX 分解（成璐 2026-11-09 设计），无限预算。
            # decompose_hierarchy 内部已边拆边核验，直接返回 fact table。
            from s5_hierarchy import decompose_hierarchy
            nodes_all, rounds_log, facts = decompose_hierarchy(question, qid=qid)
            rec["stages"]["p1h_hierarchy"] = rounds_log
            n_v = sum(1 for f in facts if f["status"] == "verified")
            rec["n_nodes"], rec["n_verified"] = len(facts), n_v
            rec["stages"]["p2p3_nodes"] = facts
            rec["budget_used"] = 0
            print(f"  [{tag}] hierarchy P1H+P2/P3 done: {n_v}/{len(facts)} verified", flush=True)
        elif rec.get("_use_state_machine"):
            # v16: 状态机臂 — P1e 探索式分解（多轮回退 + 已确认事实注入）
            nodes_all, rounds_log = decompose_explore(question, qid=qid)
            rec["stages"]["p1e_state_machine"] = rounds_log
            facts = []
            for node in nodes_all:
                node_rec = {"id": node["id"], "claim": node["claim"],
                            "level": node.get("level", "?"),
                            "source": node.get("source", "search"),
                            "search_query": node.get("search_query", "")}
                if node.get("source") in ("given", "knowledge"):
                    node_rec.update(status="verified", evidence="模型先验/题面给定，未触发检索",
                                    corrected_claim=node["claim"])
                    facts.append(node_rec)
                    continue
                srcs, err = search_node(node, qid=qid)
                if err:
                    status, evidence, corrected, raw = ("degraded", f"检索失败: {err}", node["claim"], "")
                else:
                    status, evidence, corrected, raw = verify_node(node, srcs)
                node_rec.update(status=status, evidence=evidence,
                                corrected_claim=corrected or node["claim"])
                facts.append(node_rec)
            n_v = sum(1 for f in facts if f["status"] == "verified")
            rec["n_nodes"], rec["n_verified"] = len(facts), n_v
            rec["stages"]["p2p3_nodes"] = facts
            rec["budget_used"] = _budget_used["n"]
            print(f"  [{tag}] state-machine P2/P3 done: {n_v}/{len(facts)} verified", flush=True)
        else:
            _run_p1p2p3(rec, tag, question, qid=qid)
            facts = rec["stages"]["p2p3_nodes"]
            n_v = rec["n_verified"]
    # P0: 目录树落盘 — 成璐的项目标准：每个父节点一个文件夹，其子节点清单就是该文件夹的 INDEX.md
    if rec.get("_use_hierarchy"):
        try:
            import os as _os, json as _js
            base = _os.path.join(rec.get("out_path", ".") or ".", "tree", rec.get("tag", "?"))
            # id -> node; parent 关系靠 level 前缀无法恢复，这里用 supports/顺序近似：按 level 分层写
            from collections import defaultdict as _dd
            by_lv = _dd(list)
            for f in facts:
                by_lv[f.get("level", "?")].append(f)
            _os.makedirs(base, exist_ok=True)
            with open(_os.path.join(base, "INDEX.md"), "w") as fi:
                fi.write(f"# {rec.get('tag','?')} 目录树\n\n")
                for lv in sorted(by_lv, key=lambda x: str(x).lstrip("L")):
                    seg = by_lv[lv]
                    fi.write(f"## {lv}（{len(seg)} 条）\n")
                    for f in seg:
                        st = {"verified": "✅", "degraded": "⚠️", "failed": "❌"}.get(f["status"], "?")
                        fi.write(f"- [{f['id']}]{st} {f['corrected_claim']}\n")
            print(f"  [{rec.get('tag')}] tree written to {base}/INDEX.md ({len(facts)} entries)", flush=True)
        except Exception as e:
            print(f"  [{rec.get('tag')}] tree write failed: {e}", flush=True)
    # P4
    table = "\n".join(
        f"{f['id']}: {f['corrected_claim']}  [status={f['status']}; evidence: {f['evidence'][:120]}]"
        for f in facts)
    prompt = P4_SYNTHESIZE.format(question=question, fact_table=table) + _perturb()
    # v17 无限预算：fact table 巨大时单次 8000 token 输出不够，按层分段合成再合并
    if rec.get("_use_hierarchy") and len(facts) > 200:
        from collections import defaultdict as _dd
        by_lv = _dd(list)
        for f in facts:
            by_lv[f.get("level", "?")].append(f)
        parts = []
        for lv in sorted(by_lv, key=lambda x: str(x).lstrip("L")):
            seg = "\n".join(
                f"{f['id']} ({lv}): {f['corrected_claim']}  [status={f['status']}; evidence: {f['evidence'][:80]}]"
                for f in by_lv[lv])
            p = (f"你是研究员。基于下面第 {lv} 层的已核验事实，回答原问题中该层涉及的部分。"
                 f"只写结论+数值/公式，每条标来源条目 id，不要重复其他层的内容。\n\n"
                 f"【问题】\n{question}\n\n【第 {lv} 层事实】\n{seg}") + _perturb()
            out_l, _ = call_llm(p, max_tokens=4000, temperature=0.7, top_p=0.95)
            parts.append(f"=== 第 {lv} 层 ===\n{out_l or '(空)'}")
        merge_p = (f"你是研究员。下面是同一道问题按目录树分层得到的各层结论摘要。"
                   f"请把它们合并成一份完整最终答案：覆盖问题全部子问，保留所有具体数值/公式/排序，"
                   f"消除层间重复，最后给一个明确的推荐结论。\n\n【问题】\n{question}\n\n"
                   + "\n\n".join(parts)) + _perturb()
        answer, usage = call_llm(merge_p, max_tokens=8000, temperature=0.7, top_p=0.95)
        print(f"  [{rec.get('tag')}] hierarchy segmented synthesis: {len(facts)} facts, {len(parts)} layers", flush=True)
    else:
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
    ap.add_argument("--state-machine", action="store_true",
                    help="v16: P1e exploratory decomposition loop (multi-round backtracking + confirmed-fact injection)")
    ap.add_argument("--hierarchy", action="store_true",
                    help="v17: per-layer INDEX decomposition, unlimited budget (Chenglu 2026-11-09 design)")
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
        if getattr(args, "hierarchy", False) and not args.dry_run:
            # v17 hierarchical arm: per-layer INDEX decomposition (unlimited budget)
            rec2 = {"tag": tag, "arm": "S5-hier", "qid": qid, "rep": rep,
                    "model": LLM_MODEL, "ts": datetime.now(timezone.utc).isoformat(),
                    "stages": {}, "_use_hierarchy": True, "out_path": args.out}
            r = run_one(qid, rep, dry_run=False, rec_override=rec2)
        elif getattr(args, "state_machine", False) and not args.dry_run:
            # v16 state-machine arm: P1e loop (rec carries the flag)
            rec2 = {"tag": tag, "arm": "S5-sm", "qid": qid, "rep": rep,
                    "model": LLM_MODEL, "ts": datetime.now(timezone.utc).isoformat(),
                    "stages": {}, "_use_state_machine": True}
            r = run_one(qid, rep, dry_run=False, rec_override=rec2)
        else:
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