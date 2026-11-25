#!/bin/bash
# origin: ai · 2026-11-25 · 队列 STEP1-synth/STEP2/STEP3 补跑（vLLM 依赖项）
# 背景: post-pilot 队列 4 步中 3 步失败 (queue-verify 1/5→2/5 PASS 后定位):
#   STEP1-synth: GOLD 缺 l4-disambig 条目 → KeyError (已修 s8b_pilot.py, 免重跑树, l4-synth-recover.py 恢复)
#   STEP2 gptr: 队列用系统 python3 无 gpt_researcher (改用 .venv-gptr)
#   STEP3 J4: PROMPT.format 撞字面花括号 (已修 tjudge1_llm_fallback.py)
# 门控: 等 T-REPAIR-1 PID 退出 + vLLM /v1/models ready (vLLM 独占, 502 风险已知)。
# 顺序: L4 synth 恢复 (~6 调用) → L4 judge (机械) → gptr 全臂 (~1h) → J4 (~数十调用)。
# 落盘: logs/vllm-catchup-<ts>.log
set -uo pipefail
PFB=/Users/a1-6/Desktop/workspace/pfb
SA=$PFB/experiments/stage-ablation
BJ=$PFB/modules/B-pipeline-ablation
TR_PID=${1:?用法: vllm-catchup.sh <t-repair1_pid>}
TS=$(date +%Y%m%d-%H%M%S)
LOG=$SA/logs/vllm-catchup-$TS.log
mkdir -p "$SA/logs"

log() { echo "[$(date '+%H:%M:%S')] $*" | tee -a "$LOG"; }

log "CATCHUP-START waiting T-REPAIR-1 PID=$TR_PID"
while kill -0 "$TR_PID" 2>/dev/null; do sleep 120; done
log "T-REPAIR-1 PID=$TR_PID exited"

# vLLM ready 探测 (最多 30 分钟)
ready=0
for i in $(seq 1 90); do
  if curl -sf http://127.0.0.1:8787/v1/models >/dev/null 2>&1; then ready=1; break; fi
  sleep 20
done
if [ "$ready" != "1" ]; then log "FATAL: vLLM 未就绪, 中止"; exit 2; fi
log "vLLM /v1/models OK (try $i)"

# ---- Step 1: L4-disambig synth 恢复 (免重跑树) ----
log "C1 l4-synth-recover START"
( cd "$SA" && python3 -u l4-synth-recover.py ) >> "$LOG" 2>&1
rc=$?
log "C1 l4-synth-recover rc=$rc"

# ---- Step 2: L4 judge (机械判读 A/B/C/D, 不耗 vLLM) ----
log "C2 l4-judge START"
( cd "$SA" && python3 -u "$BJ/research/l4-disambig-judge.py" "$SA" ) >> "$LOG" 2>&1
rc=$?
log "C2 l4-judge rc=$rc"

# ---- Step 3: gptr 全臂 (.venv-gptr, gpt_researcher 0.17.0) ----
log "C3 gptr-full-arm START"
( cd "$SA" && "$PFB/.venv-gptr/bin/python" -u gptr_pfb_3q.py ) >> "$LOG" 2>&1
rc=$?
log "C3 gptr-full-arm rc=$rc"

# ---- Step 4: J4 LLM 兜底裁决 (花括号已修) ----
log "C4 tjudge1-J4 START"
( cd "$BJ" && python3 -u tjudge1_llm_fallback.py ) >> "$LOG" 2>&1
rc=$?
log "C4 tjudge1-J4 rc=$rc"

# ---- 终验: 产物级鉴别力 (queue-verify 只认队列日志; 这里直接查 4 产物) ----
log "VERIFY products:"
for f in "$SA/runs-s5-sm-l4-disambig-synth.json" "$SA/runs-gptr-pfb/summary.json" "$BJ/tjudge1-llm-fallback-all-adjudicated.json"; do
  if [ -f "$f" ] && [ "$(stat -f %m "$f")" -gt "$(date -j -f '%Y%m%d-%H%M%S' "${TS}" '+%s')" ]; then
    log "  FRESH $f"
  elif [ -f "$f" ]; then
    log "  STALE $f"
  else
    log "  MISSING $f"
  fi
done
log "CATCHUP-DONE log=$LOG"
