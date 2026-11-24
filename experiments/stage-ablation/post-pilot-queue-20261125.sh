#!/bin/bash
# # origin: ai · 2026-11-25 05:55 · post-pilot 串行队列（4 实验, 等 vLLM 释放后自动串跑）
# 组装: Lead 亲写（subagent deleg_0c26baaa 死于 27b 输出 token 上限, 命令细节从其转录 salvage + 逐一核验）
# 状态: 【未 arm】— 由 Lead 审查后启动:
#   setsid nohup bash post-pilot-queue-20261125.sh > /dev/null 2>&1 &
# 红线遵守: 等待期只 kill -0 探活 + GET /v1/models（非生成调用, 不干扰 pilot）; 不改任何在跑的 .sh
set -uo pipefail

PFB=/Users/a1-6/Desktop/workspace/pfb
SA=$PFB/experiments/stage-ablation
BJ=$PFB/modules/B-pipeline-ablation
TS=$(date +%Y%m%d-%H%M%S)
LOG=$PFB/experiments/stage-ablation/logs/post-pilot-queue-$TS.log
mkdir -p "$PFB/experiments/stage-ablation/logs"

log() { echo "[$(date '+%H:%M:%S')] $*" | tee -a "$LOG"; }

# ---- Gate 1: 等 pilot PID 退出 ----
PILOT_PID=${1:-53387}
log "QUEUE-START waiting pilot PID=$PILOT_PID"
while kill -0 "$PILOT_PID" 2>/dev/null; do
  sleep 120
done
log "pilot PID=$PILOT_PID exited"

# ---- Gate 2: vLLM 就绪探测（GET /v1/models, 非生成调用）----
for i in $(seq 1 30); do
  if curl -sf -m 5 http://127.0.0.1:8787/v1/models > /dev/null 2>&1; then
    log "vLLM /v1/models OK (try $i)"; break
  fi
  log "vLLM not ready (try $i/30), sleep 30s"; sleep 30
done

# ---- Step 1: L4 消歧义重跑（预注册 l4-disambig-prereg-20261125.md, budget 300, ~40-60min）----
log "STEP1 L4-disambig START"
( cd "$SA" && SM_SEED=42 SM_SYNTH_FULL=1 python3 -u s5_state_machine.py l4-disambig \
    --qid=l4-disambig --question-file l4-disambig-question.txt \
    --obj-mode=formula --synth --max-nodes 300 --max-depth 5 ) >> "$LOG" 2>&1
rc=$?
log "STEP1 L4-disambig rc=$rc"

# ---- Step 2: gptr 全臂重跑（gptr_pfb_3q.py, pfb 多通道检索器含 bing, rootcause 20261125 确认 DDGS(bing) OK）----
log "STEP2 gptr-full-arm START"
( cd "$SA" && python3 -u gptr_pfb_3q.py ) >> "$LOG" 2>&1
rc=$?
log "STEP2 gptr-full-arm rc=$rc"

# ---- Step 3: T-JUDGE-1 J4 LLM 兜底（102 条, 自带 /v1/models 探测, 忙则 rc=2）----
log "STEP3 T-JUDGE-1-J4 START"
( cd "$BJ" && python3 -u tjudge1_llm_fallback.py ) >> "$LOG" 2>&1
rc=$?
log "STEP3 T-JUDGE-1-J4 rc=$rc"

# ---- Step 4: learn-to-think 臂C（3 次调用, 预注册 5e6294aba, runner 44350b270 dry-run 验证过）----
log "STEP4 armC START"
( cd "$PFB" && python3 -u tasks/learn-to-think/exp03-armc/run_armc.py ) >> "$LOG" 2>&1
rc=$?
log "STEP4 armC rc=$rc"

log "QUEUE-DONE log=$LOG"
