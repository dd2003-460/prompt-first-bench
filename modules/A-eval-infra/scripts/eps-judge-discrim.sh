#!/bin/bash
# origin: ai · 2026-11-25 · eps-judge 鉴别力测试（预注册: POS 必须 aligned=1, 负例必须 0）
# 定位: 机械筛查半边已离线验证 (POS HIT / armC 3 负例 0 命中 / FP 过命中→证实两级必要)。
#   本脚本补判官半边: 等 vLLM 空闲 → eps-judge 跑 discrim-test.json (POS + FP 2 样本)。
# 验收: POS aligned=true 且 FP aligned=false → 判官鉴别力 PASS, 明早 armC' 判决可信。
#   任一不符 → 判官不可信, armC' 的 eps-judge 结果需 D 人工终核 (lossless L69 双标注者)。
# 依赖: 等 vllm-catchup (PID 36173) 退出 + vLLM /v1/models ready。
#   时序: 与 armc-prime-post (69029) 同门抢 vLLM, 但本测试仅 2 样本 ~30s,
#   先跑完验证判官, 再让 armC-prime 用已验证的判官 (若 FAIL, 明早解读时知道判官不可信)。
# 落盘: logs/eps-judge-discrim-<ts>.log + modules/G-think-mechanism/learn-to-think/exp03-armc/discrim-test_judge.json
set -uo pipefail
PFB=/Users/a1-6/Desktop/workspace/pfb
SA=$PFB/experiments/stage-ablation
LT=$PFB/modules/G-think-mechanism/learn-to-think/exp03-armc
GATE_PID=${1:?用法: eps-judge-discrim.sh <gate_pid>}
TS=$(date +%Y%m%d-%H%M%S)
LOG=$SA/logs/eps-judge-discrim-$TS.log
mkdir -p "$SA/logs"
log() { echo "[$(date '+%H:%M:%S')] $*" | tee -a "$LOG"; }

log "EJD-START waiting gate PID=$GATE_PID"
while kill -0 "$GATE_PID" 2>/dev/null; do sleep 120; done
log "gate PID=$GATE_PID exited"

ready=0
for i in $(seq 1 90); do
  if curl -sf http://127.0.0.1:8787/v1/models >/dev/null 2>&1; then ready=1; break; fi
  sleep 20
done
if [ "$ready" != "1" ]; then log "FATAL: vLLM 未就绪, 中止"; exit 2; fi
log "vLLM /v1/models OK (try $i)"

log "EJD-RUN eps-judge on discrim-test.json"
( cd "$LT" && python3 -u eps-judge.py discrim-test.json ) >> "$LOG" 2>&1
rc=$?
log "EJD-RUN rc=$rc"

# 机械验收 (确定性判读, 不靠 LLM 自评)
python3 - "$LT/discrim-test_judge.json" >> "$LOG" 2>&1 <<'PYEOF'
import json, sys
d = json.load(open(sys.argv[1]))
v = {o["arm"]: o["verdict"] for o in d["verdicts"]}
pos_ok = v.get("POS", {}).get("aligned") is True
fp_ok = v.get("FP", {}).get("aligned") is False
print(f"[accept] POS aligned={v.get('POS',{}).get('aligned')} (expect True) | FP aligned={v.get('FP',{}).get('aligned')} (expect False)")
print(f"[accept] {'PASS' if (pos_ok and fp_ok) else 'FAIL — 判官不可信, armC-prime 的 eps-judge 结果需 D 人工终核'}")
sys.exit(0 if (pos_ok and fp_ok) else 1)
PYEOF
log "EJD-ACCEPT rc=$?"
log "EJD-DONE log=$LOG"
