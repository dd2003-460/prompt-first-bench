"""Judge v2: depth-gradient rubric scoring for nat domain.

Each gold point is decomposed into 3-4 depth levels. Judge scores each level 0/1,
weighted sum gives continuous [0,1] per point, mean across points = run score.

This replaces the binary coverage metric (denominator=6 → only 7 discrete values)
with a continuous resolution that distinguishes "mentioned the concept" from
"derived the correct quantitative relationship".

Weighting scheme — k·log(k) frequency-rarity weighting (成璐 2026-11-08):
  - Depth levels are ordered by rarity: shallow = common (high base rate), deep = rare (low base rate).
  - The value of reaching a level scales with how RARE it is (frequency × information content).
  - Pure log(k) would under-weight deep levels; multiplying by k compensates:
      w_k = k · ln(k+1) / Σ_j j·ln(j+1)   for k in {1..K}
    K=3 → weights ≈ [0.29, 0.40, 0.31]... wait no:
    k·ln(k+1): 1·ln2=0.693, 2·ln3=2.197, 3·ln4=4.159 → normalize: [0.11, 0.35, 0.54]
    K=4: 0.693, 2.197, 4.159, 6.438 → [0.08, 0.24, 0.45, 0.69]... no:
    sum=13.49 → [0.051, 0.163, 0.308, 0.477]
  - So deeper levels get disproportionately more weight. A run that reaches level 4
    but not level 1 gets 0.477 (not 0.25 as uniform would give).
  - This is the production formula from bench/self-opt-tester/bench.md O3:
      w_v = 1 + min(−log₂ p̃_v, log₂(1/ε))
    where p̃ = blind-generation base rate. For our fixed depth ladder, we use the
    deterministic k·ln(k+1) proxy instead of LLM-estimated p̃ (cheaper, no same-family
    judge bias, monotonic by construction).

Usage: python3 judge_v2_depth.py --runs runs-prod --arm S0 --q nat --reps 1-30
"""
import argparse, json, math, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ablation_harness import call_llm

# Depth-level rubric for nat (CDN cache) gold points
# Each point: list of (weight, description) — weights are k·ln(k+1) normalized (deeper = rarer = more valuable)
# K=3: [0.11, 0.35, 0.54]   K=4: [0.05, 0.16, 0.31, 0.48]

def _w3():
    raw = [k * math.log(k + 1) for k in range(1, 4)]
    s = sum(raw)
    return [r / s for r in raw]  # ≈ [0.11, 0.35, 0.54]

def _w4():
    raw = [k * math.log(k + 1) for k in range(1, 5)]
    s = sum(raw)
    return [r / s for r in raw]  # ≈ [0.05, 0.16, 0.31, 0.48]

W3 = _w3()
W4 = _w4()

NAT_RUBRIC = {
    "pt1": [
        (W3[0], "提到用 Pareto/Zipf 累积质量估算命中率（头部 k% 对象承载大部分请求）"),
        (W3[1], "给出具体公式或推导步骤（如 H(k) = 1 - (1-k)^{1-α} 或等价表述）"),
        (W3[2], "代入题面参数（α=1.1, N=10⁵, C=128GB）算出数值区间"),
    ],
    "pt2": [
        (W3[0], "指出 α=1.1 接近临界值 1，分布重尾，容量利用率对头部集中度敏感"),
        (W3[1], "说明 128GB 能覆盖的头部比例决定命中率量级（定性）"),
        (W3[2], "给出覆盖比例的估算（如 top 10-20% 对象占 >80% 字节流量）"),
    ],
    "pt3": [
        (W3[0], "提到 LFU 优势受对象更新/热度漂移限制"),
        (W3[1], "将 1%/天 更新率与 LFU 频率表老化关联（定性）"),
        (W3[2], "量化提升上限（给出百分点范围 + 推导依据，非拍脑袋）"),
    ],
    "pt4": [
        (W3[0], "区分按字节命中率 vs 按请求命中率（两个口径分开报）"),
        (W3[1], "解释为什么大小-热度负相关导致两口径不同"),
        (W3[2], "分别给出两个口径的数值或关系式"),
    ],
    "pt5": [
        (W4[0], "提到'驻留时间'/'residence time'/'停留时间'概念"),
        (W4[1], "给出 T_res 的量级估计（天/小时级，非分钟级；如 ~100 天或 ~30 天）"),
        (W4[2], "将 T_res 与访问间隔做了显式对比（T_res >> inter-visit gap）"),
        (W4[3], "推导出折扣因子并给出数值（如 p_stale = 1-exp(-u·T_res)，代入得具体折数）"),
    ],
    "pt6": [
        (W3[0], "明确标注哪些数字是估算、哪些是假设"),
        (W3[1], "列出关键假设（如 miss 惩罚、对象不可分割性、稳态假设）"),
        (W3[2], "对至少一个假设说明如果改变会怎样（敏感性）"),
    ],
}

SOC_RUBRIC = {
    "pt1": [
        (W4[0], "假设链起点包含'生存压力/金钱资源=定向压力'"),
        (W4[1], "假设链起点包含'偏好噪声/随机演化残留'"),
        (W4[2], "没有直接跳到禀赋效应/损失厌恶等现成心理学标签"),
        (W4[3], "从起点到逐利行为有中间推导步骤（非一步到位）"),
    ],
    "pt2": [
        (W4[0], "给出至少一个解释候选（信号理论/锚定/比价成本等）"),
        (W4[1], "解释候选有机制说明（为什么高挂价→快成交）"),
        (W4[2], "评估了该解释的适用边界或局限"),
        (W4[3], "考虑了多个候选之间的竞争关系"),
    ],
    "pt3": [
        (W4[0], "给出至少一个解释候选（负面信号/咨询滞后/等待更低锚点等）"),
        (W4[1], "解释候选有机制说明（为什么降价→无咨询）"),
        (W4[2], "评估了该解释的适用边界或局限"),
        (W4[3], "考虑了多个候选之间的竞争关系"),
    ],
    "pt4": [
        (W3[0], "明确指出哪条假设链能同时覆盖两个现象"),
        (W3[1], "明确指出哪条只能覆盖一个"),
        (W3[2], "对'同一假设 vs 不同假设'给出判断依据"),
    ],
    "pt5": [
        (W3[0], "判定最可能驱动均衡的利益相关方（点名）"),
        (W3[1], "给出依据（数据里谁的行为变了/谁的收益结构变了）"),
        (W3[2], "排除了其他利益相关方的理由"),
    ],
    "pt6": [
        (W3[0], "提出具体最小干预方案"),
        (W3[1], "明确说清受害者是谁"),
        (W3[2], "说明为什么是'最小'的（而非更激进的替代）"),
    ],
    "pt7": [
        (W3[0], "每个关键断言带置信度标注"),
        (W3[1], "低置信的显式标出（不是全部高置信）"),
        (W3[2], "置信度标注有依据（为什么这个给 0.6 那个给 0.9）"),
    ],
}


def build_judge_prompt(qid: str, answer: str) -> str:
    rubric = NAT_RUBRIC if qid == "nat" else SOC_RUBRIC
    points_desc = []
    for pt_name, levels in rubric.items():
        pts = []
        for i, (w, desc) in enumerate(levels, 1):
            pts.append(f"  L{i}: {desc}")
        K = len(levels)
        # show what each score means on the [0,1] scale
        anchors = f"  (0=未触及, {1/K:.2f}=仅达L1, {2/K:.2f}=达L2, ..., 1.00=全部{K}层达成)"
        points_desc.append(f"{pt_name} [{K}层]{anchors}:\n" + "\n".join(pts))
    
    rubric_text = "\n".join(points_desc)
    return (
        "你是严格评分员。下面是一道题的深度评分标准和一个候选回答。\n"
        "对每个要点，给出一个 **0.00-1.00 的连续深度分**，表示候选回答在该要点上实际达到的深度位置。\n\n"
        "**打分规则（必须严格遵守）：**\n"
        "- 分数 = 实际达成的最高层级 / 总层数，可以在层级之间插值\n"
        "- 例：4层要点，提到了概念但没给量级 → 在 L1 和 L2 之间 → 0.25-0.35\n"
        "- 例：4层要点，给了量级和对比但没推导出数值 → 在 L3 和 L4 之间 → 0.65-0.75\n"
        "- **不要只给 0、1/K、2/K...这些离散锚点**——如果回答部分达到了某层（比如给了公式但没代入参数），给该层位置的一半（如 L2 部分达成 → 0.17 而非 0.33）\n"
        "- 仅提到概念名称但无量化/推导/对比 = 不超过 0.25\n"
        "- '打0.99折'≠'基于驻留时间推导折扣因子'——前者是拍脑袋，后者需要 T_res 量级 + 与访问间隔的显式对比\n"
        "- 给出公式但未代入题面参数 = 不超过 0.75（4层时）\n"
        "- 拿不准时往低判（宁严勿松）\n"
        "- 分数必须是两位小数的数字，不要输出 0/1 列表\n\n"
        f"深度评分标准：\n{rubric_text}\n\n"
        f"候选回答：\n{answer[:12000]}\n\n"
        '输出 JSON：{"scores": {"pt1": 0.xx, "pt2": 0.xx, ...}}\n'
        "每个值是一个 0.00-1.00 的数字。只输出 JSON，不要解释。"
    )


def score_run(qid: str, answer: str) -> dict:
    """Score one answer with depth rubric. Returns per-point continuous scores."""
    prompt = build_judge_prompt(qid, answer)
    content, _ = call_llm(prompt, max_tokens=2000, temperature=0)
    m = re.search(r"\{.*\}", content, re.S)
    try:
        d = json.loads(m.group(0)) if m else {}
    except json.JSONDecodeError:
        return {"error": content[:500]}
    
    rubric = NAT_RUBRIC if qid == "nat" else SOC_RUBRIC
    # LLM sometimes wraps in {"scores": {...}}, sometimes returns flat {pt1: x, ...}
    if "scores" in d and isinstance(d["scores"], dict):
        scores_raw = d["scores"]
    else:
        scores_raw = d
    point_scores = {}
    total = 0
    n_points = 0
    for pt_name, levels in rubric.items():
        raw = scores_raw.get(pt_name, 0)
        # handle both old format (list) and new format (scalar)
        if isinstance(raw, list):
            # legacy: convert 0/1 list to weighted score
            fixed = list(int(x) for x in raw[:len(levels)])
            for i in range(len(fixed) - 1, 0, -1):
                if fixed[i] == 1:
                    fixed[i-1] = 1
            score = sum(w * v for (w, _), v in zip(levels, fixed))
            point_scores[pt_name] = {"score": round(score, 3), "raw_levels": fixed}
        else:
            try:
                score = max(0.0, min(1.0, float(raw)))
            except (ValueError, TypeError):
                score = 0.0
            point_scores[pt_name] = {"score": round(score, 3)}
        total += score
        n_points += 1
    
    overall = total / max(n_points, 1)
    return {"point_scores": point_scores, "overall": round(overall, 4),
            "raw": scores_raw}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", default="runs-prod")
    ap.add_argument("--arm", default="S0")
    ap.add_argument("--q", default="nat")
    ap.add_argument("--reps", default="1-30")
    args = ap.parse_args()
    
    lo, hi = args.reps.split("-")
    results = []
    for rep in range(int(lo), int(hi) + 1):
        fp = f"{args.runs}/{args.arm}-{args.q}-r{rep}.json"
        if not os.path.exists(fp):
            continue
        d = json.load(open(fp))
        ans = d["answer"]
        r = score_run(args.q, ans)
        r["tag"] = f"{args.arm}-{args.q}-r{rep}"
        results.append(r)
        pts_str = " ".join(f"{k}={v['score']}" for k, v in r.get("point_scores", {}).items())
        print(f"{r['tag']}: overall={r.get('overall', 'ERR')} (pts: {pts_str})", flush=True)
    
    # summary
    if results and "overall" in results[0]:
        overalls = [r["overall"] for r in results if "overall" in r]
        mean = sum(overalls) / len(overalls)
        sd = (sum((x-mean)**2 for x in overalls)/max(len(overalls)-1,1))**0.5
        print(f"\n=== SUMMARY: {args.arm}-{args.q} n={len(overalls)} ===")
        print(f"mean={mean:.4f} ± {sd:.4f}")
        # per-point means
        for pt in (NAT_RUBRIC if args.q=="nat" else SOC_RUBRIC):
            vals = [r["point_scores"][pt]["score"] for r in results if pt in r.get("point_scores",{})]
            if vals:
                pm = sum(vals)/len(vals)
                print(f"  {pt}: {pm:.3f}")
        # distribution
        buckets = [0]*10
        for o in overalls:
            b = min(int(o*10), 9)
            buckets[b] += 1
        print(f"distribution: {' '.join(f'{b/10:.1f}-{(b+1)/10:.1f}:{c}' for b,c in enumerate(buckets) if c)}")
    
    out_fp = f"{args.runs}/judge-v2-{args.arm}-{args.q}.json"
    with open(out_fp, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved → {out_fp}")


if __name__ == "__main__":
    main()