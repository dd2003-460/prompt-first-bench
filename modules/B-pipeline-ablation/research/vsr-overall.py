#!/usr/bin/env python3
"""weighted vsr overall 承重数字固化 — 0.5636 (draft §4.1 / abstract)

draft 声明: "weighted vsr 0.5636 (359 candidates, 220 reachable = 61%)".

口径 (url-retention-gap.py 同口径):
  - 19 树 = 21 树 − 2 棵 idea2 r3 (retrieval channel outage, 2026-11-23)
  - weighted vsr = sum(verified) / sum(reachable) = 124/220 = 0.5636
  - reach rate = sum(reachable) / sum(cand) = 220/359 = 61%
  - 数据源: data/source-verify.json (21 条, 含 2 棵 r3)
Reproduce: python3 vsr-overall.py
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SV = os.path.join(HERE, "..", "data", "source-verify.json")

d = json.load(open(SV))
# 排除 2 棵 idea2 r3 (channel outage)
excl = [x for x in d if not (x["fam"] == "idea2" and "-r3-" in x["tag"])]
tot_cand = sum(x["n_cand"] for x in excl)
tot_reach = sum(x["reachable"] for x in excl)
tot_v = sum(x["verified"] for x in excl)

print(f"19 树 (21 − 2 idea2 r3 channel outage):")
print(f"  cand={tot_cand}  reach={tot_reach}  V={tot_v}")
print(f"  weighted vsr = V/reach = {tot_v}/{tot_reach} = {tot_v/tot_reach:.4f}  (目标 0.5636)")
print(f"  reach rate = reach/cand = {tot_reach}/{tot_cand} = {tot_reach/tot_cand*100:.0f}%  (目标 61%)")
