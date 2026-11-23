#!/usr/bin/env python3
"""拆墙 r1 vs 原批 719 三 rep: 命中集重叠对照 (2026-11-24)

问题: 拆墙 r1 (719 节点) 与原批 r3 (197 节点) 命中集只共享 3/6 unit。
这是深度展开的效应, 还是 run-to-run 方差?
对照: 原批 719 三 rep (r1=351, r2=379, r3=197 节点) 之间的两两重叠。
若原批 rep 间重叠也低 (~3-4/6-9) → run-to-run 方差主导, 3/6 无特殊含义。
若原批 rep 间重叠高 (~6-7/6-9) → 方差小, 拆墙 r1 的 3/6 特别低 → 深度展开改变覆盖内容。
对象: Q6 域, 46-unit gold, thr=0.70。
"""
import sys, os, json, glob
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "modules", "B-pipeline-ablation"))
from judge_v1 import load_run_nodes
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-m3")
gu = json.load(open(os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "gold-q6-units.json")))
gu = gu["units"] if isinstance(gu, dict) and "units" in gu else gu
gemb = model.encode([u["text"] for u in gu], normalize_embeddings=True, show_progress_bar=False)
print(f"Q6 gold units: {len(gu)}")

def hit(runf, thr=0.70):
    nodes = load_run_nodes(runf)
    nemb = model.encode([n["claim"] for n in nodes], normalize_embeddings=True, show_progress_bar=False)
    sim = nemb @ gemb.T
    return set(j for j in range(len(gu)) if sim[:, j].max() >= thr), len(nodes)

# 原批 719 三 rep
Q6D = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "q6-budget-scan")
ND = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "q6-719-nodepth")
hits = {}
for rep in [1, 2, 3]:
    fs = glob.glob(os.path.join(Q6D, f"q6-719-r{rep}-*.json"))
    if fs:
        h, n = hit(fs[0])
        hits[f"orig-r{rep}"] = (h, n)
        print(f"orig-r{rep} (n={n}): {len(h)}/46 = {sorted(h)}")
    else:
        print(f"!! orig-r{rep} 文件未找到")
# 拆墙 r1
nd = os.path.join(ND, "q6-719-nd-r1-20261124-034034.json")
h, n = hit(nd)
hits["nd-r1"] = (h, n)
print(f"nd-r1 (n={n}): {len(h)}/46 = {sorted(h)}")

# 两两重叠
names = list(hits.keys())
print("\n两两重叠 (交集/较小集):")
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        a, na = hits[names[i]]
        b, nb = hits[names[j]]
        inter = a & b
        print(f"  {names[i]} ∩ {names[j]}: {len(inter)}/min({len(a)},{len(b)}) = {sorted(inter)}")

# unit 性质: 拆墙 r1 新增/丢失 (vs orig-r3)
nd_set = hits["nd-r1"][0]
o3_set = hits["orig-r3"][0]
print("\n拆墙 r1 新增 unit (vs orig-r3):")
for j in sorted(nd_set - o3_set):
    print(f"  unit {j}: {gu[j]['text'][:80]}")
print("\n拆墙 r1 丢失 unit (vs orig-r3):")
for j in sorted(o3_set - nd_set):
    print(f"  unit {j}: {gu[j]['text'][:80]}")

json.dump({k: {"units": sorted(v[0]), "n_nodes": v[1]} for k, v in hits.items()},
          open(os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "nodepth-r1-vs-orig-hits-20261124.json"), "w"),
          indent=1, ensure_ascii=False)
print("\n落盘 nodepth-r1-vs-orig-hits-20261124.json")
