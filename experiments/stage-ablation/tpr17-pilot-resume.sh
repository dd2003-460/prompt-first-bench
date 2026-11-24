#!/bin/bash
# T-PR-17 pilot resume (2026-11-24 22:5x)
# 用途: waiter fail-fast 中止后, 只补跑缺失/退化 cell, 不重跑已成功的.
# 已知失败模式: vLLM 瞬时 502 → call_llm 重试耗尽返回 None → _verify_batch 线程池
#   解包 None → TypeError FATAL (见 q7-300-r2-dup-rootcause-20261124.md). 7h pilot 期间
#   概率非零. waiter 用 break 2 中止整批但无重试 → 本脚本补这个缺口.
# 判"cell 已成功": 该 cell json 存在 且 n_nodes>=CKPT_FLOOR 且 n_llm_calls>=50 (非退化).
# 只写 $OUT 下自己的 cell 文件, 不碰 q7 队列进程/产物, 不改 s5_state_machine.py.
set -u
PFB=/Users/a1-6/Desktop/workspace/pfb
OUT=${1:-$PFB/modules/B-pipeline-ablation/data/tpr17}
CKPT_FLOOR=381   # r3 checkpoint 节点数 (与 waiter 一致)
MIN_LLM=50       # 退化判据 (与 runbook step 1 一致)
CKPT=r3
BUDGET=719
SEED=719
LOG="$OUT/tpr17-pilot-resume-$(date +%Y%m%d-%H%M%S).log"
mkdir -p "$OUT"
echo "[resume] start $(date '+%F %T'), OUT=$OUT" > "$LOG"

# vLLM 健康探测 (best-effort, 与 waiter 同端口)
ok=0
for i in 1 2 3; do
  if curl -sf -m 5 http://127.0.0.1:8787/health >/dev/null 2>&1 || \
     curl -sf -m 5 http://127.0.0.1:8787/v1/models >/dev/null 2>&1; then
    echo "[resume] vLLM probe OK $(date '+%F %T')" >> "$LOG"; ok=1; break
  fi
  echo "[resume] vLLM probe miss $i/3, 60s 后重试" >> "$LOG"; sleep 60
done
if [ $ok -ne 1 ]; then
  echo "[resume] vLLM 三次探测失败 — 不跑 (避免 9 个 cell 全崩). 查 vLLM 后重跑本脚本." >> "$LOG"
  echo "vLLM 不健康, 已中止. 日志: $LOG"
  exit 2
fi

done_n=0; skip_n=0; fail_n=0
for arm in canonical verify-off null-control; do
  for rep in 1 2 3; do
    f="$OUT/${arm}_${CKPT}_r${rep}.json"
    # 判已成功: 文件存在 + n_nodes>=floor + n_llm_calls>=min
    st=$(/usr/bin/python3 -c "
import json
try:
    d=json.load(open('$f'))
    print('OK' if (d.get('n_nodes',0)>=$CKPT_FLOOR and d.get('n_llm_calls',0)>=$MIN_LLM) else 'BAD')
except Exception:
    print('MISS')
")
    if [ "$st" = "OK" ]; then
      echo "[resume] SKIP $arm r$rep (已成功)" >> "$LOG"; skip_n=$((skip_n+1)); continue
    fi
    echo "[resume] RUN $arm r$rep (st=$st) $(date '+%F %T')" >> "$LOG"
    ( cd "$PFB/experiments/stage-ablation" && python3 tpr17_runner.py --mode run \
        --arm "$arm" --checkpoint "$CKPT" --rep "$rep" --budget "$BUDGET" \
        --seed "$SEED" --out "$OUT" ) >> "$LOG" 2>&1
    rc=$?
    # 跑完再验一次
    st2=$(/usr/bin/python3 -c "
import json
try:
    d=json.load(open('$f'))
    print('OK' if (d.get('n_nodes',0)>=$CKPT_FLOOR and d.get('n_llm_calls',0)>=$MIN_LLM) else 'BAD')
except Exception:
    print('MISS')
")
    if [ "$st2" = "OK" ]; then
      echo "[resume] DONE $arm r$rep rc=$rc $(date '+%F %T')" >> "$LOG"; done_n=$((done_n+1))
    else
      echo "[resume] FAIL $arm r$rep rc=$rc st2=$st2 — 跳过继续 (不中止, 瞬时故障重试)" >> "$LOG"
      fail_n=$((fail_n+1))
    fi
  done
done
echo "[resume] COMPLETE $(date '+%F %T') — done=$done_n skip=$skip_n fail=$fail_n" >> "$LOG"
echo "resume 完成: done=$done_n skip=$skip_n fail=$fail_n. 日志: $LOG"
# fail>0 时退出码 1 (提示人工复查), 否则 0
[ $fail_n -eq 0 ] && exit 0 || exit 1
