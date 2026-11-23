#!/bin/bash
# Q6 budget scan 重跑验证 (rep 独立性修复后): 300/719 档 × 3 reps
# 前置: q6_budget_scan_queue.sh 15 run 全部结束 (队列在跑时本脚本不能跑, 同 vLLM 负载)
# 与首批的差异:
#   ① export Q6_REP=$rep → research_hook cache key 含 rep 标识, 各 rep source 检索独立
#      (首批 key 不含 rep, source 层共享, rep 方差是下界 — 见 partial-analysis limitation)
#   ② 评分块 stderr 落盘 (2>> stderr.log, 修首批 2>/dev/null 吞异常)
#   ③ 输出到 q6-budget-scan-rerun/ 独立目录, 不碰首批数据
# 用法: 后台跑, 完成通知
set -u
cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
QFILE=/Users/a1-6/Desktop/workspace/pfb/bench/questions/Q6-network-arch.txt
OUT=/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/q6-budget-scan-rerun
LOG=/tmp/q6-budget-scan-rerun-queue.log
mkdir -p "$OUT"
echo "=== q6-budget-scan RERUN (rep-independent) started $(date '+%F %T') ===" | tee "$LOG"

for budget in 300 719; do
  for rep in 1 2 3; do
    ts=$(date '+%Y%m%d-%H%M%S')
    t0=$(date +%s)
    SM_CKPT_DIR="$OUT/checkpoints" Q6_REP="$rep" python3 s5_state_machine.py \
      --question-file "$QFILE" --qid q6 --max-nodes $budget \
      > "$OUT/q6-${budget}-r${rep}.stdout" 2>&1
    rc=$?
    t1=$(date +%s)
    dur=$((t1 - t0))
    if [ -f runs-s5-sm-q6.json ]; then
      cp runs-s5-sm-q6.json "$OUT/q6-${budget}-r${rep}-${ts}.json"
      echo "budget=$budget rep=$rep rc=$rc wall_s=$dur out=q6-${budget}-r${rep}-${ts}.json" | tee -a "$LOG"
      Q6_REP="$rep" python3 - "$OUT/q6-${budget}-r${rep}-${ts}.json" "$budget" "$rep" "$dur" "$OUT/q6-scan-scores.json" 2>> "$OUT/q6-score-stderr.log" << 'PYEOF'
import sys, json, os
sys.path.insert(0, '/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation')
from judge_v1 import judge_run
from metacog_axis import compute_metacog, load_run_nodes
f, budget, rep, wall, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
try:
    rj = judge_run(f)
    rm = compute_metacog(load_run_nodes(f))
    rec = {"budget": budget, "rep": rep, "wall_s": wall, "n_nodes": rj["n_nodes_raw"],
           "judge": {"total": rj["total_score"], "depth": rj["layers"]["structure"]["depth_score"], "cov": rj["layers"]["coverage"]["coverage"]},
           "metacog": {"total": round(rm["metacog_total"],4), "gap": round(rm["gap_rate"],4), "ret": round(rm["retrieval_rate"],4), "hg": round(rm["healthy_gap_rate"],4), "post": round(rm["post_retrieval_accuracy"],4)}}
    scores = json.load(open(out)) if os.path.exists(out) else []
    scores.append(rec)
    json.dump(scores, open(out, 'w'), ensure_ascii=False, indent=1)
    print(f"  [score] {rec['judge']['total']:.4f} depth={rec['judge']['depth']:.3f} cov={rec['judge']['cov']:.3f} metacog={rec['metacog']['total']:.4f} gap={rec['metacog']['gap']:.4f}")
except Exception as e:
    print(f"  [score-err] {e}")
PYEOF
    else
      echo "budget=$budget rep=$rep rc=$rc wall_s=$dur out=MISSING" | tee -a "$LOG"
    fi
  done
done
echo "=== q6-budget-scan RERUN DONE $(date '+%F %T') ===" | tee -a "$LOG"
