#!/usr/bin/env python3
"""s5_state_machine 实验监控脚本 — 机械检查，输出 JSON 状态。

用法:
  python3 s5_monitor.py          # 检查并输出 JSON
  python3 s5_monitor.py --quiet  # 只在异常时输出

设计原则:
  - 纯机械检查，不做判断（判断留给 cron agent）
  - 输出确定性（无时间戳），配合 cron monitor 字段做 diff
  - 状态存 monitor-state.json，跨次对比
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timezone

BASE = "/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation"
LOG = "/tmp/t53b/gpu_formula_r02.sm.log"
SYNTH = os.path.join(BASE, "runs-s5-sm-gpu-synth.json")
WATCHER_LOG = os.path.join(BASE, "ablation-watcher.log")
CC_STATE = "/Users/a1-6/Desktop/workspace/pfb/tasks/T53-bus/cc-state.json"
STATE_FILE = os.path.join(BASE, "monitor-state.json")


def run(cmd):
    """Run a shell command, return (stdout, returncode)."""
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        return r.stdout.strip(), r.returncode
    except Exception as e:
        return str(e), -1


def find_s5_pids():
    """Find s5_state_machine process PIDs."""
    out, rc = run("pgrep -f 's5_state_machine'")
    if rc != 0 or not out:
        return []
    return [p.strip() for p in out.split("\n") if p.strip()]


def check_process(pids):
    """Check if processes are alive and get CPU time.

    Uses the Python process (not the shell wrapper) for CPU time.
    """
    if not pids:
        return {"alive": False, "pids": [], "cpu_time": None, "etime": None}
    # Find the Python process (the actual s5_state_machine, not the shell wrapper)
    python_pid = None
    for pid in pids:
        out, rc = run(f"ps -o command= -p {pid}")
        if rc == 0 and "python" in out.lower() and "s5_state_machine" in out:
            # Make sure it's the Python binary, not a shell wrapper that mentions python
            if "zsh" not in out.lower() and "bash" not in out.lower():
                python_pid = pid
                break
    if not python_pid:
        # Fallback: use the last pid (usually the actual process)
        python_pid = pids[-1]
    # macOS ps doesn't support --no-headers; use awk to skip header
    out, rc = run(f"ps -o etime,time -p {python_pid} | tail -1")
    if rc != 0 or not out.strip():
        return {"alive": False, "pids": pids, "cpu_time": None, "etime": None}
    parts = out.split()
    return {
        "alive": True,
        "pids": pids,
        "python_pid": python_pid,
        "etime": parts[0] if parts else None,
        "cpu_time": parts[1] if len(parts) > 1 else None,
    }


def check_log():
    """Check log file line count and last lines."""
    if not os.path.exists(LOG):
        return {"exists": False, "lines": 0, "last_lines": []}
    out, _ = run(f"wc -l < {LOG}")
    lines = int(out.strip()) if out.strip().isdigit() else 0
    tail, _ = run(f"tail -5 {LOG}")
    return {
        "exists": True,
        "lines": lines,
        "last_lines": tail.split("\n") if tail else [],
    }


def check_synth():
    """Check synth output file mtime."""
    if not os.path.exists(SYNTH):
        return {"exists": False, "mtime": None}
    mtime = os.path.getmtime(SYNTH)
    return {
        "exists": True,
        "mtime": datetime.fromtimestamp(mtime, tz=timezone.utc).isoformat(),
    }


def check_watcher():
    """Check watcher log."""
    if not os.path.exists(WATCHER_LOG):
        return {"exists": False, "last_lines": []}
    tail, _ = run(f"tail -3 {WATCHER_LOG}")
    return {
        "exists": True,
        "last_lines": tail.split("\n") if tail else [],
    }


def check_cc_state():
    """Check cc-state.json progress."""
    if not os.path.exists(CC_STATE):
        return {"exists": False, "done": 0, "total": 0}
    try:
        with open(CC_STATE) as f:
            d = json.load(f)
        done = sum(1 for w in d.get("work_units", []) if w.get("done"))
        total = len(d.get("work_units", []))
        return {"exists": True, "done": done, "total": total}
    except Exception:
        return {"exists": True, "done": 0, "total": 0}


def load_prev_state():
    """Load previous monitor state for comparison."""
    if not os.path.exists(STATE_FILE):
        return {}
    try:
        with open(STATE_FILE) as f:
            return json.load(f)
    except Exception:
        return {}


def save_state(state):
    """Save current monitor state."""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def main():
    quiet = "--quiet" in sys.argv

    pids = find_s5_pids()
    proc = check_process(pids)
    log = check_log()
    synth = check_synth()
    watcher = check_watcher()
    cc = check_cc_state()
    prev = load_prev_state()

    # Determine status
    if not proc["alive"]:
        # Check if log has a normal end marker
        last = "\n".join(log["last_lines"])
        if "traceback" in last.lower() or "error" in last.lower():
            status = "crash"
        elif "done" in last.lower() or "complete" in last.lower():
            status = "done"
        else:
            status = "exited"
    else:
        # Process alive — check if log is progressing
        prev_lines = prev.get("log", {}).get("lines", 0)
        if log["lines"] > prev_lines:
            status = "running"
        else:
            # No new lines — check CPU time to see if it's stuck
            prev_cpu = prev.get("process", {}).get("cpu_time", "0:00.00")
            if proc["cpu_time"] and proc["cpu_time"] != prev_cpu:
                status = "running"  # CPU still ticking, just slow
            else:
                status = "stuck"

    # Check watcher
    watcher_alive = watcher["exists"] and any(
        "started" in line.lower() or "monitor" in line.lower()
        for line in watcher["last_lines"]
    )

    state = {
        "status": status,
        "process": proc,
        "log": {"lines": log["lines"], "last": log["last_lines"][-1] if log["last_lines"] else None},
        "synth": synth,
        "watcher": {"exists": watcher["exists"], "last": watcher["last_lines"][-1] if watcher["last_lines"] else None},
        "cc_state": cc,
    }

    save_state(state)

    # Output
    if quiet and status == "running" and watcher_alive:
        sys.exit(0)  # No output = no change for cron monitor

    print(json.dumps(state, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
