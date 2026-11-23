#!/usr/bin/env python3
"""Finding (2) 难度梯度的字段分解 — 梯度由哪个字段驱动?

承重发现 (2026-11-23): finding (2) "难度梯度 nat<soc<gpu" 用 pooled gap_rate
(claim+evidence+corrected_claim)。本脚本分解 claim vs evidence 字段:
  - claim (监控轴 a): nat 0.0162 < soc 0.0261 < gpu 0.0921 — 梯度完整保持
  - evidence (核验阶段 b/c): nat 0.0026 < soc 0.0045 < gpu 0.0089 — 梯度弱, 量级小
  - evidence 占 pooled 仅 9-15%
结论: 难度梯度是**监控轴 (claim 字段) 现象**, 不是核验文本现象。
     finding (2) 的核心落在 detector-robust 的监控轴上 — 强化论文。

口径: 与 finding2-difficulty-gradient-cleaned.py 完全一致 (sm-era, node.json 递归,
按 id/mtime 去重, 跳过 <20 节点, NO_UNCERTAIN 7-pattern 清洗口径)。
Reproduce: python3 finding2-field-decomposition.py
"""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from metacog_axis import DEFENSIVE_RE

NO_UNCERTAIN = re.compile(r"\[待核验\]|未验证|待确认|需要验证|无法确定|缺乏数据|信息不足")
ARCHIVE = os.path.join(HERE, "..", "..", "..", "experiments", "stage-ablation", "checkpoints", "archive")


def run_nodes(adir):
    best = {}
    for f in glob.glob(adir + "/**/node.json", recursive=True):
        try:
            n = json.load(open(f))
        except Exception:
            continue
        nid = n.get("id")
        if nid is None:
            continue
        mt = os.path.getmtime(f)
        if nid not in best or mt > best[nid][0]:
            best[nid] = (mt, n)
    return [v[1] for v in best.values()]


print(f"{'域':>4} {'n_runs':>6} {'pooled':>8} {'claim':>8} {'evidence':>9} {'ev%':>5}")
for dom in ["nat", "soc", "gpu"]:
    dirs = [d for d in glob.glob(os.path.join(ARCHIVE, f"sm-{dom}-2026112*")) if os.path.isdir(d)]
    pooled, claim, ev = [], [], []
    for d in dirs:
        nodes = run_nodes(d)
        if len(nodes) < 20:
            continue
        n = len(nodes)
        pooled.append(sum(1 for x in nodes if NO_UNCERTAIN.search(
            str(x.get('claim', '')) + ' ' + str(x.get('evidence', '')) + ' ' + str(x.get('corrected_claim', '')))) / n)
        claim.append(sum(1 for x in nodes if NO_UNCERTAIN.search(str(x.get('claim', '')))) / n)
        ev.append(sum(1 for x in nodes if NO_UNCERTAIN.search(str(x.get('evidence', '')))) / n)
    pm, cm, em = sum(pooled) / len(pooled), sum(claim) / len(claim), sum(ev) / len(ev)
    print(f"{dom:>4} {len(pooled):>6} {pm:>8.4f} {cm:>8.4f} {em:>9.4f} {em/pm*100:>4.0f}%")

print("\n结论: 难度梯度由 claim 字段 (监控轴) 驱动 (85-91% of pooled),")
print("      evidence 字段贡献小 (9-15%) — finding (2) 是监控轴现象, detector-robust")
