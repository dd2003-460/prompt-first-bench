#!/bin/bash
# origin: ai · 2026-11-25 · T-REPAIR-1 完成后自动分析 watcher
# 作用: 等 T-REPAIR-1 4 臂执行器 PID 退出 → 跑 t-repair1-analysis.py(4 臂析因 + P-A/P-B/P-A+B 判别)
# 落盘: logs/t-repair1-postcheck-<ts>.log
# 用法: background=true 起, 完成后 notify
set -uo pipefail
PFB=/Users/a1-6/Desktop/workspace/pfb
SA=$PFB/experiments/stage-ablation
BJ=$PFB/modules/B-pipeline-ablation
TR1_PID=${1:?用法: t-repair1-postcheck.sh <t-repair1_pid>}
TS=$(date +%Y%m%d-%H%M%S)
OUT=$SA/logs/t-repair1-postcheck-$TS.log
echo "[$(date '+%H:%M:%S')] TR1-POSTCHECK-START waiting T-REPAIR-1 PID=$TR1_PID" | tee "$OUT"
while kill -0 "$TR1_PID" 2>/dev/null; do sleep 180; done
echo "[$(date '+%H:%M:%S')] T-REPAIR-1 PID=$TR1_PID exited, running analysis" | tee -a "$OUT"

# 先核验 4 臂产物齐全(12 runs json), 缺则标 FAIL 但仍跑分析(分析脚本自身会报臂数不足)
N_RUNS=$(find "$BJ/data/t-repair1/arms" -name '*.json' 2>/dev/null | wc -l | tr -d ' ')
echo "arms runs json count: $N_RUNS (expect 12)" | tee -a "$OUT"

( cd "$BJ/research" && python3 t-repair1-analysis.py ) >> "$OUT" 2>&1
echo "analysis rc=$?" >> "$OUT"

echo "[$(date '+%H:%M:%S')] TR1-POSTCHECK-DONE out=$OUT" | tee -a "$OUT"
