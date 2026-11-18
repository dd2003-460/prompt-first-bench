#!/bin/bash
# T53b watchdog：批量执行器挂了自动重启
# 2026-11-19 修复（诊断报告 /tmp/monitor-diagnosis-20261119-0246.md）：
#   1. 进程检测改用 PID 文件 + kill -0（原 pgrep -f "t53b-batch.sh" 在 bash 解释器
#      argv 被截断时匹配失败 → 误判 batch 死亡 → 每分钟重启 → 02:46-02:57 共 12 条
#      进程树并存，11 个 SM 并发写同一组 checkpoint 互相污染）
#   2. 重启前强制清场：杀掉任何残留的 batch/driver/SM 进程（防双 SM 写冲突），
#      并清掉当前 pending qid 的旧树形 ckpt 目录（SM 会从中 resume 出污染状态）
set -uo pipefail
cd /Users/a1-6/Desktop/workspace/pfb
STAGE=experiments/stage-ablation
CC_STATE=tasks/T53-bus/cc-state.json
LOG=/tmp/t53b-watchdog.log
BATCH_PIDFILE=/tmp/t53b-batch.pid

log() { echo "[$(date '+%F %H:%M:%S')] $*" >> "$LOG"; }

# 按脚本名杀进程树（driver/SM 用；batch 用 PID 文件，避免 pgrep -f 自匹配/截断问题）
kill_by_name() {
  local pat="$1" p
  for p in $(ps -axo pid=,command= | grep -F "$pat" | grep -v grep | awk '{print $1}'); do
    kill "$p" 2>/dev/null || true
  done
}

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

  # ── 检测 batch 是否存活：优先 PID 文件 + kill -0；PID 文件缺失/失效时回退 ps 扫描 ──
  BATCH_ALIVE=0
  if [ -f "$BATCH_PIDFILE" ]; then
    BPID=$(cat "$BATCH_PIDFILE" 2>/dev/null)
    if [ -n "${BPID:-}" ] && kill -0 "$BPID" 2>/dev/null; then
      # 二次确认该 PID 确实是 batch 脚本（防 PID 复用误判）
      if ps -p "$BPID" -o command= 2>/dev/null | grep -qF "t53b-batch.sh"; then
        BATCH_ALIVE=1
      fi
    fi
  fi
  if [ "$BATCH_ALIVE" -eq 0 ]; then
    # 回退：ps 扫描（grep -F 固定串，避免正则/截断问题）
    if ps -axo command= 2>/dev/null | grep -qF "t53b-batch.sh"; then
      BATCH_ALIVE=1
    fi
  fi

  if [ "$BATCH_ALIVE" -eq 0 ]; then
    # ── 重启前强制清场（2026-11-19 事故修复）──
    # 旧逻辑"SM/driver 还在跑就等"在 12 条进程树并存时永远等不到，且等待期间
    # 多 SM 持续互相污染 checkpoint。新逻辑：直接杀掉所有残留，保证重启后
    # 全机只有 watchdog 启动的这一条 batch 树。
    RESID=$(ps -axo command= 2>/dev/null | grep -cE "ablation_driver\.sh|s5_state_machine\.py" || true)
    if [ "$RESID" -gt 0 ]; then
      log "发现 $RESID 个残留 driver/SM 进程，强制清场（防双 SM 写冲突）"
      kill_by_name "ablation_driver.sh"
      kill_by_name "s5_state_machine.py"
      sleep 5
      # 二次确认，杀不掉的（D 状态）再 SIGKILL
      for p in $(ps -axo pid=,command= 2>/dev/null | grep -E "ablation_driver\.sh|s5_state_machine\.py" | grep -v grep | awk '{print $1}'); do
        kill -9 "$p" 2>/dev/null || true
      done
      sleep 2
    fi
    # 清掉当前 pending qid 的旧树形 ckpt 目录（SM 启动时会从中 resume，
    # 残留的污染状态会让新 run 从坏状态继续）
    QID="${PENDING%%_*}"
    CKPT_DIR="$STAGE/checkpoints/sm-${QID}-r${PENDING##*_r}"
    if [ -d "$CKPT_DIR" ]; then
      log "清残留 ckpt 树: $CKPT_DIR"
      rm -rf "$CKPT_DIR"
    fi
    # commit + 重启（写 PID 文件供下轮检测）
    log "批量执行器不在，清场后重启"
    cd /Users/a1-6/Desktop/workspace/pfb
    git add tasks/T53-bus/cc-state.json \
            experiments/stage-ablation/ablation-runs/ \
            experiments/stage-ablation/ablation-notes/ \
            experiments/stage-ablation/ablation-results.json 2>/dev/null
    git commit -m "T53b: watchdog checkpoint (batch driver died, resuming)" 2>/dev/null >> "$LOG"
    nohup bash "$STAGE/t53b-batch.sh" >> /tmp/t53b-batch.log 2>&1 &
    NEWPID=$!
    echo "$NEWPID" > "$BATCH_PIDFILE"
    log "已重启 PID: $NEWPID（断点续跑：从 cc-state.json 读第一个 pending）"
  fi

  sleep 60
done

log "=== watchdog 结束 ==="
