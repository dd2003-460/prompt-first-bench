#!/bin/zsh
# E3 预算扫描 batch（research-agi-budget goal，2026-11-22 设计定稿）。
# 单变量：max_nodes（预算轴）。5 档 × 3 reps = 15 runs，串行（vLLM 单实例）。
# 固定变量：qid=gpu（gold 最完整）、max_depth=5、max_kids=8、β=3.0、θ=0.10、
#           seed=42、formula 臂、SM_SYNTH_FULL=1（synth 放开，隔离 decompose 侧预算效应）。
# 用法: zsh budget_scan_batch.sh
# 前置: matched 批完成（vLLM 负载释放）+ B prompt 修复完成（用修复后 prompt 跑）。
set -euo pipefail
setopt NULL_GLOB
cd /Users/a1-6/Desktop/workspace/pfb
STAGE=experiments/stage-ablation
LOGDIR=/tmp/ablation-budget-scan
RUNS_DIR=modules/B-pipeline-ablation/data/t53b/runs_budget_scan
NOTES_DIR=modules/B-pipeline-ablation/data/t53b/notes-budget-scan
RESULTS=modules/B-pipeline-ablation/data/t53b/results-budget-scan.json
mkdir -p "$LOGDIR" "$RUNS_DIR" "$NOTES_DIR"

# 5 档预算（E1 设计）：50/100/150/300/719
BUDGETS=(50 100 150 300 719)
REPS=(1 2 3)
QID=gpu

echo "=== budget scan: ${#BUDGETS[@]} 档 × ${#REPS[@]} reps = $(( ${#BUDGETS[@]} * ${#REPS[@]} )) runs (started $(date '+%F %T')) ==="

for B in "${BUDGETS[@]}"; do
  for R in "${REPS[@]}"; do
    RUN="gpu_budget${B}_r${R}"
    LOG="$LOGDIR/${RUN}.sm.log"
    echo "=== $RUN (max_nodes=$B, rep $R) started $(date '+%F %T') ==="
    # 清场：归档上一 run 的文件（checkpoint 是原始数据，mv 不 rm）
    ARCHIVE="$STAGE/checkpoints/archive/budget-${B}-r${R}-$(date +%Y%m%d-%H%M%S)"
    mkdir -p "$ARCHIVE"
    for f in "$STAGE/checkpoints/sm-${QID}-r"* \
             "$STAGE/runs-s5-sm-${QID}.json" \
             "$STAGE/runs-s5-sm-${QID}-synth.json" \
             "$STAGE/runs-s5-sm-${QID}-checkpoint.json"; do
      [ -e "$f" ] && mv "$f" "$ARCHIVE/"
    done
    T0=$(date +%s)
    RC=0
    SM_SEED=42 SM_SYNTH_FULL=1 python3 -u "$STAGE/s5_state_machine.py" "$QID" \
      --obj-mode=formula --synth --max-nodes "$B" --max-depth 5 \
      > "$LOG" 2>&1 || RC=$?
    # FATAL → resume（同 driver 逻辑）
    RESUME_TRIES=0
    while [ $RC -ne 0 ] && [ $RESUME_TRIES -lt 3 ]; do
      CKPT="$(pwd)/$STAGE/runs-s5-sm-${QID}-checkpoint.json"
      if [[ ! -f "$CKPT" ]] || (( $(stat -f %m "$CKPT") < T0 )); then break; fi
      RESUME_TRIES=$((RESUME_TRIES+1))
      echo "[resume] $RUN 第${RESUME_TRIES}/3次: $CKPT"
      T0=$(date +%s)
      SM_SEED=42 SM_SYNTH_FULL=1 python3 -u "$STAGE/s5_state_machine.py" "$QID" \
        --obj-mode=formula --synth --max-nodes "$B" --max-depth 5 \
        --resume "$CKPT" >> "$LOG" 2>&1 || RC=$?
    done
    if [ $RC -ne 0 ]; then
      echo "[FAIL] $RUN rc=$RC after $(( $(date +%s) - T0 ))s — 查 $LOG，继续下一 run"
      continue
    fi
    ELAPSED=$(( $(date +%s) - T0 ))
    # 记账：拷贝 + 补元数据 + 提取分数
    python3 - "$RUN" "$B" "$R" "$ELAPSED" "$RUNS_DIR" "$STAGE" <<'PY'
import json, sys, shutil
run, budget, rep, elapsed, runs_dir, stage = sys.argv[1:7]
src = f"{stage}/runs-s5-sm-gpu-synth.json"
dst = f"{runs_dir}/{run}.json"
d = json.load(open(src))
d.update({"run": run, "budget_max_nodes": int(budget), "rep": int(rep),
          "elapsed_s": int(elapsed), "seed": 42, "max_depth": 5,
          "objective_mode": "formula", "synth_full": True,
          "prompt_version": "post-B-fix"})
json.dump(d, open(dst, "w"), ensure_ascii=False, indent=1)
print(f"  [bookkeeping] {run}: nodes={d.get('n_nodes')} depth={d.get('depth_score')} "
      f"cov={d.get('coverage')} {elapsed}s")
PY
  done
done

echo "=== budget scan DONE $(date '+%F %T') ==="
# Pareto 汇总
python3 - "$RUNS_DIR" "$RESULTS" <<'PY'
import json, sys, glob, os
runs_dir, results = sys.argv[1:3]
rows = []
for f in sorted(glob.glob(f"{runs_dir}/*.json")):
    d = json.load(open(f))
    rows.append({"run": d.get("run"), "budget": d.get("budget_max_nodes"),
                 "rep": d.get("rep"), "n_nodes": d.get("n_nodes"),
                 "depth": d.get("depth_score"), "coverage": d.get("coverage"),
                 "elapsed_s": d.get("elapsed_s")})
rows.sort(key=lambda r: (r["budget"] or 0, r["rep"] or 0))
json.dump(rows, open(results, "w"), ensure_ascii=False, indent=1)
print(f"\n{'budget':>7} {'rep':>3} {'nodes':>6} {'depth':>7} {'cov':>6} {'s':>6}")
for r in rows:
    print(f"{r['budget']:>7} {r['rep']:>3} {str(r['n_nodes']):>6} "
          f"{str(r['depth']):>7} {str(r['coverage']):>6} {str(r['elapsed_s']):>6}")
# 每档均值
from collections import defaultdict
by_b = defaultdict(list)
for r in rows:
    if r["depth"] is not None:
        by_b[r["budget"]].append(r["depth"])
print(f"\n{'budget':>7} {'mean_depth':>11} {'n':>3}")
for b in sorted(by_b):
    v = by_b[b]
    print(f"{b:>7} {sum(v)/len(v):>11.4f} {len(v):>3}")
print(f"\nresults → {results}")
PY
