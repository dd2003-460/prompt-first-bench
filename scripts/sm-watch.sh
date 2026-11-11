#!/bin/bash
# sm-watch: 盯 s5_state_machine 运行，只在"有更新"时发通知（用户 2026-11-12 要求：别爆炸，有更新再叫）
# 用法: ./scripts/sm-watch.sh <log_file> [max_hours]
# 触发条件（任一）:
#   1. 出现新的 "[SM] rN:" 轮次行（新轮完成）
#   2. 出现 FATAL/LEAK/STOP/DONE/max_nodes/max_depth
#   3. 进程消失且日志无 DONE（异常死亡）
# 静默期: 每 120s 检查一次，无变化不发任何消息。
LOG="$1"
MAX_H="${2:-8}"

LAST_SIG=""

sig() {
  # 签名 = 最新轮次行 + 关键事件计数 + 最新节点总数
  local last_round events nodes
  last_round=$(grep -o "\[SM\] r[0-9]*:" "$LOG" 2>/dev/null | tail -1)
  events=$(grep -c "FATAL\|LEAK in decompose\|\[SM\] STOP\|DONE:\|max_nodes=\|max_depth=" "$LOG" 2>/dev/null)
  nodes=$(grep -o "total [0-9]*" "$LOG" 2>/dev/null | tail -1)
  echo "${last_round}|${events}|${nodes}"
}

START_TS=$(date +%s)
while true; do
  ELAPSED=$(( ($(date +%s) - START_TS) / 3600 ))
  if [ "$ELAPSED" -ge "$MAX_H" ]; then
    osascript -e "display notification \"sm-watch: ${MAX_H}h 超时退出\" with title \"T53 SM\"" 2>/dev/null
    break
  fi

  CUR_SIG=$(sig)
  if [ "$CUR_SIG" != "$LAST_SIG" ] && [ -n "$CUR_SIG" ]; then
    LAST_SIG="$CUR_SIG"
    MSG=$(grep "\[SM\]" "$LOG" 2>/dev/null | tail -3 | tr '\n' ' ' | cut -c1-200)
    osascript -e "display notification \"$MSG\" with title \"T53 SM 更新\"" 2>/dev/null
    echo "$(date '+%H:%M:%S') NOTIFY: $MSG" >> "${LOG}.watch-log"
  fi

  # 进程死亡检测
  if ! pgrep -f "s5_state_machine.py" > /dev/null 2>&1; then
    if grep -q "DONE:" "$LOG" 2>/dev/null; then
      osascript -e "display notification \"r-run DONE — $(grep DONE: '$LOG' | tail -1 | cut -c1-150)\" with title \"T53 SM 完成\"" 2>/dev/null
      echo "$(date '+%H:%M:%S') DONE detected" >> "${LOG}.watch-log"
    else
      osascript -e "display notification \"进程已退出但无 DONE — 可能崩溃，查日志尾部\" with title \"T53 SM 异常\"" 2>/dev/null
      echo "$(date '+%H:%M:%S') PROCESS DIED without DONE" >> "${LOG}.watch-log"
    fi
    break
  fi

  sleep 120
done