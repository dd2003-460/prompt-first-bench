#!/usr/bin/env python3
"""T4b 验收核验（Lead 用）：runs 完整性 + raw 原始返回比对 + 截断声明在位。
用法: python3 verify_t4b.py  （在 pfb 仓根目录跑）
退出码 0=全过，非 0=有 FAIL 项。
"""
import json, os, sys, hashlib

BASE = "tasks/think-mechanism-paper/pilot"
fails = []
oks = []

# 1. runs.json 完整性
runs = json.load(open(f"{BASE}/runs.json"))
runs = runs if isinstance(runs, list) else runs.get("runs", [])
if len(runs) == 10:
    oks.append("runs.json: 10 runs")
else:
    fails.append(f"runs.json: {len(runs)} runs (expect 10)")
statuses = [r.get("status") for r in runs]
if statuses.count("ok") >= 9:
    oks.append(f"runs status: {statuses.count('ok')}/10 ok")
else:
    fails.append(f"runs status: only {statuses.count('ok')}/10 ok")
fr = {}
for r in runs:
    fr[r.get("finish_reason")] = fr.get(r.get("finish_reason"), 0) + 1
oks.append(f"finish_reason dist: {fr}")

# 2. raw/ 原始返回存在且与 runs.json 的 full_text 一致（抽全量 10 个）
raw_dir = f"{BASE}/raw"
if os.path.isdir(raw_dir):
    mism = []
    for r in runs:
        rid = r.get("run_id") or (f"{r.get('prompt_id')}-{r.get('condition')}")
        p = f"{raw_dir}/{rid}.json"
        if not os.path.exists(p):
            mism.append(f"{rid}: raw 文件缺失")
            continue
        raw = json.load(open(p))
        # 兼容两种结构：choices[0].message.content 或嵌套
        try:
            ct = raw["choices"][0]["message"]["content"]
        except Exception:
            try:
                ct = raw["data"]["choices"][0]["message"]["content"]
            except Exception:
                mism.append(f"{rid}: raw 结构无法解析")
                continue
        ft = r.get("full_text", "")
        if ct != ft:
            # 允许 runs.json 存了 strip 后的版本
            if ct.strip() != ft.strip():
                mism.append(f"{rid}: raw content 与 runs.json full_text 不一致")
    if not mism:
        oks.append("raw/: 10/10 原始返回与 runs.json 一致")
    else:
        fails.append("raw/: " + "; ".join(mism))
else:
    fails.append("raw/ 目录缺失（任务书要求每次调用存原始返回）")

# 3. results.md 截断声明在位
res = open(f"{BASE}/results.md").read()
if "length" in res and ("1500" in res):
    oks.append("results.md: 截断声明在位")
else:
    fails.append("results.md: 截断声明缺失")
if "n=1" in res:
    oks.append("results.md: n=1 声明在位")
else:
    fails.append("results.md: n=1 声明缺失")

# 4. scores.json 存在
if os.path.exists(f"{BASE}/scores.json"):
    oks.append("scores.json 存在")
else:
    fails.append("scores.json 缺失")

print("=== T4b 核验 ===")
for o in oks:
    print("OK  ", o)
for f in fails:
    print("FAIL", f)
print(f"\n{'ALL PASS' if not fails else f'{len(fails)} FAIL'}")
sys.exit(1 if fails else 0)
