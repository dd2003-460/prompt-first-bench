#!/bin/bash
# Q6 budget scan 719 落地后一键分析 (2026-11-23 21:10)
# 前置: q6_budget_scan_queue.sh (pid 11929) DONE — 15/15 run 全落地
# 做三件事:
#   1. 全量 CI 分析 (q6_full_analysis.py, 已升级 mean[95%CI]+Welch 档间差)
#   2. 300/719 档 rep 方差对照 (原批 cache 共享 vs 理论独立)
#   3. 触发 rep 独立重跑 (q6_budget_scan_rerun_rep.sh, vLLM 负载已释放)
set -u
cd /Users/a1-6/Desktop/workspace/pfb
SCAN=modules/B-pipeline-ablation/data/q6-budget-scan

# 前置检查: 15 run 全落地?
N=$(ls "$SCAN"/q6-*-r*-[0-9]*.json 2>/dev/null | wc -l | tr -d ' ')
echo "=== 落地 run 数: $N/15 ==="
if [ "$N" -lt 15 ]; then
  echo "⚠️ 未满 15, 列出缺失:"
  for b in 50 100 150 300 719; do for r in 1 2 3; do
    ls "$SCAN"/q6-${b}-r${r}-[0-9]*.json >/dev/null 2>&1 || echo "  缺 q6-${b}-r${r}"
  done; done
  echo "继续跑已有 run 的分析 (缺失档 CI 标注 n 不足)"
fi

echo ""
echo "=== [1/3] 全量 CI 分析 (mean[95%CI] + Welch 档间差) ==="
/usr/bin/python3 modules/B-pipeline-ablation/research/q6_full_analysis.py 2>&1 | tee "$SCAN/full-analysis-$(date '+%Y%m%d-%H%M').txt"

echo ""
echo "=== [2/3] 300/719 档 rep 方差对照 (原批, cache 共享) ==="
python3 - "$SCAN" << 'PYEOF'
import sys, json, os, statistics as st
SCAN = sys.argv[1]
scores = json.load(open(os.path.join(SCAN, "q6-scan-scores.json")))
for b in [300, 719]:
    ms = [r["metacog"]["total"] for r in scores if r["budget"]==b]
    if len(ms)>=2:
        print(f"  budget={b}: metacog reps={ms} mean={st.mean(ms):.4f} sd={st.stdev(ms):.4f} (原批, cache 共享→方差为下界)")
    else:
        print(f"  budget={b}: 仅 {len(ms)} rep, 方差不可算")
PYEOF

echo ""
echo "=== [3/3] 触发 rep 独立重跑 (Q6_REP, 验证 cache 共享压低方差假设) ==="
echo "  启动 q6_budget_scan_rerun_rep.sh (300/719×3, 独立输出目录)..."
nohup bash experiments/stage-ablation/q6_budget_scan_rerun_rep.sh > /tmp/q6-rerun-launch.log 2>&1 &
echo "  rerun pid=$! (输出: modules/B-pipeline-ablation/data/q6-budget-scan-rerun/)"
echo ""
echo "=== 全部触发完成. 重跑落地后对比: 300 档新批 rep sd vs 原批 0.030 — 回升=cache 共享压低假设成立 ==="
