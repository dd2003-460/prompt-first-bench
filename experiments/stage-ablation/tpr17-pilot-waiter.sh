#!/bin/bash
# T-PR-17 pilot 自动启动 waiter (2026-11-24 21:2x)
# 等 q7 队列 DONE (= vLLM 释放, DONE 行在所有 run+评分之后写, 见 queue.sh L66)
# → 9-cell pilot: 3 臂(canonical/verify-off/null-control) × L3 ckpt(r3, 381 节点) × n=3, budget=719
# fail-fast: 任一 cell rc!=0 或 n_nodes<381(checkpoint 下限) → 中止整批, 写报告.
# 只写 $OUT 下自己的文件, 不碰 q7 队列进程/产物.
set -u
PFB=/Users/a1-6/Desktop/workspace/pfb
OUT=$PFB/modules/B-pipeline-ablation/data/tpr17
LOG=/tmp/q7-budget-scan.log
REP="$OUT/tpr17-pilot-report-$(date +%Y%m%d-%H%M%S).md"
QUEUE_PID=99447
CKPT_FLOOR=381   # r3 checkpoint 节点数 (preflight 3e3859d31)
mkdir -p "$OUT"
echo "[waiter] start $(date '+%F %T'), 等 queue DONE (PID $QUEUE_PID)" > "$REP"

# 1) 等队列结束 (DONE 行 或 队列 PID 消失)
while true; do
  if grep -q 'queue DONE' "$LOG" 2>/dev/null; then break; fi
  if ! kill -0 "$QUEUE_PID" 2>/dev/null; then
    echo "[waiter] queue PID $QUEUE_PID gone without DONE line — proceeding anyway" >> "$REP"
    break
  fi
  sleep 120
done
echo "[waiter] queue ended $(date '+%F %T')" >> "$REP"

# 2) vLLM 健康探测 (best-effort, 8787 ninfer/qwen3.8-27b; 探测失败不阻塞, 首个 cell 才是真正的测试)
for i in 1 2 3; do
  if curl -sf -m 5 http://127.0.0.1:8787/health >/dev/null 2>&1 || curl -sf -m 5 http://127.0.0.1:8787/v1/models >/dev/null 2>&1; then
    echo "[waiter] vLLM probe OK $(date '+%F %T')" >> "$REP"; break
  fi
  echo "[waiter] vLLM probe miss $i/3, 60s 后重试" >> "$REP"; sleep 60
done

# 3) 9-cell pilot, fail-fast
ABORT=0
for arm in canonical verify-off null-control; do
  for rep in 1 2 3; do
    f="$OUT/${arm}_r3_r${rep}.json"
    echo "[waiter] cell arm=$arm rep=$rep start $(date '+%F %T')" >> "$REP"
    ( cd "$PFB/experiments/stage-ablation" && python3 tpr17_runner.py --mode run --arm "$arm" --checkpoint r3 --rep "$rep" --budget 719 --out "$OUT" ) >> "$REP" 2>&1
    rc=$?
    if [ $rc -ne 0 ]; then
      echo "[waiter] cell arm=$arm rep=$rep rc=$rc — ABORT 整批" >> "$REP"; ABORT=1; break 2
    fi
    ok=$(/usr/bin/python3 -c "
import json
try:
    d=json.load(open('$f'))
    print('OK' if d.get('n_nodes',0)>=$CKPT_FLOOR else 'LOW')
except Exception:
    print('ERR')
")
    nn=$(/usr/bin/python3 -c "import json;print(json.load(open('$f')).get('n_nodes'))" 2>/dev/null)
    echo "[waiter] cell arm=$arm rep=$rep sanity=$ok n_nodes=$nn" >> "$REP"
    if [ "$ok" != "OK" ]; then
      echo "[waiter] sanity fail ($ok) — ABORT 整批" >> "$REP"; ABORT=1; break 2
    fi
  done
done

# 4) 汇总
if [ $ABORT -eq 0 ]; then
  echo "[waiter] PILOT COMPLETE $(date '+%F %T') — 9/9 cells" >> "$REP"
else
  echo "[waiter] PILOT ABORTED $(date '+%F %T')" >> "$REP"
fi
/usr/bin/python3 - "$OUT" "$REP" << 'PYEOF'
import sys, json, glob
out, rep = sys.argv[1], sys.argv[2]
lines = ["\n## pilot summary (F2b 多指标, 分析 T5 用)\n"]
for f in sorted(glob.glob(out + '/canonical_r3_r*.json') + glob.glob(out + '/verify-off_r3_r*.json') + glob.glob(out + '/null-control_r3_r*.json')):
    try:
        d = json.load(open(f))
        lines.append(f"- {d.get('arm')} r{d.get('rep')}: n={d.get('n_nodes')} depth={d.get('depth')} ver={d.get('verified_ratio')} "
                     f"tok={d.get('tokens_total')} llm={d.get('n_llm_calls')} tool={d.get('tool_calls')} "
                     f"ev_delta={d.get('evidence_delta_chars')} parent_acc={d.get('parent_link_accuracy')}")
    except Exception as e:
        lines.append(f"- {f}: ERR {e}")
open(rep, 'a').write('\n'.join(lines) + '\n')
print('\n'.join(lines))
PYEOF
echo "[waiter] done $(date '+%F %T') report=$REP"
exit 0
