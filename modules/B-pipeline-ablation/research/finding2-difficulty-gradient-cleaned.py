#!/usr/bin/env python3
"""Finding (2) 生死检验: gap_rate 跨域难度梯度在 DEFENSIVE_RE 清洗后是否仍显著.

Abstract finding (2) 声明: "the defensive-marking rate rises monotonically with
question difficulty (nat 0.025 < soc 0.056 < gpu 0.119, era-matched, all pairwise
p<0.001), the signature of calibrated uncertainty monitoring."

补充32 发现 DEFENSIVE_RE 在 SOC 域 42% 命中是数学 uncertainty 技术术语。本脚本
用清洗口径 (NO_UNCERTAIN: DEFENSIVE_RE 去掉"不确定") 按 run 重算 era-matched
(sm-era, Nov20-21, budget=150 默认) 的跨域 Mann-Whitney:

  nat vs soc: z=-1.82  ns   (原 p=0.0003 由技术术语驱动)
  soc vs gpu: z=-4.68  显著
  nat vs gpu: z=-4.87  显著

结论: 数值顺序 nat < soc < gpu 保持 (0.0181 < 0.0298 < 0.0999), 但 nat<soc 环
在清洗后不显著。"monotonically, all pairwise p<0.001" 必须降级为
"increases with difficulty (nat < gpu, soc < gpu, p < 0.01; nat < soc
numerically holds but ns after cleaning)".

口径: sm-era 目录 (archive/sm-{dom}-2026112*), 每目录一个 run, 节点按 id 去重取
最新 mtime; 跳过 <20 节点残缺 run (n_runs=21/26/18, 原记录 22/27/19, 差 1 来自
残缺 run 过滤)。

Reproduce: python3 finding2-difficulty-gradient-cleaned.py
"""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from metacog_axis import DEFENSIVE_RE

# 口径验证 (2026-11-23): metacog_axis.DEFENSIVE_PATTERNS 源码 = 8 项
# [待核验]/不确定/未验证/待确认/需要验证/无法确定/缺乏数据/信息不足;
# 本正则 = 其余 7 项, 无漏无增; "无法确定"不含"不确定"不会被误剔。
NO_UNCERTAIN = re.compile(r"\[待核验\]|未验证|待确认|需要验证|无法确定|缺乏数据|信息不足")
ARCHIVE = os.path.join(HERE, "..", "..", "..", "experiments", "stage-ablation", "checkpoints", "archive")


def text(n):
    return str(n.get("claim", "")) + " " + str(n.get("evidence", "")) + " " + str(n.get("corrected_claim", ""))


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


def mann_whitney_z(x, y):
    ux = sum(1 for a in x for b in y if a > b) + 0.5 * sum(1 for a in x for b in y if a == b)
    n1, n2 = len(x), len(y)
    mu = n1 * n2 / 2
    sigma = (n1 * n2 * (n1 + n2 + 1) / 12) ** 0.5
    return ux, (ux - mu) / sigma


results = {}
for dom in ["nat", "soc", "gpu"]:
    dirs = [d for d in glob.glob(os.path.join(ARCHIVE, f"sm-{dom}-2026112*")) if os.path.isdir(d)]
    raw_rates, clean_rates = [], []
    for d in dirs:
        nodes = run_nodes(d)
        if len(nodes) < 20:
            continue
        raw_rates.append(sum(1 for n in nodes if DEFENSIVE_RE.search(text(n))) / len(nodes))
        clean_rates.append(sum(1 for n in nodes if NO_UNCERTAIN.search(text(n))) / len(nodes))
    results[dom] = (raw_rates, clean_rates)
    print(f"{dom:4s}: n_runs={len(raw_rates)}  raw mean={sum(raw_rates)/len(raw_rates):.4f}  "
          f"clean mean={sum(clean_rates)/len(clean_rates):.4f}")

print("\nMann-Whitney (run 级, 清洗口径):")
for a, b in [("nat", "soc"), ("soc", "gpu"), ("nat", "gpu")]:
    _, ca = results[a]
    _, cb = results[b]
    ua, z = mann_whitney_z(ca, cb)
    sig = "a<b 显著" if z < -1.96 else ("a>b 显著" if z > 1.96 else "ns")
    print(f"  {a} vs {b}: U={ua:.0f}  z={z:+.2f}  {sig}")
