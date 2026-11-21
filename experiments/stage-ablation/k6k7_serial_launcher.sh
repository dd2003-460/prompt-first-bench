#!/bin/zsh
# K6+K7 串行 launcher（research-agi-budget goal，2026-11-22）
# 串行理由：K6 的 Arm B 基线 0.4261 是特定负载下采的；K7 并发会引入
# NVFP4+MTP 非确定性，破坏 K6 单变量对比（同负载要求）。
# K7 内部 15 run 同窗口可比，但 K6 的 Arm A 必须与 Arm B 同条件。
# 用法: zsh k6k7_serial_launcher.sh  （后台跑，~7-9h）
set -uo pipefail
cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
LOG=/tmp/ablation-k6k7.log
echo "=== K6+K7 serial launcher started $(date '+%F %T') ===" | tee "$LOG"

# K6: merge 消融（Arm A concat vs Arm B merge=0.4261，单变量 merge on/off）
# 输入 719-node 树（runs-s5-sm-gpu-resume.json），qid=gpu（judge 用 gpu gold）
if [ -f /tmp/merge-ablation/merge-ablation-concat.json ]; then
  echo "[K6] 已存在 /tmp/merge-ablation/merge-ablation-concat.json，跳过" | tee -a "$LOG"
else
  mkdir -p /tmp/merge-ablation
  echo "[K6] merge 消融 started $(date '+%F %T')" | tee -a "$LOG"
  python3 -u merge_ablation.py runs-s5-sm-gpu-resume.json gpu /tmp/merge-ablation/merge-ablation \
    2>&1 | tee -a "$LOG"
  echo "[K6] merge 消融 finished $(date '+%F %T')" | tee -a "$LOG"
fi

# K7: 预算扫描（max_nodes 50/100/150/300/719 × 3 reps = 15 runs，串行）
echo "[K7] 预算扫描 started $(date '+%F %T')" | tee -a "$LOG"
zsh budget_scan_batch.sh 2>&1 | tee -a "$LOG"
echo "[K7] 预算扫描 finished $(date '+%F %T')" | tee -a "$LOG"

echo "=== K6+K7 DONE $(date '+%F %T') ===" | tee -a "$LOG"
