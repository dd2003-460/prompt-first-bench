#!/bin/bash
# T53b watchdog：批量执行器挂了自动重启
set -uo pipefail
cd /Users/a1-6/Desktop/workspace/pfb
STAGE=experiments/stage-ablation
CC_STATE=tasks/T53-bus/cc-state.json
LOG=/tmp/t53b-watchdog.log

log() { echo "[$(date '+%F %H:%M:%S')] $*" >> "$LOG"; }

log "=== watchdog 启动 (pid $$) ==="

while true; do
  code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 http://127.0.0.1:8787/health 2>/dev/null)
  if [ "$code" != "200" ]; then
    log "8787 不健康，等 60s"
    sleep 60
    continue
  fi

  PENDING=$(python3 -c "
import json, re
s=json.load(open('$CC_STATE'))
pat=re.compile(r'^(gpu|nat|soc)_(formula|text)_r(\d{2})$')
for wu in s['work_units']:
    if not wu.get('done') and pat.match(wu.get('name','')):
        print(wu['name']); break
")

  if [ -z "$PENDING" ]; then
    log "全部完成，watchdog 退出"
    break
  fi

  if ! pgrep -f "t53b-batch.sh" > /dev/null 2>&1; then
    # 防双 SM：如果 SM 或 driver 还在跑（批量执行器被 kill 但孙进程存活），
    # 等它们完成记账后再重启，否则两个 SM 写同一组 checkpoint 会冲突
    if pgrep -f "s5_state_machine.py" > /dev/null 2>&1; then
      log "批量执行器不在但 SM 还在跑，等 SM 完成（防双 SM 冲突）"
      sleep 60
      continue
    fi
    if pgrep -f "ablation_driver.sh" > /dev/null 2>&1; then
      log "批量执行器不在但 driver 还在跑（judge/记账中），等它完成"
      sleep 60
      continue
    fi
    # 安全了：没有 SM/driver 在跑，commit + 重启
    log "批量执行器不在且无 SM/driver 残留，commit 后重启"
    cd /Users/a1-6/Desktop/workspace/pfb
    git add tasks/T53-bus/cc-state.json \
            experiments/stage-ablation/ablation-runs/ \
            experiments/stage-ablation/ablation-notes/ \
            experiments/stage-ablation/ablation-results.json 2>/dev/null
    git commit -m "T53b: watchdog checkpoint (batch driver died, resuming)" 2>/dev/null >> "$LOG"
    bash "$STAGE/t53b-batch.sh" >> /tmp/t53b-batch.log 2>&1 &
    log "已重启 PID: $!（断点续跑：从 cc-state.json 读第一个 pending）"
  fi

  sleep 60
done

log "=== watchdog 结束 ==="
