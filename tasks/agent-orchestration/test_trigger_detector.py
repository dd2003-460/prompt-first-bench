#!/usr/bin/env python3
# origin: ai — trigger_detector selftest (taskcard D1b, 6 cases, stdlib only)
import json, os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from trigger_detector import detect
FAILED = []
def tmp(c):
    fd, p = tempfile.mkstemp()
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(c)
    return p
E = tmp("")
def chk(name, got, want):
    ok = got == want
    print(("PASS " if ok else "FAIL ") + name)
    if not ok: FAILED.append(name)
def c_gap():
    r = detect(E, tmp("精度 0.92"))
    chk("gap", r["signal"], "缺口")
def c_contra():
    # 同主题词需 >=4 字公共块(检测器阈值), 故两侧补上下文
    r = detect(tmp(json.dumps({"evidence": "实验得分 0.92 记录"})), tmp("实验得分 0.87 记录"))
    chk("矛盾", r["signal"], "矛盾")
def c_stuck():
    r = detect(tmp(json.dumps({"last_op": "X"})), tmp("op: X"), diff_empty=True)
    chk("卡住", r["signal"], "卡住")
def c_none_src():
    r = detect(E, tmp("精度 0.92 @run-12"))
    chk("none-src", r["signal"], "none")
def c_none_empty():
    r = detect(E, tmp(""))
    chk("none-empty", r["signal"], "none")
def c_count():
    p = tmp("精度 0.92")
    r1 = detect(E, p)
    r2 = detect(tmp(json.dumps({"trigger": r1})), p)
    chk("count", (r1["count"], r2["count"]), (1, 2))
for f in (c_gap, c_contra, c_stuck, c_none_src, c_none_empty, c_count):
    f()
if FAILED:
    sys.exit(1)
print("ALL 6 PASS")
