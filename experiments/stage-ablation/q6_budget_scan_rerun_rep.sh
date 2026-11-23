#!/bin/bash
# Q6 budget scan 重跑 (rep 独立 cache 验证, 2026-11-23 21:05)
# 目的: 原批 3 rep 共享 source cache (research_hook.py cache key 不含 rep) → rep 方差被压低
#   (见 data/q6-budget-scan/partial-analysis-20261123.md "根因已确认" 段)。
# 本脚本: 300/719 档 × 3 reps, export Q6_REP=$rep → cache key 含 rep → rep 间 source 层独立。
# 前置: q6_budget_scan_queue.sh (pid 11929) 已结束 — vLLM 负载释放, 否则并发破坏同负载前提。
# 输出: $OUT 独立目录 (不碰原批 q6-*.json), 评分写 $OUT/q6-rerun-scores.json。
# 对照: 跑完后 300 档新批 rep 方差 vs 原批 (0.0003/0.030) — 方差回升 = cache 共享压低假设成立。
set -u
cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
QFILE=/Users/a1-6/Desktop/workspace/pfb/bench/questions/Q6-network-arch.txt
OUT=/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/q6-budget-scan-rerun
LOG=/tmp/q6-budget-scan-rerun.log
mkdir -p "$OUT"
echo "=== q6-budget-scan-rerun queue started $(date '+%F %T') ===" | tee "$LOG"

for budget in 300 719; do
  for rep in 1 2 3; do
    ts=$(date '+%Y%m%d-%H%M%S')
    t0=$(date +%s)
    # Q6_REP=$rep → research_hook.py _REP_TAG → cache key 含 rep (rep 间 source 独立)
    # /usr/bin/python3 绝对路径 — 后台 session PATH 不带用户 python 目录, sentence_transformers 缺失 (4e9c175db 坑)
    Q6_REP="$rep" SM_CKPT_DIR="$OUT/checkpoints" /usr/bin/python3 s5_state_machine.py \
      --question-file "$QFILE" --qid q6 --max-nodes $budget \
      > "$OUT/q6-${budget}-r${rep}.stdout" 2>&1
    rc=$?
    t1=$(date +%s)
    dur=$((t1 - t0))
    if [ -f runs-s5-sm-q6.json ]; then
      cp runs-s5-sm-q6.json "$OUT/q6-${budget}-r${rep}-${ts}.json"
      echo "budget=$budget rep=$rep rc=$rc wall_s=$dur out=q6-${budget}-r${rep}-${ts}.json" | tee -a "$LOG"
      # 评分 (stderr 落盘 — 修原批 2>/dev/null 吞异常, 见 partial-analysis 数据质量事件段; /usr/bin/python3 绝对路径)
      /usr/bin/python3 - "$OUT/q6-${budget}-r${rep}-${ts}.json" "$budget" "$rep" "$dur" "$OUT/q6-rerun-scores.json" 2>>"$OUT/q6-score-stderr.log" << 'PYEOF'
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
echo "=== q6-budget-scan-rerun queue DONE $(date '+%F %T') ===" | tee -a "$LOG"

# [对比] 重跑批 (rep 独立 cache) vs 原批 (cache 共享) rep 方差
# 判据: 重跑 sd 显著 > 原批 sd (300 原批 judge=0.0212 metacog=0.0304) → cache 共享压低方差假设成立
# 719 档注意: 重跑同样不传 --max-depth → 仍撞 max_depth=4 (~351 节点), 测的是方差非 719 预算
echo "=== [对比] 重跑批 vs 原批 rep 方差 (cache 共享压低假设验证) ===" | tee -a "$LOG"
/usr/bin/python3 - "$OUT" << 'PYEOF' | tee -a "$LOG"
import sys, json, os, statistics as st
OUT = sys.argv[1]
ORIG = "/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/q6-budget-scan"
def load(p):
    try: return json.load(open(p))
    except Exception: return []
orig = load(os.path.join(ORIG, "q6-scan-scores.json"))
rerun = load(os.path.join(OUT, "q6-rerun-scores.json"))
print(f"  {'budget':<8} {'轴':<9} {'原批 sd (n)':<18} {'重跑 sd (n)':<18} 判定")
for b in [300, 719]:
    for axis, key in [("judge", "judge"), ("metacog", "metacog")]:
        oj = [r[key]["total"] for r in orig if r.get("budget") == b]
        rj = [r[key]["total"] for r in rerun if r.get("budget") == b]
        os_ = f"{st.stdev(oj):.4f} (n={len(oj)})" if len(oj) >= 2 else f"n={len(oj)} 不可算"
        rs_ = f"{st.stdev(rj):.4f} (n={len(rj)})" if len(rj) >= 2 else f"n={len(rj)} 不可算"
        verdict = ""
        if len(oj) >= 2 and len(rj) >= 2:
            verdict = "↑ 回升 (假设支持)" if st.stdev(rj) > st.stdev(oj) * 1.3 else "≈ 持平 (假设存疑)"
        print(f"  {b:<8} {axis:<9} {os_:<18} {rs_:<18} {verdict}")
print("  判据: 重跑 sd > 原批 sd × 1.3 → cache 共享压低方差假设成立; 持平 → 方差本就这么低, cache 非主因")
PYEOF
