#!/bin/bash
# 接力链 v2 (2026-11-23 23:35, D 指令"不要限制深度"后重排):
# 重跑批 (pid 25483) 退出 → 30s → Q6 719 无深度墙批 (3 rep, ~2.5h) → Q7 扫描 (15 runs, ~11h)
# 优先级: Q6 719 无深度墙 > Q7 — 前者直接补 draft 核心 claim (干净预算测试), 后者是第三域扩展
RERUN_PID=25483
LOG=/tmp/relay-v2.log
echo "=== relay-v2 started $(date '+%F %T'), waiting for rerun $RERUN_PID ===" | tee "$LOG"
while kill -0 "$RERUN_PID" 2>/dev/null; do
  sleep 60
done
echo "=== rerun $RERUN_PID exited $(date '+%F %T'), sleeping 30s ===" | tee -a "$LOG"
sleep 30
echo "=== phase 1: q6-719-nodepth $(date '+%F %T') ===" | tee -a "$LOG"
bash /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation/q6_719_nodepth_queue.sh >> "$LOG" 2>&1
echo "=== phase 2: q7 scan $(date '+%F %T') ===" | tee -a "$LOG"
bash /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation/q7_budget_scan_queue.sh >> "$LOG" 2>&1
echo "=== relay-v2 all done $(date '+%F %T') ===" | tee -a "$LOG"
