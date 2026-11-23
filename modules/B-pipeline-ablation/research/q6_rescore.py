#!/usr/bin/env python3
"""Q6 budget scan 补评分 — 幂等重建 q6-scan-scores.json

队列内评分块因执行环境问题 (python3 - 嵌套 heredoc 的 stdin 被 SM 的 2>&1
影响) 静默失败: run 数据完好, 仅 scores 缺失。本脚本遍历 q6-budget-scan
所有 run json (q6-{budget}-r{rep}-{ts}.json), judge + metacog 双轴评分,
按 (budget, rep) 去重, 重建 scores 文件。幂等: 重复跑不产生重复条目。

用法: python3 q6_rescore.py   (队列跑完后跑一次补全 15 个)
"""
import sys, json, os, glob, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "modules", "B-pipeline-ablation"))
from judge_v1 import judge_run
from metacog_axis import compute_metacog, load_run_nodes

SCAN = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "q6-budget-scan")
OUT = os.path.join(SCAN, "q6-scan-scores.json")

recs = {}
for f in sorted(glob.glob(os.path.join(SCAN, "q6-*-*.json"))):
    if f.endswith("scores.json"):
        continue
    m = re.search(r"q6-(\d+)-r(\d+)-", os.path.basename(f))
    if not m:
        continue
    budget, rep = int(m.group(1)), int(m.group(2))
    try:
        rj = judge_run(f)
        rm = compute_metacog(load_run_nodes(f))
        recs[(budget, rep)] = {
            "budget": budget, "rep": rep,
            "n_nodes": rj["n_nodes_raw"],
            "judge": {"total": rj["total_score"],
                      "depth": rj["layers"]["structure"]["depth_score"],
                      "cov": rj["layers"]["coverage"]["coverage"]},
            "metacog": {"total": round(rm["metacog_total"], 4),
                        "gap": round(rm["gap_rate"], 4),
                        "ret": round(rm["retrieval_rate"], 4),
                        "hg": round(rm["healthy_gap_rate"], 4),
                        "post": round(rm["post_retrieval_accuracy"], 4)},
        }
        print(f"  [score] budget={budget} rep={rep} n={rj['n_nodes_raw']} "
              f"judge={rj['total_score']:.4f} metacog={rm['metacog_total']:.4f} gap={rm['gap_rate']:.4f}")
    except Exception as e:
        import traceback
        print(f"  [score-err] budget={budget} rep={rep}: {e}")
        traceback.print_exc()

out = [recs[k] for k in sorted(recs)]
json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
print(f"\nrebuild: {len(out)} 条 → {os.path.basename(OUT)}")
