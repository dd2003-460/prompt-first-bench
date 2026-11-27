#!/usr/bin/env python3
"""K3 watcher: 轮询直到 ALL K3 DONE / Traceback / 200min 上限。前台跑（由 terminal background=true 托管）。"""
import os, time, subprocess, sys
AB = "/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation"
LOG = f"{AB}/oood-probe/k3-hw3.log"
PIDF = f"{AB}/oood-probe/k3-hw3.pid"
pid = open(PIDF).read().strip()
start = time.time()
cap = 200 * 60
while True:
    # 进程是否还在
    alive = subprocess.run(["kill", "-0", pid], capture_output=True).returncode == 0
    try:
        txt = open(LOG).read()
    except Exception:
        txt = ""
    done = "ALL K3 DONE" in txt
    tb = "Traceback" in txt
    el = (time.time() - start) / 60
    if done:
        print(f"=== WATCHER: ALL K3 DONE at +{el:.0f}min ===", flush=True); break
    if tb:
        print(f"=== WATCHER: Traceback at +{el:.0f}min ===", flush=True); break
    if not alive:
        print(f"=== WATCHER: process dead at +{el:.0f}min (no DONE/Traceback) ===", flush=True); break
    if time.time() - start >= cap:
        print(f"=== WATCHER: 200min cap reached at +{el:.0f}min ===", flush=True); break
    time.sleep(30)
print("=== WATCHER EXIT ===", flush=True)
for ln in open(LOG).read().splitlines():
    if any(k in ln for k in ("arm done", "SM=", "ALL K3 DONE", "Traceback")):
        print(ln, flush=True)
print("--- log tail 8 ---", flush=True)
for ln in open(LOG).read().splitlines()[-8:]:
    print(ln, flush=True)
