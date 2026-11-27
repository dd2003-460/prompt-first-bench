#!/usr/bin/env python3
"""对比 gated vs baseline 150 同判据 (append 进 gated JSON 的 comparison_vs_baseline)."""
import json

GATED = "data/q9-budget-scan-gated/mech-level-scan-gated-20261127.json"
BASE = "data/q9-budget-scan/mech-level-scan-20261127.json"


def rates(counts, prefixes):
    agg = {"total": 0, "mech": 0, "spec": 0, "other": 0}
    for rt, v in counts.items():
        if any(rt.startswith(p) for p in prefixes):
            for k in agg:
                agg[k] += v[k]
    t = agg["total"]
    return {k: (agg[k], round(100 * agg[k] / t, 2)) for k in ("mech", "spec", "other")} | {"total": t}


g = json.load(open(GATED))
b = json.load(open(BASE))
gr, br = rates(g["counts_by_run"], ("gated-r",)), rates(b["counts_by_run"], ("150-r",))
comp = {
    "gated": gr, "baseline_150": br,
    "delta_other_pp": round(br["other"][1] - gr["other"][1], 2),
    "delta_mech_pp": round(gr["mech"][1] - br["mech"][1], 2),
    "note": "同判官 (qwen3.8-27b@8787) 同偏置 (calibration 44%, 偏松 other→mech): 相对差有效, 绝对值不可信",
}
g["comparison_vs_baseline"] = comp
json.dump(g, open(GATED, "w"), ensure_ascii=False, indent=1)
print(json.dumps(comp, ensure_ascii=False))
