#!/bin/bash
# v13 (pure abstract few-shot) × 50 reps stability run
set -u
cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
REPS=50
OUT="runs-s5-gpu-v13"
LOG="$OUT/run.log"
mkdir -p "$OUT"
echo "[$(date '+%F %T')] === v13 stability run start (reps=$REPS) ===" >> "$LOG"
for ((r=1; r<=REPS; r++)); do
  if [[ -f "$OUT/S5-gpu-r${r}.json" ]]; then
    echo "[$(date '+%F %T')] r$r already done — skip" >> "$LOG"
    continue
  fi
  echo "[$(date '+%F %T')] r$r start" >> "$LOG"
  python3 s5_pipeline.py --qs gpu --reps 1 --out "$OUT" >> "$LOG" 2>&1 \
    | grep -E "P1:|P1.5:|P2/P3 done|P4\+J|CACHE-HIT|WEBLLM" >> "$LOG"
  echo "[$(date '+%F %T')] r$r end" >> "$LOG"
done
echo "[$(date '+%F %T')] === v13 done: $(ls $OUT/*.json 2>/dev/null | wc -l | tr -d ' ') reps ===" >> "$LOG"
echo "ALL DONE v13"