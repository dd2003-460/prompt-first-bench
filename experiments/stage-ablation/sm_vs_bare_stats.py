#!/usr/bin/env python3
"""SM vs bare 同负载对比统计（matched 批，2026-11-22）。
SM: runs_sm_matched/*.json (depth_score 字段)
bare: runs_matched/*_judge.json (overall 字段)
口径: 同 qid 配对，Welch t + Mann-Whitney U + Cliff's δ + bootstrap CI。
"""
import json, glob, os, math, re, sys
from datetime import datetime

ROOT = "/Users/a1-6/Desktop/workspace/pfb"
SM_DIR = f"{ROOT}/modules/B-pipeline-ablation/data/t53b/runs_sm_matched"
BARE_DIR = f"{ROOT}/modules/B-pipeline-ablation/data/t53b/runs_matched"
OUT = f"{ROOT}/modules/B-pipeline-ablation/reports/t53b/stats-sm-vs-bare-matched.md"
QIDS = ["nat", "soc", "gpu"]

def load_runs(d, kind):
    """SM: depth 在 main 文件 depth_score 字段；bare: depth 在 judge 文件 overall 字段。
    只读对应文件，避免另一类文件（无该字段）覆盖。"""
    out = {}
    for f in glob.glob(f"{d}/*.json"):
        b = os.path.basename(f)
        m = re.match(r"(\w+)_(formula|bare)_r(\d{2})(\.json|_judge\.json)$", b)
        if not m:
            continue
        qid, arm, rnd, is_judge = m.group(1), m.group(2), int(m.group(3)), m.group(4) == "_judge.json"
        if kind == "sm" and is_judge:
            continue
        if kind == "bare" and not is_judge:
            continue
        d_ = json.load(open(f))
        depth = d_.get("depth_score") if kind == "sm" else d_.get("overall")
        nodes = d_.get("n_nodes") if kind == "sm" else None
        out.setdefault(qid, {})[rnd] = {"depth": depth, "nodes": nodes}
    return out

def welch_t(a, b):
    na, nb = len(a), len(b)
    ma, mb = sum(a)/na, sum(b)/nb
    va = sum((x-ma)**2 for x in a)/(na-1)
    vb = sum((x-mb)**2 for x in b)/(nb-1)
    se = math.sqrt(va/na + vb/nb)
    if se == 0:
        return 0.0, 0.0, 1.0
    t = (ma-mb)/se
    df = (va/na + vb/nb)**2 / ((va/na)**2/(na-1) + (vb/nb)**2/(nb-1))
    # t→p 用正态近似（df≥10 时误差可忽略；n=10 配对各 10 样本）
    from math import erf, sqrt
    p = 2*(1 - 0.5*(1+erf(abs(t)/sqrt(2))))
    return t, df, p

def mann_whitney_u(a, b):
    """按 (值, 组) 排序分配平均秩（处理重复值），R1 = a 组秩和。"""
    combined = sorted([(v, gi) for gi, vals in ((0, a), (1, b)) for v in vals])
    ranks = [0.0] * len(combined)
    i = 0
    while i < len(combined):
        j = i
        while j+1 < len(combined) and combined[j+1][0] == combined[i][0]:
            j += 1
        avg_rank = (i+1+j+1)/2
        for k in range(i, j+1):
            ranks[k] = avg_rank
        i = j+1
    r1 = sum(r for (v, gi), r in zip(combined, ranks) if gi == 0)
    u1 = r1 - len(a)*(len(a)+1)/2
    u2 = len(a)*len(b) - u1
    n1, n2 = len(a), len(b)
    mu = n1*n2/2
    sigma = math.sqrt(n1*n2*(n1+n2+1)/12)
    if sigma == 0:
        return min(u1, u2), 1.0
    z = (min(u1, u2) - mu)/sigma
    from math import erf, sqrt
    p = 2*(1 - 0.5*(1+erf(abs(z)/sqrt(2))))
    return min(u1, u2), p

def cliffs_delta(a, b):
    gt = lt = 0
    for x in a:
        for y in b:
            if x > y: gt += 1
            elif x < y: lt += 1
    n = len(a)*len(b)
    return (gt-lt)/n

def main():
    sm = load_runs(SM_DIR, "sm")
    bare = load_runs(BARE_DIR, "bare")
    lines = ["# SM vs bare 同负载对比（matched 批，2026-11-22）", ""]
    lines.append(f"生成: {datetime.now().astimezone().isoformat(timespec='seconds')}")
    lines.append("口径: 两臂同窗口同负载（2026-11-21 20:30 ~ 11-22 06:50 并发）| judge 同族 qwen3.8-27b | seed=42")
    lines.append("数据: SM 30 run（bug 期间 19 轮从 archive 恢复，recover_sm_matched.py 21/21 映射验证）| bare 30 run")
    lines.append("")
    lines.append("| 题 | 臂 | n | depth mean±SE | 95%CI | nodes mean |")
    lines.append("|---|---|---|---|---|---|")
    for qid in QIDS:
        for arm, data in [("SM", sm), ("bare", bare)]:
            rs = data.get(qid, {})
            deps = [v["depth"] for v in rs.values() if v["depth"] is not None]
            nodes = [v["nodes"] for v in rs.values() if v["nodes"] is not None]
            if not deps:
                lines.append(f"| {qid} | {arm} | 0 | — | — | — |")
                continue
            m = sum(deps)/len(deps)
            se = math.sqrt(sum((x-m)**2 for x in deps)/(len(deps)-1))/math.sqrt(len(deps))
            lo, hi = m-1.96*se, m+1.96*se
            nm = f"{sum(nodes)/len(nodes):.0f}" if nodes else "—"
            lines.append(f"| {qid} | {arm} | {len(deps)} | {m:.4f}±{se:.4f} | [{lo:.3f},{hi:.3f}] | {nm} |")
        lines.append("")
    lines.append("## 配对对比（同题 Δ = SM − bare，独立样本检验）")
    lines.append("")
    lines.append("| 题 | n_sm | n_bare | Δdepth | t | p | U | p_U | Cliff's δ | 结论 |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|")
    for qid in QIDS:
        a = [v["depth"] for v in sm.get(qid, {}).values() if v["depth"] is not None]
        b = [v["depth"] for v in bare.get(qid, {}).values() if v["depth"] is not None]
        if not a or not b:
            lines.append(f"| {qid} | — | — | — | — | — | — | — | — | 数据缺 |")
            continue
        d = sum(a)/len(a) - sum(b)/len(b)
        t, df, p = welch_t(a, b)
        u, pu = mann_whitney_u(a, b)
        cd = cliffs_delta(a, b)
        if min(len(a), len(b)) < 8:
            verdict = f"功效不足，Δ 方向参考"
        else:
            verdict = ("SM 优 ✓" if p < 0.05 and d > 0 else
                       "bare 优 ✓" if p < 0.05 and d < 0 else
                       "不显著（Δ 方向参考）")
        lines.append(f"| {qid} | {len(a)} | {len(b)} | {d:+.4f} | {t:.2f} | {p:.3f} | {u:.0f} | {pu:.3f} | {cd:+.2f} | {verdict} |")
    lines.append("")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w").write("\n".join(lines))
    print("\n".join(lines))
    print(f"\n→ {OUT}")

if __name__ == "__main__":
    main()
