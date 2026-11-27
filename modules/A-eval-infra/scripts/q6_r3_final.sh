#!/bin/bash
# 719-r3 落地后一键分析 (2026-11-23 22:20)
# 等 q6-719-r3-*.json 出现 → 打分 → 域内/跨域 cov 分解 → CUR mon_claim → 停止原因 → repair 15runs
# 纪律: 绝对 python 路径 (后台 PATH 缺 sentence_transformers, 4e9c175db 坑), stderr 落盘, 不碰运行中进程
PY=/usr/bin/python3
SCAN=/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/q6-budget-scan
BPL=/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation
LOG=/tmp/q6-r3-final.log
echo "=== r3-final started $(date '+%F %T') ===" | tee "$LOG"
F=""
for i in $(seq 1 120); do
  F=$(ls "$SCAN"/q6-719-r3-[0-9]*.json 2>/dev/null | head -1)
  [ -n "$F" ] && break
  sleep 60
done
if [ -z "$F" ]; then
  echo "=== r3 json not found after 120min, abort ===" | tee -a "$LOG"
  exit 1
fi
echo "=== r3 landed: $F $(date '+%F %T') ===" | tee -a "$LOG"
# 停止原因 (承重归因核验: max_depth vs max_nodes vs DONE)
echo "--- stop reason ---" | tee -a "$LOG"
grep -E "max_depth=|max_nodes=|DONE" "$SCAN/q6-719-r3.stdout" | tail -3 | tee -a "$LOG"
# 打分 + 分解
cd "$BPL" && $PY - <<'EOF' 2>&1 | tee -a "$LOG"
import sys, json, glob, re
sys.path.insert(0, '.')
from judge_v1 import judge_run
from metacog_axis import load_run_nodes
f = sorted(glob.glob('data/q6-budget-scan/q6-719-r3-[0-9]*.json'))[0]
gq = json.load(open('data/gold-q6-units.json'))
gg = json.load(open('gold-gpu-units.json'))
gq_units = gq['units'] if isinstance(gq, dict) else gq
gg_units = gg['units'] if isinstance(gg, dict) else gg
rj_q = judge_run(f, gold_units=gq_units)
rj_g = judge_run(f, gold_units=gg_units)
print(f"r3 in-domain cov (Q6 gold 46): {rj_q['layers']['coverage']['coverage']:.4f} "
      f"({rj_q['layers']['coverage']['n_confirmed']}/46) depth={rj_q['layers']['structure']['depth_score']} "
      f"total={rj_q['total_score']:.4f}")
print(f"r3 cross-domain cov (GPU gold 36): {rj_g['layers']['coverage']['coverage']:.4f} "
      f"({rj_g['layers']['coverage']['n_confirmed']}/36)")
CUR = re.compile(r'\[待核验\]|不确定|未验证|待确认|需要验证|无法确定|缺乏数据|信息不足')
nodes = load_run_nodes(f)
hits = sum(1 for n in nodes if CUR.search(n.get('claim', '')))
print(f"r3 CUR claim: {hits}/{len(nodes)} = {hits/len(nodes):.4f}")
# repair 15 runs (固化口径: rework_count>0 且最终 verified)
files = sorted(glob.glob('data/q6-budget-scan/q6-*-r*-[0-9]*.json'))
tot_rw = tot_fix = 0
for x in files:
    r = json.load(open(x))
    for n in r.get('nodes', []):
        try: rc = int(n.get('rework_count', 0) or 0)
        except Exception: rc = 0
        if rc > 0:
            tot_rw += 1
            if n.get('status') == 'verified': tot_fix += 1
print(f"repair 跨域 ({len(files)} runs): {tot_fix}/{tot_rw} = {tot_fix/tot_rw*100:.1f}%")
EOF
# 追加 scores (幂等: q6_rescore 按 budget,rep 去重)
$PY research/q6_rescore.py 2>&1 | tail -3 | tee -a "$LOG"
echo "=== r3-final done $(date '+%F %T') ===" | tee -a "$LOG"
