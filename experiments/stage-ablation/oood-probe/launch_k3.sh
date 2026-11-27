#!/bin/bash
# K3 launcher: setsid nohup 脱离会话/进程组（任务卡 S2 规定）
cd /Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation
setsid nohup python3 oood-probe/run_k3_hw3.py > oood-probe/k3-hw3.log 2>&1 &
echo $! > oood-probe/k3-hw3.pid
echo "launched pid=$(cat oood-probe/k3-hw3.pid)"
