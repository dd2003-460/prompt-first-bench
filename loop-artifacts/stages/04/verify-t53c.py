#!/usr/bin/env python3
"""T53C 验收校验：≥2 系统分数落盘 / 每个分数有 source_url / 推荐 baseline 有理由。"""
import json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
P = os.path.join(ROOT, "research/sm-bench-sota-table.json")
d = json.load(open(P, encoding="utf-8"))
fails = []

def ok(cond, name, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (f" :: {detail}" if detail else ""))
    if not cond:
        fails.append(name)

systems = d["sota_systems"]
ok(len(systems) >= 2, "AC1 >=2 systems", f"{len(systems)}")

# 每个系统必须有 http URL 且至少一个非 null 数值分数
bad_url, no_num, no_quote = [], [], []
for s in systems:
    url = s.get("source_url", "")
    if not (isinstance(url, str) and url.startswith("http")):
        bad_url.append(s["name"])
    if all(v is None for v in s.get("aggregate", {}).values()):
        no_num.append(s["name"])
    if not s.get("verbatim_excerpt"):
        no_quote.append(s["name"])
ok(not bad_url, "AC2 all systems have source_url", str(bad_url))
ok(not no_num, "AC2b all systems have >=1 numeric score", str(no_num))
ok(not no_quote, "AC2c all systems have verbatim excerpt (可复核)", str(no_quote))

# 逐题：null 必须给出理由
null_missing_reason = [s["name"] for s in systems
                       if all(v is None for v in s["per_question_scores"].values())
                       and not s.get("per_question_null_reason")]
ok(not null_missing_reason, "AC2d per-question null has reason", str(null_missing_reason))

ok(bool(d.get("recommended_baseline")), "AC3 baseline chosen", d.get("recommended_baseline"))
ok(len(d.get("reasoning", "")) >= 120, "AC3b reasoning substantive", f"{len(d.get('reasoning',''))} chars")

# 重复 (name, benchmark, url) 检查
keys = [(s["name"], s["benchmark"][:40], s["source_url"]) for s in systems]
ok(len(keys) == len(set(keys)), "AC4 no duplicate system rows")

# 一致性：同 benchmark 混版本检测（DeepResearch Bench 只应出现 ICLR 口径）
drb_urls = {s["source_url"] for s in systems if "DeepResearch Bench" in s["benchmark"]}
ok(len(drb_urls) == 1, "AC5 one source version per benchmark", str(len(drb_urls)))

# 矛盾点必须记录版本漂移
ids = {c["id"] for c in d.get("contradictions", [])}
ok("X1" in ids, "AC6 version drift recorded", str(sorted(ids)))

print(f"\nSUMMARY: fails={len(fails)} systems={len(systems)} "
      f"with_numeric={d['verification']['systems_with_numeric_aggregate']} "
      f"with_url={d['verification']['systems_with_url']}")
sys.exit(1 if fails else 0)
