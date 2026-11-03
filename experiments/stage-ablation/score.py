#!/usr/bin/env python3
"""stage-ablation scorer: 6-dim M1-M6 scoring + aggregate → scoring.md.

纯 stdlib。M2/M3/M5 复用 gates.py；M1/M4 用本地 27b judge（conf ≤0.7）；
M6 URL 存活检查。judge 非独立模型，结果标注 conf 上限。
"""
import json, os, re, sys, urllib.request, time
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
    with urllib.request.urlopen(req, timeout=300) as resp:
        data = json.loads(resp.read())
    return data["choices"][0]["message"]["content"]


def judge_m1(output_text, gold_text):
    """M1 事实准确率: 断言↔gold 匹配。返回 (matched, total, notes)。"""
    prompt = f"""你是事实核查员。对照下面的【Gold 锚点】和【模型输出】，逐条判定模型输出中的可判定断言是否与 Gold 一致。

规则：
- 只判"可判定"的断言（有具体数字/规格/结论的陈述）
- 模糊表述（"可能""大概""据我所知"）不算可判定断言，跳过
- 每条断言标 match / mismatch / undecidable
- 最后给 JSON: {{"assertions": [{{"text": "...", "verdict": "match|mismatch|undecidable"}}], "matched": N, "total_decidable": M}}

【Gold 锚点】
{gold_text[:6000]}

【模型输出】
{output_text[:6000]}"""
    try:
        raw = llm_judge(prompt)
        m = re.search(r'\{.*\}', raw, re.DOTALL)
        if m:
            d = json.loads(m.group())
            return d.get("matched", 0), d.get("total_decidable", 1), raw[:200]
        return 0, 1, f"no JSON in judge response: {raw[:100]}"
    except Exception as e:
        return 0, 1, f"judge failed: {e}"


def judge_m4(output_text, gold_text):
    """M4 缺口覆盖率: 模型是否识别了 gold 中列出的关键缺口/不确定性。"""
    prompt = f"""你是研究质量评审。对照【Gold 应识别的缺口】和【模型输出】，判断模型是否主动识别并标注了这些缺口。

规则：
- 模型明确说"不确定/需要查证/查不到/未解决"算识别
- 模型直接给出答案但没提不确定性 = 未识别该缺口
- 最后给 JSON: {{"gaps_in_gold": N, "gaps_identified_by_model": M, "identified": [...], "missed": [...]}}

【Gold 应识别的缺口】
{gold_text[:4000]}

【模型输出】
{output_text[:4000]}"""
    try:
        raw = llm_judge(prompt)
        m = re.search(r'\{.*\}', raw, re.DOTALL)
        if m:
            d = json.loads(m.group())
            return d.get("gaps_identified_by_model", 0), d.get("gaps_in_gold", 1), raw[:200]
        return 0, 1, f"no JSON in judge response: {raw[:100]}"
    except Exception as e:
        return 0, 1, f"judge failed: {e}"


# ── M6 URL 存活 ─────────────────────────────────────────────────────
def check_urls(sources, sample_n=3):
    """M6 调研真实性: 抽样 ≥3 条 URL 检查存活。"""
    if not sources:
        return 0, 0, "no sources provided"
    urls = [s.get("url", "") for s in sources if s.get("url")]
    if not urls:
        return 0, 0, "no URLs in sources"
    sample = urls[:sample_n]
    alive = 0
    for url in sample:
        try:
            req = urllib.request.Request(url, method="HEAD")
            with urllib.request.urlopen(req, timeout=10) as resp:
                if resp.status < 400:
                    alive += 1
        except Exception:
            try:
                req2 = urllib.request.Request(url)
                with urllib.request.urlopen(req2, timeout=10) as resp2:
                    if resp2.status < 400:
                        alive += 1
            except Exception:
                pass
    return alive, len(sample), f"checked {len(sample)} URLs, {alive} alive"


# ── 综合评分 ────────────────────────────────────────────────────────
WEIGHTS = {"M1": 0.25, "M2": 0.20, "M3": 0.15, "M4": 0.20, "M5": 0.10, "M6": 0.10}
Q5_WEIGHT_OVERRIDES = {"M1": 0.125}  # Q5 的 M1 权重降半


def score_run(run_json_path, gold_md, arm, qid):
    with open(run_json_path) as f:
        run = json.load(f)
    output = run.get("output_text", "")
    notes = []

    # M2/M3/M5 from gates.py (map actual keys)
    ga = gate_analyze(output)
    # M2 结构完整度: fact_label_coverage (0-1) + limit_first_third_rate (0-1) → avg
    m2_norm = ((ga.get("fact_label_coverage") or 0) + (ga.get("limit_first_third_rate") or 0)) / 2.0
    # M3 缺口/不确定性标注: hedge_count (有 hedge = 识别了不确定性)
    m3_raw = ga.get("hedge_count", 0)
    m3_norm = min(m3_raw / 3.0, 1.0)  # 3+ hedges = full credit
    # M5 诚实度: 1 - unanchored_rate (数字都有锚点 = 诚实)
    m5_norm = max(0.0, 1.0 - (ga.get("unanchored_rate") or 1.0))

    # M1 事实准确率 (judge)
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
    """读 runs/*.json，按臂聚合，产出 scoring.md。"""
    all_scores = []
    for fn in sorted(os.listdir(runs_dir)):
        if not fn.endswith(".json"):
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
        try:
            sc = score_run(path, gold_md, arm, qid)
            all_scores.append(sc)
        except Exception as e:
            print(f"  score error {fn}: {e}", file=sys.stderr)

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
    args = ap.parse_args()

    if args.cmd == "aggregate":
        from ablation_harness import QUESTIONS
        aggregate(args.runs_dir, QUESTIONS)
    else:
        ap.print_help()