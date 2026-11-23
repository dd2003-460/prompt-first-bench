#!/bin/bash
# 719-r2 落地 watcher: 等 r2 json → 手动补分 (队列评分块 2>/dev/null 吞异常的替代)
# 一次性, 补分后退出. 不碰运行中进程.
SCAN=/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/q6-budget-scan
LOG=/tmp/q6-r2-score-watch.log
echo "watcher started $(date '+%F %T')" > "$LOG"
for i in $(seq 1 60); do
  f=$(ls "$SCAN"/q6-719-r2-*.json 2>/dev/null | head -1)
  [ -n "$f" ] && break
  sleep 30
done
if [ -z "$f" ]; then
  echo "30min 内 r2 未落地, 退出" >> "$LOG"
  exit 1
fi
echo "r2 落地: $f $(date '+%F %T')" >> "$LOG"
cd /Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation
python3 - "$f" >> "$LOG" 2>&1 << 'PYEOF'
import sys, json
sys.path.insert(0, '.')
from judge_v1 import judge_run
from metacog_axis import compute_metacog, load_run_nodes
f = sys.argv[1]
rj = judge_run(f)
rm = compute_metacog(load_run_nodes(f))
rec = {"budget": 719, "rep": 2, "n_nodes": rj["n_nodes_raw"],
       "judge": {"total": rj["total_score"], "depth": rj["layers"]["structure"]["depth_score"], "cov": rj["layers"]["coverage"]["coverage"]},
       "metacog": {"total": round(rm["metacog_total"],4), "gap": round(rm["gap_rate"],4), "ret": round(rm["retrieval_rate"],4), "hg": round(rm["healthy_gap_rate"],4), "post": round(rm["post_retrieval_accuracy"],4)}}
print("r2 score:", json.dumps(rec, ensure_ascii=False))
scores = json.load(open('data/q6-budget-scan/q6-scan-scores.json'))
if not any(r.get("budget")==719 and r.get("rep")==2 for r in scores):
    scores.append(rec)
    json.dump(scores, open('data/q6-budget-scan/q6-scan-scores.json','w'), ensure_ascii=False, indent=1)
    print("appended. total:", len(scores))
else:
    print("已存在, 跳过")
PYEOF
echo "watcher done $(date '+%F %T')" >> "$LOG"
