#!/bin/bash
# Q6 719 无深度墙批 (2026-11-23 23:30, D 指令"不要限制深度"):
# 原批 719 档撞 max_depth=4 (harness 默认) → 测的是深度墙前随机展开, 非模型预算需求。
# 本批: --max-nodes 719 --max-depth 10 (10 层 ≥ gold 主干深度 5, 实质无深度限制)
#   → 预算成为唯一约束, 这才是 draft 缺的"预算超饱和点"干净测试。
# 前置: rep 独立重跑队列跑完 (vLLM 不并发)。输出独立目录, 不碰原批。
# Q6 三坑全避开: Q6_REP rep 独立 cache / /usr/bin/python3 绝对路径 / 评分 stderr 落盘。
set -u
cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
QFILE=/Users/a1-6/Desktop/workspace/pfb/bench/questions/Q6-network-arch.txt
OUT=/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/q6-719-nodepth
LOG=/tmp/q6-719-nodepth.log
mkdir -p "$OUT"
echo "=== q6-719-nodepth queue started $(date '+%F %T') ===" | tee "$LOG"

for rep in 1 2 3; do
  ts=$(date '+%Y%m%d-%H%M%S')
  t0=$(date +%s)
  Q6_REP="nd$rep" SM_CKPT_DIR="$OUT/checkpoints" /usr/bin/python3 s5_state_machine.py \
    --question-file "$QFILE" --qid q6 --max-nodes 719 --max-depth 10 \
    > "$OUT/q6-719-nd-r${rep}.stdout" 2>&1
  rc=$?
  t1=$(date +%s)
  dur=$((t1 - t0))
  if [ -f runs-s5-sm-q6.json ]; then
    cp runs-s5-sm-q6.json "$OUT/q6-719-nd-r${rep}-${ts}.json"
    echo "rep=$rep rc=$rc wall_s=$dur out=q6-719-nd-r${rep}-${ts}.json" | tee -a "$LOG"
    /usr/bin/python3 - "$OUT/q6-719-nd-r${rep}-${ts}.json" "$rep" "$dur" "$OUT/q6-719-nodepth-scores.json" 2>>"$OUT/q6-719-nodepth-stderr.log" << 'PYEOF'
import sys, json, os
sys.path.insert(0, '/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation')
from judge_v1 import judge_run
from metacog_axis import compute_metacog, load_run_nodes
f, rep, wall, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
try:
    _gu = json.load(open('/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/gold-q6-units.json'))
    _gu = _gu["units"] if isinstance(_gu, dict) and "units" in _gu else _gu
    rj = judge_run(f, gold_units=_gu)
    rm = compute_metacog(load_run_nodes(f))
    rec = {"rep": rep, "wall_s": wall, "n_nodes": rj["n_nodes_raw"],
           "judge": {"total": rj["total_score"], "depth": rj["layers"]["structure"]["depth_score"], "cov": rj["layers"]["coverage"]["coverage"]},
           "metacog": {"total": round(rm["metacog_total"],4), "gap": round(rm["gap_rate"],4), "ret": round(rm["retrieval_rate"],4), "hg": round(rm["healthy_gap_rate"],4), "post": round(rm["post_retrieval_accuracy"],4)}}
    scores = json.load(open(out)) if os.path.exists(out) else []
    scores.append(rec)
    json.dump(scores, open(out, 'w'), ensure_ascii=False, indent=1)
    print(f"  [score] n={rec['n_nodes']} {rec['judge']['total']:.4f} depth={rec['judge']['depth']:.3f} cov={rec['judge']['cov']:.3f} metacog={rec['metacog']['total']:.4f}")
except Exception as e:
    print(f"  [score-err] {e}")
    import traceback; traceback.print_exc()
PYEOF
  else
    echo "rep=$rep rc=$rc wall_s=$dur out=MISSING" | tee -a "$LOG"
  fi
done
echo "=== q6-719-nodepth queue DONE $(date '+%F %T') ===" | tee -a "$LOG"
