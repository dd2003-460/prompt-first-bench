#!/bin/bash
# s1 mining V0 基线补跑（M3 队列缺口修复）: 3 reps 串行, 幂等(ckpt 存在则跳过)
# 用法: bash launch_s1_mining.sh   (DRY_RUN=1 只 echo)
set -u
cd "$(dirname "$0")"
CKPT_DIR=m3-ckpt
declare -a CMDS=("python3 run_v1_sm.py s1 mining 1" "python3 run_v1_sm.py s1 mining 2" "python3 run_v1_sm.py s1 mining 3")
i=0
for c in "${CMDS[@]}"; do
  i=$((i+1))
  rep=${c##* }
  ck="$CKPT_DIR/m3-s1-mining-r${rep}.json"
  if [ -f "$ck" ]; then echo "[skip $i/3] $ck exists"; continue; fi
  if [ "${DRY_RUN:-0}" = "1" ]; then echo "[dry $i/3] $c"; continue; fi
  echo "[$i/3] start $(date +%T): $c"
  eval "$c"
  echo "[$i/3] exit=$? $(date +%T)"
done
echo "=== s1-mining V0 queue end $(date +%Y-%m-%d\ %T) ==="
