#!/bin/bash
# 等 nat 跑完 → 清缓存 → 重跑 nat/soc/gpu（新白名单）
# 用法: bash wait-and-rerun.sh
# 前置: nat 进程 pid 由参数传入，或自动检测

set -e

cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation

# 等待 nat 进程结束
NAT_PID=$1
if [ -z "$NAT_PID" ]; then
    # 自动检测
    NAT_PID=$(pgrep -f "s5_state_machine.py --qs nat" | head -1)
fi

echo "[wait-and-rerun] Waiting for nat pid=$NAT_PID to exit..."
while kill -0 "$NAT_PID" 2>/dev/null; do
    sleep 10
done
echo "[wait-and-rerun] nat exited. Clearing cache and restarting..."

# 清缓存
rm -rf .research-cache/
echo "[wait-and-rerun] Cache cleared."

# 重跑 nat
echo "[wait-and-rerun] Starting nat..."
python3 s5_state_machine.py --qs nat --obj-mode=method_challenge --out runs-s5-sm-nat-mc-v3 2>&1 | tee runs-s5-sm-nat-mc-v3.log

# 重跑 soc
echo "[wait-and-rerun] Starting soc..."
python3 s5_state_machine.py --qs soc --obj-mode=method_challenge --out runs-s5-sm-soc-mc-v3 2>&1 | tee runs-s5-sm-soc-mc-v3.log

# 重跑 gpu
echo "[wait-and-rerun] Starting gpu..."
python3 s5_state_machine.py --qs gpu --obj-mode=method_challenge --out runs-s5-sm-gpu-mc-v3 2>&1 | tee runs-s5-sm-gpu-mc-v3.log

echo "[wait-and-rerun] All done."
