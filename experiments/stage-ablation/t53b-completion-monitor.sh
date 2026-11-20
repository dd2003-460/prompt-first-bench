#!/bin/bash
# T53b 完成监控（2026-11-20）：poll cc-state，全 done 或 watchdog 死亡时退出
# 用法: nohup bash t53b-completion-monitor.sh > /tmp/t53b-completion-monitor.log 2>&1 &
# 退出码: 0=全done, 1=watchdog死亡需介入, 2=超时(48h)
cd /Users/a1-6/Desktop/workspace/pfb
CC_STATE=tasks/T53-bus/cc-state.json
LOG=/tmp/t53b-completion-monitor.log
START=$(date +%s)
TIMEOUT=$((48*3600))
while true; do
  if ! pgrep -f "t53b-watchdog-multi.sh" > /dev/null 2>&1; then
    echo "[$(date '+%F %T')] watchdog 死亡，退出需介入" >> "$LOG"
    exit 1
  fi
  STATE=$(python3 -c 'import json;s=json.load(open("tasks/T53-bus/cc-state.json"));u=s["work_units"];print(sum(1 for x in u if x.get("done")),len(u))' 2>/dev/null)
  DONE=$(echo "$STATE" | awk '{print $1}')
  TOTAL=$(echo "$STATE" | awk '{print $2}')
  if [ -n "$DONE" ] && [ "$DONE" -ge "$TOTAL" ] 2>/dev/null; then
    echo "[$(date '+%F %T')] 全部完成 $DONE/$TOTAL" >> "$LOG"
    exit 0
  fi
  NOW=$(date +%s)
  if [ $(( (NOW - START) % 7200 )) -lt 300 ]; then
    echo "[$(date '+%F %T')] 进度 $DONE/$TOTAL" >> "$LOG"
  fi
  if [ $(( NOW - START )) -gt $TIMEOUT ]; then
    echo "[$(date '+%F %T')] 超时 48h，进度 $DONE/$TOTAL" >> "$LOG"
    exit 2
  fi
  sleep 180
done
