#!/usr/bin/env python3
"""T-PR-15 AC1-AC8 机器校验。只做可判定检查，不评价内容质量。"""
import json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SURVEY = os.path.join(ROOT, "research/text-objective-goodhart-survey.md")
LOG = os.path.join(ROOT, "research/search-log-text-objective.json")
XCHK = os.path.join(ROOT, "research/web-llm/text-objective-crosscheck.json")

fails, warns = [], []


def ok(cond, name, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (f" :: {detail}" if detail else ""))
    if not cond:
        fails.append(name)


text = open(SURVEY, encoding="utf-8").read()
lines = text.splitlines()

# AC1
ok(len(lines) >= 300, "AC1 survey>=300 lines", f"{len(lines)} lines")

# AC2
src_rows = re.findall(r"^\| S\d\d \|", text, re.M)
full_rows = re.findall(r"^\| S\d\d \|.*\| full \|", text, re.M)
ids = re.findall(r"arXiv:\d{4}\.\d{4,5}|deepmind\.google/blog", text)
ok(len(src_rows) >= 20, "AC2 sources>=20", f"{len(src_rows)} rows")
ok(len(full_rows) >= 10, "AC2 full-text>=10", f"{len(full_rows)} full")
ok(len(set(ids)) >= 20, "AC2 unique IDs>=20", f"{len(set(ids))} ids")

# AC3
verdicts = re.findall(r"\*\*判决：(\S+?)（conf ([\d.]+)）\*\*", text)
ok(len(verdicts) == 5, "AC3 five verdict lines", str(verdicts))
allowed = {"成立", "部分成立", "不成立", "证据不足"}
ok(all(v[0] in allowed for v in verdicts), "AC3 verdict vocabulary", str([v[0] for v in verdicts]))
ok(all(0 < float(v[1]) < 1 for v in verdicts), "AC3 conf in (0,1)", str([v[1] for v in verdicts]))

# AC4
sub = {
    "a": r"### 3\.1 \(a\)", "b": r"### 3\.2 \(b\)", "c": r"### 3\.3 \(c\)",
    "d": r"### 3\.4 \(d\)", "e": r"### 3\.5 \(e\)",
}
blocks = {}
for k, pat in sub.items():
    m = re.search(pat, text)
    blocks[k] = text[m.start():m.start() + 4000] if m else ""
ok(all(blocks[k] for k in sub), "AC4 five subclasses present")
for k, b in blocks.items():
    has_case = ("案例" in b) and ("arXiv:" in b or "SIGIR" in b or "[待核验" in b)
    ok(has_case, f"AC4 ({k}) has case or [待核验]")

# AC5
for h in ["假设 A", "假设 B", "假设 C"]:
    ok(h in text, f"AC5 {h} graded")
ok(re.search(r"假设 A（解释 gaming）：证据级别 = 弱", text) is not None, "AC5 A=弱")
ok(re.search(r"假设 B（约束遗漏）：证据级别 = 强", text) is not None, "AC5 B=强")
ok(re.search(r"假设 C（代理崩坏）：证据级别 = 强", text) is not None, "AC5 C=强")
ok("v17 病根" in text, "AC5 v17 root cause stated")

# AC6
log = json.load(open(LOG, encoding="utf-8"))
ok(len(log.get("counter_arguments", [])) >= 3, "AC6 counter_args>=3", f"{len(log.get('counter_arguments', []))}")

# AC7
tail = text[text.find("## 7. 对 v17 修法的启示"):]
recs = re.findall(r"^\d\. \*\*建议 \d", tail, re.M)
ok(len(recs) >= 3, "AC7 suggestions>=3", f"{len(recs)}")
ok(tail.count("落地层：") >= 3, "AC7 layer labels", f"{tail.count('落地层：')}")
ok("prompt 层" in tail, "AC7 prompt-layer tagged")

# AC8
x = json.load(open(XCHK, encoding="utf-8"))
n_svc = len(x.get("services", []))
n_ok = sum(1 for r in x.get("receipts", []) if r.get("status") == "ok")
ok(n_svc >= 2, "AC8 services>=2", f"{n_svc}")
if n_ok == 0:
    warns.append("AC8 receipts=0 -> 环境限制，按降级规则记录，未满足")
    print("WARN AC8 0 real receipts (sandbox has no endpoint); recorded as not_satisfied")
else:
    ok(n_ok >= 4, "AC8 receipts present", f"{n_ok}")
ok("contradictions" in x, "AC8 contradictions field exists")

# 附带：行数唯一性（append-only 校验的残留）
dupes = [l for l in lines if l.strip() and len(l) > 40 and lines.count(l) > 1]
print(f"INFO duplicated long lines: {len(set(dupes))}")

print("\nSUMMARY: fails=%d warns=%d" % (len(fails), len(warns)))
sys.exit(1 if fails else 0)
