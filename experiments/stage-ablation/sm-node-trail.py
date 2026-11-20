#!/usr/bin/env python3
"""T53b 节点抽查循环: 每 10min 一行摘要追加到 /tmp/t53b/node-trail.log.
只读, 不碰 SM. 62 run 跑完后 kill (pgrep -f sm-node-trail)."""
import subprocess, time, sys
PROBE = '/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation/sm_node_probe.py'
TRAIL = '/tmp/t53b/node-trail.log'
while True:
    try:
        out = subprocess.run([sys.executable, PROBE, '--compact'],
                             capture_output=True, text=True, timeout=60)
        with open(TRAIL, 'a') as f:
            f.write(out.stdout.strip() + '\n')
    except Exception as e:
        with open(TRAIL, 'a') as f:
            f.write(f'ERR {e}\n')
    time.sleep(600)
