#!/usr/bin/env python3
"""orch 队列监视器：输出队列信号（每行一个）或 IDLE。确定性输出，供 cron monitor 门禁。
信号: READY:<id> 就绪未认领 | WORKING:<id> 认领中(新鲜) | STALE:<id> 认领超时/失联 | REVIEW:<id> 回执done/failed待核
"""
import json
import os
import time

WS = "/Users/a1-6/Desktop/workspace/pfb-thinkmech"
TABLE = os.path.join(WS, "tasks/think-trigger/decomposition.md")
REC_DIR = os.path.join(WS, "tasks/agent-orchestration/receipts")
STALE_SECS = 45 * 60


def receipt(short_id):
    p = os.path.join(REC_DIR, short_id + ".json")
    if not os.path.exists(p):
        return None, None
    try:
        st = json.load(open(p, encoding="utf-8")).get("status")
    except Exception:
        st = "corrupt"
    return st, os.path.getmtime(p)


def main():
    lines = open(TABLE, encoding="utf-8").read().splitlines()
    rows = []  # (short_id, status_cell)
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
            rows.append((short, cells[-1]))
    now = time.time()
    out = []
    for short, st in rows:
        if st not in ("就绪", "执行中"):
            continue
        rst, mtime = receipt(short)
        if st == "就绪" and rst is None:
            out.append("READY:%s" % short)
        elif rst in ("done", "failed"):
            out.append("REVIEW:%s" % short)
        elif rst == "claimed":
            age = now - (mtime or 0)
            out.append(("WORKING" if age < STALE_SECS else "STALE") + ":" + short)
        else:  # 执行中但无回执/回执损坏 = 崩溃
            out.append("STALE:%s" % short)
    print("\n".join(sorted(out)) if out else "IDLE")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("MONITOR_ERROR:%s:%s" % (type(e).__name__, e))
