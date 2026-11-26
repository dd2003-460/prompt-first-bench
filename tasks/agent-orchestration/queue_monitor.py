#!/usr/bin/env python3
"""orch 队列监视器：输出队列信号（每行一个）或 IDLE。确定性输出，供 cron monitor 门禁。
信号: READY:<id> 就绪未认领 | WORKING:<id> 认领中(新鲜) | DEAD:<id> 认领中但回执PID探活失败 | STALE:<id> 认领超时/失联 | REVIEW:<id> 回执done/failed待核
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
        return None, None, None
    try:
        d = json.load(open(p, encoding="utf-8"))
        st = d.get("status")
        ev = d.get("evidence")
    except Exception:
        st, ev = "corrupt", None
    return st, os.path.getmtime(p), ev


def extract_pid(ev):
    """从 evidence 提取 pid：顶层键优先，其次嵌套 dict 内的 pid 键。无/不可解析 → None。
    顶层 pid 为 None 时继续找嵌套（避免顶层空值遮蔽嵌套有效值）。"""
    if not isinstance(ev, dict):
        return None
    candidates = []
    if "pid" in ev:
        candidates.append(ev["pid"])
    for v in ev.values():
        if isinstance(v, dict) and "pid" in v:
            candidates.append(v["pid"])
    for c in candidates:
        if c is not None:
            return c
    return None


def pid_alive(pid):
    """os.kill(pid,0) 探活。True 存活 / False 不存在 / None 不可解析（保持 WORKING）。"""
    try:
        pid = int(str(pid).strip())
    except (TypeError, ValueError):
        return None
    if pid <= 0:
        return None
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True  # 进程存在但不属于本用户
    except OSError:
        return False
    return True


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
        rst, mtime, ev = receipt(short)
        rst_l = (rst or "").lower() if isinstance(rst, str) else rst
        if st == "就绪" and rst is None:
            out.append("READY:%s" % short)
        elif rst_l in ("done", "failed"):
            out.append("REVIEW:%s" % short)
        elif rst_l == "claimed":
            age = now - (mtime or 0)
            if age < STALE_SECS:
                alive = pid_alive(extract_pid(ev))
                tag = "DEAD" if alive is False else "WORKING"
            else:
                tag = "STALE"
            out.append(tag + ":" + short)
        else:  # 执行中但无回执/回执损坏 = 崩溃
            out.append("STALE:%s" % short)
    print("\n".join(sorted(out)) if out else "IDLE")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("MONITOR_ERROR:%s:%s" % (type(e).__name__, e))
