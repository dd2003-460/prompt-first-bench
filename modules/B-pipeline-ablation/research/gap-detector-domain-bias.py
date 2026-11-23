#!/usr/bin/env python3
"""gap_rate 检测器域偏检验 — budget-invariance 的 detector-robustness

承重发现 (2026-11-23): 论文核心 finding "budget-invariance" (ANOVA F=0.036)
用现用 8-pattern 闭集检测器算。本脚本对比现用 vs 扩展检测器:
  - 现用 8 pattern: [待核验]/不确定/未验证/待确认/需要验证/无法确定/缺乏数据/信息不足
  - 扩展: + 无法验证/无法确认/无法核实/未能核实/未能确认/无法查证/缺乏.*来源/
          无.*来源/未.*找到/存疑/缺乏.*支持/缺乏.*标准/缺乏.*依据/无.*支持
    (扩展 pattern 从 Q6/GPU 实际防御措辞抽样归纳, 命中已人工验证为真防御)

口径: 与 metacog_axis.compute_metacog 一致, 扫 claim+evidence+corrected_claim。
发现:
  - 现用检测器对 GPU 漏检 ~75% (0.10→0.41), 对 Q6 漏检 77-97%
  - 现用下 GPU gap 随 budget 平坦 (0.093/0.097/0.109) → invariance
  - 扩展下 GPU gap 随 budget 上升 (0.39/0.40/0.43) → invariance 不成立
  - 结论: budget-invariance 不是 detector-robust, gap_rate 是域偏下界
"""
import json, glob, os, re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
REP = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "rep-scan")
SCAN = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "q6-budget-scan")

CUR = re.compile(r'\[待核验\]|不确定|未验证|待确认|需要验证|无法确定|缺乏数据|信息不足')
EXT = re.compile(r'\[待核验\]|不确定|未验证|待确认|需要验证|无法确定|缺乏数据|信息不足'
                 r'|无法验证|无法确认|无法核实|未能核实|未能确认|无法查证'
                 r'|缺乏.*来源|无.*来源|未.*找到|存疑|缺乏.*支持|缺乏.*标准|缺乏.*依据|无.*支持')


def gap_rates(nodes):
    n = len(nodes)
    if n == 0:
        return 0.0, 0.0
    c = e = 0
    for nd in nodes:
        txt = (nd.get('claim', '') + ' ' + nd.get('evidence', '') +
               ' ' + nd.get('corrected_claim', ''))
        if CUR.search(txt):
            c += 1
        if EXT.search(txt):
            e += 1
    return c / n, e / n


def main():
    # GPU rep-scan 分 budget
    by_tier = defaultdict(lambda: [0, 0, 0])  # tier -> [cur, ext, n]
    for f in sorted(glob.glob(os.path.join(REP, "rep-*.json"))):
        if f.endswith("scores.json"):
            continue
        m = re.search(r"rep-(\d+)-r(\d+)", os.path.basename(f))
        if not m:
            continue
        t = int(m.group(1))
        d = json.load(open(f))
        c, e = gap_rates(d.get("nodes", []))
        n = len(d.get("nodes", []))
        by_tier[t][0] += c * n
        by_tier[t][1] += e * n
        by_tier[t][2] += n

    print("GPU rep-scan 分 budget (现用 vs 扩展 gap_rate):")
    print(f"  {'tier':>5} {'n':>6} {'现用':>8} {'扩展':>8}")
    for t in sorted(by_tier):
        cur, ext, n = by_tier[t]
        print(f"  {t:>5} {n:>6} {cur/n:>8.4f} {ext/n:>8.4f}")

    # Q6 分 budget (队列跑完才有全 5 档)
    q6_tier = defaultdict(lambda: [0, 0, 0])
    for f in sorted(glob.glob(os.path.join(SCAN, "q6-*.json"))):
        if f.endswith("scores.json"):
            continue
        m = re.search(r"q6-(\d+)-r(\d+)-", os.path.basename(f))
        if not m:
            continue
        t = int(m.group(1))
        d = json.load(open(f))
        c, e = gap_rates(d.get("nodes", []))
        n = len(d.get("nodes", []))
        q6_tier[t][0] += c * n
        q6_tier[t][1] += e * n
        q6_tier[t][2] += n
    if q6_tier:
        print("\nQ6 分 budget (现用 vs 扩展 gap_rate):")
        print(f"  {'tier':>5} {'n':>6} {'现用':>8} {'扩展':>8}")
        for t in sorted(q6_tier):
            cur, ext, n = q6_tier[t]
            print(f"  {t:>5} {n:>6} {cur/n:>8.4f} {ext/n:>8.4f}")

    print("\n结论: budget-invariance (现用下 GPU 平坦) 在扩展检测器下不成立 (随 budget 升)")
    print("      → gap_rate 是闭集 regex 的域偏下界, invariance 非 detector-robust")


if __name__ == "__main__":
    main()
