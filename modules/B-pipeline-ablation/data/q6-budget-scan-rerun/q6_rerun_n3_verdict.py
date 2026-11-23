#!/usr/bin/env python3
"""Q6 重跑批 n=3 判读 (300 档 r1/r2/r3 落地后跑)。

判读项:
1. 停止机制分布: n_nodes==300 → 预算墙; <300 → 深度墙 (max_depth=4 默认)
2. metacog 均值偏移: r3 是否仍 > 原批 max (0.2227) → n=3 定论
3. gap_rate: r3 是否仍 ~0 (独立检索系统性不标 gap)
4. judge 饱和: r3 total 是否再撞 0.4139 (cov 再命中 1 unit)
5. rep 方差: rerun sd vs 原批 sd (0.0304 metacog / 0.0212 judge)

用法: python3 q6_rerun_n3_verdict.py
"""
import glob, json, os, statistics as st

OUT = os.path.dirname(os.path.abspath(__file__))
ORIG = "/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/q6-budget-scan/q6-scan-scores.json"
BUDGET = 300
ORIG_METACOG = [0.1703, 0.1698, 0.2227]
ORIG_JUDGE = [0.4000, 0.4417, 0.4278]

def load_rerun():
    rows = []
    for f in sorted(glob.glob(os.path.join(OUT, f"q6-{BUDGET}-r*-*.json"))):
        d = json.load(open(f))
        nodes = d.get("nodes", [])
        # 停止机制推断: n_nodes==budget → 预算墙; 否则深度墙 (max_depth=4)
        stop = "budget-wall" if d.get("n_nodes", len(nodes)) >= BUDGET else "depth-wall"
        # metacog 口径: 从 scores 读 (评分脚本已算), 若缺则从 run json 现算 gap
        rows.append({"file": os.path.basename(f), "n_nodes": d.get("n_nodes", len(nodes)),
                     "stop": stop, "max_depth": max((n.get("level", 0) for n in nodes), default=0)})
    return rows

def main():
    runs = load_rerun()
    scores = json.load(open(os.path.join(OUT, "q6-rerun-scores.json")))
    print(f"=== Q6 300 档重跑批 n={len(runs)} 判读 ===\n")

    print("1. 停止机制分布:")
    for r in runs:
        print(f"   {r['file']}: n={r['n_nodes']} max_depth={r['max_depth']} → {r['stop']}")
    stops = [r["stop"] for r in runs]
    if len(set(stops)) > 1:
        print(f"   ★ rep 间停止机制不一致 ({set(stops)}) → '独立检索必撞深度墙' 不成立, 停止机制是 rep 间变量")
    elif stops and stops[0] == "depth-wall":
        print("   全部深度墙 → '独立检索 300 档撞深度墙' n 确认")
    else:
        print("   全部预算墙 → 独立检索下 300 档仍是预算约束")

    print("\n2. metacog 均值偏移 (原批 max=0.2227):")
    met = [s["metacog"]["total"] for s in scores if s["budget"] == BUDGET]
    for s in scores:
        if s["budget"] == BUDGET:
            flag = " > orig max" if s["metacog"]["total"] > max(ORIG_METACOG) else ""
            print(f"   r{s['rep']}: metacog={s['metacog']['total']:.4f} (gap={s['metacog']['gap']:.4f} post={s['metacog']['post']:.3f}){flag}")
    if len(met) >= 2:
        n_above = sum(1 for m in met if m > max(ORIG_METACOG))
        print(f"   {n_above}/{len(met)} 点 > 原批 max → {'均值偏移定论' if n_above == len(met) else '非全部, 判读存疑'}")

    print("\n3. gap_rate (原批 0.023-0.033):")
    gaps = [s["metacog"]["gap"] for s in scores if s["budget"] == BUDGET]
    print(f"   rerun: {gaps}  orig: [0.0233, 0.0333, 0.0300]")
    if gaps and max(gaps) < 0.02:
        print("   ★ 独立检索系统性不标 gap (n 确认) → 检索模式是 monitoring 轴混杂")

    print("\n4. judge 饱和 (0.5×depth + 0.5×cov, depth 撞 4/5=0.8):")
    jts = [s["judge"]["total"] for s in scores if s["budget"] == BUDGET]
    print(f"   rerun: {jts}  orig: {ORIG_JUDGE}")
    if len(set(jts)) < len(jts):
        print("   ★ total 重复 → judge 轴 300 档无区分度 (depth 饱和 + cov 1/36 分辨率)")

    print("\n5. rep 方差对照 (判据: rerun sd > orig sd × 1.3):")
    for axis, orig in [("metacog", ORIG_METACOG), ("judge", ORIG_JUDGE)]:
        vals = [s[axis]["total"] for s in scores if s["budget"] == BUDGET]
        if len(vals) >= 2:
            rs, os_ = st.stdev(vals), st.stdev(orig)
            verdict = "↑ 回升" if rs > os_ * 1.3 else "≈ 持平"
            print(f"   {axis}: rerun sd={rs:.4f} (n={len(vals)}) vs orig sd={os_:.4f} → {verdict}")
        else:
            print(f"   {axis}: n={len(vals)} 不可算")

if __name__ == "__main__":
    main()
