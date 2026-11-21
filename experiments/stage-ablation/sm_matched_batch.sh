#!/bin/bash
# SM formula 臂 3 路并发重跑（2026-11-21, 与裸臂 matched batch 同时跑，同负载对比）。
# 结构：nat/soc/gpu 各一路，线内串行 —— 与 T53b SM 臂采集结构一致，
#       也与裸臂 matched batch（bare_arm_batch_matched.py）同并发结构。
# 输出隔离：spec 指向 runs_sm_matched/ + 独立 cc-state，不碰 T53b 原始数据。
# 启动: python3 无关；直接 bash sm_matched_batch.sh（后台由 Hermes 跟踪）
set -uo pipefail
cd /Users/a1-6/Desktop/workspace/pfb
STAGE=experiments/stage-ablation
SPEC=experiments/stage-ablation/spec/t53b-sm-formula-matched.json
LOGDIR=/tmp/ablation-sm-matched
mkdir -p "$LOGDIR"

lane() {
  local qid="$1"
  local log="$LOGDIR/sm-matched-${qid}.log"
  echo "[$(date '+%F %T')] lane ${qid} start" >> "$log"
  for r in 01 02 03 04 05 06 07 08 09 10; do
    local run="${qid}_formula_r${r}"
    echo "[$(date '+%F %T')] 开始: ${run}" >> "$log"
    if T53B_RUN="$run" ABLATION_SPEC="$SPEC" zsh "$STAGE/ablation_driver.sh" >> "$log" 2>&1; then
      echo "[$(date '+%F %T')] 完成: ${run}" >> "$log"
    else
      echo "[$(date '+%F %T')] 失败: ${run} rc=$?" >> "$log"
    fi
  done
  echo "[$(date '+%F %T')] lane ${qid} done" >> "$log"
}

lane nat &
lane soc &
lane gpu &
wait
echo "[$(date '+%F %T')] SM MATCHED BATCH ALL DONE" >> "$LOGDIR/sm-matched-all.log"
