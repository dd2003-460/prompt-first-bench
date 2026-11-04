#!/usr/bin/env python3
"""Emit one judge-cell JSON record from compact verdict codes and append to the v3.1 jsonl.

Compact code grammar
  "p"        pass, no flags
  "p:b"      pass, note 来源未实抓 (J1 B 级)
  "p:2a"     pass, note B-2a:外部数字无来源 (J2)
  "x"        fail, note 正文未找到该条目 / 仅交叉引用
  "f123"     J1 fail on tests 1/2/3 (① ② ③); "f4" = ④
  "gB1"      J2 fail on B-1; "gB2", "gB2a", "gB3"; combine as "gB1B2"

Notes are free text (<= 40 chars).
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "arena-hetero-judge-results-v31.jsonl"

SELF_ID = "arena-agent (Arena.ai Agent Mode; underlying model family not disclosed by platform — non-Qwen status self-reported, not certifiable)"


def expand(judge: str, code: str, note: str):
    is_j1 = judge.startswith("J1")
    if code == "p":
        verdict, tags = "pass", []
    elif code.startswith("p:"):
        verdict, tags = "pass", []
    elif code == "x":
        verdict, tags = "fail", ([] if is_j1 else [])
        note = note or "正文未找到该条目"
    elif is_j1 and code.startswith("f"):
        digits = [c for c in code[1:] if c.isdigit()]
        verdict = "fail"
        tags = [{"1": "①", "2": "②", "3": "③", "4": "④"}[d] for d in digits]
    elif (not is_j1) and code.startswith("g"):
        verdict = "fail"
        body = code[1:]
        tags = []
        for token in ["B2a", "B1", "B2", "B3"]:
            if body.startswith(token):
                tags.append(token)
                body = body[len(token):]
    else:
        raise ValueError(f"bad code {code} for {judge}")

    item = {"id": None, "verdict": verdict}
    if is_j1:
        item["tests_failed"] = tags
    else:
        item["bottom_lines_triggered"] = tags
    item["note"] = note
    return item


def cell(cell_name: str, judge: str, rows, path=OUT):
    items = []
    for iid, (code, note) in rows:
        it = expand(judge, code, note)
        it["id"] = iid
        items.append(it)
    passed = sum(1 for it in items if it["verdict"] == "pass")
    rec = {
        "cell": cell_name,
        "judge": judge,
        "items": items,
        "summary": {"total": len(items), "passed": passed},
        "model_identity": SELF_ID,
        "rubric": "v3.1",
    }
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"{cell_name:44s} {judge:14s} {passed}/{len(items)}")
    return rec
