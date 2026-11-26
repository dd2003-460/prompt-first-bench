#!/bin/bash
# r3 落地监控: 等 q6-300-r3-*.json 出现 → 等评分写入 scores → 跑 n=3 判读 → 写 r3_verdict.txt
cd /Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/q6-budget-scan-rerun
for i in $(seq 1 60); do
  f=$(ls -t q6-300-r3-*.json 2>/dev/null | head -1)
  if [ -n "$f" ]; then
    for j in $(seq 1 12); do
      n=$(python3 -c "import json;print(len([r for r in json.load(open('q6-rerun-scores.json')) if r.get('rep')==3]))" 2>/dev/null)
      [ "$n" = "1" ] && break
      sleep 10
    done
    python3 q6_rerun_n3_verdict.py > r3_verdict.txt 2>&1
    echo "R3 VERDICT DONE $(date '+%F %T')" >> r3_verdict.txt
    exit 0
  fi
  sleep 30
done
echo "R3 MONITOR TIMEOUT (no json in 30min) $(date '+%F %T')" > r3_verdict.txt
