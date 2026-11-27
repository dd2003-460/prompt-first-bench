#!/bin/bash
# Q9E 补跑队列 (2026-11-27): 300-r2/r3 + 719-r1/r2/r3
# 原队列 q9_budget_scan_queue.sh 14:47 (300-r1) 后死亡: 无 DONE 行, 进程消失, 无 300-r2 起的 log 行
# (macOS 休眠/进程组回收 — 长跑进程纪律: 起长任务用 setsid nohup, 本脚本同样适用)
# 与原队列完全同构 (qid/SM_CKPT_DIR/stdout 命名/log 路径), 只换循环范围
# 用法: setsid nohup bash q9_budget_scan_resume.sh > /tmp/q9-resume-nohup.log 2>&1 &
set -u
# 2026-11-27 22:20 修: 干净 shell 无继承 PYTHONPATH → 裸 import prompts/s5_pipeline/s8b_pilot 全挂 (5 run 秒败).
# 照抄生产 wrapper run_q9_gated.py L12-16 三目录 (D/scripts + A/scripts + stage-ablation).
export PYTHONPATH="/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/D-decomp-state-machine/scripts:/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/A-eval-infra/scripts:/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation"
cd /Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation
QFILE=/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/questions/Q9-agi-pure.txt
OUT=/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/B-pipeline-ablation/data/q9-budget-scan
LOG=/tmp/q9-budget-scan-queue.log
mkdir -p "$OUT"
echo "=== q9-budget-scan RESUME started $(date '+%F %T') (300-r2/3 + 719-r1/2/3) ===" | tee -a "$LOG"

for spec in "300 2" "300 3" "719 1" "719 2" "719 3"; do
  budget=${spec% *}; rep=${spec#* }
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
echo "=== q9-budget-scan RESUME DONE $(date '+%F %T') ===" | tee -a "$LOG"
