#!/usr/bin/env python3
"""L4 zero-convergence 0/21 承重数字固化 — draft finding 3 (abstract 核心)

draft 声明: "the L4 conclusion layer (mechanical, bias-immune) never converges
to the gold winner at any budget tier (0/21 strict, §4.4)".

口径 (T-JUDGE-1-L4-20261123.md + tjudge1_formula.l4_check):
  - 21 棵 GPU 树 = K7 budget 15 (budget-*/runs-s5-sm-gpu-synth.json, 真 answer 版;
    非 synth 版 answer 字段恒空, 2026-11-25 修复前误读)
    + idea2 6 (data/idea2/idea2-{A,B}-r{1,2,3}*.json; 无 answer 字段,
    结论散在节点 claim 里 → 0/6 恒成立, 节点 claim 3090×4 组合=0 已独立核验)
  - L4 strict: answer 最后 2000 字符出现 gold winner 配置组合
    (card_model × n_cards, gold-gpu-formulas.json ref_config)
  - 机械判定, 无 LLM, bias-immune
Reproduce: python3 l4-zero-convergence.py
"""
import json, glob, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from tjudge1_formula import l4_check

ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
ARCH = os.path.join(ROOT, "experiments", "stage-ablation", "checkpoints", "archive")
IDEA2 = os.path.join(HERE, "..", "data", "idea2")
SIDECAR = os.path.join(HERE, "..", "gold-gpu-formulas.json")

trees = []
# K7 15: budget-*/runs-s5-sm-gpu-synth.json (2026-11-25 修复: 原读非 synth 版,
# 其 answer 字段恒为空 → 0/15 是"空串不含 3090×4"的空验证, 数据换掉脚本照样输出 0/21。
# synth 版才是真 answer(18-26K 字符合成报告), 0/15 用 synth 真 answer 手工复判确认仍成立。)
for f in sorted(glob.glob(os.path.join(ARCH, "budget-*", "runs-s5-sm-gpu-synth.json"))):
    trees.append(("K7", os.path.basename(os.path.dirname(f)), f))
# idea2 6: 只取树文件(排除 idea2-scores.json 评分文件)
for f in sorted(glob.glob(os.path.join(IDEA2, "idea2-*.json"))):
    if f.endswith("-scores.json"):
        continue
    trees.append(("idea2", os.path.basename(f), f))

n = 0
hits = 0
for fam, name, f in trees:
    try:
        strict, det = l4_check(f, SIDECAR)
    except Exception as e:
        print(f"  {fam:6s} {name:40s} ERROR: {e}")
        continue
    n += 1
    hits += int(strict)
    print(f"  {fam:6s} {name:40s} strict={int(strict)}  loose={det['loose']}  full={det['full_combo']}")

print(f"\nL4 strict: {hits}/{n}  (目标 0/21)")
print(f"结论: {'0/21 复现 ✓' if hits == 0 and n == 21 else '与目标不符 ✗'}")
