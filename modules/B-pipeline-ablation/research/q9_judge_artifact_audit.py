#!/usr/bin/env python3
"""Q9 预算扫描: judge 伪影可复现审计 (2026-11-27 红队重接地)

背景: retrospective §8 的 +0.43/+0.26/-33% 三个决定性数字当时是
context 内 ad-hoc 算的, 脚本未落盘。本脚本从一手文件重算:
  - judge 分: llm-judge-coverage-20261127.json (per-run n_gates_hit)
  - L1 提及: 节点 claim 提到量化/蒸馏/更小架构 (按节点去重, 非按次数)
  - L2 推导: 节点 claim 同时含 (量化相关词) + (带单位具体数字) — 推导级
  - 预算轴: 50/100/150/300 各档均值

注意: L2 定义是原审计(22/1198)的可复现近似, 原脚本已失;
本定义偏严(要求量化语境+带单位数字同现), 数字与原值可能有出入,
结论看相关方向和预算轴趋势, 不看绝对值。
"""
import json, glob, re, os, statistics

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "q9-budget-scan")
RUNS = sorted(glob.glob(os.path.join(DATA, "q9-*-r*.json")))
JUDGE = json.load(open(os.path.join(DATA, "llm-judge-coverage-20261127.json")))

L1_PAT = re.compile(r"量化|quantiz|NVFP4|\bFP4\b|更小.{0,4}(模型|架构)|蒸馏|distill|参数量|model size", re.I)
NUM_PAT = re.compile(r"\d+(?:\.\d+)?\s*(?:GB|TB|MB|GB/s|TB/s|tokens?/?sec|TFLOP|GFLOP|%|倍|x\b)", re.I)

rows = []
for f in RUNS:
    r = json.load(open(f))
    name = os.path.basename(f)
    bud = name.split("-")[1].split("r")[0]
    nodes = r.get("nodes", [])
    l1 = l2 = 0
    for n in nodes:
        c = n.get("claim") or ""
        if L1_PAT.search(c):
            l1 += 1
            if NUM_PAT.search(c):
                l2 += 1
    rows.append(dict(file=name, bud=int(bud), n=len(nodes), l1=l1, l2=l2,
                     l1d=l1/max(len(nodes),1), l2d=l2/max(len(nodes),1)))

# 挂 judge 分 (per-run n_gates_hit)
for row in rows:
    m = re.match(r"q9-(\d+)-r(\d)", row["file"])
    bud, rr = m.group(1), m.group(2)
    det = JUDGE["detail"].get(bud, {}).get(f"r{rr}")
    row["judge"] = det["n_gates_hit"] if det else None

print(f"{'run':38} {'bud':>4} {'n':>4} {'L1%':>6} {'L2%':>6} {'judge':>5}")
for row in rows:
    jv = row["judge"]
    print(f"{row['file']:38} {row['bud']:>4} {row['n']:>4} "
          f"{row['l1d']*100:>5.1f}% {row['l2d']*100:>5.2f}% {jv if jv is not None else '-':>5}")

def spearman(xs, ys):
    def rank(a):
        o = sorted(range(len(a)), key=lambda i: a[i]); rk=[0]*len(a)
        for p,i in enumerate(o): rk[i]=p
        return rk
    rx, ry = rank(xs), rank(ys)
    mx, my = statistics.mean(rx), statistics.mean(ry)
    num = sum((a-mx)*(b-my) for a,b in zip(rx,ry))
    den = (sum((a-mx)**2 for a in rx)*sum((b-my)**2 for b in ry))**.5
    return num/den if den else float("nan")

ok = [r for r in rows if r["judge"] is not None]
js  = [r["judge"] for r in ok]
l1s = [r["l1d"] for r in ok]
l2s = [r["l2d"] for r in ok]
print(f"\ncorr(judge, L1密度) = {spearman(js,l1s):+.3f}")
print(f"corr(judge, L2密度) = {spearman(js,l2s):+.3f}")

# 预算轴
axis = {}
for r in rows:
    axis.setdefault(r["bud"], []).append(r)
print("\n预算轴 (均值):")
prev = None
for b in sorted(axis):
    g = axis[b]
    jm = statistics.mean([r["judge"] for r in g if r["judge"] is not None])
    l1 = statistics.mean([r["l1d"] for r in g])*100
    l2 = statistics.mean([r["l2d"] for r in g])*100
    delta = f"  judge {prev[0]:.2f}->{jm:.2f} ({(jm/prev[0]-1)*100:+.0f}%), L2 {prev[1]:.2f}%->{l2:.2f}% ({(l2/prev[1]-1)*100:+.0f}%)" if prev else ""
    print(f"  bud {b:>4}: judge={jm:.2f}  L1={l1:.1f}%  L2={l2:.2f}%{delta}")
    prev = (jm, l2)

out = dict(per_run=rows,
           corr_judge_l1=round(spearman(js,l1s),3),
           corr_judge_l2=round(spearman(js,l2s),3))
dst = os.path.join(DATA, "judge-artifact-audit-20261127.json")
json.dump(out, open(dst,"w"), ensure_ascii=False, indent=2)
print(f"\n落盘 {os.path.relpath(dst, DATA)}")
