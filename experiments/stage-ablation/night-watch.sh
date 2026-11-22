#!/bin/bash
# night-watch.sh — 确定性监控脚本（无时间戳，供 cron monitor 用）
# 输出格式: GPTR:<state> LGNAT:<state> LGGPU:<state> RALPH:<state> 8787:<state>
# state: alive|dead|done|notstarted|ok|fail
cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
# 空 locale 下 pgrep 会报 illegal byte sequence 全失败→误判全 dead；固定 C locale
export LC_ALL=C LANG=C

gptr="dead"
if grep -q "ALL DONE" /tmp/gptr-official-3q.log 2>/dev/null; then
  gptr="done"
elif pgrep -f "gptr_official" > /dev/null 2>&1; then
  gptr="alive"
fi

lgnat="dead"
if grep -qE "\[LG:stop\]|FINAL|Traceback" /tmp/lg-pfb-full-nat.log 2>/dev/null; then
  lgnat="done"
elif pgrep -f "langgraph-pfb-full.*nat" > /dev/null 2>&1; then
  lgnat="alive"
fi

lggpu="notstarted"
# 2026-11-19: 产物 json 存在即 done（log 可能被 ralph 二次启动覆盖成错误信息）
if [ -f runs-langgraph-pfb-gpu.json ]; then
  lggpu="done"
elif [ -f /tmp/lg-pfb-full-gpu.log ]; then
  if grep -qE "\[LG:stop\]|FINAL|Traceback" /tmp/lg-pfb-full-gpu.log 2>/dev/null; then
    lggpu="done"
  elif pgrep -f "langgraph-pfb-full.*gpu" > /dev/null 2>&1; then
    lggpu="alive"
  else
    lggpu="dead"
  fi
fi

ralph="dead"
# 2026-11-19: 全完成后 ralph 正常退出，DONE_FLAG 存在则判 done（非故障，不触发重启）
if [ -f /tmp/ralph-night-done.txt ] && grep -q "ALL TASKS DONE" /tmp/ralph-night-done.txt 2>/dev/null; then
  ralph="done"
elif pgrep -f "ralph-night.sh" > /dev/null 2>&1; then
  ralph="alive"
fi

h8787="fail"
code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 http://127.0.0.1:8787/health 2>/dev/null)
[ "$code" = "200" ] && h8787="ok"

echo "GPTR:$gptr LGNAT:$lgnat LGGPU:$lggpu RALPH:$ralph 8787:$h8787"
