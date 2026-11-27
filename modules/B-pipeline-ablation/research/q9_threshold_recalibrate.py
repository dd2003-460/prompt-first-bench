#!/usr/bin/env python3
"""Q9 域阈值重标定（红队 2026-11-27 预案的机械执行）

COS_THRESHOLD=0.70 是 gpu 域标定，Q9 域 sim 分布整体偏低（median ~0.59），
0.70 下 gate 命中率全 0 = 阈值伪影，非真实零覆盖。
本脚本: 对已完成的 budget 档算 per-gate best-sim 分布 + 阈值扫描矩阵，
输出 JSON 供 P1 判决（P1 判决需全 5 档到位，本脚本只做机械提取）。
run json 不动，只重算 embedding 相似度，不重跑 SM。
"""
import json, glob, re, os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from sentence_transformers import SentenceTransformer
from judge_v1 import load_run_nodes

HERE = os.path.dirname(os.path.abspath(__file__))
SCAN_DIR = os.path.join(HERE, "..", "data", "q9-budget-scan")
GOLD = os.path.join(HERE, "..", "data", "gold-q9-units.json")
THRESHOLDS = [0.50, 0.55, 0.60, 0.62, 0.65, 0.70]


def main():
    model = SentenceTransformer("BAAI/bge-m3")
    gold = json.load(open(GOLD))
    units = gold["units"]
    gate_jids = gold["gate_units"]  # 11 主端点 gate（J 命名）
    gid = [u["unit_id"] for u in units]
    # J-id → unit_id 映射（unit.j_id 字段）
    jmap = {u["j_id"]: u["unit_id"] for u in units if u.get("j_id")}
    gate_uids = [jmap[j] for j in gate_jids if j in jmap]
    assert len(gate_uids) == 11, f"expect 11 gate units, got {len(gate_uids)}: {gate_uids}"
    runs = []
    for p in sorted(glob.glob(os.path.join(SCAN_DIR, "q9-*.json"))):
        m = re.match(r"q9-(\d+)-r(\d+)-", os.path.basename(p))
        if m:
            runs.append((int(m.group(1)), int(m.group(2)), p))
    sim_cache = {}
    for b, r, p in runs:
        nodes = load_run_nodes(p)
        ne = model.encode([n["claim"] for n in nodes], normalize_embeddings=True)
        ge = model.encode([u["text"] for u in units], normalize_embeddings=True)
        sim_cache[(b, r)] = ne @ ge.T
    budgets = sorted({b for b, _, _ in runs})
    result = {
        "note": "Q9 域阈值重标定诊断; P1 判决需全 5 档到位, 本文件仅机械提取",
        "budgets_done": budgets,
        "gate_best_sim": {},
        "threshold_sweep": {},
        "matrices": {},
    }
    # per-gate best sim（跨所有已完成 run）
    for g in gid:
        gi = gid.index(g)
        vals = []
        for br, sim in sim_cache.items():
            vals.append(float(sim[:, gi].max()))
        result["gate_best_sim"][g] = round(max(vals), 3) if vals else None
    for thr in THRESHOLDS:
        sweep = {}
        matrices = {}
        gate_sweep = {}
        for b in budgets:
            reps = [(b, rr) for rr in range(1, 4) if (b, rr) in sim_cache]
            hits = {}
            ghits = {}
            for g in gid:
                gi = gid.index(g)
                n = sum(1 for br in reps if (sim_cache[br] >= thr)[:, gi].any())
                hits[g] = round(n / len(reps), 2)
            for g in gate_uids:
                ghits[g] = hits[g]
            matrices[str(b)] = hits
            sweep[str(b)] = round(sum(hits.values()) / len(gid), 3)
            gate_sweep[str(b)] = round(sum(ghits.values()) / len(gate_uids), 3)
        result["threshold_sweep"][f"{thr:.2f}"] = sweep
        result["matrices"][f"{thr:.2f}"] = matrices
        result.setdefault("gate_sweep", {})[f"{thr:.2f}"] = gate_sweep
    out = os.path.join(SCAN_DIR, "threshold-recalibration-20261127.json")
    json.dump(result, open(out, "w"), indent=1, ensure_ascii=False)
    print(f"-> {out}")
    for thr in THRESHOLDS:
        print(f"  thr={thr:.2f}: " + "  ".join(
            f"b{b}={result['threshold_sweep'][f'{thr:.2f}'][str(b)]}" for b in budgets)
            + "  | gates: " + "  ".join(
            f"b{b}={result['gate_sweep'][f'{thr:.2f}'][str(b)]}" for b in budgets))


if __name__ == "__main__":
    main()
