#!/bin/bash
# 过夜 GPU 队列 (2026-11-22): Idea 2 完成后自动接补重复 + 自动双轴评分
# 设计: ① 等 idea2_runner 结束 (poll log) ② 补重复 100/150/300 × 5 reps (peak 定位优先,
#       50/719 端点趋势已明确不补) ③ 每个 run 完自动 judge_v1 + metacog 评分 append
# 用法: 后台跑, 预计 15 runs × ~45min ≈ 11h
set -u
cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
IDEA2_LOG=/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/idea2/idea2-run.log
OUT=/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/rep-scan
LOG=/tmp/rep-scan-queue.log
mkdir -p "$OUT"
echo "=== rep-scan queue started $(date '+%F %T') ===" | tee "$LOG"

# ① 等 Idea 2 完成 (120s 轮询)
while ! grep -q "idea2 done" "$IDEA2_LOG" 2>/dev/null; do
  sleep 120
done
echo "[queue] idea2 done detected $(date '+%F %T')" | tee -a "$LOG"

# ② 补重复: 100/150/300 × 5 reps (r4-r8, 接续 K7 已有 r1-r3)
for budget in 100 150 300; do
  for rep in 4 5 6 7 8; do
    ts=$(date '+%Y%m%d-%H%M%S')
    t0=$(date +%s)
    python3 s5_state_machine.py gpu --max-nodes $budget > "$OUT/rep-${budget}-r${rep}.stdout" 2>&1
    rc=$?
    t1=$(date +%s)
    dur=$((t1 - t0))
    if [ -f runs-s5-sm-gpu.json ]; then
      cp runs-s5-sm-gpu.json "$OUT/rep-${budget}-r${rep}-${ts}.json"
      echo "budget=$budget rep=$rep rc=$rc wall_s=$dur out=rep-${budget}-r${rep}-${ts}.json" | tee -a "$LOG"
      # ③ 自动双轴评分
      python3 - "$OUT/rep-${budget}-r${rep}-${ts}.json" "$budget" "$rep" "$dur" "$OUT/rep-scan-scores.json" 2>/dev/null << 'PYEOF'
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
    print(f"  [score] {rec['judge']['total']:.4f} depth={rec['judge']['depth']:.3f} cov={rec['judge']['cov']:.3f} metacog={rec['metacog']['total']:.4f}")
except Exception as e:
    print(f"  [score-err] {e}")
PYEOF
    else
      echo "budget=$budget rep=$rep rc=$rc wall_s=$dur out=MISSING" | tee -a "$LOG"
    fi
    # 2026-11-23: 删除了原来的 `rm -rf checkpoints/sm-gpu-r*` — 它违反红线
    # "别清 checkpoint, 这是原始数据" (D 2026-11-22), 且静默删 (2>/dev/null)。
    # 队列 11-23 跑完 15 run 后, rep-scan 时代的实时 checkpoint 已被删且从未进 git,
    # 不可恢复 (核心数据 rep-*.json 在删前已 cp 到 $OUT, 安全)。
    # checkpoint 是原始数据, 不删; 磁盘占用由 git + archive 管理, 不由队列脚本清。
  done
done
echo "=== rep-scan queue DONE $(date '+%F %T') ===" | tee -a "$LOG"
