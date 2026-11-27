#!/bin/bash
# OBJHACK runner: 等 judge(2887) 释放 8787 → 串行 4 runs → 指标计算
# 2026-11-27 · spec: modules/B-pipeline-ablation/data/objfmt-hack/spec.md
set -u
cd /Users/a1-6/Desktop/workspace/pfb-thinkmech
SA=experiments/stage-ablation
ARMS=modules/B-pipeline-ablation/data/objfmt-hack/arms
mkdir -p "$ARMS"

# 1) 等 judge 退出 (8787 独占)
while ps -p 2887 >/dev/null 2>&1; do sleep 30; done
echo "[runner] judge exited, 8787 free, $(date +%H:%M:%S)"

# 2) 串行 4 runs (预算 100 固定, 单变量=obj-mode)
for arm in text formula; do
  for r in 1 2; do
    qid="objfmt-${arm}-r${r}"
    echo "[runner] START ${qid} $(date +%H:%M:%S)"
    python3 "$SA/s5_state_machine.py" "$qid" --qid "$qid" \
      --obj-mode="$arm" --max-nodes 100 \
      > "$ARMS/${qid}.stdout" 2>&1
    rc=$?
    echo "[runner] END ${qid} rc=$rc $(date +%H:%M:%S)"
    cp "$SA/runs-s5-sm-${qid}.json" "$ARMS/" 2>/dev/null || echo "[runner] WARN no json for ${qid}"
  done
done

# 3) 指标
python3 modules/B-pipeline-ablation/research/objfmt_hack_metrics.py \
  > "$ARMS/../hack-metrics.stdout" 2>&1
echo "[runner] DONE $(date +%H:%M:%S)"
