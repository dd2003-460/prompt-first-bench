#!/bin/bash
# origin: ai · 2026-11-25 · armC' 后置 watcher（vllm-catchup 完成后自动跑）
# 作用: 等 vllm-catchup.sh (PID 传入) 退出 → vLLM ready → 跑 armC' (3 样本) → 机械评分
#   (armc-eps-screen.py: flip T3 原词表 + ε_pred gold 轴, 鉴别力已验证)。
# 背景: learn-to-think 05-accept REJECTED (ε_pred 0/3) → 回 03 发 armC' 补充任务书。
#   armC' 只依赖 vLLM 空闲, 不依赖 catchup C1-C4 成败 (catchup 失败也继续)。
# 落盘: logs/armc-prime-post-<ts>.log + tasks/learn-to-think/exp03-armc/armc_prime_raw_outputs.json
# 用法: background=true 起, 完成后 notify
set -uo pipefail
PFB=/Users/a1-6/Desktop/workspace/pfb
SA=$PFB/experiments/stage-ablation
LT=$PFB/tasks/learn-to-think/exp03-armc
CATCHUP_PID=${1:?用法: armc-prime-post.sh <vllm-catchup_pid>}
TS=$(date +%Y%m%d-%H%M%S)
LOG=$SA/logs/armc-prime-post-$TS.log
mkdir -p "$SA/logs"

log() { echo "[$(date '+%H:%M:%S')] $*" | tee -a "$LOG"; }

log "ARMCP-START waiting vllm-catchup PID=$CATCHUP_PID"
while kill -0 "$CATCHUP_PID" 2>/dev/null; do sleep 120; done
log "vllm-catchup PID=$CATCHUP_PID exited"

# vLLM ready 探测 (最多 30 分钟)
ready=0
for i in $(seq 1 90); do
  if curl -sf http://127.0.0.1:8787/v1/models >/dev/null 2>&1; then ready=1; break; fi
  sleep 20
done
if [ "$ready" != "1" ]; then log "FATAL: vLLM 未就绪, 中止"; exit 2; fi
log "vLLM /v1/models OK (try $i)"

# C1: armC' 跑数 (3 样本, ~2-3 min, 预注册红线: runner 已 commit)
log "ARMCP-1 armC-prime RUN START"
( cd "$LT" && python3 -u run_armc_prime.py ) >> "$LOG" 2>&1
rc1=$?
log "ARMCP-1 armC-prime rc=$rc1"

# C2: 机械评分 (flip + ε_pred gold 轴, 纯 CPU)
if [ -f "$LT/armc_prime_raw_outputs.json" ]; then
  log "ARMCP-2 eps-screen START"
  ( cd "$LT" && python3 -u armc-eps-screen.py armc_prime_raw_outputs.json ) >> "$LOG" 2>&1
  rc2=$?
  log "ARMCP-2 eps-screen rc=$rc2"
  # 产物核验 (skill #24: 3 样本 + 非空)
  python3 -c "
import json,sys
d=json.load(open('$LT/armc_prime_raw_outputs.json'))
n=len(d.get('samples',[]))
ok=n>=3 and all((s.get('content') or s.get('reasoning')) for s in d['samples'])
print(f'[verify] armC-prime samples={n} nonempty={ok}')
sys.exit(0 if ok else 1)
" >> "$LOG" 2>&1
  log "ARMCP-VERIFY rc=$?"
else
  log "FATAL: armc_prime_raw_outputs.json 未生成 (rc1=$rc1), 评分跳过"
fi

log "ARMCP-DONE log=$LOG"
