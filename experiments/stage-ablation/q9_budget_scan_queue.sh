#!/bin/bash
# Q9 (q9-agi) budget scan 队列 (2026-11-27): research-agi-budget 子项⑤ — AGI 题面 E 预算扫描
# 设计: experiments/stage-ablation/tasks/q9-e-experiment-design-20261124.md (端点冻结)
#   5 档 (50/100/150/300/719, 与 K7 gpu / q6 同档位, 跨域曲线可比) × 3 reps = 15 runs × ~45min ≈ 11h
#   主端点 = per-budget gate 叶命中率 (11 gate 叶, gold-q9-units.json) — 找 gate 命中率首次达 100% 的最小预算
#   P1 预测: gate 叶多为单事实判据, ~100-150 节点饱和 (远低于 cov 轴 ~300 拐点)
#
# 与 q6 脚本的差异 (最小化, 评分全部后置):
#   ① QFILE = questions/Q9-agi-pure.txt (纯题面, 已去 gold 段, 泄漏检查 0 — 防答案泄露进 prompt)
#   ② qid = q9-agi, OUT = data/q9-budget-scan (隔离, 不碰 q6/gpu/nat/soc 数据)
#   ③ 不做增量双轴评分 (judge gold 公式跨域错位 + 主端点是 per-gate 矩阵, 均后置算)
#      — 只跑 SM + 存 run json + 记日志; 评分由后置分析任务从 run json + gold-q9-units.json 直接算
# 输出隔离 (2026-11-23 15:53 事故后纪律):
#   ① SM_CKPT_DIR → $OUT/checkpoints (不碰 checkpoints/sm-* 原始数据)
#   ② runs-s5-sm-q9-agi.json 是 q9-agi 专属新文件, 跑完 cp 到 $OUT
# 用法: 后台跑, 完成通知 (executor-cron 认领, pid 文件 + monitor 跟踪)
set -u
cd /Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation
QFILE=/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/questions/Q9-agi-pure.txt
OUT=/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/B-pipeline-ablation/data/q9-budget-scan
LOG=/tmp/q9-budget-scan-queue.log
mkdir -p "$OUT"
echo "=== q9-budget-scan queue started $(date '+%F %T') ===" | tee "$LOG"

for budget in 50 100 150 300 719; do
  for rep in 1 2 3; do
    ts=$(date '+%Y%m%d-%H%M%S')
    t0=$(date +%s)
    SM_CKPT_DIR="$OUT/checkpoints" python3 s5_state_machine.py \
      --question-file "$QFILE" --qid q9-agi --max-nodes $budget --max-depth 10 \
      > "$OUT/q9-${budget}-r${rep}.stdout" 2>&1
    rc=$?
    t1=$(date +%s)
    dur=$((t1 - t0))
    if [ -f runs-s5-sm-q9-agi.json ]; then
      cp runs-s5-sm-q9-agi.json "$OUT/q9-${budget}-r${rep}-${ts}.json"
      nn=$(python3 -c "import json;print(json.load(open('$OUT/q9-${budget}-r${rep}-${ts}.json'))['n_nodes'])" 2>/dev/null || echo "?")
      echo "budget=$budget rep=$rep rc=$rc wall_s=$dur n_nodes=$nn out=q9-${budget}-r${rep}-${ts}.json" | tee -a "$LOG"
    else
      echo "budget=$budget rep=$rep rc=$rc wall_s=$dur out=MISSING" | tee -a "$LOG"
    fi
  done
done
echo "=== q9-budget-scan queue DONE $(date '+%F %T') ===" | tee -a "$LOG"
