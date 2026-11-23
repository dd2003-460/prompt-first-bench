#!/usr/bin/env python3
"""healthy_gap_rate 两口径固化 — 84% / 93.5% (draft finding 1 承重数字)

draft line 48 声明: "93.5% of the time (unverifiable ÷ (unverifiable +
contradicted); 84% if the ambiguous class is included in the denominator)
the correct diagnosis is 'unverifiable'".

本脚本从 metacog-budget-scan-v1.1.json (83 runs) 复现两口径:
  - 二分类: sum(n_unverifiable) / sum(n_unverifiable + n_contradicted)
  - 三分类: sum(n_unverifiable) / sum(n_unverifiable + n_contradicted + n_ambiguous)
口径: 83-run corpus (含 K7 15 runs), 全语料聚合 (非 run 级均值)。
Reproduce: python3 healthy-gap-rate-2class.py
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
V11 = os.path.join(HERE, "..", "data", "t53b", "metacog-budget-scan-v1.1.json")

runs = json.load(open(V11))
unv = sum(r["n_unverifiable"] for r in runs)
con = sum(r["n_contradicted"] for r in runs)
amb = sum(r["n_ambiguous"] for r in runs)
n_runs = len(runs)

two = unv / (unv + con)
three = unv / (unv + con + amb)

print(f"83-run corpus (n_runs={n_runs}):")
print(f"  unverifiable={unv}  contradicted={con}  ambiguous={amb}")
print(f"  二分类 84%?  unv/(unv+con) = {unv}/{unv+con} = {two*100:.1f}%")
print(f"  三分类 93.5%? unv/(unv+con+amb) = {unv}/{unv+con+amb} = {three*100:.1f}%")
print(f"\n对照 draft line 48: 93.5% (二分类) / 84% (三分类, 含 ambiguous)")
print(f"对照 T-JUDGE-1 line 479: 4802/5702=84.2% (83 runs) / 4611/5495=83.9% (160 棵全语料)")
