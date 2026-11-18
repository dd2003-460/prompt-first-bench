#!/bin/bash
# restart.sh — 重启指定实验进程（供 cron agent / 手动调用）
# 用法: bash restart.sh [gptr|lgnat|lggpu|ralph|all]
# 设计：前台跑本脚本，内部用 & 起实验进程（脚本退出后进程被 init 收养，脱离会话，不怕会话断）
set -u
cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation

PY39="/Library/Developer/CommandLineTools/usr/bin/python3"
PYVENV=".venv-d1/bin/python"

gptr_done()  { grep -q "ALL DONE" /tmp/gptr-official-3q.log 2>/dev/null; }
lgnat_done() { grep -qE "\[LG:stop\]|FINAL|Traceback" /tmp/lg-pfb-full-nat.log 2>/dev/null; }
lggpu_done() { grep -qE "\[LG:stop\]|FINAL|Traceback" /tmp/lg-pfb-full-gpu.log 2>/dev/null; }

restart_gptr() {
  if pgrep -f "gptr_official" > /dev/null 2>&1; then echo "gptr: already running"; return; fi
  if gptr_done; then echo "gptr: already done"; return; fi
  echo "gptr: restarting..."
  $PYVENV -u gptr_official_3q.py > /tmp/gptr-official-3q.log 2>&1 &
  echo "gptr: pid $!"
}

restart_lgnat() {
  if pgrep -f "langgraph-pfb-full.*nat" > /dev/null 2>&1; then echo "lgnat: already running"; return; fi
  if lgnat_done; then echo "lgnat: already done"; return; fi
  echo "lgnat: restarting..."
  rm -f /tmp/langgraph-pfb-full-nat.sqlite*
  $PY39 -u langgraph-pfb-full.py nat --max-nodes 12 --max-depth 2 > /tmp/lg-pfb-full-nat.log 2>&1 &
  echo "lgnat: pid $!"
}

restart_lggpu() {
  if pgrep -f "langgraph-pfb-full.*gpu" > /dev/null 2>&1; then echo "lggpu: already running"; return; fi
  if lggpu_done; then echo "lggpu: already done"; return; fi
  echo "lggpu: starting..."
  rm -f /tmp/langgraph-pfb-full-gpu.sqlite*
  $PY39 -u langgraph-pfb-full.py gpu --max-nodes 12 --max-depth 2 > /tmp/lg-pfb-full-gpu.log 2>&1 &
  echo "lggpu: pid $!"
}

restart_ralph() {
  if pgrep -f "ralph-night.sh" > /dev/null 2>&1; then echo "ralph: already running"; return; fi
  echo "ralph: restarting..."
  bash ralph-night.sh > /tmp/ralph-night-stdout.log 2>&1 &
  echo "ralph: pid $!"
}

TARGET="${1:-all}"
case "$TARGET" in
  gptr)  restart_gptr ;;
  lgnat) restart_lgnat ;;
  lggpu) restart_lggpu ;;
  ralph) restart_ralph ;;
  all)   restart_gptr; restart_lgnat; restart_lggpu; restart_ralph ;;
  *) echo "unknown target: $TARGET (use gptr|lgnat|lggpu|ralph|all)"; exit 1 ;;
esac
