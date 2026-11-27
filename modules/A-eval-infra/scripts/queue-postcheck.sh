#!/bin/bash
# origin: ai · 2026-11-25 · 队列 DONE 后自动核验 watcher
# 作用: 等 post-pilot 队列 PID 退出 → 跑 queue-verify.py(5 项产物鉴别力) → 跑 l4-disambig-judge.py(A/B/C/D 判读)
# 落盘: logs/queue-postcheck-<ts>.log (两个脚本的完整输出)
# 用法: background=true 起, 完成后 notify
set -uo pipefail
PFB=/Users/a1-6/Desktop/workspace/pfb
SA=$PFB/experiments/stage-ablation
QUEUE_PID=${1:?用法: queue-postcheck.sh <queue_pid>}
TS=$(date +%Y%m%d-%H%M%S)
OUT=$SA/logs/queue-postcheck-$TS.log
echo "[$(date '+%H:%M:%S')] POSTCHECK-START waiting queue PID=$QUEUE_PID" | tee "$OUT"
while kill -0 "$QUEUE_PID" 2>/dev/null; do sleep 120; done
echo "[$(date '+%H:%M:%S')] queue PID=$QUEUE_PID exited, running verification" | tee -a "$OUT"

# 队列日志路径(最新一个)
QL=$(ls -t "$SA"/logs/post-pilot-queue-*.log 2>/dev/null | head -1)
echo "queue log: $QL" | tee -a "$OUT"

# 1) 产物鉴别力核验(存在+新鲜+非退化)
( cd "$SA" && python3 queue-verify.py "$QL" ) >> "$OUT" 2>&1
echo "queue-verify rc=$?" >> "$OUT"

# 2) L4-disambig 判读(A/B/C/D, 机械判定)
( cd "$SA" && python3 "$PFB/modules/B-pipeline-ablation/research/l4-disambig-judge.py" "$SA" ) >> "$OUT" 2>&1
echo "l4-judge rc=$?" >> "$OUT"

echo "[$(date '+%H:%M:%S')] POSTCHECK-DONE out=$OUT" | tee -a "$OUT"
