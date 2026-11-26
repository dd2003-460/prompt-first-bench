#!/usr/bin/env python3
"""orch 队列监视器：输出就绪任务短 ID（每行一个）或 IDLE。确定性输出，供 cron monitor 门禁。"""
import json
import os

WS = "/Users/a1-6/Desktop/workspace/pfb-thinkmech"
TABLE = os.path.join(WS, "tasks/think-trigger/decomposition.md")
REC_DIR = os.path.join(WS, "tasks/think-trigger/exp-results/receipts")


def receipt_status(short_id):
    p = os.path.join(REC_DIR, short_id + ".json")
    if not os.path.exists(p):
        return None
    try:
        return json.load(open(p, encoding="utf-8")).get("status")
    except Exception:
        return "corrupt"


def main():
    lines = open(TABLE, encoding="utf-8").read().splitlines()
    tasks = []  # (short_id, status_cell)
    in_table = False
    for ln in lines:
        if ln.startswith("| 任务 |") and "载体" in ln:
            in_table = True
            continue
        if not in_table:
            continue
        if ln.startswith("|---") or ln.startswith("|--"):
            continue
        if not ln.startswith("|"):
            in_table = False
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) >= 7:
            short = cells[0].split(":")[0].split("：")[0].strip()
            tasks.append((short, cells[-1]))
    ready = [sid for sid, st in tasks
             if st == "就绪" and receipt_status(sid) is None]
    print("\n".join(sorted(ready)) if ready else "IDLE")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("MONITOR_ERROR:%s:%s" % (type(e).__name__, e))
