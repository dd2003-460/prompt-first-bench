#!/usr/bin/env python3
"""Q6 budget scan 补评脚本 — 队列评分块间歇性静默失败(2>/dev/null 吞 stderr),
本脚本扫所有已落地 run json, 补齐 q6-scan-scores.json 里缺失的 (budget, rep)。
用法: python3 rescore_q6.py [scan_dir]   (默认 data/q6-budget-scan)
幂等: 已评过的 (budget, rep) 跳过, 重复跑安全。
"""
import sys, os, json, glob, re

SCAN = sys.argv[1] if len(sys.argv) > 1 else \
    '/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/q6-budget-scan'
SCORES = os.path.join(SCAN, 'q6-scan-scores.json')
sys.path.insert(0, '/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation')
from judge_v1 import judge_run
from metacog_axis import compute_metacog, load_run_nodes

# 已评过的 (budget, rep)
scores = json.load(open(SCORES)) if os.path.exists(SCORES) else []
done = {(r['budget'], r['rep']) for r in scores}

# 所有落地 run json (q6-<budget>-r<rep>-<ts>.json)
runs = []
for f in glob.glob(os.path.join(SCAN, 'q6-*-r*.json')):
    m = re.match(r'q6-(\d+)-r(\d+)-\d+\.json$', os.path.basename(f)) or \
       re.match(r'q6-(\d+)-r(\d+)-\d+-\d+\.json$', os.path.basename(f))
    if m:
        runs.append((int(m.group(1)), int(m.group(2)), f))

missing = [(b, r, f) for (b, r, f) in runs if (b, r) not in done]
print(f"落地 run {len(runs)}, 已评 {len(done)}, 缺 {len(missing)}")

for b, r, f in sorted(missing):
    try:
        rj = judge_run(f)
        rm = compute_metacog(load_run_nodes(f))
        rec = {"budget": b, "rep": r, "wall_s": 0, "n_nodes": rj["n_nodes_raw"],
               "judge": {"total": rj["total_score"], "depth": rj["layers"]["structure"]["depth_score"], "cov": rj["layers"]["coverage"]["coverage"]},
               "metacog": {"total": round(rm["metacog_total"],4), "gap": round(rm["gap_rate"],4), "ret": round(rm["retrieval_rate"],4), "hg": round(rm["healthy_gap_rate"],4), "post": round(rm["post_retrieval_accuracy"],4)}}
        scores.append(rec)
        json.dump(scores, open(SCORES, 'w'), ensure_ascii=False, indent=1)
        print(f"  [补评] {b}-r{r} metacog={rec['metacog']['total']:.4f} judge={rec['judge']['total']:.4f}")
    except Exception as e:
        import traceback; traceback.print_exc()
        print(f"  [补评失败] {b}-r{r}: {e}")

print(f"完成, scores 现 {len(scores)} 条")
