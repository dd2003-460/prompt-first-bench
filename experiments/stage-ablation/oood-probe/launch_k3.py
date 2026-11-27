#!/usr/bin/env python3
"""K3 launcher: os.setsid() 脱离会话/进程组（macOS 无 setsid 命令，等效实现，任务卡 S2 语义）"""
import os, sys
AB = "/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation"
logf = open(f"{AB}/oood-probe/k3-hw3.log", "wb")
pid = os.fork()
if pid == 0:
    os.setsid()
    os.chdir(AB)
    os.dup2(logf.fileno(), 1)
    os.dup2(logf.fileno(), 2)
    os.execvp("python3", ["python3", "oood-probe/run_k3_hw3.py"])
with open(f"{AB}/oood-probe/k3-hw3.pid", "w") as f:
    f.write(str(pid))
print(f"launched pid={pid}")
