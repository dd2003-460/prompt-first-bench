#!/usr/bin/env python3
"""T8-C3v3 rubric v3.2 replay 验收脚手架（Lead 独立复算，不信任 arena 自报）。

用法: python3 validate_v32_replay.py <results-v32.jsonl> [results-v31.jsonl]

验收项（对应任务书 T8-C3v3-rubric-v32-replay-task.md）：
  A. 完整性: 36 cell = 18 artifacts × {J1-strict-v3, J2-lenient-v3}，无重复
  B. §6-A 围栏恢复: v3.1 中两个 ```markdown 首行 cell 的 J1 分数 ≥ 0.8
  C. §6-B 交叉引用: 报告 note 含「仅交叉引用」的 cell 数（v3.1 基线 7 cell）
  D. G2 spread: per (config,domain) 双判官 pass-rate spread，报告 >0.05 的 cell
  E. inter-judge κ: J1 vs J2 item-level pooled κ（同族双判口径，标注非真 IRR）
  F. 方法学红旗: 检测 verdict 是否疑似来自确定性脚本而非 LLM 判断
     （同一 judge 对内容不同的 artifact 给出逐 id 完全相同的 verdict 序列 → 警告）

口径限定（§4 硬规则）: 所有输出统计量标注 (a) 聚合口径 (b) tie-break (c) judge 族。
"""
import json, sys, math
from collections import defaultdict

def load(path):
    rows = []
    with open(path) as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                print(f"  WARN: line {i+1} 非 JSON，跳过")
    return rows

def item_pass(row):
    """per-item pass rate: pass items / total items（tie-break: N/A，比率无平局）"""
    items = row.get("items", [])
    if not items:
        return None
    p = sum(1 for it in items if str(it.get("verdict", "")).lower() == "pass")
    return p / len(items)

def _judges(rows):
    return {r["judge"] for r in rows}

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    rows = load(sys.argv[1])
    base_rows = load(sys.argv[2]) if len(sys.argv) > 2 else None

    # ---- A. 完整性 ----
    seen = set()
    dup = 0
    for r in rows:
        key = (r.get("cell"), r.get("judge"))
        if key in seen: dup += 1
        seen.add(key)
    n_cells = len({r["cell"] for r in rows})
    n_judges = len({r["judge"] for r in rows})
    ok_A = (len(rows) == 36 and dup == 0 and n_judges == 2)
    print(f"[A] 完整性: {len(rows)} rows, {n_cells} cells, judges={sorted({j for j in _judges(rows)})}, dup={dup} -> {'PASS' if ok_A else 'FAIL'}")

    # ---- B. §6-A 围栏恢复 ----
    # v3.1 summary §6-A 点名: B-nofreeze/D1/stage01 (0/28) 与 B-none/D2/stage01 (0/22)
    # 两个 ```markdown 首行 stage01 cell（J1 pass-rate==0）
    fence_cells = []
    if base_rows:
        for r in base_rows:
            if r.get("judge","").startswith("J1"):
                pr = item_pass(r)
                if pr is not None and pr <= 0.0:
                    fence_cells.append(r["cell"])
    print(f"[B] §6-A 围栏 cell（v3.1 J1 pass-rate==0）: {fence_cells}")
    b_ok = True
    for c in fence_cells:
        v32 = [item_pass(r) for r in rows if r["cell"]==c and r["judge"].startswith("J1")]
        v31 = [item_pass(r) for r in base_rows if r["cell"]==c and r["judge"].startswith("J1")]
        ok = all(v is not None and v >= 0.8 for v in v32)
        b_ok &= ok
        print(f"    {c}: v3.1={v31} v3.2={v32} -> {'PASS' if ok else 'FAIL'} (验收线 J1≥0.8)")
    if not fence_cells:
        print("    （基线文件中未找到全 fail cell — 请人工核对 v3.1 summary §6-A 点名的 cell）")

    # ---- C. §6-B 交叉引用 ----
    # v3.1 summary §6-B: "7 cell" = stage03 中「仅交叉引用/仅评分维度」id 判死导致的分歧 cell。
    # jsonl 口径: item note 含「仅交叉引用」的 cell 数（v3.1 实测 6 cell，summary 记 7 含近似项）。
    xref = [r["cell"] for r in rows if any("仅交叉引用" in str(it.get("note","")) for it in r.get("items",[]))]
    xref_v31 = [r["cell"] for r in (base_rows or []) if any("仅交叉引用" in str(it.get("note","")) for it in r.get("items",[]))]
    print(f"[C] §6-B 交叉引用 cell: v3.1={len(xref_v31)} v3.2={len(xref)} -> {sorted(set(xref))}")

    # ---- D. G2 spread ----
    by_cd = defaultdict(dict)
    for r in rows:
        cd = r["cell"].rsplit("/",1)[0]
        by_cd[cd][r["judge"]] = item_pass(r)
    spreads = {}
    for cd, d in by_cd.items():
        js = [v for k,v in d.items() if v is not None]
        if len(js) == 2:
            spreads[cd] = abs(js[0]-js[1])
    bad = {k:v for k,v in spreads.items() if v > 0.05}
    print(f"[D] G2 spread (per config/domain, |J1-J2| pass-rate): {len(spreads)-len(bad)}/{len(spreads)} ≤0.05; FAIL={bad}")

    # ---- E. inter-judge κ (pooled item-level, 同族双判口径) ----
    pairs = []
    for r1 in rows:
        for r2 in rows:
            if r1["cell"]==r2["cell"] and r1["judge"].startswith("J1") and r2["judge"].startswith("J2"):
                m1 = {it["id"]: (str(it.get("verdict","")).lower()=="pass") for it in r1.get("items",[])}
                m2 = {it["id"]: (str(it.get("verdict","")).lower()=="pass") for it in r2.get("items",[])}
                ids = set(m1) & set(m2)
                for i in ids:
                    pairs.append((m1[i], m2[i]))
    if pairs:
        n = len(pairs)
        po = sum(a==b for a,b in pairs)/n
        p1 = sum(a for a,_ in pairs)/n; p2 = sum(b for _,b in pairs)/n
        pe = p1*p2 + (1-p1)*(1-p2)
        kappa = (po-pe)/(1-pe) if pe != 1 else float('nan')
        print(f"[E] inter-judge κ (pooled item-level, n={n}; tie-break N/A; 同族双判≠真IRR): {kappa:.3f}")
    else:
        print("[E] 无可配对 cell")

    # ---- F. 方法学红旗 ----
    seq_by_judge = defaultdict(list)
    for r in rows:
        seq = tuple(str(it.get("verdict","")) for it in r.get("items",[]))
        seq_by_judge[r["judge"]].append((r["cell"], seq))
    flags = []
    for j, lst in seq_by_judge.items():
        uniq = {s for _, s in lst}
        if len(uniq) == 1 and len(lst) > 3:
            flags.append(f"{j}: {len(lst)} 个不同 artifact 给出完全相同的 verdict 序列 — 疑似确定性脚本判定而非 LLM 盲判")
    print(f"[F] 方法学红旗: {flags if flags else '无'}")

    ok = ok_A and b_ok
    print(f"\n总判定: {'ACCEPT' if ok else 'REVIEW'}（B 未达或 A 不完整时不得直接采信）")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()