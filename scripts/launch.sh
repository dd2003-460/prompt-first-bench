#!/usr/bin/env bash
# launch.sh — pfb pipeline 唯一启动方式（防静默死）
# 用法: ./scripts/launch.sh <tag> -- <python 命令...>
#   例: ./scripts/launch.sh v18-hier -- python3 experiments/stage-ablation/s5_pipeline.py --hierarchy ...
# 保证: log 落盘 + PID 文件 + 退出时追加 exit code 行（进程死了也能看到）
set -u
if [ $# -lt 2 ] || [ "$1" = "--" ]; then echo "usage: $0 <tag> -- <cmd...>" >&2; exit 2; fi
tag="$1"; shift
[ "$1" = "--" ] && shift
log="runs-$tag-console.log"
pidf="runs-$tag.pid"
cd "$(dirname "$0")/.."
(
  { date '+%F %T'; echo "[launch] tag=$tag cmd=$*"; } >> "$log"
  "$@" >> "$log" 2>&1
  rc=$?
  echo "[launch] $(date '+%F %T') EXIT=$rc tag=$tag" >> "$log"
) &
echo $! > "$pidf"
echo "launched pid=$(cat "$pidf") log=$log"