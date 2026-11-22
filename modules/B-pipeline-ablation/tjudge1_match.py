#!/usr/bin/env python3
"""T-JUDGE-1 J3+J5: embedding 匹配 + 客观指标（首跑 = gpu）

流程: 解析 gold Q1 单元 + checkpoint 树 → bge-m3 编码 → 每输出节点 top-1 余弦
     → 阈值匹配（首跑用 provisional 0.60，分布输出后标定）→ 指标
产出: 匹配明细 JSON + 指标摘要（覆盖率/精确率/压缩率/相似度分布）
LLM 兜底（J4）: 低于阈值的节点清单输出，供后续二元裁决（本脚本不调 LLM）
"""
import json, os, sys
import numpy as np
from sentence_transformers import SentenceTransformer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tjudge1_parse import parse_gold_q1, parse_checkpoint, GOLD, CKPT

PROV_THRESHOLD = 0.65  # 首跑标定选定（0.60 假匹配多 / 0.70 覆盖塌），见 decomp J3
MAGNET_LIMIT = 3       # 一个 gold 单元吸 >=N 个节点 → 磁体，匹配降级送 LLM 兜底


def embed(model, texts):
    return model.encode(texts, normalize_embeddings=True, show_progress_bar=False)


def main():
    model = SentenceTransformer("BAAI/bge-m3")
    gold = parse_gold_q1(GOLD)
    gold_emb = embed(model, [u["text"] for u in gold])

    out = {"threshold": PROV_THRESHOLD, "runs": {}}
    for ck in sorted(os.path.join(CKPT, p) for p in os.listdir(CKPT)
                     if p.startswith("sm-gpu-r") and os.path.isdir(os.path.join(CKPT, p))):
        name = os.path.basename(ck)
        nodes = parse_checkpoint(ck)
        node_emb = embed(model, [u["text"] for u in nodes])
        sim = node_emb @ gold_emb.T  # (n_nodes, n_gold)
        top1 = sim.argmax(axis=1)
        top1_sim = sim[np.arange(len(nodes)), top1]

        matches = []
        for i, u in enumerate(nodes):
            g = gold[top1[i]]
            matches.append({
                "node_id": u["unit_id"], "node_depth": u["depth"],
                "gold_id": g["unit_id"], "gold_kind": g["kind"],
                "sim": round(float(top1_sim[i]), 4),
                "matched": bool(top1_sim[i] >= PROV_THRESHOLD),
                "node_text": u["text"][:120], "gold_text": g["text"][:120],
            })
        matched_nodes = [m for m in matches if m["matched"]]
        matched_gold_ids = {m["gold_id"] for m in matched_nodes}

        # 磁体检测: gold 单元吸 >=MAGNET_LIMIT 个节点 → 其匹配降级 pending_llm
        from collections import Counter
        absorb = Counter(m["gold_id"] for m in matches if m["matched"])
        magnets = {g for g, c in absorb.items() if c >= MAGNET_LIMIT}
        for m in matches:
            if m["matched"] and m["gold_id"] in magnets:
                m["status"] = "pending_llm"  # 磁体匹配，待 LLM 二元裁决
            elif m["matched"]:
                m["status"] = "confirmed"
            else:
                m["status"] = "unmatched"
        confirmed = {m["gold_id"] for m in matches if m["status"] == "confirmed"}
        pending = {m["gold_id"] for m in matches if m["status"] == "pending_llm"}

        # 指标（J5）—— confirmed 为主口径，pending（磁体降级）单列
        matched_node_len = sum(len(m["node_text"]) for m in matched_nodes)  # 截断前重算
        confirmed_nodes = [m for m in matches if m["status"] == "confirmed"]
        full_node_len = sum(len(u["text"]) for u in nodes if u["unit_id"] in
                            {m["node_id"] for m in confirmed_nodes})
        confirmed_gold_len = sum(len(g["text"]) for g in gold if g["unit_id"] in confirmed)
        coverage_by_kind = {}
        for kind in ("spec", "misread", "conclusion", "gap"):
            gk = [g for g in gold if g["kind"] == kind]
            mk = [g for g in gk if g["unit_id"] in confirmed]
            coverage_by_kind[kind] = f"{len(mk)}/{len(gk)}"
        out["runs"][name] = {
            "n_nodes": len(nodes), "n_gold": len(gold),
            "coverage_confirmed": f"{len(confirmed)}/{len(gold)} = {len(confirmed)/len(gold):.3f}",
            "coverage_incl_pending": f"{len(matched_gold_ids)}/{len(gold)} = {len(matched_gold_ids)/len(gold):.3f}",
            "coverage_by_kind": coverage_by_kind,
            "magnet_gold_units": sorted(magnets),
            "pending_llm_gold_units": sorted(pending),
            "precision": f"{len(confirmed_nodes)}/{len(nodes)} = {len(confirmed_nodes)/len(nodes):.3f}",
            "compression_ratio": round(full_node_len / confirmed_gold_len, 3) if confirmed_gold_len else None,
            "sim_distribution": {
                "min": round(float(top1_sim.min()), 3),
                "p25": round(float(np.percentile(top1_sim, 25)), 3),
                "median": round(float(np.median(top1_sim)), 3),
                "p75": round(float(np.percentile(top1_sim, 75)), 3),
                "max": round(float(top1_sim.max()), 3),
                "n_below_threshold": int((top1_sim < PROV_THRESHOLD).sum()),
            },
            "matches": matches,
        }
    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tjudge1-match-gpu.json")
    json.dump(out, open(outpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"明细 → {outpath}")
    for name, r in out["runs"].items():
        print(f"\n=== {name} ===")
        print(f"  覆盖率(confirmed): {r['coverage_confirmed']}  (含磁体pending: {r['coverage_incl_pending']})")
        print(f"  按类(confirmed): {r['coverage_by_kind']}")
        print(f"  精确率: {r['precision']}  压缩率: {r['compression_ratio']}")
        if r["magnet_gold_units"]:
            print(f"  磁体 gold 单元(降级送LLM): {r['magnet_gold_units']}")
        d = r["sim_distribution"]
        print(f"  sim 分布: min={d['min']} p25={d['p25']} med={d['median']} p75={d['p75']} max={d['max']} "
              f"低于{PROV_THRESHOLD}: {d['n_below_threshold']}")
        top = sorted([m for m in r["matches"] if m["status"] == "confirmed"], key=lambda m: -m["sim"])[:5]
        print("  top5 confirmed 匹配:")
        for m in top:
            print(f"    {m['sim']:.3f} [{m['node_id']}] → {m['gold_id']} ({m['gold_kind']})")
            print(f"         节点: {m['node_text'][:70]}")
            print(f"         gold: {m['gold_text'][:70]}")

    # LLM 兜底清单（J4）: 磁体匹配的节点，供 27b 二元裁决（等 K7 释放 vLLM 后跑）
    fallback = []
    for name, r in out["runs"].items():
        for m in r["matches"]:
            if m["status"] == "pending_llm":
                fallback.append({"run": name, "node_id": m["node_id"], "node_text": m["node_text"],
                                 "candidate_gold": m["gold_id"], "sim": m["sim"]})
    fbpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tjudge1-llm-fallback-gpu.json")
    json.dump(fallback, open(fbpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nLLM 兜底清单 → {fbpath} ({len(fallback)} 条待裁决)")


if __name__ == "__main__":
    main()
