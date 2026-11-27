#!/bin/bash
# Q9E 补跑队列 v2 (2026-11-28 00:4x): 幂等 + 每 run 独立 ckpt 目录 + 失败重试
# v1 死因记录: 22:21/22:51 两次 SIGTERM (会话重建), 22:55 脱离版 300-r2 成功后 300-r3 被 SIGKILL (00:33, 凶手未定: 无 sleep/jetsam 记录)
# v2 设计 (整体而非补丁):
#   1. 幂等: 每 (budget,rep) 先查 OUT 里已有 q9-B-rR-*.json 且 n_nodes>=budget*0.99 → 跳过
#   2. 每 run 独立 ckpt 目录 (SM_CKPT_DIR=$OUT/ckpts/B-rR) → 消除跨 run 目录复用污染 (r1-r4 混写两次事故)
#   3. 单 run 失败重试 1 次 (间隔 60s)
#   4. 每 run 结束打 LOG 行 (watcher 据此判断)
# 用法: 由 watcher v3 通过 launch_q9_detached_v2.sh 拉起 (PPID=1)
set -u
export PYTHONPATH="/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/D-decomp-state-machine/scripts:/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/A-eval-infra/scripts:/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation"
cd /Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation || exit 1
QFILE=/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/questions/Q9-agi-pure.txt
OUT=/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/B-pipeline-ablation/data/q9-budget-scan
LOG=/tmp/q9-budget-scan-queue.log
mkdir -p "$OUT/ckpts"
echo "=== q9-budget-scan QUEUE-V2 started $(date '+%F %T') ===" | tee -a "$LOG"

# 幂等检查: 该 (budget,rep) 已有合格产出?
already_done() {
  local budget=$1 rep=$2
  local f
  for f in "$OUT"/q9-${budget}-r${rep}-*.json; do
    [ -f "$f" ] || continue
    local nn
    nn=$(python3 -c "import json;print(json.load(open('$f'))['n_nodes'])" 2>/dev/null || echo 0)
    local need=$((budget * 99 / 100))
    if [ "$nn" -ge "$need" ] 2>/dev/null; then
      echo "$f"
      return 0
    fi
  done
  return 1
}

for spec in "300 2" "300 3" "719 1" "719 2" "719 3"; do
  budget=${spec% *}; rep=${spec#* }
  done_file=$(already_done $budget $rep)
  if [ -n "$done_file" ]; then
    echo "budget=$budget rep=$rep SKIP (existing: $(basename $done_file))" | tee -a "$LOG"
    continue
  fi
  CKPT="$OUT/ckpts/${budget}-r${rep}"
  mkdir -p "$CKPT"
  for attempt in 1 2; do
    ts=$(date '+%Y%m%d-%H%M%S')
    t0=$(date +%s)
    SM_CKPT_DIR="$CKPT" python3 s5_state_machine.py \
      --question-file "$QFILE" --qid q9-agi --max-nodes $budget --max-depth 10 \
      > "$OUT/q9-${budget}-r${rep}.stdout" 2>&1
    rc=$?
    t1=$(date +%s)
    dur=$((t1 - t0))
    if [ -f runs-s5-sm-q9-agi.json ]; then
      # 2026-11-28 00:4x 修: runs-s5-sm-q9-agi.json 是 SM 固定输出名 (从不清理),
      # 上一 run 被杀后残留 → 下一 run 若也异常会复制上次的旧文件冒充产出 (300-r3 假文件事故).
      # 校验: mtime 必须晚于本次 run 开始时刻 (t0), 否则视为 MISSING.
      if [ "$(stat -f %m runs-s5-sm-q9-agi.json)" -gt "$t0" ]; then
        cp runs-s5-sm-q9-agi.json "$OUT/q9-${budget}-r${rep}-${ts}.json"
        nn=$(python3 -c "import json;print(json.load(open('$OUT/q9-${budget}-r${rep}-${ts}.json'))['n_nodes'])" 2>/dev/null || echo "?")
        echo "budget=$budget rep=$rep rc=$rc wall_s=$dur n_nodes=$nn out=q9-${budget}-r${rep}-${ts}.json attempt=$attempt" | tee -a "$LOG"
        [ $rc -eq 0 ] && break
      else
        echo "budget=$budget rep=$rep rc=$rc wall_s=$dur out=STALE_SKIP (runs json mtime<=t0, 疑似上次残留) attempt=$attempt" | tee -a "$LOG"
      fi
    else
      echo "budget=$budget rep=$rep rc=$rc wall_s=$dur out=MISSING attempt=$attempt" | tee -a "$LOG"
    fi
    [ $attempt -eq 1 ] && { echo "retry in 60s..." | tee -a "$LOG"; sleep 60; }
  done
done
echo "=== q9-budget-scan QUEUE-V2 DONE $(date '+%F %T') ===" | tee -a "$LOG"
