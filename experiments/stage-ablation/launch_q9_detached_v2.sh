#!/bin/bash
# q9 队列 v2 detached 启动器: double-fork + setsid → PPID=1
cd /Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation || exit 1
python3 - <<'EOF'
import os, sys
pid = os.fork()
if pid > 0:
    sys.exit(0)
os.setsid()
if os.fork() > 0:
    os._exit(0)
devnull = os.open(os.devnull, os.O_RDWR)
log = open('/tmp/q9-resume-nohup.log', 'ab')
os.dup2(devnull, 0); os.dup2(log.fileno(), 1); os.dup2(log.fileno(), 2)
os.execvp('bash', ['bash', 'q9_budget_scan_queue_v2.sh'])
EOF
echo "launcher-v2: grandchild detached $(date '+%F %T')"
