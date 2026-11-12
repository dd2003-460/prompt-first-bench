#!/bin/bash
# DRB pilot 启动脚本（C3 后由 Lead 落盘）：内存门槛 + pgrep 检查 + nohup 启动
set -u
cd "$(dirname "$0")/../.."
OUT="experiments/stage-ablation/drb-pilot"
QID="${1:-drb-1}"
QF="$OUT/queries/$QID.json"
LOG="$OUT/run-$QID-console.log"

# 1. 无同名进程
if pgrep -f "s5_state_machine.py.*$QID" >/dev/null; then
  echo "[$(date '+%F %T')] ABORT: $QID 进程已存在"; exit 1
fi

# 2. RAM 门槛：free+purgeable ≥8GB 硬过；否则看 inactive（macOS 压力下自动换出，可回收）≥16GB 软过
free_gb=$(python3 -c "import subprocess,re;s=subprocess.check_output(['vm_stat']).decode();pg=int(re.search(r'page size of (\d+)',s).group(1));g=lambda k:int(re.search(k+r':\s+(\d+)',s).group(1))*pg/1e9;print(f\"{g('Pages free')+g('Pages purgeable'):.1f} {g('Pages inactive'):.1f}\")")
FREE=${free_gb% *}; INACT=${free_gb#* }
echo "[$(date '+%F %T')] free+purgeable=${FREE}GB inactive=${INACT}GB (hard: free>=8 | soft: inactive>=16)"
if python3 -c "exit(0 if $FREE>=8 or $INACT>=16 else 1)"; then
  :
else
  echo "[$(date '+%F %T')] RAM below both thresholds — NOT starting"; exit 2
fi

# 3. 启动（cwd=repo root；PYTHONPATH 指向 stage-ablation，因为 s5_state_machine import ablation_harness/s5_pipeline）
export PYTHONPATH="experiments/stage-ablation:${PYTHONPATH:-}"
nohup python3 experiments/stage-ablation/s5_state_machine.py --question-file "$QF" --qid "$QID" > "$LOG" 2>&1 &
PID=$!
echo "[$(date '+%F %T')] STARTED $QID pid=$PID log=$LOG"
sleep 20
if kill -0 $PID 2>/dev/null; then
  echo "[$(date '+%F %T')] alive after 20s; head of log:"; tail -5 "$LOG"
else
  echo "[$(date '+%F %T')] DIED within 20s — full log:"; cat "$LOG"
  exit 3
fi
