#!/bin/bash
# 719 落地后自动接 rep 独立重跑 (2026-11-23 21:12)
# 原队列 pid 11929 结束 → 等 30s (vLLM 负载释放) → 起 q6_budget_scan_rerun_rep.sh
# 前置纪律: 不并发 (vLLM NVFP4+MTP 并发非确定), 不碰原批输出目录
ORIG_PID=11929
LOG=/tmp/q6-rerun-watchdog.log
echo "=== watchdog started $(date '+%F %T'), waiting for $ORIG_PID ===" | tee "$LOG"
while kill -0 "$ORIG_PID" 2>/dev/null; do
  sleep 60
done
echo "=== orig queue $ORIG_PID exited $(date '+%F %T'), sleeping 30s ===" | tee -a "$LOG"
sleep 30
bash /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation/q6_budget_scan_rerun_rep.sh >> "$LOG" 2>&1
echo "=== rerun queue finished $(date '+%F %T') ===" | tee -a "$LOG"
