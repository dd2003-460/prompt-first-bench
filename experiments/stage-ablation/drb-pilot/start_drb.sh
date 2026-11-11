#!/bin/bash
# DRB pilot 启动脚本（C3 后由 Lead 落盘）：内存门槛 + pgrep 检查 + nohup 启动
set -u
OUT="drb-pilot"
QID="${1:-drb-1}"
QF="$OUT/queries/$QID.json"
LOG="$OUT/run-$QID-console.log"

# 1. 无同名进程
if pgrep -f "s5_state_machine.py.*$QID" >/dev/null; then
  echo "[$(date '+%F %T')] ABORT: $QID 进程已存在"; exit 1
fi

# 2. free RAM 门槛 ≥8GB
free_gb=$(python3 -c "import subprocess,re;s=subprocess.check_output(['vm_stat']).decode();pg=int(re.search(r'page size of (\d+)',s).group(1));free=int(re.search(r'Pages free:\s+(\d+)',s).group(1));purge=int(re.search(r'Pages purgeable:\s+(\d+)',s).group(1));print(round((free+purge)*pg/1e9,1))")
echo "[$(date '+%F %T')] free+purgeable RAM = ${free_gb}GB (need >=8)"
if python3 -c "exit(0 if $free_gb>=8 else 1)"; then
  :
else
  echo "[$(date '+%F %T')] RAM below threshold — NOT starting"; exit 2
fi

# 3. 启动
nohup python3 s5_state_machine.py --question-file "$QF" --qid "$QID" > "$LOG" 2>&1 &
PID=$!
echo "[$(date '+%F %T')] STARTED $QID pid=$PID log=$LOG"
sleep 20
if kill -0 $PID 2>/dev/null; then
  echo "[$(date '+%F %T')] alive after 20s; head of log:"; tail -5 "$LOG"
else
  echo "[$(date '+%F %T')] DIED within 20s — full log:"; cat "$LOG"
  exit 3
fi
