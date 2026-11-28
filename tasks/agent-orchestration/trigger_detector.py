#!/usr/bin/env python3
# origin: ai — 触发器三信号检测器 (矛盾/卡住/缺口), 契约见 taskcard-trigger-detector-d1a.md
# 输入: 上一拍回执 JSON + 本拍计划文本; 输出: trigger.json {signal, evidence, count}
import json, re, sys, difflib
NUM = re.compile(r"\d+(?:\.\d+)?")
SRC = re.compile(r"(path|commit|运行|@)", re.I)
TS = re.compile(r"_at$|time|stamp", re.I)


def _load(p):
    try:
        with open(p, encoding="utf-8") as f:
            t = f.read().strip()
        return json.loads(t) if t else {}
    except (OSError, ValueError):
        return {}


def _strings(o, k=""):  # 回执里可比对的字符串值, 跳过时间戳类字段
    if isinstance(o, dict):
        for kk, v in o.items():
            yield from _strings(v, kk)
    elif isinstance(o, list):
        for v in o:
            yield from _strings(v, k)
    elif isinstance(o, str) and not TS.search(k):
        yield o


def _nums(s):
    return set(NUM.findall(s))


def detect(prev_receipt_path, plan_path, diff_empty=False):
    prev = _load(prev_receipt_path)
    try:
        with open(plan_path, encoding="utf-8") as f:
            plan = f.read()
    except OSError:
        plan = ""
    lines = [l.strip() for l in plan.splitlines() if l.strip()]
    sig, ev = "none", ""
    # 1) 矛盾: plan 含数字句子 vs 回执字符串值, 同主题(最长公共块>=4)但数字集不同
    for l in lines:
        ln = _nums(l)
        if ln and any(ln != (sn := _nums(s)) and sn
                      and difflib.SequenceMatcher(None, NUM.sub("", l), NUM.sub("", s)).find_longest_match().size >= 4
                      for s in _strings(prev)):
            sig, ev = "矛盾", f"plan[{l[:60]}] vs receipt[{[s for s in _strings(prev) if _nums(s) and _nums(s) != ln][0][:60]}]"
            break
    # 2) 卡住: 回执 last_op 与本拍 op 相同 且 diff 为空
    if sig == "none":
        op = next((l[3:].strip() for l in lines if l.lower().startswith("op:")), "")
        lo = prev.get("last_op")
        if op and lo and op == lo and (diff_empty or not prev.get("diff_since")):
            sig, ev = "卡住", f"last_op={lo} 重复且 diff 为空"
    # 3) 缺口: 含数字的行无出处标注 (path/commit/运行/@)
    if sig == "none":
        bad = [l for l in lines if NUM.search(l) and not SRC.search(l)]
        if bad:
            sig, ev = "缺口", "; ".join(bad[:3])[:120]
    # count: 上拍同信号则累计 +1, 否则 1
    pt = prev.get("trigger")
    cnt = pt.get("count", 0) + 1 if (sig != "none" and isinstance(pt, dict) and pt.get("signal") == sig) else 1
    return {"signal": sig, "evidence": ev, "count": cnt}


def main():
    a = sys.argv[1:]
    diff_empty = "--diff-empty" in a
    a = [x for x in a if x != "--diff-empty"]
    if len(a) != 2:
        print(f"usage: {sys.argv[0]} <prev_receipt> <plan> [--diff-empty]", file=sys.stderr)
        sys.exit(2)
    print(json.dumps(detect(a[0], a[1], diff_empty), ensure_ascii=False))


if __name__ == "__main__":
    main()
