#!/bin/bash
# 12h 稳定性长跑：每个 S5 版本跑满 50 reps（统计下限），自动切版本。
# 检索走 .research-cache/（同 query 命中直接读文件，不打 DDG/Perplexity）。
# LLM 步骤（P1/P1.5/verify）不缓存 —— 那才是被测量对象，需要跨 rep 独立。
# 用户指令 2026-11-08：保留各版本、聪明复用稳定步骤、别碰登录态会话。
set -u
cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation

REPS=50          # 每版本样本量（两版本对比 α=0.05 power=0.8 的下限，见 chat 推导）
MAX_HOURS=12     # 总预算
START=$(date +%s)

for V in v12 v13; do
  OUT="runs-s5-gpu-$V"
  mkdir -p "$OUT"
  LOG="$OUT.log"
  echo "[$(date '+%F %T')] === $V start (reps=$REPS, out=$OUT) ===" >> "$LOG"

  # 跑满 REPS 或到总预算为止
  for ((r=1; r<=REPS; r++)); do
    ELAPSED=$(( ($(date +%s) - START) / 3600 ))
    if (( ELAPSED >= MAX_HOURS )); then
      echo "[$(date '+%F %T')] MAX_HOURS reached at $V r$r — stopping." >> "$LOG"
      break 2
    fi
    # 单 rep；--reps 1 每次新进程，避免内存累积。断点续跑：已有 rN.json 则跳过
    if [[ -f "$OUT/S5-gpu-r${r}.json" ]]; then
      echo "[$(date '+%F %T')] $V r$r already done — skip" >> "$LOG"
      continue
    fi
    echo "[$(date '+%F %T')] $V r$r start" >> "$LOG"
    python3 s5_pipeline.py --qs gpu --reps 1 --out "$OUT" >> "$LOG" 2>&1 \
      | grep -E "P1:|P1.5:|P2/P3 done|P4\+J|CACHE-HIT|WEBLLM" >> "$LOG"
    echo "[$(date '+%F %T')] $V r$r end" >> "$LOG"
  done
  echo "[$(date '+%F %T')] === $V done: $(ls $OUT/*.json 2>/dev/null | wc -l | tr -d ' ') reps ===" >> "$LOG"
done

echo "[$(date '+%F %T')] ALL DONE (total $(( ($(date +%s) - START ) / 3600 ))h)" >> "${OUT:-last}.log"
echo "[$(date '+%F %T')] ALL DONE"