#!/bin/bash
# Ralph Loop 夜间监控（2026-11-18）
# 监控 gptr + langgraph，挂了重启，全完成后写报告+commit
set -u
cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation

LOG=/tmp/ralph-night.log
DONE_FLAG=/tmp/ralph-night-done.txt
GPTR_LOG=/tmp/gptr-official-3q.log
GPTR_PFB_LOG=/tmp/gptr-pfb-3q.log
LG_NAT_LOG=/tmp/lg-pfb-full-nat.log
LG_GPU_LOG=/tmp/lg-pfb-full-gpu.log
GPTR_RETRIES=0
GPTR_PFB_RETRIES=0
GPTR_PFB_STARTED=0
LG_NAT_RETRIES=0
LG_GPU_STARTED=0
LG_GPU_RETRIES=0
MAX_RETRY=2
INTERVAL=300  # 5分钟

log() { echo "[$(date '+%H:%M:%S')] $*" >> "$LOG"; }

check_8787() {
  local code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 http://127.0.0.1:8787/health 2>/dev/null)
  [ "$code" = "200" ]
}

gptr_done() { grep -q "ALL DONE" "$GPTR_LOG" 2>/dev/null; }
gptr_running() { ps aux | grep "gptr_official" | grep -v grep > /dev/null 2>&1; }
gptr_pfb_done() { grep -q "ALL DONE" "$GPTR_PFB_LOG" 2>/dev/null; }
gptr_pfb_running() { ps aux | grep "gptr_pfb_3q" | grep -v grep > /dev/null 2>&1; }
lg_nat_done() { grep -qE "\[LG:stop\]|FINAL" "$LG_NAT_LOG" 2>/dev/null; }
lg_nat_running() { ps aux | grep "langgraph-pfb-full.*nat" | grep -v grep > /dev/null 2>&1; }
lg_gpu_done() {
  # 2026-11-19 诊断修复：log 判定会被二次启动的 rm+重定向清空/覆盖（19:06:58 事故），
  # 改为"产物 json 存在 或 log 有停止标记"双通道判定，与 night-watch.sh 对齐。
  [ -f "runs-langgraph-pfb-gpu.json" ] && return 0
  grep -qE "\[LG:stop\]|FINAL" "$LG_GPU_LOG" 2>/dev/null
}
lg_gpu_running() { ps aux | grep "langgraph-pfb-full.*gpu" | grep -v grep > /dev/null 2>&1; }

restart_gptr() {
  if [ $GPTR_RETRIES -ge $MAX_RETRY ]; then
    log "gptr: 重试 $MAX_RETRY 次仍失败，跳过"
    return 1
  fi
  GPTR_RETRIES=$((GPTR_RETRIES+1))
  log "gptr: 重启 (第${GPTR_RETRIES}次)"
  .venv-d1/bin/python -u gptr_official_3q.py > "$GPTR_LOG" 2>&1 &
}

restart_lg_nat() {
  if [ $LG_NAT_RETRIES -ge $MAX_RETRY ]; then
    log "langgraph nat: 重试 $MAX_RETRY 次仍失败，跳过"
    return 1
  fi
  LG_NAT_RETRIES=$((LG_NAT_RETRIES+1))
  log "langgraph nat: 重启 (第${LG_NAT_RETRIES}次)"
  rm -f /tmp/langgraph-pfb-full-nat.sqlite*
  /Library/Developer/CommandLineTools/usr/bin/python3 -u langgraph-pfb-full.py nat > "$LG_NAT_LOG" 2>&1 &
}

start_lg_gpu() {
  if [ $LG_GPU_RETRIES -ge $MAX_RETRY ]; then
    log "langgraph gpu: 重试 $MAX_RETRY 次仍失败，跳过"
    return 1
  fi
  LG_GPU_RETRIES=$((LG_GPU_RETRIES+1))
  log "langgraph gpu: 启动 (第${LG_GPU_RETRIES}次)"
  # 2026-11-19 诊断修复：启动前再查一次 done，防"进程不在+log 被覆盖"窗口内误重启已完成任务
  if lg_gpu_done; then
    log "langgraph gpu: 启动前复查发现已完成，取消启动"
    return 0
  fi
  rm -f /tmp/langgraph-pfb-full-gpu.sqlite*
  /Library/Developer/CommandLineTools/usr/bin/python3 -u langgraph-pfb-full.py gpu > "$LG_GPU_LOG" 2>&1 &
}

start_gptr_pfb() {
  if [ $GPTR_PFB_RETRIES -ge $MAX_RETRY ]; then
    log "gptr pfb: 重试 $MAX_RETRY 次仍失败，跳过"
    return 1
  fi
  GPTR_PFB_RETRIES=$((GPTR_PFB_RETRIES+1))
  log "gptr pfb: 启动 (第${GPTR_PFB_RETRIES}次)"
  .venv-d1/bin/python -u gptr_pfb_3q.py > "$GPTR_PFB_LOG" 2>&1 &
}

write_report() {
  log "写汇总报告..."
  local report="runs-gptr-official/night-report.md"
  {
    echo "# 夜间运行报告（2026-11-18）"
    echo ""
    echo "## GPT-Researcher 三题×3rep（depth=6/breadth=6）"
    echo ""
    if [ -f "runs-gptr-official/summary.json" ]; then
      echo '```json'
      cat runs-gptr-official/summary.json
      echo '```'
    else
      echo "summary.json 不存在（gptr 未完成）"
    fi
    echo ""
    echo "## GPT-Researcher pfb 检索层 三题×3rep（depth=6/breadth=6）"
    echo ""
    if [ -f "runs-gptr-pfb/summary.json" ]; then
      echo '```json'
      cat runs-gptr-pfb/summary.json
      echo '```'
    else
      echo "summary.json 不存在（gptr pfb 未完成）"
    fi
    echo ""
    echo "## LangGraph pfb 状态机"
    echo ""
    echo "### nat"
    if [ -f "$LG_NAT_LOG" ]; then
      echo '```'
      grep -E "\[LG:(stop|checkpoint)|S_α|verified|FINAL" "$LG_NAT_LOG" | tail -20
      echo '```'
    fi
    echo ""
    echo "### gpu"
    if [ -f "$LG_GPU_LOG" ]; then
      echo '```'
      grep -E "\[LG:(stop|checkpoint)|S_α|verified|FINAL" "$LG_GPU_LOG" | tail -20
      echo '```'
    else
      echo "gpu 未运行"
    fi
    echo ""
    echo "## 异常记录"
    echo ""
    grep -iE "error|fail|502|traceback" "$GPTR_LOG" 2>/dev/null | tail -10
    grep -iE "error|fail|502|traceback" "$GPTR_PFB_LOG" 2>/dev/null | tail -10
    grep -iE "error|fail|502|traceback" "$LG_NAT_LOG" 2>/dev/null | tail -10
    grep -iE "error|fail|502|traceback" "$LG_GPU_LOG" 2>/dev/null | tail -10
    echo ""
    echo "## 监控日志"
    echo ""
    echo '```'
    cat "$LOG"
    echo '```'
  } > "$report"
  log "报告写好: $report"
}

git_commit() {
  log "git commit..."
  cd /Users/a1-6/Desktop/workspace/pfb
  git add experiments/stage-ablation/runs-gptr-official/ \
          experiments/stage-ablation/runs-gptr-pfb/ \
          experiments/stage-ablation/s5-pipeline-spec.md \
          experiments/stage-ablation/gptr_official_3q.py \
          experiments/stage-ablation/gptr_pfb_3q.py \
          experiments/stage-ablation/pfb_retriever.py \
          experiments/stage-ablation/cc-tasks/ \
          experiments/stage-ablation/ralph-night.sh 2>/dev/null
  git commit -m "night-run: gptr official+pfb 3q×3rep (depth6/breadth6) + langgraph nat/gpu + s5 spec + ralph monitor" 2>&1 >> "$LOG"
  cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
}

# 主循环
# 2026-11-19: 上一轮已写 DONE_FLAG 则直接退出，防二次启动把已完成的 log 覆盖成"文件不存在"错误
if grep -q "ALL TASKS DONE" "$DONE_FLAG" 2>/dev/null; then
  log "DONE_FLAG 已存在（ALL TASKS DONE），直接退出"
  exit 0
fi
log "=== Ralph Night 启动 ==="
log "gptr 进程: $(ps aux | grep gptr_official | grep -v grep | awk '{print $2}')"
log "langgraph nat 进程: $(ps aux | grep 'langgraph-pfb-full.*nat' | grep -v grep | awk '{print $2}')"

# 初始化标志位：检测已在跑的进程（2026-11-19：手动启动 lg gpu / gptr pfb 后重启 ralph-night 用）。
# 不加这段，lg_nat_done=true 且 LG_GPU_STARTED=0 会触发 start_lg_gpu → rm sqlite + 启动重复 lg gpu，
# 把正在跑的进程 checkpoint 删掉。
if lg_gpu_running; then
  LG_GPU_STARTED=1
  log "langgraph gpu: 已在运行，标记 LG_GPU_STARTED=1（不重启）"
fi
if gptr_pfb_running; then
  GPTR_PFB_STARTED=1
  log "gptr pfb: 已在运行，标记 GPTR_PFB_STARTED=1（不重启）"
fi

while true; do
  # 检查 8787
  if ! check_8787; then
    log "8787 不健康，等 60s 再查"
    sleep 60
    continue
  fi

  # gptr 监控
  if ! gptr_done; then
    if ! gptr_running; then
      log "gptr: 进程不在且未完成"
      restart_gptr
    fi
  fi

  # langgraph nat 监控
  if ! lg_nat_done; then
    if ! lg_nat_running; then
      log "langgraph nat: 进程不在且未完成"
      restart_lg_nat
    fi
  fi

  # langgraph nat 完成 → 启动 gpu
  if lg_nat_done && [ $LG_GPU_STARTED -eq 0 ]; then
    LG_GPU_STARTED=1
    start_lg_gpu
  fi

  # langgraph gpu 监控
  if [ $LG_GPU_STARTED -eq 1 ] && ! lg_gpu_done; then
    if ! lg_gpu_running; then
      log "langgraph gpu: 进程不在且未完成"
      start_lg_gpu
    fi
  fi

  # langgraph gpu 完成 → 启动 gptr pfb（若已在跑则只标记，防双启动）
  # 2026-11-19：gptr pfb 改为与 lg gpu 并发（8787 有余量，T53b 已并发无问题）；
  # 手动启动后 ralph-night 看到 gptr_pfb_running 就只标记，不再重复启动。
  if lg_gpu_done && [ $GPTR_PFB_STARTED -eq 0 ]; then
    if gptr_pfb_running; then
      GPTR_PFB_STARTED=1
      log "gptr pfb: 已在运行（手动启动），标记不重启"
    else
      GPTR_PFB_STARTED=1
      start_gptr_pfb
    fi
  fi

  # gptr pfb 监控
  if [ $GPTR_PFB_STARTED -eq 1 ] && ! gptr_pfb_done; then
    if ! gptr_pfb_running; then
      log "gptr pfb: 进程不在且未完成"
      start_gptr_pfb
    fi
  fi

  # 全部完成？
  if gptr_done && lg_nat_done && lg_gpu_done && gptr_pfb_done; then
    log "全部完成，写报告"
    write_report
    git_commit
    echo "ALL TASKS DONE" > "$DONE_FLAG"
    log "=== Ralph Night 结束 ==="
    break
  fi

  # 安全检查：如果所有进程都不在且都失败了
  if ! gptr_running && ! lg_nat_running && ! lg_gpu_running && ! gptr_pfb_running; then
    if ! gptr_done && ! lg_nat_done && ! lg_gpu_done && ! gptr_pfb_done; then
      log "警告：所有进程都不在且都未完成，检查是否全部失败"
      # 给 2 个周期让重启生效
      sleep $INTERVAL
      if ! gptr_running && ! lg_nat_running && ! lg_gpu_running && ! gptr_pfb_running; then
        log "确认全部失败，写报告后退出"
        write_report
        git_commit
        echo "ALL FAILED" > "$DONE_FLAG"
        log "=== Ralph Night 结束（全部失败）==="
        break
      fi
    fi
  fi

  sleep $INTERVAL
done
