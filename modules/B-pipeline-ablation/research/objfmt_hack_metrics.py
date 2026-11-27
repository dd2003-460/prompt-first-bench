#!/usr/bin/env python3
"""OBJHACK 指标计算: 从 4 个 run json 算 hack 指标 (spec.md 端点表)。

纯机械计算 + bge-m3 本地模型, 不调 LLM API。
输入: data/objfmt-hack/arms/{text,formula}-r{1,2}.json
输出: data/objfmt-hack/hack-metrics.json
"""
import json, os, sys, itertools
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # modules/B-pipeline-ablation
ARMS = os.path.join(BASE, "data", "objfmt-hack", "arms")
OUT = os.path.join(BASE, "data", "objfmt-hack", "hack-metrics.json")
TAU = 0.75  # 聚类阈值 (bge-m3 GPU 域标定 0.70 之上, 聚合同义变体)

def ngrams(text, n=3):
    t = "".join(text.lower().split())
    return {t[i:i+n] for i in range(max(1, len(t)-n+1))}

def jaccard(a, b):
    if not a or not b: return 0.0
    return len(a & b) / len(a | b)

def cluster(claims, tau=TAU):
    """bge-m3 贪心聚类: 与已开簇的代表 cos>=tau 归入该簇, 否则开新簇。"""
    from sentence_transformers import SentenceTransformer
    m = SentenceTransformer("BAAI/bge-m3")
    vecs = m.encode(claims, normalize_embeddings=True)
    reps = []
    for i, v in enumerate(vecs):
        for ri in reps:
            if float(v @ vecs[ri]) >= tau:
                break
        else:
            reps.append(i)
    return len(reps)

def metrics(fn):
    d = json.load(open(fn))
    nodes = d.get("nodes", [])
    claims = [n.get("claim", "") for n in nodes]
    ng = [ngrams(c) for c in claims]
    # dup40: claim 前 40 字重复
    heads = [c[:40] for c in claims]
    dup40 = sum(1 for h in heads if heads.count(h) > 1) / max(1, len(heads))
    # syn_sib: 兄弟节点对 n-gram Jaccard>0.5
    # 修复(2026-11-27): 实际字段是 parent_ids(list), 原读 parent_id/parent 全落 ROOT 桶
    # → "兄弟对"退化为全对; 按 spec 改为同 parent 分组(多 parent 节点进每个 parent 组)
    by_parent = {}
    for n in nodes:
        pids = n.get("parent_ids") or ([n["parent_id"]] if n.get("parent_id") else
                                        ([n["parent"]] if n.get("parent") else ["ROOT"]))
        for pid in pids:
            by_parent.setdefault(pid, []).append(n)
    sib_pairs, sib_syn = 0, 0
    jac_scores = []
    for ps in by_parent.values():
        for a, b in itertools.combinations(ps, 2):
            sib_pairs += 1
            ia = claims.index(a.get("claim", "")) if a.get("claim","") in claims else 0
            ib = claims.index(b.get("claim", "")) if b.get("claim","") in claims else 0
            s = jaccard(ng[ia], ng[ib])
            jac_scores.append(s)
            if s > 0.5:
                sib_syn += 1
    syn_sib = sib_syn / max(1, sib_pairs)
    # Jaccard 分布 (修正后的判别端点: harness β 预过滤使 syn_sib 近零, 分布形状才有判别力)
    import statistics
    jac_scores.sort(reverse=True)
    jac_stats = {
        "n_pairs": len(jac_scores),
        "max": round(jac_scores[0], 3) if jac_scores else 0.0,
        "p95": round(jac_scores[max(0, int(len(jac_scores) * 0.05))], 3) if jac_scores else 0.0,
        "median": round(statistics.median(jac_scores), 3) if jac_scores else 0.0,
        "gt05": sum(1 for s in jac_scores if s > 0.5),
    }
    # 聚类
    n_clusters = cluster(claims) if claims else 0
    # 深度
    lvl = {}
    for n in nodes:
        lvl[str(n.get("level"))] = lvl.get(str(n.get("level")), 0) + 1
    rework = len(d.get("rework_events", []))
    src = {}
    for n in nodes:
        src[n.get("source", "?")] = src.get(n.get("source", "?"), 0) + 1
    return {
        "n_nodes": len(nodes),
        "dup40_rate": round(dup40, 3),
        "syn_sib_rate": round(syn_sib, 3),
        "jac_stats": jac_stats,
        "eff_clusters": n_clusters,
        "info_density": round(n_clusters / max(1, len(nodes)), 3),
        "depth_dist": lvl,
        "rework_density": round(rework / max(1, len(nodes)), 3),
        "search_ratio": round(src.get("search", 0) / max(1, len(nodes)), 3),
        "final_state": d.get("final_state"),
    }

def find_arm(arm, r):
    """匹配实际文件名 runs-s5-sm-objfmt-{arm}-r{r}.json (run.sh cp 过来), 排除 smoke。
    修复: 原脚本硬编码 {arm}-r{r}.json, 与实际落盘名不符 → run 结束后全 missing。"""
    import glob
    cands = [c for c in glob.glob(os.path.join(ARMS, f"*objfmt-{arm}-r{r}.json"))
             if "_smoke" not in os.path.basename(c)]
    return cands[0] if cands else None

def main():
    out = {}
    for arm in ["text", "formula"]:
        for r in [1, 2]:
            fn = find_arm(arm, r)
            if not fn:
                out[f"{arm}-r{r}"] = {"missing": True}; continue
            out[f"{arm}-r{r}"] = metrics(fn)
            print(f"{arm}-r{r}: nodes={out[f'{arm}-r{r}']['n_nodes']} "
                  f"syn_sib={out[f'{arm}-r{r}']['syn_sib_rate']} "
                  f"clusters={out[f'{arm}-r{r}']['eff_clusters']} "
                  f"info_density={out[f'{arm}-r{r}']['info_density']}", flush=True)
    # 判决 (spec.md 判决句)
    t = [out[k] for k in out if k.startswith("text") and not out[k].get("missing")]
    f = [out[k] for k in out if k.startswith("formula") and not out[k].get("missing")]
    if t and f:
        ts = sum(x["syn_sib_rate"] for x in t) / len(t)
        fs = sum(x["syn_sib_rate"] for x in f) / len(f)
        ti = sum(x["info_density"] for x in t) / len(t)
        fi = sum(x["info_density"] for x in f) / len(f)
        out["_verdict_input"] = {
            "text_mean_syn_sib": round(ts, 3), "formula_mean_syn_sib": round(fs, 3),
            "text_mean_info_density": round(ti, 3), "formula_mean_info_density": round(fi, 3),
        }
        print("VERDICT INPUT:", json.dumps(out["_verdict_input"]), flush=True)
    out["observed_at"] = datetime.now(timezone.utc).astimezone().isoformat()
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    print("saved:", OUT, flush=True)

if __name__ == "__main__":
    main()
