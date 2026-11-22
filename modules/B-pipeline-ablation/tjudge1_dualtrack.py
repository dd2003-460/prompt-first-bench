#!/usr/bin/env python3
"""T-JUDGE-1 J6: dual-track 对照（新 embedding judge vs 旧 LLM judge）

数据源: runs_budget_scan/*.json（13 个完成 run，K7 还在跑 719_r2/r3）
  - 旧 judge: 同 JSON 的 judge.scores（15 点 rubric 0/1）+ depth_score
  - 树体: 不在该 JSON。budget_scan_batch.sh 在新 run 开始时把上一 run 的文件
    mv 到 checkpoints/archive/budget-{新B}-r{新R}-{新ts}/（目录名=新 run 时间戳，
    内容=上一 run 的树）。映射已验证: 归档目录内 runs-s5-sm-gpu.json 的 n_nodes
    与 runs_budget_scan 序列一一对应（错位一格）。
新 judge: bge-m3 对 gold Q1 16 单元 embedding 匹配（同 tjudge1_match 口径:
  阈值 0.65, 磁体 MAGNET_LIMIT=3, confirmed 为主口径）

产出:
  1. 每 run 新指标（coverage_confirmed / compression / sim 分布）
  2. 新旧对照: 旧 cov(15点) vs 新 cov(16单元) 逐 run 表 + Spearman/Pearson
  3. depth_score(旧, 树结构) vs 新 coverage 的相关
  4. 归档树体映射验证（archive 目录名 = 新 run 时间戳, 内容 = 上一 run）

用法: python3 tjudge1_dualtrack.py
不占 vLLM（纯 Mac MPS embedding + 本地 JSON）。
"""
import json, glob, os, sys
import numpy as np
from sentence_transformers import SentenceTransformer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tjudge1_parse import load_gold

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS_DIR = os.path.join(HERE, "data/t53b/runs_budget_scan")
OUT = os.path.join(HERE, "tjudge1-dualtrack.json")
THRESHOLD = 0.65
MAGNET_LIMIT = 3


def spearman(xs, ys):
    def rank(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
                j += 1
            avg = (i + j) / 2 + 1
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r
    rx, ry = rank(xs), rank(ys)
    n = len(xs)
    mx, my = sum(rx) / n, sum(ry) / n
    cov = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    vx = (sum((x - mx) ** 2 for x in rx)) ** 0.5
    vy = (sum((y - my) ** 2 for y in ry)) ** 0.5
    return cov / (vx * vy) if vx and vy else float("nan")


def pearson(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    cov = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    vx = (sum((x - mx) ** 2 for x in xs)) ** 0.5
    vy = (sum((y - my) ** 2 for y in ys)) ** 0.5
    return cov / (vx * vy) if vx and vy else float("nan")


def main():
    model = SentenceTransformer("BAAI/bge-m3")
    gold = load_gold("gpu")
    gold_emb = model.encode([u["text"] for u in gold], normalize_embeddings=True, show_progress_bar=False)

    # 旧 judge 分: runs_budget_scan/*.json
    old = {}
    for f in sorted(glob.glob(os.path.join(RUNS_DIR, "*.json"))):
        d = json.load(open(f))
        if d.get("depth_score") is not None:
            old[d["n_nodes"]] = d

    # 树体: 归档目录（错位一格映射）→ 按 runs-s5-sm-gpu.json 的 n_nodes 对回旧 judge
    # （目录名=新 run 时间戳，内容=上一 run；K6 启动前的残留文件 n_nodes 不在 old 里 → 自动跳过）
    rows = []
    for ad in sorted(glob.glob(os.path.join(HERE, "../../experiments/stage-ablation/checkpoints/archive/budget-*"))):
        rf = os.path.join(ad, "runs-s5-sm-gpu.json")
        if not os.path.exists(rf):
            continue
        t = json.load(open(rf))
        nn = t.get("n_nodes")
        if nn not in old:
            print(f"skip {os.path.basename(ad)}: n_nodes={nn} 不在 runs_budget_scan（K7 前残留/进行中）")
            continue
        d = old[nn]
        claims = [n["claim"] for n in t["nodes"]]
        node_emb = model.encode(claims, normalize_embeddings=True, show_progress_bar=False)
        sim = node_emb @ gold_emb.T
        top1 = sim.argmax(axis=1)
        top1_sim = sim[np.arange(len(claims)), top1]

        from collections import Counter
        matched = top1_sim >= THRESHOLD
        absorb = Counter(top1[i] for i in range(len(claims)) if matched[i])
        magnets = {g for g, c in absorb.items() if c >= MAGNET_LIMIT}
        confirmed = {top1[i] for i in range(len(claims))
                     if matched[i] and top1[i] not in magnets}
        pending = {top1[i] for i in range(len(claims))
                   if matched[i] and top1[i] in magnets}

        rows.append({
            "run": d.get("run"),
            "budget": d.get("budget_max_nodes"),
            "rep": d.get("rep"),
            "n_nodes": d.get("n_nodes"),
            "depth_score": d.get("depth_score"),
            "old_cov15": (d.get("judge") or {}).get("coverage"),
            "new_cov_confirmed": len(confirmed) / len(gold),
            "new_cov_incl_pending": (len(confirmed) + len(pending)) / len(gold),
            "n_magnet_units": len(magnets),
            "n_pending_nodes": int(sum(1 for i in range(len(claims)) if matched[i] and top1[i] in magnets)),
            "sim_median": round(float(np.median(top1_sim)), 3),
            "sim_p75": round(float(np.percentile(top1_sim, 75)), 3),
        })

    out = {"threshold": THRESHOLD, "magnet_limit": MAGNET_LIMIT,
           "n_runs": len(rows), "rows": rows}

    # 对照统计
    if len(rows) >= 3:
        old = [r["old_cov15"] for r in rows if r["old_cov15"] is not None]
        new = [r["new_cov_confirmed"] for r in rows if r["old_cov15"] is not None]
        dep = [r["depth_score"] for r in rows]
        newall = [r["new_cov_confirmed"] for r in rows]
        out["correlation"] = {
            "old_cov15_vs_new_cov": round(spearman(old, new), 3),
            "old_cov15_vs_new_cov_pearson": round(pearson(old, new), 3),
            "depth_vs_new_cov_spearman": round(spearman(dep, newall), 3),
            "depth_vs_old_cov15_spearman": round(spearman(dep, old), 3),
            "n": len(old),
        }

    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"明细 → {OUT}\n")
    print(f"{'run':20s} {'节点':>4s} {'depth':>6s} {'旧cov15':>7s} {'新cov16':>7s} {'含pending':>8s} {'磁体':>3s}")
    for r in rows:
        oc = f"{r['old_cov15']:.3f}" if r["old_cov15"] is not None else "  NA"
        print(f"{r['run']:20s} {r['n_nodes']:4d} {r['depth_score']:6.4f} {oc:>7s} "
              f"{r['new_cov_confirmed']:7.3f} {r['new_cov_incl_pending']:8.3f} {r['n_magnet_units']:3d}")
    if "correlation" in out:
        c = out["correlation"]
        print(f"\n对照 (n={c['n']}): 旧cov15 vs 新cov16 Spearman={c['old_cov15_vs_new_cov']} "
              f"Pearson={c['old_cov15_vs_new_cov_pearson']}")
        print(f"depth vs 新cov Spearman={c['depth_vs_new_cov_spearman']}  "
              f"depth vs 旧cov15 Spearman={c['depth_vs_old_cov15_spearman']}")


if __name__ == "__main__":
    main()
