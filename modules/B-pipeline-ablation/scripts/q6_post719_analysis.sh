#!/bin/bash
# Q6 budget scan 719 落地后一键分析 (2026-11-23 21:10)
# 前置: q6_budget_scan_queue.sh (pid 11929) DONE — 15/15 run 全落地
# 做两件事:
#   1. 全量 CI 分析 (q6_full_analysis.py, 已升级 mean[95%CI]+Welch 档间差)
#   2. 300/719 档 rep 方差对照 (原批 cache 共享 vs 理论独立)
# rep 独立重跑由 q6_rerun_watchdog.sh (pid 74600) 自动接力, 本脚本不重复触发
#   (2026-11-23 21:17 修正: 原 [3/3] 会与 watchdog 双启重跑队列 → vLLM 并发非确定)
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
echo "=== [1.5/3] 各 rep 实际节点数 (K7 硬顶验证 + 719 是否花满预算) ==="
python3 - "$SCAN" << 'PYEOF'
import sys, json, os, glob
SCAN = sys.argv[1]
print("  budget  rep  realized_nodes  (max_nodes=预算; <预算 = 模型提前自然停止, 预算没花满)")
for b in [50, 100, 150, 300, 719]:
    for r in [1, 2, 3]:
        fs = sorted(glob.glob(os.path.join(SCAN, f"q6-{b}-r{r}-[0-9]*.json")))
        if not fs:
            print(f"  {b:<7} r{r}    (未落地)")
            continue
        d = json.load(open(fs[-1]))
        n = len(d.get("nodes", []))
        flag = "" if n >= b else f"  ← {n}/{b} 未花满!"
        print(f"  {b:<7} r{r}    {n}{flag}")
PYEOF

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
echo "=== 分析完成. rep 独立重跑由 watchdog (q6_rerun_watchdog.sh) 自动接力 ==="
echo "=== 重跑落地后对比: 300 档新批 rep sd vs 原批 0.030 — 回升=cache 共享压低假设成立 ==="
