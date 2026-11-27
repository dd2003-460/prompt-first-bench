#!/usr/bin/env python3
"""验收 + 决策树输入聚合: mech-level-scan 结果 → mech_rate(budget, level)。
用法: python3 q9_mech_scan_accept.py
验收: ① counts_by_level total 和=1198 ② 3 条 mech_samples 回溯原 json ③ calibration 字段存在 ④ commit 存在
输出: 决策树输入表 (budget × level 的 mech_rate) + 验收 PASS/FAIL
"""
import json, glob, re, sys, subprocess

BASE = '/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/B-pipeline-ablation'
RES = f'{BASE}/data/q9-budget-scan/mech-level-scan-20261127.json'
RUNS = sorted(glob.glob(f'{BASE}/data/q9-budget-scan/q9-*-r*.json'))

fails = []
try:
    d = json.load(open(RES))
except Exception as e:
    print(f"FAIL: 结果 JSON 不存在/不可读: {e}"); sys.exit(1)

# ① totals
tot = sum(v.get('total', 0) for v in d.get('counts_by_level', {}).values())
if tot != 1198: fails.append(f"totals={tot} != 1198")

# ② 回溯 3 条 mech_samples
src = {}
for f in RUNS:
    tag = f.split('/')[-1][:10]
    for n in json.load(open(f))['nodes']:
        src[(tag, str(n.get('id')))] = (n.get('claim') or '')
miss = 0
for s in (d.get('mech_samples') or [])[:3]:
    c = src.get((s.get('run'), str(s.get('id'))), '')
    if s.get('claim_excerpt', '')[:40] not in c: miss += 1
if miss: fails.append(f"{miss}/3 mech_samples 回溯失败")

# ③ calibration
cal = d.get('calibration')
if cal is None: fails.append("缺 calibration 字段")

# ④ commit
log = subprocess.run(['git', '-C', '/Users/a1-6/Desktop/workspace/pfb-thinkmech', 'log', '--oneline', '-5'], capture_output=True, text=True).stdout
if '机制级' not in log and 'mech' not in log.lower(): fails.append("未见 mech 扫描 commit")

# 决策树输入: budget × level 的 mech_rate
def budget_of(tag):
    m = re.match(r'q9-(\d+)-r', tag)
    return m.group(1) if m else '?'
agg = {}
for tag, v in d.get('counts_by_run', {}).items():
    b = budget_of(tag)
    a = agg.setdefault(b, {'total': 0, 'mech': 0, 'by_level': {}})
    a['total'] += v.get('total', 0); a['mech'] += v.get('mech', 0)
lvl_agg = {}
for lv, v in d.get('counts_by_level', {}).items():
    lvl_agg[lv] = (v.get('mech', 0), v.get('total', 0))

print("=== 验收 ===")
print("PASS" if not fails else "FAIL: " + "; ".join(fails))
print("\n=== 决策树输入: mech_rate(budget) ===")
for b in sorted(agg):
    a = agg[b]
    print(f"  budget {b}: mech {a['mech']}/{a['total']} = {a['mech']/max(a['total'],1):.3f}")
print("\n=== mech_rate(level) ===")
for lv in sorted(lvl_agg):
    m, t = lvl_agg[lv]
    print(f"  {lv}: {m}/{t} = {m/max(t,1):.3f}")
print(f"\ncalibration: {json.dumps(cal, ensure_ascii=False)[:300] if cal else 'MISSING'}")
print(f"conclusion: {d.get('conclusion')}")
