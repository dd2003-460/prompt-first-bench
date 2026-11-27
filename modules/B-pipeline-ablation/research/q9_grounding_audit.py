#!/usr/bin/env python3
# origin: ai
# q9_grounding_audit.py — 接地真伪判别器 v1
# 不信模型自报"已验证/已实测"，只看轨迹里有没有真工具溯源:
#   grounded_rate = final_text 数字中能在工具输出(result_head/output_head)里找到子串的占比
#   sim_flag      = 自报实测类措辞 且 零工具调用 (散文模拟)
# 输入: gpu-model-probe-20261127.json (A/B 臂) + _C.json (C 臂)，脚本 json.load，不整读进上下文。
import json
import os
import re
from datetime import date

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "q9-budget-scan")
INPUTS = [
    os.path.join(BASE, "gpu-model-probe-20261127.json"),
    os.path.join(BASE, "gpu-model-probe-20261127_C.json"),
    os.path.join(BASE, "gpu-model-probe-20261127_D.json"),
]

NUM_RE = re.compile(r"\d+(?:\.\d+)?")
# v1 基础词 + 补词（2026-11-27 锚点校准: C 臂 ep1/ep2 未用"实测"，而是直接把
# 硬件规格表当事实陈述并给"性能预测"——零工具下断言性能数字同样属散文模拟）。
# 补词只影响零工具臂: A/B 臂 n_code_calls>0，AND 条件天然免疫误伤。
SIM_KEYWORDS = re.compile(
    r"实测|已验证|已查证|measured|verified|benchmark|实证|参数对比|性能预测",
    re.IGNORECASE,
)


def extract_numbers(final_text):
    """判据1: 数字 token, 1-8 位数字, 排除年份 19xx/20xx 和纯 0/1。"""
    d = set()
    for tok in NUM_RE.findall(final_text or ""):
        digits = tok.replace(".", "")
        if not (1 <= len(digits) <= 8):
            continue
        if re.fullmatch(r"(19|20)\d\d", tok):
            continue
        if tok in ("0", "1"):
            continue
        d.add(tok)
    return d


def trace_pool(ep):
    """判据2: 拼接所有 tool_calls.result_head + code_runs.output_head。"""
    parts = []
    for step in ep.get("trajectory") or []:
        for tc in step.get("tool_calls") or []:
            rh = tc.get("result_head")
            if rh:
                parts.append(str(rh))
    for cr in ep.get("code_runs") or []:
        oh = cr.get("output_head")
        if oh:
            parts.append(str(oh))
    return "\n".join(parts)


def audit_arm(arm_name, per_episode):
    rows = []
    for ep in per_episode:
        d = extract_numbers(ep.get("final_text"))
        pool = trace_pool(ep)
        grounded = len({x for x in d if x in pool}) / len(d) if d else 1.0
        n_search = int(ep.get("n_search_calls") or 0)
        n_code = int(ep.get("n_code_calls") or 0)
        sim = bool(SIM_KEYWORDS.search(ep.get("final_text") or "")) and n_search == 0 and n_code == 0
        rows.append({
            "ep": ep.get("ep"),
            "arm": ep.get("arm", arm_name),
            "n_numbers": len(d),
            "grounded_rate": round(grounded, 4),
            "sim_flag": sim,
            "n_search_calls": n_search,
            "n_code_calls": n_code,
        })
    return rows


def main():
    all_rows = []
    for path in INPUTS:
        with open(path) as f:
            data = json.load(f)
        for arm_name, arm in data.get("arms", {}).items():
            all_rows.extend(audit_arm(arm_name, arm.get("per_episode") or []))

    # stdout: 每臂汇总
    arms = {}
    for r in all_rows:
        arms.setdefault(r["arm"], []).append(r)
    print(f"{'arm':<20} {'eps':>3} {'mean_grounded_rate':>18} {'sim_flag':>8}")
    for arm_name in sorted(arms):
        rows = arms[arm_name]
        mean_gr = sum(r["grounded_rate"] for r in rows) / len(rows)
        n_sim = sum(1 for r in rows if r["sim_flag"])
        print(f"{arm_name:<20} {len(rows):>3} {mean_gr:>18.4f} {n_sim:>8}")

    out_path = os.path.join(BASE, f"grounding-audit-{date.today().strftime('%Y%m%d')}.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    payload = {
        "generated_at": date.today().isoformat(),
        "inputs": [os.path.basename(p) for p in INPUTS],
        "criteria": {
            "numbers": r"regex \d+(?:\.\d+)?, 1-8 digits, excl years 19xx/20xx and pure 0/1",
            "pool": "concat trajectory[*].tool_calls[*].result_head + code_runs[*].output_head",
            "grounded_rate": "|{d in D: d substring of P}|/|D|, 1.0 if D empty",
            "sim_flag": "final_text matches 实测|已验证|已查证|measured|verified|benchmark|实证|参数对比|性能预测 (ci) AND n_search_calls==0 AND n_code_calls==0",
        },
        "per_arm_summary": {
            arm_name: {
                "n_episodes": len(rows),
                "mean_grounded_rate": round(sum(r["grounded_rate"] for r in rows) / len(rows), 4),
                "n_sim_flag": sum(1 for r in rows if r["sim_flag"]),
            }
            for arm_name, rows in sorted(arms.items())
        },
        "episodes": all_rows,
    }
    with open(out_path, "w") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
