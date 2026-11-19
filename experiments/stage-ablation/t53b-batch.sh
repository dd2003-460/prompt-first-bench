#!/bin/bash
# T53b 消融实验批量执行器（2026-11-19）
# 循环调用 ablation_driver.sh，每个 run 完成后 driver 自动更新 cc-state.json
# 失败时标记 done=true + 写 cc-to-lead.md（避免无限循环）
# 全部完成后 git commit
# 启动: setsid nohup bash t53b-batch.sh > /tmp/t53b-batch.log 2>&1 &

set -uo pipefail
cd /Users/a1-6/Desktop/workspace/pfb
STAGE=experiments/stage-ablation
CC_STATE=tasks/T53-bus/cc-state.json
# 支持 QID 过滤：bash t53b-batch.sh nat 只跑 nat 题（并行模式）
QID_FILTER="${1:-}"
if [ -n "$QID_FILTER" ]; then
  LOG="/tmp/t53b-batch-${QID_FILTER}.log"
  PIDFILE="/tmp/t53b-batch-${QID_FILTER}.pid"
else
  LOG=/tmp/t53b-batch.log
  PIDFILE=/tmp/t53b-batch.pid
fi
echo $$ > "$PIDFILE"

log() { echo "[$(date '+%F %H:%M:%S')] $*" >> "$LOG"; }

log "=== T53b 批量执行器启动 (pid $$, qid=${QID_FILTER:-all}) ==="

RUNS=0
OK=0
FAIL=0
MAX_RUNS=60  # 安全上限（55 个 pending + 余量）

while [ $RUNS -lt $MAX_RUNS ]; do
  # 取下一个 pending run（可选 QID 过滤）
  PENDING=$(QID_FILTER="$QID_FILTER" python3 -c "
import json, re, os
s=json.load(open('$CC_STATE'))
pat=re.compile(r'^(gpu|nat|soc)_(formula|text)_r(\d{2})$')
qid_filter = os.environ.get('QID_FILTER','')
for wu in s['work_units']:
    name = wu.get('name','')
    if not wu.get('done') and pat.match(name):
        if qid_filter and not name.startswith(qid_filter + '_'):
            continue
        print(name); break
")

  if [ -z "$PENDING" ]; then
    log "所有 run 已完成"
    break
  fi

  log "开始: $PENDING (第 $((RUNS+1))/$MAX_RUNS)"
  RUNS=$((RUNS+1))

  # 跑一个 run（前台，无超时——driver 内部 SM_SEED=42，约 30min/run）
  # T53B_RUN 传给 driver，避免 driver 自己取 pending 时跨题抢 run（并行模式）
  if T53B_RUN="$PENDING" zsh "$STAGE/ablation_driver.sh" >> "$LOG" 2>&1; then
    log "完成: $PENDING"
    OK=$((OK+1))
  else
    RC=$?
    log "失败: $PENDING (rc=$RC)，标记 done 跳过"
    FAIL=$((FAIL+1))
    # 标记为 done=true（避免无限循环）
    # 用 heredoc + 环境变量传递，避免 bash 对多行双引号字符串的变量展开边界行为（T1 测试暴露）
    T53B_PENDING="$PENDING" T53B_RC="$RC" T53B_CC_STATE="$CC_STATE" python3 << 'PYEOF'
import json, os
cc_state = os.environ['T53B_CC_STATE']
pending = os.environ['T53B_PENDING']
rc = os.environ['T53B_RC']
s = json.load(open(cc_state))
for wu in s['work_units']:
    if wu.get('name') == pending:
        wu['done'] = True
        wu['note'] = (wu.get('note','') + ' | 批量执行器: 失败 rc=' + rc + '，标记跳过').strip(' |')
        break
json.dump(s, open(cc_state,'w'), ensure_ascii=False, indent=2)
PYEOF
    {
      echo "## 批量执行器失败: $PENDING ($(date '+%F %T'))"
      echo "rc=${RC}，查 /tmp/t53b-batch.log"
      echo ""
    } >> tasks/T53-bus/cc-to-lead.md
  fi
done

log "=== T53b 批量执行器结束: $RUNS runs ($OK ok, $FAIL fail) ==="

# git commit
cd /Users/a1-6/Desktop/workspace/pfb
git add tasks/T53-bus/cc-state.json \
        experiments/stage-ablation/ablation-runs/ \
        experiments/stage-ablation/ablation-notes/ \
        experiments/stage-ablation/ablation-results.json \
        tasks/T53-bus/cc-to-lead.md 2>/dev/null
git commit -m "T53b: $RUNS ablation runs ($OK ok, $FAIL fail) via batch driver" 2>&1 >> "$LOG"
log "git commit 完成"
