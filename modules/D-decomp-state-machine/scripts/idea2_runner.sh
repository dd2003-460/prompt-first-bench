#!/bin/bash
# Idea 2: checkpoint-as-cache 一致性实验 (2026-11-22)
# A 臂: 从头跑 (L0→L4 全新生成)
# B 臂: --resume 从 r2 checkpoint (L1=6+L2=28+L3=88 固定前缀, 只续拆 L3+)
# 同 budget 150 (--max-nodes 150), 各 3 reps, 记 wall time
# 输出: data/idea2/idea2-<arm>-r<rep>-<ts>.json + idea2-manifest.json
set -u
cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
OUT=/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/idea2
mkdir -p "$OUT"
CKPT="checkpoints/archive/budget-150-r1-20261122-093447/sm-gpu-r2"
LOG="$OUT/idea2-run.log"
echo "=== idea2 start $(date '+%F %T') ===" >> "$LOG"

run_arm() {
  local arm=$1 rep=$2
  local extra=""
  [ "$arm" = "B" ] && extra="--resume $CKPT"
  local t0=$(date +%s)
  python3 s5_state_machine.py gpu --max-nodes 150 $extra > "$OUT/idea2-${arm}-r${rep}.stdout" 2>&1
  local rc=$?
  local t1=$(date +%s)
  local dur=$((t1 - t0))
  local ts=$(date '+%Y%m%d-%H%M%S')
  if [ -f runs-s5-sm-gpu.json ]; then
    cp runs-s5-sm-gpu.json "$OUT/idea2-${arm}-r${rep}-${ts}.json"
    echo "arm=$arm rep=$rep rc=$rc wall_s=$dur out=idea2-${arm}-r${rep}-${ts}.json" | tee -a "$LOG"
  else
    echo "arm=$arm rep=$rep rc=$rc wall_s=$dur out=MISSING" | tee -a "$LOG"
  fi
  # 清掉本轮 checkpoint 目录, 防 B 臂 rep2 探测到 rep1 的 sm-gpu-r* 续跑
  rm -rf checkpoints/sm-gpu-r* 2>/dev/null
}

for rep in 1 2 3; do
  run_arm A $rep
  run_arm B $rep
done
echo "=== idea2 done $(date '+%F %T') ===" >> "$LOG"
