#!/usr/bin/env python3
"""阈值悬崖 vs 形状结论 robustness (2026-11-24)

扰动测试发现 cov 对阈值是悬崖 (0.65=0.496 / 0.70=0.3185 / 0.80=0.015)。
本脚本回答最狠的一刀: 形状结论 (cor(cov, n_nodes) + 分箱单调性) 在阈值悬崖下保持吗?
若 cor 在 0.65/0.70/0.75 都高且分箱单调 → 平台/上升结论对阈值 robust (阈值只缩放绝对值);
若 cor 随阈值塌 → 形状结论本身是阈值 artifact, 承重声明需降级。
对象: GPU K7 15 棵 archive 树 (cor=0.563 的 30 树口径的一半, 方向性检查)。
"""
import sys, os, json, glob, statistics as st, math
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "modules", "B-pipeline-ablation"))
from judge_v1 import load_gold, load_run_nodes, layer_coverage
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-m3")
gold = load_gold("gpu")
ARCH = os.path.join(ROOT, "experiments", "stage-ablation", "checkpoints", "archive")
runs = sorted(glob.glob(os.path.join(ARCH, "budget-*-r*", "runs-s5-sm-gpu.json")))
runs = [r for r in runs if "rerun" not in r and "nodepth" not in r][:15]
nodes_list = [load_run_nodes(r) for r in runs]
nn = [len(n) for n in nodes_list]

def cor(x, y):
    mx, my = st.mean(x), st.mean(y)
    den = math.sqrt(sum((a-mx)**2 for a in x)) * math.sqrt(sum((b-my)**2 for b in y))
    return sum((a-mx)*(b-my) for a, b in zip(x, y)) / den if den else None

def bins(covs, lo_hi=(0,200,400,600,800)):
    edges = [0,200,400,600,800]
    out=[]
    for i in range(len(edges)-1):
        sel=[c for c,n in zip(covs,nn) if edges[i]<=n<edges[i+1]]
        out.append((f"{edges[i]}-{edges[i+1]}", len(sel), round(st.mean(sel),4) if sel else None))
    return out

print(f"{'thr':>5} {'mean':>7} {'cor':>7}  bins (0-200/200-400/400-600/600-800)")
results=[]
for thr in [0.65, 0.70, 0.75, 0.80]:
    covs=[]
    for nodes in nodes_list:
        s,_ = layer_coverage(nodes, gold, model, thr)
        covs.append(s)
    c = cor(nn, covs)
    b = bins(covs)
    mono = all(b[i][2] <= b[i+1][2]+1e-9 for i in range(len(b)-1) if b[i][2] is not None and b[i+1][2] is not None)
    bstr = " / ".join(f"{x[0]}:{x[2]}(n={x[1]})" for x in b)
    print(f"{thr:>5} {st.mean(covs):>7.4f} {c:>7.4f}  {bstr}  mono={mono}")
    results.append({"thr": thr, "mean": round(st.mean(covs),4), "cor": round(c,4) if c else None,
                    "bins": b, "monotonic": mono})
json.dump(results, open(os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "threshold-shape-robustness-20261124.json"), "w"), indent=1)
print("\n落盘 threshold-shape-robustness-20261124.json")
