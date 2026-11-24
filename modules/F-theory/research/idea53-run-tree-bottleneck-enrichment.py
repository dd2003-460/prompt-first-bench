#!/usr/bin/env python3
"""#53 深层节点信息贡献 — run 树侧瓶颈内容富集测量 (2026-11-23, e413443f5).

测量: gold 瓶颈#1 内容 (占空比 duty_demand) 在 run 树的 level 分布 + verified 率,
对照全体节点基线, 判富集是否显著.

轴陷阱 (承重): run 树 level (L1-L4, judge 层) ≠ gold 主干深度 (结构分支 5 层),
两轴不可直接映射. 本脚本只测 run 树自身坐标系 (judge 层轴).

口径:
- 锚点: gold 瓶颈#1 = duty_demand (业务需求占空比), 正则 占空比|duty (case-insensitive)
- 节点: claim+evidence+corrected_claim 全字段 json.dumps 后匹配
- 基线: 全体节点 level 分布 + verified 率
- 树: rep-scan/*.json (排除 era-matched* 和 scores), n_nodes>=20

skill rule 14: 逐文件验字段存在性 (level/status 缺失的节点跳过不默认),
自变量退化检查 (level 取值 <3 个时富集不可解释).

⚠ 基率伪影修正 (2026-11-24, 见 idea53-supply-bottleneck-enrichment.py):
本脚本 duty 锚点基率仅 0.4% (稀缺), 测得 L4 富集 1.51x. 但 10 个不同基率锚点
对照显示 基率(log) 与 L4 富集倍数 r=-0.930: 高频类别词 (量化 58.8%/显存 47.4%/
TCO 36.3%) 富集全 ≈1.0x. 即 1.51x 部分是"稀缺锚点集中结论层"的基率伪影,
不能与供给侧宽口径 (基率 19%, 富集 1.10x) 跨锚点直接比大小. 解读富集倍数
必须带基率. 供需两侧同落 L4 → L4 是"瓶颈判定层"类别属性, 非供需差异.
"""
import json, glob, re, sys
from collections import Counter

ANCHOR = re.compile(r'占空比|duty', re.I)
FILES = [f for f in glob.glob('modules/B-pipeline-ablation/data/rep-scan/*.json')
         if 'era-matched' not in f and 'scores' not in f]

lv_all = Counter(); st_all = Counter(); n = 0
lv_hit = Counter(); st_hit = Counter(); n_hit = 0
qid_set = set(); n_trees = 0
missing_field = 0

for f in FILES:
    d = json.load(open(f))
    if not isinstance(d, dict) or 'nodes' not in d:
        continue
    nodes = d['nodes']
    if len(nodes) < 20:
        continue
    n_trees += 1
    qid_set.add(d.get('qid'))
    for nd in nodes:
        lv = nd.get('level'); st = nd.get('status')
        if lv is None or st is None:
            missing_field += 1
            continue
        n += 1
        lv_all[lv] += 1; st_all[st] += 1
        text = json.dumps(nd, ensure_ascii=False)
        if ANCHOR.search(text):
            n_hit += 1
            lv_hit[lv] += 1; st_hit[st] += 1

print(f"qid: {qid_set} | 树 {n_trees} 棵 | 节点 {n} (缺字段跳过 {missing_field})")
print(f"锚点命中节点: {n_hit}")
if n_hit == 0:
    print("无命中, 退出"); sys.exit(1)

# 自变量退化检查
lv_vals = sorted(lv_all)
if len(lv_vals) < 3:
    print(f"⚠ level 取值退化: {lv_vals}, 富集不可解释"); sys.exit(2)

print("\n=== level 分布 (锚点 vs 全体) ===")
for lv in lv_vals:
    a = lv_all[lv]/n; h = lv_hit.get(lv,0)/n_hit
    print(f"  {lv}: 全体 {lv_all[lv]:4d} ({a:.0%}) | 锚点 {lv_hit.get(lv,0):3d} ({h:.0%}) | 富集比 {h/a if a else float('nan'):.2f}x")

print("\n=== verified 率 ===")
va = st_all.get('verified',0)/n; vh = st_hit.get('verified',0)/n_hit
print(f"  全体 verified: {va:.0%} | 锚点 verified: {vh:.0%} | Δ {vh-va:+.0%}")
print(f"  锚点 status: {dict(st_hit.most_common())}")
