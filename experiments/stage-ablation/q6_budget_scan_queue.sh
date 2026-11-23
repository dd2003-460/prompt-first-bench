#!/bin/bash
# Q6 budget scan 队列 (2026-11-23): general 方法论 A1 — metacog 轴跨域验证
# 设计: modules/B-pipeline-ablation/research/GENERAL-METHODOLOGY-PATH-20261123.md
#   5 档 (50/100/150/300/719, 与 K7 gpu 同档位) × 3 reps = 15 runs × ~45min ≈ 11h
#   跑完自动双轴评分 (judge_v1 默认 gpu gold — 跨域时 cov 层偏低是预期, B4 用 --gold-units Q6 重评)
# 输出隔离 (2026-11-23 15:53 事故后纪律):
#   ① SM_CKPT_DIR → $OUT/checkpoints (不碰 checkpoints/sm-* 原始数据)
#   ② runs-s5-sm-q6.json 是 q6 专属新文件 (gpu/nat/soc 的 run json 不受影响), 跑完 cp 到 $OUT
# 用法: 后台跑, 完成通知
set -u
cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
QFILE=/Users/a1-6/Desktop/workspace/pfb/bench/questions/Q6-network-arch.txt
OUT=/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/q6-budget-scan
LOG=/tmp/q6-budget-scan-queue.log
mkdir -p "$OUT"
echo "=== q6-budget-scan queue started $(date '+%F %T') ===" | tee "$LOG"

for budget in 50 100 150 300 719; do
  for rep in 1 2 3; do
    ts=$(date '+%Y%m%d-%H%M%S')
    t0=$(date +%s)
    SM_CKPT_DIR="$OUT/checkpoints" python3 s5_state_machine.py \
      --question-file "$QFILE" --qid q6 --max-nodes $budget \
      > "$OUT/q6-${budget}-r${rep}.stdout" 2>&1
    rc=$?
    t1=$(date +%s)
    dur=$((t1 - t0))
    if [ -f runs-s5-sm-q6.json ]; then
      cp runs-s5-sm-q6.json "$OUT/q6-${budget}-r${rep}-${ts}.json"
      echo "budget=$budget rep=$rep rc=$rc wall_s=$dur out=q6-${budget}-r${rep}-${ts}.json" | tee -a "$LOG"
      # 自动双轴评分 (judge 用默认 gpu gold — metacog 轴 gold-free 不受影响;
      # quality 轴跨域 cov 偏低是预期, B4 阶段用 judge_v1 --gold-units Q6 重评)
      python3 - "$OUT/q6-${budget}-r${rep}-${ts}.json" "$budget" "$rep" "$dur" "$OUT/q6-scan-scores.json" 2>/dev/null << 'PYEOF'
import sys, json, os
sys.path.insert(0, '/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation')
from judge_v1 import judge_run
from metacog_axis import compute_metacog, load_run_nodes
f, budget, rep, wall, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
try:
    rj = judge_run(f)
    rm = compute_metacog(load_run_nodes(f))
    rec = {"budget": budget, "rep": rep, "wall_s": wall, "n_nodes": rj["n_nodes"],
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
echo "=== q6-budget-scan queue DONE $(date '+%F %T') ===" | tee -a "$LOG"
