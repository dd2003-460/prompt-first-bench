#!/bin/bash
# pipeline-snapshot-loop.sh — 定期重算 pipeline-state.json（幂等，崩溃安全）
# 独立于 batch/watchdog，不碰 SM 代码和 corpus。
# 启动: nohup bash pipeline-snapshot-loop.sh > /tmp/pipeline-snapshot.log 2>&1 &
# 单实例锁
LOCK=/tmp/pipeline-snapshot.lock
if [ -f "$LOCK" ]; then
  OLD=$(cat "$LOCK" 2>/dev/null)
  if [ -n "${OLD:-}" ] && kill -0 "$OLD" 2>/dev/null; then
    echo "already running (pid $OLD), exit" >> /tmp/pipeline-snapshot.log
    exit 0
  fi
fi
echo $$ > "$LOCK"
SNAP=/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation/pipeline_snapshot.py
INTERVAL=${SNAP_INTERVAL:-600}
while true; do
  python3 "$SNAP" >> /tmp/pipeline-snapshot.log 2>&1
  sleep "$INTERVAL"
done
