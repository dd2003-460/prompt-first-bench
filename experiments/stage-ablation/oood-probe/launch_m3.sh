#!/bin/bash
# M3 夜间队列：8787 单实例串行，11 reps
# 顺序: V1 cyclone 3 → V1 mining 3 → V0(s1) cyclone 2 → V1 hw 3
# 每 rep 独立 ckpt (m3-ckpt/m3-<arm>-<domain>-r<rep>.json)，runner 内置幂等（ckpt 存在则 SKIP）
# 串行: 单个脱离进程内 for 循环逐个跑（前一个退出才起下一个，8787 不并发）
# 脱离会话: macOS 无 setsid 二进制 → python fork+os.setsid 等价脱离（新会话，不随本进程组回收）
# 用法: ./launch_m3.sh            真实启动
#       DRY_RUN=1 ./launch_m3.sh  只 echo 不执行
set -u
cd /Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation
LOG=oood-probe/m3-queue.log
PIDF=oood-probe/m3-queue.pid

CMDS=(
  "python3 oood-probe/run_v1_sm.py v1 cyclone 1"
  "python3 oood-probe/run_v1_sm.py v1 cyclone 2"
  "python3 oood-probe/run_v1_sm.py v1 cyclone 3"
  "python3 oood-probe/run_v1_sm.py v1 mining 1"
  "python3 oood-probe/run_v1_sm.py v1 mining 2"
  "python3 oood-probe/run_v1_sm.py v1 mining 3"
  "python3 oood-probe/run_v1_sm.py s1 cyclone 1"
  "python3 oood-probe/run_v1_sm.py s1 cyclone 2"
  "python3 oood-probe/run_v1_sm.py v1 hw 1"
  "python3 oood-probe/run_v1_sm.py v1 hw 2"
  "python3 oood-probe/run_v1_sm.py v1 hw 3"
)

if [ "${DRY_RUN:-0}" = "1" ]; then
  echo "# DRY RUN — ${#CMDS[@]} reps:"
  i=0
  for c in "${CMDS[@]}"; do i=$((i+1)); echo "$i. $c"; done
  exit 0
fi

# 串行队列体：单进程内逐个跑，写同一日志（here-doc 生成临时队列脚本，跑完即删）
QS=oood-probe/.m3-queue-body.sh
{
  echo "echo '=== M3 queue start \$(date +%F %T) ==='"
  i=0
  for c in "${CMDS[@]}"; do
    i=$((i+1))
    echo "echo \"[\$i/${#CMDS[@]}] start \$(date +%T): $c\""
    echo "$c"
    echo "echo \"[\$i/${#CMDS[@]}] exit=\$? \$(date +%T)\""
  done
  echo "echo '=== M3 queue end \$(date +%F %T) ==='"
} > "$QS"

# fork → setsid → bash 队列脚本；stdout/stderr 追加进 LOG；真实 PID 写 PIDF
pid=$(python3 -c '
import os, sys
pid = os.fork()
if pid == 0:
    os.setsid()
    fd = os.open(sys.argv[1], os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    os.dup2(fd, 1); os.dup2(fd, 2)
    os.execvp("/bin/bash", ["/bin/bash", sys.argv[2]])
print(pid)
' "$LOG" "$QS")
echo "$pid" > "$PIDF"
rm -f "$QS"
echo "launched serial queue pid=$pid (log=$LOG, pidfile=$PIDF, ${#CMDS[@]} reps)"
