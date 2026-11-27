#!/bin/bash
# q9 队列 detached 启动器 (2026-11-27): double-fork + setsid → PPID=1, 存活于 Hermes 会话重建
# 纪律来源: q9_budget_scan_resume.sh 头部注释 (长跑进程用 setsid nohup); 今晚第 4 次被 SIGTERM (proc_f06dfc56a00e)
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
os.execvp('bash', ['bash', 'q9_budget_scan_resume.sh'])
EOF
echo "launcher: grandchild detached"
sleep 5
pgrep -f "q9_budget_scan_resume.sh" >/dev/null && echo "queue ALIVE (pid $(pgrep -f q9_budget_scan_resume.sh | head -1))" || echo "queue NOT running — FAIL"
