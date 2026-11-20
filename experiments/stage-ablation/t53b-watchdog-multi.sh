#!/bin/bash
# T53b 多路 watchdog（2026-11-20）
# 监控三路 batch（nat/soc/gpu）+ 各路线 SM 进程
# 功能：
#   1. SM 日志 stale 检测（>600s 未更新 → kill SM，driver 捕获 RC 进入 resume）
#   2. batch 进程死亡检测（PID 文件 + kill -0，挂了自动重启对应路线）
#   3. 8787 健康检查（不健康时等 60s 再继续）
# 启动: nohup bash t53b-watchdog-multi.sh > /tmp/t53b-watchdog-multi.log 2>&1 &
set -uo pipefail
cd /Users/a1-6/Desktop/workspace/pfb
STAGE=experiments/stage-ablation
CC_STATE=tasks/T53-bus/cc-state.json
LOG=/tmp/t53b-watchdog-multi.log
WATCHDOG_LOCK=/tmp/t53b-watchdog-multi.lock
SM_STALE_THRESHOLD=1800  # 30 分钟未写日志判定卡死（180s 曾误杀 13 个正常 run，1800s 验证安全）

# single-instance lock
if [ -f "$WATCHDOG_LOCK" ]; then
  OLDW=$(cat "$WATCHDOG_LOCK" 2>/dev/null)
  if [ -n "${OLDW:-}" ] && kill -0 "$OLDW" 2>/dev/null; then
    if ps -p "$OLDW" -o command= 2>/dev/null | grep -qF "t53b-watchdog-multi.sh"; then
      echo "watchdog-multi already running (pid $OLDW), this instance exits" >> "$LOG" 2>/dev/null
      exit 0
    fi
  fi
fi
echo $$ > "$WATCHDOG_LOCK"

log() { echo "[$(date '+%F %H:%M:%S')] $*" >> "$LOG"; }

log "=== 多路 watchdog 启动 (pid $$) ==="

# 按脚本名杀进程树
kill_by_name() {
  local pat="$1" p
  for p in $(ps -axo pid=,command= | grep -F "$pat" | grep -v grep | awk '{print $1}'); do
    kill "$p" 2>/dev/null || true
  done
}

while true; do
  # ── 8787 健康检查 ──
  code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 http://127.0.0.1:8787/health 2>/dev/null)
  if [ "$code" != "200" ]; then
    log "8787 不健康，等 60s"
    sleep 60
    continue
  fi

  # ── 逐路检查 ──
  for QID in nat soc gpu; do
    BATCH_PIDFILE="/tmp/t53b-batch-${QID}.pid"
    BATCH_LOG="/tmp/t53b-batch-${QID}.log"

    # 1. 检查 batch 进程是否存活
    BATCH_ALIVE=0
    if [ -f "$BATCH_PIDFILE" ]; then
      BPID=$(cat "$BATCH_PIDFILE" 2>/dev/null)
      if [ -n "${BPID:-}" ] && kill -0 "$BPID" 2>/dev/null; then
        if ps -p "$BPID" -o command= 2>/dev/null | grep -qF "t53b-batch.sh"; then
          BATCH_ALIVE=1
        fi
      fi
    fi
    if [ "$BATCH_ALIVE" -eq 0 ]; then
      # 回退：ps 扫描（按 qid 过滤，避免误判其他路线）
      if ps -axo command= 2>/dev/null | grep -F "t53b-batch.sh ${QID}" | grep -v grep > /dev/null; then
        BATCH_ALIVE=1
      fi
    fi

    if [ "$BATCH_ALIVE" -eq 0 ]; then
      # 检查该路线是否还有 pending run
      PENDING=$(QID="$QID" python3 -c "
import json, re, os
s=json.load(open('$CC_STATE'))
pat=re.compile(r'^${QID}_(formula|text)_r(\d{2})$')
for wu in s['work_units']:
    if not wu.get('done') and pat.match(wu.get('name','')):
        print(wu['name']); break
")
      if [ -n "$PENDING" ]; then
        log "[$QID] batch 不在，重启"
        nohup bash "$STAGE/t53b-batch.sh" "$QID" >> "$BATCH_LOG" 2>&1 &
        NEWPID=$!
        echo "$NEWPID" > "$BATCH_PIDFILE"
        log "[$QID] restarted batch PID: $NEWPID"
      else
        log "[$QID] 无 pending run，跳过"
      fi
      continue
    fi

    # 2. SM stale 检测：从 batch 日志提取当前 run，检查 SM 日志 mtime
    CUR_RUN=$(grep "开始:" "$BATCH_LOG" 2>/dev/null | tail -1 | sed -E 's/.*开始: ([a-z0-9_]+) \(第.*/\1/')
    if [ -n "$CUR_RUN" ]; then
      SM_LOG="/tmp/t53b/${CUR_RUN}.sm.log"
      if [ -f "$SM_LOG" ]; then
        SM_PID=$(pgrep -f "s5_state_machine.py ${QID}" 2>/dev/null | head -1)
        if [ -n "$SM_PID" ]; then
          NOW=$(date +%s)
          MT=$(stat -f %m "$SM_LOG")
          AGE=$(( NOW - MT ))
          if [ "$AGE" -gt "$SM_STALE_THRESHOLD" ]; then
            # 2026-11-20 误杀修复：日志 stale 不等于卡死——SM 在长 LLM 调用序列期间
            # 不写日志（proxy 日志实证 03:45 误杀时三路都在活跃发请求）。
            # 活性检查：有子进程（curl 检索）或 TCP 连接（等 8787 LLM）= 在干活，跳过。
            CHILDREN=$(pgrep -P "$SM_PID" 2>/dev/null | wc -l | tr -d ' ')
            TCP=$(lsof -p "$SM_PID" 2>/dev/null | grep -c TCP)
            # 2026-11-20 二次修复：children/TCP 都抓不到"纯 Python 处理中"的 SM
            # （无子进程、无连接、日志块缓冲 mtime 假 stale）。加 CPU 时间采样：
            # 5s 内累计 CPU 时间在涨 = 活着。
            C1=$(ps -o time= -p "$SM_PID" 2>/dev/null | tr -d ' ')
            sleep 5
            C2=$(ps -o time= -p "$SM_PID" 2>/dev/null | tr -d ' ')
            if [ -n "$C2" ] && [ "$C2" != "$C1" ]; then
              log "[$QID] SM stale 但 CPU 在动 (pid ${SM_PID}, cpu ${C1}→${C2})，跳过 kill"
              continue
            fi
            if [ "$CHILDREN" -gt 0 ] || [ "$TCP" -gt 0 ]; then
              log "[$QID] SM stale 但活跃 (pid ${SM_PID}, children=${CHILDREN} tcp=${TCP})，跳过 kill"
              continue
            fi
            log "[$QID] SM stale: ${CUR_RUN} 日志 ${AGE}s 未更新 (pid ${SM_PID})，无子进程无连接，kill 恢复"
            # 2026-11-20: kill 前抓栈。py-spy 在 macOS 需 root（后台进程不能 sudo），
            # 改用系统自带 sample（同用户进程免 root，已验证可用）。Python 3.9 无符号，
            # 帧名是 ???，但 call graph 能区分 CPU 递归卡死 vs I/O 等待（实证：
            # 14:16 抓 nat_formula_r05，1392/1392 采样全在主线程递归链上）。
            # 2026-11-20 升级: 先 SIGUSR1 触发 faulthandler dump 全线程 Python 栈
            # 到 .sm.log（SM 入口已注册 faulthandler.register(SIGUSR1)），比 sample
            # 的 ??? 帧能定位到具体 Python 行。sample 保留作 CPU 分布佐证。
            # 门控: SIGUSR1 默认动作是终止进程——旧代码 SM（未注册 faulthandler）
            # 收到会直接死，等于误杀。只有日志含注册标记（新代码进程）才发。
            if grep -q "faulthandler SIGUSR1 registered" "$SM_LOG" 2>/dev/null; then
              kill -USR1 "$SM_PID" 2>/dev/null
              sleep 2
              log "[$QID] 已发 SIGUSR1 抓 Python 栈 → ${SM_LOG} 尾部"
            else
              log "[$QID] SM 为旧代码进程（无 faulthandler 标记），跳过 SIGUSR1 防误杀"
            fi
            if /usr/bin/sample "$SM_PID" 2 -file "/tmp/t53b/${CUR_RUN}.stale-sample.txt" >/dev/null 2>&1; then
              log "[$QID] 已抓 sample 栈 → /tmp/t53b/${CUR_RUN}.stale-sample.txt"
            fi
            kill "$SM_PID" 2>/dev/null
            sleep 3
            if kill -0 "$SM_PID" 2>/dev/null; then
              log "[$QID] SM ${SM_PID} 未退出，SIGKILL"
              kill -9 "$SM_PID" 2>/dev/null
            fi
          fi
        fi
      fi
    fi
  done

  sleep 60
done
