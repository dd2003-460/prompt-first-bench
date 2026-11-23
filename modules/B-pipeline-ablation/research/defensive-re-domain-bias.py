#!/usr/bin/env python3
"""DEFENSIVE_RE 域偏倚审计 + 清洗后三域 (a)<->(b) 耦合复算.

发现 (2026-11-23): metacog_axis.DEFENSIVE_RE 在 nat/soc 上把数学技术术语
"不确定" (uncertainty 概念, 如 "不确定性高" / "σ_pref 正相关" / "量化不确定性")
误判为防御性语言。GPU 的缺口文本是 "[质询]...参考来源仅提供了概述" (真检索批判),
nat/soc 大量是 "不确定" 技术语境。

清洗口径: 节点 = 真防御性 当且仅当 命中 DEFENSIVE_RE 中至少一个
非"不确定"的词 (即 NO_UNCERTAIN 正则命中)。仅命中"不确定" = 技术术语, 排除。

复算三域耦合 (与补充29/31 同口径, 仅清洗技术术语), 看耦合在清洗后是否仍显著.

Reproduce: python3 defensive-re-domain-bias.py
"""
import glob, json, os, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from metacog_axis import DEFENSIVE_RE

# DEFENSIVE_RE 去掉"不确定" (技术术语) 后的对照正则
NO_UNCERTAIN = re.compile(r"\[待核验\]|未验证|待确认|需要验证|无法确定|缺乏数据|信息不足")


def text(n):
    return str(n.get("claim", "")) + " " + str(n.get("evidence", "")) + " " + str(n.get("corrected_claim", ""))


def is_def_full(n):
    return bool(DEFENSIVE_RE.search(text(n)))


def is_def_clean(n):
    # 至少命中一个非"不确定"的防御性词
    return bool(NO_UNCERTAIN.search(text(n)))


def load_dom(dom):
    seen = set()
    nodes = []
    for f in glob.glob(f"experiments/stage-ablation/checkpoints/archive/sm-{dom}-*/sm-{dom}-r*/**/node.json", recursive=True):
        try:
            n = json.load(open(f))
        except Exception:
            continue
        k = (n.get("id"), str(n.get("level", "")), n.get("source"), n.get("status"), str(n.get("claim", ""))[:60])
        if k in seen:
            continue
        seen.add(k)
        nodes.append(n)
    return nodes


def load_rep():
    nodes = []
    for f in glob.glob("modules/B-pipeline-ablation/data/rep-scan/rep-*.json"):
        if f.endswith("scores.json"):
            continue
        t = json.load(open(f))
        nodes += t if isinstance(t, list) else t.get("nodes", [])
    return nodes


def two_prop_z(p1, n1, p2, n2):
    if n1 == 0 or n2 == 0:
        return float("nan")
    p = (p1 * n1 + p2 * n2) / (n1 + n2)
    if not (0 < p < 1):
        return float("nan")
    return (p1 - p2) / (p * (1 - p) * (1 / n1 + 1 / n2)) ** 0.5


def sf(ns):
    return sum(1 for n in ns if n.get("source") == "search") / len(ns) if ns else 0.0


print("=== 域偏倚: DEFENSIVE_RE 命中里多少是仅'不确定' (技术术语) ===")
for label, nodes in [("GPU", load_rep()), ("NAT", load_dom("nat")), ("SOC", load_dom("soc"))]:
    full = [n for n in nodes if is_def_full(n)]
    clean = [n for n in full if is_def_clean(n)]
    tech_only = [n for n in full if not is_def_clean(n)]
    print(f"  {label:4s}: DEF命中={len(full)}  真防御性={len(clean)}  仅'不确定'(技术)={len(tech_only)} "
          f"({len(tech_only) / max(len(full),1) * 100:.0f}%)")

print("\n=== 清洗后三域 (a)<->(b) 耦合 (真防御性 vs 非, search 占比) ===")
for label, nodes in [("GPU", load_rep()), ("NAT", load_dom("nat")), ("SOC", load_dom("soc"))]:
    d = [n for n in nodes if is_def_clean(n)]
    nd = [n for n in nodes if not is_def_clean(n)]
    sd, sn = sf(d), sf(nd)
    z = two_prop_z(sd, len(d), sn, len(nd))
    print(f"  {label:4s}: def={len(d):4d}  def_search={sd:.3f}  nondef_search={sn:.3f}  "
          f"diff={sd - sn:+.3f}  z={z:+.2f}")
