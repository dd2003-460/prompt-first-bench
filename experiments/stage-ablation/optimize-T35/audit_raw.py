#!/usr/bin/env python3
"""T35 阶段A交叉验证（独立来源2）：只读原始 JSON，独立复算，不引用 paper 文字结论。

输出：
  optimize-T35/audit-raw-out.txt  （人读）
  optimize-T35/audit.json         （机读，供 01/04 引用）
纯 stdlib，不联网、不调用 27B。
"""
import json, os, glob
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)  # experiments/stage-ablation/
RUNS = os.path.join(BASE, "runs")
out_lines = []
def p(s=""):
    print(s)
    out_lines.append(s)

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

report = {}

# ── 1. runs/ S7/S7T/S7F/S7V 字段完整性 + 有效 run 数 ──────────────
p("=== 1. runs/ 字段完整性与有效 run 数（原始 JSON） ===")
REQ = ["arm", "qid", "rep", "output_text", "sources", "tokens"]
arm_audit = {}
for arm in ["S7", "S7T", "S7F", "S7V"]:
    files = sorted(glob.glob(os.path.join(RUNS, arm + "-Q*-r*.json")))
    full = 0; nonempty_out = 0; src_nonempty = 0; err = 0
    missing_cases = []
    for fp in files:
        d = load(fp)
        miss = [k for k in REQ if k not in d]
        if miss:
            missing_cases.append((os.path.basename(fp), miss))
        else:
            full += 1
        if d.get("output_text"):
            nonempty_out += 1
        if d.get("sources"):
            src_nonempty += 1
        if d.get("error"):
            err += 1
    arm_audit[arm] = {
        "files": len(files), "full_fields": full, "nonempty_output": nonempty_out,
        "sources_nonempty": src_nonempty, "error_runs": err,
        "missing_cases": missing_cases,
    }
    p(f"  {arm}: files={len(files)} full_fields={full} nonempty_output={nonempty_out} "
      f"sources_nonempty={src_nonempty} error_runs={err} missing={missing_cases}")
report["run_audit"] = arm_audit

# ── 2. S7V / S7F / S7 在 Q1/Q4 各 rep 的 sources 数（pilot 对照组信息） ──
p("\n=== 2. pilot 题目 Q1/Q4 各 rep 的 sources 数 / output 长度 ===")
pilot_src = {}
for arm in ["S7", "S7F", "S7V"]:
    for q in ["Q1", "Q4"]:
        for r in [1, 2, 3]:
            fp = os.path.join(RUNS, f"{arm}-{q}-r{r}.json")
            d = load(fp)
            pilot_src[f"{arm}-{q}-r{r}"] = {
                "n_sources": len(d.get("sources", [])),
                "out_len": len(d.get("output_text", "")),
                "tok_out": d.get("tokens", {}).get("out"),
            }
            p(f"  {arm}-{q}-r{r}: n_sources={len(d.get('sources', []))} "
              f"out_len={len(d.get('output_text', ''))} tok_out={d.get('tokens', {}).get('out')}")
report["pilot_sources"] = pilot_src

# ── 3. raw-data-full-perdim.json 结构与 S0-S5 total 复算 ──────────
p("\n=== 3. raw-data-full-perdim.json（90-run 汇编）独立复算 ===")
rawp = os.path.join(BASE, "raw-data-full-perdim.json")
raw = load(rawp)
for k, v in raw.items():
    p(f"  key={k} type={type(v).__name__} len={len(v) if hasattr(v, '__len__') else '-'}")
    if isinstance(v, list) and v and isinstance(v[0], dict):
        p(f"    [0] keys={sorted(v[0].keys())}")
        p(f"    [0] sample={json.dumps(v[0], ensure_ascii=False)[:300]}")
    elif isinstance(v, dict):
        p(f"    keys={list(v.keys())[:15]}")

# 尝试从 per_run 复算 total 均值
per_run = raw.get("local_gatefixed_per_run")
arm_means = {}
if isinstance(per_run, list) and per_run:
    fields = set()
    for r in per_run[:10]:
        if isinstance(r, dict):
            fields |= set(r.keys())
    p(f"  local_gatefixed_per_run fields={sorted(fields)}")
    # 找 total 字段
    total_key = None
    for cand in ["total", "total_score", "weighted_total", "score_total"]:
        if cand in fields:
            total_key = cand
            break
    arm_key = "arm" if "arm" in fields else None
    p(f"  detected total_key={total_key} arm_key={arm_key}")
    if total_key and arm_key:
        agg = defaultdict(list)
        for r in per_run:
            a, t = r.get(arm_key), r.get(total_key)
            if a and isinstance(t, (int, float)):
                agg[a].append(t)
        for a in sorted(agg):
            arm_means[a] = round(sum(agg[a]) / len(agg[a]), 4)
            p(f"  {a}: n={len(agg[a])} mean_{total_key}={arm_means[a]:.4f}")
        if "S0" in arm_means and "S5" in arm_means:
            p(f"  S5 - S0 = {arm_means['S5'] - arm_means['S0']:+.4f}  (paper/Abstract: +0.182)")
        if "S0" in arm_means and "S1" in arm_means:
            p(f"  S1 - S0 = {arm_means['S1'] - arm_means['S0']:+.4f}  (paper §4.1: +0.129)")
report["raw_arm_means"] = arm_means

# ── 4. t23v2_arm_summary（若含 S6/S7） ──────────────────────────
summ = raw.get("t23v2_arm_summary")
if summ is not None:
    p("\n=== 4. t23v2_arm_summary ===")
    p("  " + json.dumps(summ, ensure_ascii=False)[:800])
    report["t23v2_arm_summary"] = summ

# 落盘
with open(os.path.join(HERE, "audit-raw-out.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines) + "\n")
with open(os.path.join(HERE, "audit.json"), "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
p("\nSaved: audit-raw-out.txt / audit.json")
