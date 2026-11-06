#!/usr/bin/env python3
"""stage-ablation scorer: 6-dim M1-M6 scoring + aggregate → scoring.md.

纯 stdlib。M2/M3/M5 复用 gates.py；M1/M4 用本地 27b judge（conf ≤0.7）；
M6 URL 存活检查。judge 非独立模型，结果标注 conf 上限。
"""
import json, os, re, sys, urllib.request, time, statistics
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from gates import analyze as gate_analyze

LLM_URL = "http://127.0.0.1:8787/v1/chat/completions"
LLM_MODEL = "qwen3.8-27b"
JUDGE_CONF_CAP = 0.7  # judge 自判 conf 上限

# ── LLM judge ───────────────────────────────────────────────────────
def llm_judge(prompt, max_tokens=4000):
    payload = json.dumps({
        "model": LLM_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
        "max_tokens": max_tokens,
    }).encode()
    req = urllib.request.Request(LLM_URL, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read())
    return data["choices"][0]["message"]["content"]


def detect_gold_type(gold_text):
    """检测 gold 类型: 'data' (含具体数值) 或 'methodology' (方法论型)。
    data 型: ≥5 行含具体数值+单位 (%/$/GB/tok/s 等)
    methodology 型: 主要是结构/方法描述，无大量具体数字
    """
    import re as _re
    numeric_lines = len(_re.findall(r'\d+\.?\d*\s*(%|GB|TB|\$|tok/s|GPU·h|/M|/million|ms)\b', gold_text))
    # Need ≥10 specific data points with units to be 'data' type
    # Methodology-type golds may have a few numbers in examples but aren't primarily data
    return 'data' if numeric_lines >= 10 else 'methodology'


def _smart_truncate(text, limit=12000):
    """Truncate to `limit` chars, preferring the half with more numeric content.
    Two-pass outputs (e.g. S8E) often put structure first and numbers second;
    naive [:limit] can slice off all quantitative assertions."""
    if len(text) <= limit:
        return text
    mid = len(text) // 2
    import re as _re
    n_first = len(_re.findall(r'\d+\.?\d*\s*(%|GB|TB|\$|tok/s|GPU·h|/M|million|ms|元|USD|B\b|K\b|M\b)', text[:mid]))
    n_second = len(_re.findall(r'\d+\.?\d*\s*(%|GB|TB|\$|tok/s|GPU·h|/M|million|ms|元|USD|B\b|K\b|M\b)', text[mid:]))
    if n_second > n_first * 2:
        # Numbers concentrated in second half → keep tail
        return "…[truncated head]…" + text[-limit:]
    return text[:limit]


def judge_m1(output_text, gold_text, gold_type=None):
    """M1 事实准确率。返回 (matched, total, notes)。
    gold_type: 'data' | 'methodology' | None(auto-detect)
    - data 型: 对照 gold 文本判 match/mismatch/undecidable
    - methodology 型: 提取断言 → 对照公开事实（judge 训练知识）判 correct/incorrect
    """
    if gold_type is None:
        gold_type = detect_gold_type(gold_text)

    if gold_type == 'data':
        prompt = f"""你是事实核查员。对照下面的【Gold 锚点】和【模型输出】，逐条判定模型输出中的可判定断言是否与 Gold 一致。

规则：
- 只判"可判定"的断言（有具体数字/规格/结论的陈述）
- 模糊表述（"可能""大概""据我所知"）不算可判定断言，跳过
- 每条断言标 match / mismatch / undecidable
- **必须提取模型输出中所有可判定断言**（通常 5-15 条），不要只挑 1-2 条
- 如果模型输出中有表格、列表、公式，其中的每个数值都是独立断言
- 最后给 JSON: {{"assertions": [{{"text": "...", "verdict": "match|mismatch|undecidable"}}], "matched": N, "total_decidable": M}}

【Gold 锚点】
{_smart_truncate(gold_text)}

【模型输出】
{_smart_truncate(output_text)}"""
    else:
        # Methodology type: verify against public knowledge, not gold text
        prompt = f"""你是事实核查员。以下是一个 AI agent 的分解树输出（gold 是方法论型的，不含具体数字）。
请从输出中提取 10-20 个最关键的定量断言（具体数字+单位），然后基于你已知的公开信息逐条判断是否正确。

规则：
- 只判有具体数值的断言（benchmark 分数、价格、硬件规格等）
- 数值在合理范围内（±10%）算 correct
- 明显错误（差 >30% 或指标名不对）算 incorrect
- 无法判断的标 uncertain（不计入分母）
- 最后给 JSON: {{"assertions": [{{"text": "...", "value": "...", "verdict": "correct|incorrect|uncertain"}}], "matched": N_correct, "total_decidable": N_correct+N_incorrect}}

【模型输出】
{_smart_truncate(output_text)}"""

    try:
        raw = llm_judge(prompt)
        m = re.search(r'\{.*\}', raw, re.DOTALL)
        if m:
            d = json.loads(m.group())
            return d.get("matched", 0), d.get("total_decidable", 1), f"[{gold_type}] {raw[:2000]}"
        return 0, 1, f"no JSON in judge response: {raw[:100]}"
    except Exception as e:
        return 0, 1, f"judge failed: {e}"


def judge_m4(output_text, gold_text):
    """M4 缺口覆盖率: 模型是否识别了 gold 中列出的关键缺口/不确定性。"""
    prompt = f"""你是研究质量评审。对照【Gold 应识别的缺口】和【模型输出】，判断模型是否主动识别并标注了这些缺口。

规则：
- 模型明确说"不确定/需要查证/查不到/未解决/无法核实/需进一步调研"算识别
- 用表格或列表显式列出"不确定性因素/局限/待验证项/黑盒项/无法确定项"也算识别（这是 gap 识别的常见形式，不要因措辞不同而漏判）
- 报告通篇断言、零处承认任何局限 = 未识别
- 最后给 JSON: {{"gaps_in_gold": N, "gaps_identified_by_model": M, "identified": [...], "missed": [...]}}

【Gold 应识别的缺口】
{gold_text[:8000]}

【模型输出】
{output_text[:8000]}"""
    try:
        raw = llm_judge(prompt)
        m = re.search(r'\{.*\}', raw, re.DOTALL)
        if m:
            d = json.loads(m.group())
            return d.get("gaps_identified_by_model", 0), d.get("gaps_in_gold", 1), raw[:2000]
        return 0, 1, f"no JSON in judge response: {raw[:100]}"
    except Exception as e:
        return 0, 1, f"judge failed: {e}"


# ── M6 URL 存活 ─────────────────────────────────────────────────────
_URL_CACHE = {}

def check_urls(sources, sample_n=3):
    """M6 调研真实性: 抽样 ≥3 条 URL 检查存活（带缓存）。"""
    if not sources:
        return 0, 0, "no sources provided"
    urls = [s.get("url", "") for s in sources if s.get("url")]
    if not urls:
        return 0, 0, "no URLs in sources"
    sample = urls[:sample_n]
    alive = 0
    for url in sample:
        if url in _URL_CACHE:
            if _URL_CACHE[url]:
                alive += 1
            continue
        ok = False
        try:
            req = urllib.request.Request(url, method="HEAD")
            with urllib.request.urlopen(req, timeout=5) as resp:
                ok = resp.status < 400
        except Exception:
            try:
                req2 = urllib.request.Request(url)
                with urllib.request.urlopen(req2, timeout=5) as resp2:
                    ok = resp2.status < 400
            except Exception:
                pass
        _URL_CACHE[url] = ok
        if ok:
            alive += 1
    return alive, len(sample), f"checked {len(sample)} URLs, {alive} alive"


# ── 综合评分 ────────────────────────────────────────────────────────
WEIGHTS = {"M1": 0.25, "M2": 0.20, "M3": 0.15, "M4": 0.20, "M5": 0.10, "M6": 0.10}
Q5_WEIGHT_OVERRIDES = {"M1": 0.125}  # Q5 的 M1 权重降半


def score_run(run_json_path, gold_md, arm, qid, multi_n=1):
    with open(run_json_path) as f:
        run = json.load(f)
    output = run.get("output_text", "")
    sources = run.get("sources", [])  # M5 兜底：产物声明的来源列表
    notes = []

    # M2/M3/M5 from gates.py (map actual keys)
    ga = gate_analyze(output, sources=sources if sources else None)
    # M2 结构完整度: limit_first_third_rate (限制声明前置) + 结构化标记（有表格/列表/分节）
    has_structure = bool(re.search(r'\|.*\|', output)) or bool(re.search(r'^\s*[-*]\s+\S', output, re.M)) or output.count('#') >= 3
    m2_norm = ((ga.get("limit_first_third_rate") or 0) * 0.5 + (1.0 if has_structure else 0.0) * 0.5)
    # M3 缺口/不确定性标注: hedge_count (有 hedge = 识别了不确定性)
    m3_raw = ga.get("hedge_count", 0)
    m3_norm = min(m3_raw / 3.0, 1.0)  # 3+ hedges = full credit
    # M5 诚实度: 加权锚点率（行内强锚点=1.0, 弱锚点=0.5, sources兜底=0.3, 无=0）
    m5_norm = ga.get("anchored_rate_weighted") or 0.0

    # M1 事实准确率 (judge) — multi-sample reduces non-determinism
    if multi_n > 1:
        m1_scores = []
        for i in range(multi_n):
            try:
                mm, mt, mn = judge_m1(output, gold_md)
                m1_scores.append(mm / max(mt, 1))
            except Exception as e:
                pass
        m1_norm = statistics.median(m1_scores) if m1_scores else 0.0
        notes.append(f"M1 judge: multi({multi_n}) median={m1_norm:.3f} raw={[f'{x:.3f}' for x in m1_scores]}")
    else:
        m1_matched, m1_total, m1_note = judge_m1(output, gold_md)
        m1_norm = m1_matched / max(m1_total, 1)
        notes.append(f"M1 judge: {m1_note}")

    # M4 缺口覆盖 (judge)
    m4_id, m4_total, m4_note = judge_m4(output, gold_md)
    m4_norm = m4_id / max(m4_total, 1)
    notes.append(f"M4 judge: {m4_note}")

    # M6 URL 存活
    m6_alive, m6_checked, m6_note = check_urls(run.get("sources", []))
    m6_norm = m6_alive / max(m6_checked, 1) if m6_checked > 0 else 0.0
    notes.append(f"M6: {m6_note}")

    # 归一化 (M2/M3/M5 已算好; M1/M4/M6 从 judge/URL 来)
    scores = {
        "M1": min(m1_norm, 1.0),
        "M2": m2_norm,
        "M3": m3_norm,
        "M4": min(m4_norm, 1.0),
        "M5": max(0.0, m5_norm),
        "M6": m6_norm,
    }

    weights = dict(WEIGHTS)
    if qid == "Q5":
        weights.update(Q5_WEIGHT_OVERRIDES)
        # 重新归一化权重使总和=1
        wsum = sum(weights.values())
        weights = {k: v / wsum for k, v in weights.items()}

    total = sum(scores[k] * weights[k] for k in scores)

    return {
        "arm": arm, "qid": qid, "rep": run.get("rep", 0),
        "scores": scores, "total": round(total, 4),
        "boundary_violation": ga.get("boundary_violation", False),
        "notes": notes,
        "judge_conf_cap": JUDGE_CONF_CAP,
        "wall_s": run.get("wall_s", 0),
        "tokens": run.get("tokens", {}),
    }


# ── 聚合 ────────────────────────────────────────────────────────────
def aggregate(runs_dir, questions):
    """读 runs/*.json，按臂聚合，产出 scoring.md（4 并发）。"""
    from concurrent.futures import ThreadPoolExecutor, as_completed

    # 收集所有要评分的 (fn, path, arm, qid, gold_md)
    tasks = []
    for fn in sorted(os.listdir(runs_dir)):
        if not fn.endswith(".json") or "-old" in fn:
            continue
        path = os.path.join(runs_dir, fn)
        with open(path) as f:
            run = json.load(f)
        arm = run.get("arm", "?")
        qid = run.get("qid", "?")
        rep = run.get("rep", 0)
        if arm not in ("S0", "S1", "S2", "S3", "S4", "S5") or qid not in questions:
            continue
        gold_path = questions[qid]["gold_file"]
        if not os.path.exists(gold_path):
            print(f"  skip {fn}: gold not found at {gold_path}", file=sys.stderr)
            continue
        gold_md = open(gold_path).read()
        tasks.append((fn, path, arm, qid, gold_md))

    all_scores = []
    def _score_one(task):
        fn, path, arm, qid, gold_md = task
        try:
            return score_run(path, gold_md, arm, qid, multi_n=args.multi)
        except Exception as e:
            print(f"  score error {fn}: {e}", file=sys.stderr)
            return None

    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(_score_one, t): t[0] for t in tasks}
        for fut in as_completed(futures):
            sc = fut.result()
            if sc:
                all_scores.append(sc)

    if not all_scores:
        print("No scored runs found.", file=sys.stderr)
        return ""

    # 按臂汇总
    arms_order = ["S0", "S1", "S2", "S3", "S4", "S5"]
    present_arms = [a for a in arms_order if any(s["arm"] == a for s in all_scores)]

    lines = [
        "# Stage-Ablation Scoring",
        "",
        f"> generated: {datetime.now(timezone.utc).isoformat()}",
        f"> runs scored: {len(all_scores)}",
        f"> judge: local 27b (self-judge, conf cap {JUDGE_CONF_CAP})",
        f"> n per arm×q: varies (see table)",
        "",
        "## 6-Dim × Arm Summary",
        "",
        "| Arm | Q | Rep | M1 | M2 | M3 | M4 | M5 | M6 | Total | Wall(s) | Tokens(out) |",
        "|-----|---|-----|----|----|----|----|----|----|-------|---------|-------------|",
    ]
    for s in all_scores:
        sc = s["scores"]
        lines.append(
            f"| {s['arm']} | {s['qid']} | r{s['rep']} | "
            f"{sc['M1']:.2f} | {sc['M2']:.2f} | {sc['M3']:.2f} | "
            f"{sc['M4']:.2f} | {sc['M5']:.2f} | {sc['M6']:.2f} | "
            f"**{s['total']:.3f}** | {s['wall_s']} | {s['tokens'].get('out', '?')} |"
        )

    # Δ_k 增量
    lines += ["", "## Per-Level Delta (Δ_k = avg(S_k) - avg(S_{k-1}))", ""]
    arm_means = {}
    for a in present_arms:
        vals = [s["total"] for s in all_scores if s["arm"] == a]
        arm_means[a] = sum(vals) / len(vals) if vals else 0
    lines.append("| Transition | Mean Prev | Mean Cur | Δ | Sign |")
    lines.append("|------------|-----------|----------|---|------|")
    prev = None
    for a in present_arms:
        if prev is not None:
            delta = arm_means[a] - arm_means[prev]
            sign = "+" if delta >= 0 else "-"
            lines.append(f"| {prev}→{a} | {arm_means[prev]:.3f} | {arm_means[a]:.3f} | {delta:+.3f} | {sign} |")
        prev = a

    # DESIGN §8 判据
    lines += ["", "## DESIGN §8 Criteria Check", ""]
    all_positive = all(
        arm_means[b] >= arm_means[a]
        for a, b in zip(present_arms[:-1], present_arms[1:])
    )
    lines.append(f"1. **每级增量符号**: {'✅ all positive' if all_positive else '⚠️ some negative'} — see Δ table above")
    lines.append(f"2. **S5 vs D1 总分序**: N/A — D1 baseline unavailable (Python 3.9 vs GPT Researcher 3.10+ requirement, see runs/d1-choice.md)")

    # 诚实条款
    lines += [
        "",
        "## Honesty Clause",
        "",
        f"- Judge is the same model being evaluated (self-bias risk); conf capped at {JUDGE_CONF_CAP}",
        "- n=2 per arm×question → directional only, not statistically significant",
        "- S2+ arms: web research hook not implemented (ego-browser stub) → M6 scores reflect zero sources",
        "- D1 comparison: N/A (environment incompatibility, documented in d1-choice.md)",
        "- M1/M4 depend on gold anchor quality; Q5 gold is opinion-survey type (lower confidence)",
    ]

    md = "\n".join(lines) + "\n"
    out_path = os.path.join(HERE, "scoring.md")
    with open(out_path, "w") as f:
        f.write(md)
    print(f"\nscoring.md written: {out_path}")
    return md


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd")
    agg_p = sub.add_parser("aggregate")
    agg_p.add_argument("--runs-dir", default=os.path.join(HERE, "runs"))
    agg_p.add_argument("--multi", type=int, default=1, help="M1 judge samples per run (median aggregation)")
    args = ap.parse_args()

    if args.cmd == "aggregate":
        from ablation_harness import QUESTIONS
        aggregate(args.runs_dir, QUESTIONS)
    else:
        ap.print_help()