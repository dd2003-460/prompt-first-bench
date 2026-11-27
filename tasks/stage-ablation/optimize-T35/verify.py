#!/usr/bin/env python3
"""T35 阶段C 独立复算：从 scores.json + 原始 runs/*.json 重算所有汇总数字，输出 mismatch 数。

三层确定性复算（不重新调用 judge，judge 逐 run 分数本身视为评分输出）：
  L1 逐 run：用 score.py 的 WEIGHTS 从 scores 重新加权算 total，与 scores.json 存值比对。
  L2 汇总：从逐 run 分数重算 per-arm×Q 的 M1/M4/M6/total 均值（供 02/03 表格引用）。
  L3 原始 JSON 对账：arm/qid/rep、output_text 非空、sources 数、wall_s、tokens.out。
输出 verify-out.txt（人读）+ verify.json（机读）。目标 mismatch = 0。
"""
import json, os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
sys.path.insert(0, BASE)
from score import WEIGHTS, Q5_WEIGHT_OVERRIDES  # 只读复用口径

sc = json.load(open(os.path.join(HERE, "scores.json"), encoding="utf-8"))
runs = sc["runs"]
lines = []
def p(s=""):
    print(s); lines.append(s)

mismatches = []

def run_path(arm, qid, rep):
    if arm == "S8E":
        return os.path.join(HERE, "runs", f"S8E-{qid}-r{rep}.json")
    return os.path.join(BASE, "runs", f"{arm}-{qid}-r{rep}.json")

# ── L1 逐 run total 加权复算 ─────────────────────────────────────
p("=== L1 逐 run total 加权复算（score.py WEIGHTS） ===")
for s in runs:
    w = dict(WEIGHTS)
    if s["qid"] == "Q5":
        w.update(Q5_WEIGHT_OVERRIDES)
        ws = sum(w.values())
        w = {k: v / ws for k, v in w.items()}
    calc = sum(s["scores"][k] * w[k] for k in w)
    ok = round(calc, 4) == round(s["total"], 4)
    if not ok:
        mismatches.append(f"L1 total {s['arm']}-{s['qid']}-r{s['rep']}: calc={calc:.4f} stored={s['total']}")
    p(f"  {s['arm']}-{s['qid']}-r{s['rep']}: calc={calc:.4f} stored={s['total']} {'OK' if ok else 'MISMATCH'}")
p(f"  L1 mismatches: {sum(1 for m in mismatches if m.startswith('L1'))}")

# ── L2 per-arm×Q 均值复算 ────────────────────────────────────────
p("\n=== L2 per-arm×Q 均值复算（r1,r2） ===")
agg = defaultdict(list)
for s in runs:
    agg[(s["arm"], s["qid"])].append(s)
summary = {}
p("| Arm | Q | n | M1 | M4 | M6 | Total |")
p("|---|---|---|---|---|---|---|")
for arm in ("S7", "S7V", "S8E"):
    for q in ("Q1", "Q4"):
        rs = agg[(arm, q)]
        n = len(rs)
        m1 = sum(s["scores"]["M1"] for s in rs) / n
        m4 = sum(s["scores"]["M4"] for s in rs) / n
        m6 = sum(s["scores"]["M6"] for s in rs) / n
        tot = sum(s["total"] for s in rs) / n
        summary[f"{arm}-{q}"] = {"n": n, "M1": round(m1, 4), "M4": round(m4, 4),
                                 "M6": round(m6, 4), "total": round(tot, 4)}
        p(f"| {arm} | {q} | {n} | {m1:.4f} | {m4:.4f} | {m6:.4f} | {tot:.4f} |")

# 与 scores-summary.txt 里的表逐格比对
p("\n=== L2b 与 scores-summary.txt 表格比对 ===")
sumtxt = open(os.path.join(HERE, "scores-summary.txt"), encoding="utf-8").read()
for key, v in summary.items():
    arm, q = key.split("-")
    # 在汇总表里找对应行
    hit = [ln for ln in sumtxt.splitlines() if ln.startswith(f"| {arm} | {q} |")]
    if not hit:
        mismatches.append(f"L2b row missing: {key}")
        continue
    cells = [c.strip() for c in hit[0].strip("|").split("|")]
    # cells: Arm,Q,M1,M4,M6,Total
    for label, val in (("M1", 2), ("M4", 3), ("M6", 4), ("total", 5)):
        if abs(float(cells[val]) - v[label]) > 5e-5:
            mismatches.append(f"L2b {key} {label}: summary={cells[val]} recomputed={v[label]}")
p(f"  L2b mismatches: {sum(1 for m in mismatches if m.startswith('L2b'))}")

# ── L3 原始 JSON 字段对账 ─────────────────────────────────────────
p("\n=== L3 原始 runs JSON 字段对账 ===")
for s in runs:
    arm, q, r = s["arm"], s["qid"], s["rep"]
    fp = run_path(arm, q, r)
    d = json.load(open(fp, encoding="utf-8"))
    tag = f"{arm}-{q}-r{r}"
    checks = {
        "arm": d.get("arm") == arm,
        "qid": d.get("qid") == q,
        "rep": d.get("rep") == r,
        "output_nonempty": bool(d.get("output_text")),
        "wall_s": d.get("wall_s") == s.get("wall_s"),
        "tok_out": d.get("tokens", {}).get("out") == s.get("tokens", {}).get("out"),
    }
    bad = [k for k, v in checks.items() if not v]
    if bad:
        mismatches.append(f"L3 {tag}: {bad}")
    p(f"  {tag}: sources={len(d.get('sources', []))} out_len={len(d.get('output_text', ''))} "
      f"wall_s={d.get('wall_s')} tok_out={d.get('tokens', {}).get('out')} {'OK' if not bad else 'MISMATCH ' + str(bad)}")
p(f"  L3 mismatches: {sum(1 for m in mismatches if m.startswith('L3'))}")

p("\n=== 总 mismatch 数 ===")
p(f"  TOTAL MISMATCH = {len(mismatches)}  (目标 0)")
for m in mismatches:
    p("    " + m)

with open(os.path.join(HERE, "verify-out.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
with open(os.path.join(HERE, "verify.json"), "w", encoding="utf-8") as f:
    json.dump({"mismatch_count": len(mismatches), "mismatches": mismatches,
               "per_arm_q": summary}, f, ensure_ascii=False, indent=2)
