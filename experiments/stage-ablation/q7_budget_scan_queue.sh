#!/bin/bash
# Q7 budget scan 队列 (2026-11-23 22:55): general 方法论 A1 — 第三域验证 (GPU+Q6+Q7)
# 前置: rep 独立重跑队列 (q6_budget_scan_rerun_rep.sh) 跑完, vLLM 负载释放
# 设计: 同 Q6 扫描 5 档 (50/100/150/300/719) × 3 reps = 15 runs
# Q6 踩坑全避开:
#   ① Q6_REP=$rep → cache key 含 rep → rep 间 source 独立 (Q6 原批 cache 共享压低方差)
#   ② /usr/bin/python3 绝对路径 (后台 PATH 缺 sentence_transformers, 4e9c175db 坑)
#   ③ 评分 stderr 落盘 (Q6 原批 2>/dev/null 吞异常, 719-r1 静默失败)
# 输出: $OUT 独立目录, 评分写 $OUT/q7-scan-scores.json
# !! 2026-11-24 澄清 (Q6 36/46-unit bug 同源排查): 评分实际用 Q7 in-domain gold (52 units,
#    见下方 judge_run(f, gold_units=_gu), _gu=gold-q7-units.json), 不是 gpu gold。
#    旧注释"默认 gpu gold = 跨域口径"与代码不符, 已修正 — 跨域口径需另跑 judge_v1 --gold-units gold-gpu-units.json。
set -u
cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
QFILE=/Users/a1-6/Desktop/workspace/pfb/bench/questions/Q7-storage-arch.txt
OUT=/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/q7-budget-scan
LOG=/tmp/q7-budget-scan.log
mkdir -p "$OUT"
echo "=== q7-budget-scan queue started $(date '+%F %T') ===" | tee "$LOG"

for budget in 50 100 150 300 719; do
  for rep in 1 2 3; do
    ts=$(date '+%Y%m%d-%H%M%S')
    t0=$(date +%s)
    # Q6_REP 是 research_hook.py 的通用 rep 标识变量名 (历史命名, 非 Q6 专属) —
    # 设值后 cache key 含 rep → rep 间 source 独立, 对 Q7 同样生效
    # --max-depth 10: D 2026-11-23 指令"不要限制深度" — 默认 max_depth=4 是 harness
    # 人工约束, 会把约束产物误读为模型行为; 10 层 ≥ gold 主干深度 5, 实质无限制,
    # 预算 (--max-nodes) 成为唯一约束 → 干净的预算轴
    Q6_REP="$rep" SM_CKPT_DIR="$OUT/checkpoints" /usr/bin/python3 s5_state_machine.py \
      --question-file "$QFILE" --qid q7 --max-nodes $budget --max-depth 10 \
      > "$OUT/q7-${budget}-r${rep}.stdout" 2>&1
    rc=$?
    t1=$(date +%s)
    dur=$((t1 - t0))
    if [ -f runs-s5-sm-q7.json ]; then
      cp runs-s5-sm-q7.json "$OUT/q7-${budget}-r${rep}-${ts}.json"
      echo "budget=$budget rep=$rep rc=$rc wall_s=$dur out=q7-${budget}-r${rep}-${ts}.json" | tee -a "$LOG"
      /usr/bin/python3 - "$OUT/q7-${budget}-r${rep}-${ts}.json" "$budget" "$rep" "$dur" "$OUT/q7-scan-scores.json" 2>>"$OUT/q7-score-stderr.log" << 'PYEOF'
import sys, json, os
sys.path.insert(0, '/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation')
from judge_v1 import judge_run
from metacog_axis import compute_metacog, load_run_nodes
f, budget, rep, wall, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
try:
    _gu = json.load(open('/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/gold-q7-units.json'))
    _gu = _gu["units"] if isinstance(_gu, dict) and "units" in _gu else _gu
    rj = judge_run(f, gold_units=_gu)
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
    import traceback; traceback.print_exc()
PYEOF
    else
      echo "budget=$budget rep=$rep rc=$rc wall_s=$dur out=MISSING" | tee -a "$LOG"
    fi
  done
done
echo "=== q7-budget-scan queue DONE $(date '+%F %T') ===" | tee -a "$LOG"
