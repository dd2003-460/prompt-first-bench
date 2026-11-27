#!/usr/bin/env python3
"""
pipeline_snapshot.py — 实验管线固化层：存档 manifest + 增量变化记录（2026-11-21）

管线四步的分工（固化后）：
  跑          → t53b-batch.sh + ablation_driver.sh（已有，不动）
  存档        → driver 跑前 mv 旧 ckpt 到 checkpoints/archive/（已有）
               + driver 跑完 copy 自包含 run 文件到 ablation-runs/（已有）
               + 本脚本生成 manifest 索引（新增）
  记录增量    → 本脚本：每 (qid,arm) 按时间序算 round 间 delta（新增）
  继续跑      → batch 循环 + watchdog（已有，不动）

设计原则：
  - 幂等：输出是 ablation-runs/*.json 的纯函数，随时重跑，不 append、不双记账
  - 解耦：只读 ablation-runs/，写 pipeline-state.json（新文件），不碰 SM/driver/corpus
  - 增量口径：同 (qid,arm) 内按 round 排序，delta = 本轮 - 上轮
    （Δcoverage/Δdepth/Δn_nodes + 模式集变化 patterns_added/lost + K^t 指标）

用法:
  python3 pipeline_snapshot.py            # 全量重算 → ablation-runs/pipeline-state.json
  python3 pipeline_snapshot.py --show     # 重算后打印摘要
"""
import json, os, glob, re, sys
from datetime import datetime

STAGE = os.path.dirname(os.path.abspath(__file__))
RUNS_DIR = os.path.join(STAGE, "..", "..", "modules/B-pipeline-ablation/data/t53b", "runs")
OUT = os.path.join(RUNS_DIR, "pipeline-state.json")

# ── 模式关键词表（v1，从 47 run 实测 claim 词频推得，2026-11-21）──
# 每域一组 (模式名, 关键词)；claim 命中任一关键词 → 归该模式；多命中取首个；无命中 → other
PATTERNS = {
    "gpu": [
        ("vram",       ["显存", "权重", "kv cache", "精度", "量化", "fp8", "bf16", "int8"]),
        ("throughput", ["tok/s", "tpot", "ttft", "吞吐", "batch", "延迟"]),
        ("cost",       ["tco", "成本", "价格", "性价比", "功耗", "watt"]),
        ("bandwidth",  ["带宽", "pcie", "nvlink", "io"]),
        ("compat",     ["兼容", "单卡", "双卡", "rtx", "a100", "h100", "h800", "l40"]),
        ("microarch",  ["sm", "微架构", "roofline", "算力", "flops", "mtp"]),
        ("filter",     ["过滤", "排除", "硬性", "约束", "可行性"]),
        ("scoring",    ["评分", "打分", "排序", "对比", "推荐", "最优"]),
        ("spec",       ["规格", "参数", "显存容量", "gb", "内存"]),
    ],
    "nat": [
        ("hit_rate",   ["命中率", "命中", "byte", "字节", "hit"]),
        ("eviction",   ["lru", "lfu", "淘汰", "驱逐", "替换", "update"]),
        ("pareto",     ["pareto", "前沿", "权衡", "tradeoff"]),
        ("distribution", ["分布", "hot", "cold", "热门", "冷", "zipf", "对象大小"]),
        ("capacity",   ["缓存容量", "容量", "cache size", "大小"]),
        ("correction", ["修正", "copula", "校准", "偏差"]),
        ("scoring",    ["评分", "排序", "最优", "推荐", "效率"]),
    ],
    "soc": [
        ("pricing",    ["挂价", "定价", "ask", "price", "降价", "标价"]),
        ("deal",       ["成交", "deal", "gmv", "周期", "咨询"]),
        ("behavior",   ["损失厌恶", "阈值", "心理", "行为", "锚定", "噪声", "noise"]),
        ("ctr",        ["ctr", "点击", "曝光", "流量", "search"]),
        ("projection", ["下游投影", "投影", "预测", "估计", "量化"]),
        ("cost",       ["成本", "利润", "收益", "margin"]),
        ("scoring",    ["评分", "排序", "最优", "推荐", "策略"]),
    ],
}


def classify(claim: str, qid: str) -> str:
    c = claim.lower()
    for name, kws in PATTERNS.get(qid, []):
        if any(k in c for k in kws):
            return name
    return "other"


def load_runs():
    runs = []
    for f in sorted(glob.glob(os.path.join(RUNS_DIR, "*.json"))):
        if f.endswith("_judge.json") or f == OUT:
            continue
        try:
            d = json.load(open(f))
        except Exception as e:
            print(f"[WARN] skip {os.path.basename(f)}: {e}", file=sys.stderr)
            continue
        if "nodes" not in d:
            continue
        run_name = os.path.basename(f)[:-5]
        m = re.match(r"^(gpu|nat|soc)_(formula|text)_r(\d{2})$", run_name)
        if not m:
            continue
        qid, arm, rnd = m.group(1), m.group(2), int(m.group(3))
        nodes = d.get("nodes", [])
        patterns = {}
        for n in nodes:
            p = classify(n.get("claim", ""), qid)
            patterns[p] = patterns.get(p, 0) + 1
        runs.append({
            "run": run_name, "qid": qid, "arm": arm, "round": rnd,
            "coverage": d.get("coverage"), "depth": d.get("depth_score"),
            "n_nodes": len(nodes),
            "n_verified": sum(1 for n in nodes if n.get("status") == "verified"),
            "n_degraded": sum(1 for n in nodes if n.get("status") == "degraded"),
            "patterns": patterns,
            "n_patterns": len([p for p in patterns if p != "other"]),
            "file": f"modules/B-pipeline-ablation/data/t53b/runs/{run_name}.json",
            "mtime": datetime.fromtimestamp(os.path.getmtime(f)).astimezone().isoformat(),
        })
    return runs


def build_deltas(runs):
    """同 (qid,arm) 按 round 排序，delta = 本轮 - 上轮。"""
    groups = {}
    for r in runs:
        groups.setdefault((r["qid"], r["arm"]), []).append(r)
    out = []
    for (qid, arm), rs in sorted(groups.items()):
        rs.sort(key=lambda r: r["round"])
        prev = None
        for r in rs:
            delta = None
            if prev:
                pset, cset = set(prev["patterns"]), set(r["patterns"])
                delta = {
                    "d_coverage": round((r["coverage"] or 0) - (prev["coverage"] or 0), 4) if r["coverage"] is not None else None,
                    "d_depth": round((r["depth"] or 0) - (prev["depth"] or 0), 4) if r["depth"] is not None else None,
                    "d_n_nodes": r["n_nodes"] - prev["n_nodes"],
                    "patterns_added": sorted(pset - cset),
                    "patterns_lost": sorted(cset - pset),
                }
            out.append({
                "run": r["run"], "qid": qid, "arm": arm, "round": r["round"],
                "coverage": r["coverage"], "depth": r["depth"], "n_nodes": r["n_nodes"],
                "n_patterns": r["n_patterns"],
                "prev_run": prev["run"] if prev else None,
                "delta": delta,
            })
            prev = r
    return out


def main():
    show = "--show" in sys.argv
    runs = load_runs()
    deltas = build_deltas(runs)
    state = {
        "generated_at": datetime.now().astimezone().isoformat(),
        "n_runs": len(runs),
        "runs": runs,
        "deltas": deltas,
    }
    with open(OUT, "w") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    print(f"[snapshot] {len(runs)} runs → {os.path.relpath(OUT, STAGE)}")
    if show:
        # 每 (qid,arm) 一行摘要
        by_g = {}
        for d in deltas:
            by_g.setdefault((d["qid"], d["arm"]), []).append(d)
        for (qid, arm), ds in sorted(by_g.items()):
            covs = [d["coverage"] for d in ds if d["coverage"] is not None]
            nodes = [d["n_nodes"] for d in ds]
            all_pats = set()
            for d in ds:
                for r in runs:
                    if r["run"] == d["run"]:
                        all_pats |= set(r["patterns"])
            print(f"  {qid}_{arm}: n={len(ds)} cov={min(covs):.3f}-{max(covs):.3f} "
                  f"nodes={min(nodes)}-{max(nodes)} patterns={len(all_pats)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
