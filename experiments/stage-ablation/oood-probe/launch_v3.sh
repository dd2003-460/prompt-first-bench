#!/bin/bash
# V3 队列（M3b）: 8787 单实例串行, 6 reps
# 顺序: V3 cyclone 3 → V3 hw 3（埋雷域剔除: 题面含埋雷数据, 注入"质疑题面"会泄雷, 测不干净）
# 幂等: ckpt 存在则 SKIP（runner 内置）
# 用法: bash launch_v3.sh            真实启动
#       DRY_RUN=1 bash launch_v3.sh  只 echo 不执行
set -u
cd "$(dirname "$0")"
LOG=v3-queue.log
PIDF=v3-queue.pid

CMDS=(
  "python3 run_v1_sm.py v3 cyclone 1"
  "python3 run_v1_sm.py v3 cyclone 2"
  "python3 run_v1_sm.py v3 cyclone 3"
  "python3 run_v1_sm.py v3 hw 1"
  "python3 run_v1_sm.py v3 hw 2"
  "python3 run_v1_sm.py v3 hw 3"
)

if [ "${DRY_RUN:-0}" = "1" ]; then
  echo "# DRY RUN — ${#CMDS[@]} reps:"
  i=0
  for c in "${CMDS[@]}"; do i=$((i+1)); echo "$i. $c"; done
  exit 0
fi

QS=.v3-queue-body.sh
{
  echo "echo '=== V3 queue start \$(date +%Y-%m-%d %T) ==='"
  i=0
  for c in "${CMDS[@]}"; do
    i=$((i+1))
    echo "echo \"[$i/${#CMDS[@]}] start \$(date +%T): $c\""
    echo "$c"
    echo "echo \"[$i/${#CMDS[@]}] exit=\$? \$(date +%T)\""
  done
  echo "echo '=== V3 queue end \$(date +%Y-%m-%d %T) ==='"
} > "$QS"

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
