#!/bin/bash
# Q7 接力 watchdog (2026-11-23 23:15 重启): rep 独立重跑队列 (pid 25483, 23:11:42 重启) 跑完 → 30s → 起 Q7 扫描队列
# 前置纪律: 不并发 (vLLM NVFP4+MTP 并发非确定), 等重跑批完全结束再起 Q7
# 23:12 事故: 旧 watchdog 盯 10045(被杀), 25483 还在跑时 Q7 就提前启动 → 已杀 Q7, 本 watchdog 改盯 25483
RERUN_PID=25483
LOG=/tmp/q7-relay-watchdog.log
echo "=== q7-relay started $(date '+%F %T'), waiting for rerun $RERUN_PID ===" | tee "$LOG"
while kill -0 "$RERUN_PID" 2>/dev/null; do
  sleep 60
done
echo "=== rerun $RERUN_PID exited $(date '+%F %T'), sleeping 30s ===" | tee -a "$LOG"
sleep 30
bash /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation/q7_budget_scan_queue.sh >> "$LOG" 2>&1
echo "=== q7 queue finished $(date '+%F %T') ===" | tee -a "$LOG"
