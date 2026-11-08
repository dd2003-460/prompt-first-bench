"""Judge v2: depth-gradient rubric scoring for nat domain.

Each gold point is decomposed into 3-4 depth levels. Judge scores each level 0/1,
weighted sum gives continuous [0,1] per point, mean across points = run score.

This replaces the binary coverage metric (denominator=6 → only 7 discrete values)
with a continuous resolution that distinguishes "mentioned the concept" from
"derived the correct quantitative relationship".

Usage: python3 judge_v2_depth.py --runs runs-prod --arm S0 --q nat --reps 1-30
"""
import argparse, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ablation_harness import call_llm

# Depth-level rubric for nat (CDN cache) gold points
# Each point: list of (weight, description) — weights sum to 1.0 per point
NAT_RUBRIC = {
    "pt1": [
        (0.3, "提到用 Pareto/Zipf 累积质量估算命中率（头部 k% 对象承载大部分请求）"),
        (0.3, "给出具体公式或推导步骤（如 H(k) = 1 - (1-k)^{1-α} 或等价表述）"),
        (0.4, "代入题面参数（α=1.1, N=10⁵, C=128GB）算出数值区间"),
    ],
    "pt2": [
        (0.4, "指出 α=1.1 接近临界值 1，分布重尾，容量利用率对头部集中度敏感"),
        (0.3, "说明 128GB 能覆盖的头部比例决定命中率量级（定性）"),
        (0.3, "给出覆盖比例的估算（如 top 10-20% 对象占 >80% 字节流量）"),
    ],
    "pt3": [
        (0.3, "提到 LFU 优势受对象更新/热度漂移限制"),
        (0.3, "将 1%/天 更新率与 LFU 频率表老化关联（定性）"),
        (0.4, "量化提升上限（给出百分点范围 + 推导依据，非拍脑袋）"),
    ],
    "pt4": [
        (0.4, "区分按字节命中率 vs 按请求命中率（两个口径分开报）"),
        (0.3, "解释为什么大小-热度负相关导致两口径不同"),
        (0.3, "分别给出两个口径的数值或关系式"),
    ],
    "pt5": [
        (0.2, "提到'驻留时间'/'residence time'/'停留时间'概念"),
        (0.3, "给出 T_res 的量级估计（天/小时级，非分钟级；如 ~100 天或 ~30 天）"),
        (0.3, "将 T_res 与访问间隔做了显式对比（T_res >> inter-visit gap）"),
        (0.2, "推导出折扣因子并给出数值（如 p_stale = 1-exp(-u·T_res)，代入得具体折数）"),
    ],
    "pt6": [
        (0.4, "明确标注哪些数字是估算、哪些是假设"),
        (0.3, "列出关键假设（如 miss 惩罚、对象不可分割性、稳态假设）"),
        (0.3, "对至少一个假设说明如果改变会怎样（敏感性）"),
    ],
}

SOC_RUBRIC = {
    "pt1": [
        (0.3, "假设链起点包含'生存压力/金钱资源=定向压力'"),
        (0.3, "假设链起点包含'偏好噪声/随机演化残留'"),
        (0.2, "没有直接跳到禀赋效应/损失厌恶等现成心理学标签"),
        (0.2, "从起点到逐利行为有中间推导步骤（非一步到位）"),
    ],
    "pt2": [
        (0.3, "给出至少一个解释候选（信号理论/锚定/比价成本等）"),
        (0.3, "解释候选有机制说明（为什么高挂价→快成交）"),
        (0.2, "评估了该解释的适用边界或局限"),
        (0.2, "考虑了多个候选之间的竞争关系"),
    ],
    "pt3": [
        (0.3, "给出至少一个解释候选（负面信号/咨询滞后/等待更低锚点等）"),
        (0.3, "解释候选有机制说明（为什么降价→无咨询）"),
        (0.2, "评估了该解释的适用边界或局限"),
        (0.2, "考虑了多个候选之间的竞争关系"),
    ],
    "pt4": [
        (0.4, "明确指出哪条假设链能同时覆盖两个现象"),
        (0.3, "明确指出哪条只能覆盖一个"),
        (0.3, "对'同一假设 vs 不同假设'给出判断依据"),
    ],
    "pt5": [
        (0.4, "判定最可能驱动均衡的利益相关方（点名）"),
        (0.3, "给出依据（数据里谁的行为变了/谁的收益结构变了）"),
        (0.3, "排除了其他利益相关方的理由"),
    ],
    "pt6": [
        (0.4, "提出具体最小干预方案"),
        (0.3, "明确说清受害者是谁"),
        (0.3, "说明为什么是'最小'的（而非更激进的替代）"),
    ],
    "pt7": [
        (0.4, "每个关键断言带置信度标注"),
        (0.3, "低置信的显式标出（不是全部高置信）"),
        (0.3, "置信度标注有依据（为什么这个给 0.6 那个给 0.9）"),
    ],
}


def build_judge_prompt(qid: str, answer: str) -> str:
    rubric = NAT_RUBRIC if qid == "nat" else SOC_RUBRIC
    points_desc = []
    for pt_name, levels in rubric.items():
        pts = []
        for w, desc in levels:
            pts.append(f"  {w:.1f}: {desc}")
        points_desc.append(f"{pt_name}:\n" + "\n".join(pts))
    
    rubric_text = "\n".join(points_desc)
    return (
        "你是评分员。下面是一道题的深度评分标准和一个候选回答。\n"
        "对每个要点的每个深度层级，判断候选回答是否达到该层级（达到=1，未达到=0）。\n"
        "注意：高层级达成隐含低层级达成（如果给了高层级 1，低层级自动 1）。\n\n"
        f"深度评分标准：\n{rubric_text}\n\n"
        f"候选回答：\n{answer[:12000]}\n\n"
        '输出 JSON：{"scores": {"pt1": [0或1, ...], "pt2": [...], ...}}\n'
        "每个列表的长度必须对应该要点的层级数。"
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
    scores_raw = d.get("scores", {})
    point_scores = {}
    total_weighted = 0
    n_points = 0
    for pt_name, levels in rubric.items():
        raw = scores_raw.get(pt_name, [])
        # enforce monotonicity: if level i is 1, all lower levels must be 1
        enforced = []
        seen_one = False
        for i in range(len(levels)):
            if not seen_one and i > 0 and raw[i] == 1:
                # higher level achieved without lower → force lower to 1
                pass
            val = int(raw[i]) if i < len(raw) else 0
            enforced.append(val)
        # fix monotonicity properly (bottom-up)
        fixed = list(enforced)
        for i in range(len(fixed) - 1, 0, -1):
            if fixed[i] == 1:
                fixed[i-1] = 1
        weighted = sum(w * v for (w, _), v in zip(levels, fixed))
        point_scores[pt_name] = {"levels": fixed, "score": round(weighted, 3)}
        total_weighted += weighted
        n_points += 1
    
    overall = total_weighted / max(n_points, 1)
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