"""rubric v2 重放脚本：用 J1-strict-v2 / J2-lenient-v2 重打 r6 全部 run。

动机：r244 发现 J1/J2 旧版 rubric 在 54/346 item 上分歧（一致率 ~74% < 85% 门槛），
且判官选择能翻转头条结论。v2 rubric 修了三个根因（来源真实性硬判据 /
保留不确定性不再豁免 / 具体性操作化）。本脚本在 ninfer :8787 上重放打分，
产出 AC1-AC4 判定回执 receipt-r7-rubric-v2-replay.json。

用法：python replay-rubric-v2.py [--limit N]（--limit 只跑前 N 个 run 做冒烟）
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS_R6 = HERE.parent / "runs-r6"
PROMPTS = json.loads((HERE / "judge-prompts-rubric-v2.json").read_text())
OUT = HERE / "receipt-r7-rubric-v2-replay.json"

NINFER_URL = "http://localhost:8787/v1/chat/completions"
MODEL = "qwen3.8-27b"


def call_ninfer(prompt_text: str, artifact_text: str) -> dict:
    payload = {
        "model": MODEL,
        "temperature": 0,
        "max_tokens": 4096,
        "messages": [
            {"role": "system", "content": prompt_text},
            {"role": "user", "content": f"请审计以下工件：\n\n{artifact_text}"},
        ],
    }
    req = urllib.request.Request(
        NINFER_URL,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=300) as resp:
        body = json.loads(resp.read())
    return {
        "raw": body["choices"][0]["message"]["content"],
        "latency_s": round(time.time() - t0, 1),
    }


def parse_verdicts(raw: str) -> dict | None:
    raw = raw.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
    try:
        j = json.loads(raw)
    except Exception:
        return None
    items = j.get("items")
    if not isinstance(items, list):
        return None
    out = {}
    for it in items:
        iid = it.get("id")
        v = it.get("verdict")
        if iid and v in ("pass", "fail"):
            out[iid] = v
    return out or None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=0, help="只跑前 N 个 run（冒烟用）")
    args = ap.parse_args()

    # 收集 r6 全部 (config, domain, seed) run（排除判官文件 *-J1/-J2；
# 不用 glob('*/*/*/seed*.json')——实测该 pattern 在此目录树返回空，原因未查明）
    runs = sorted(
        rf
        for c in RUNS_R6.iterdir() if c.is_dir()
        for d in c.iterdir() if d.is_dir()
        for rf in d.iterdir()
        if rf.suffix == ".json" and rf.name.startswith("seed") and not re.search(r"-J\d", rf.name)
    )
    if args.limit:
        runs = runs[: args.limit]
    print(f"重放 {len(runs)} run × 2 判官 ...")

    results = {}
    for i, rf in enumerate(runs, 1):
        key = str(rf.relative_to(RUNS_R6))[:-5]  # 去掉 .json
        artifact = json.loads(rf.read_text()).get("output", "")
        entry = {}
        for judge_key in ("J1-strict-v2", "J2-lenient-v2"):
            ptext = PROMPTS["prompts"][judge_key]["text"]
            try:
                res = call_ninfer(ptext, artifact)
                verdicts = parse_verdicts(res["raw"])
                entry[judge_key] = {
                    "score": (sum(v == "pass" for v in verdicts.values()) / len(verdicts))
                    if verdicts else None,
                    "n_items": len(verdicts) if verdicts else 0,
                    "verdicts": verdicts,
                    "latency_s": res["latency_s"],
                    "parse_ok": verdicts is not None,
                }
            except Exception as e:
                entry[judge_key] = {"error": repr(e)}
            print(f"  [{i}/{len(runs)}] {key} {judge_key}: done")
        results[key] = entry

    # ---- AC 计算 ----
    agree_total = agree_hit = 0
    for key, e in results.items():
        j1 = e.get("J1-strict-v2", {}).get("verdicts") or {}
        j2 = e.get("J2-lenient-v2", {}).get("verdicts") or {}
        common = set(j1) & set(j2)
        agree_hit += sum(j1[k] == j2[k] for k in common)
        agree_total += len(common)
    ac1_rate = agree_hit / agree_total if agree_total else None

    def score_of(key, judge):
        return results.get(key, {}).get(judge, {}).get("score")

    # AC2 阳性对照：P1 植入件单独打
    ac2 = None
    p1_path = HERE / "positive-control-x5-mutated.md"
    if p1_path.exists():
        p1_text = p1_path.read_text()
        fails = []
        for judge_key in ("J1-strict-v2", "J2-lenient-v2"):
            try:
                res = call_ninfer(PROMPTS["prompts"][judge_key]["text"], p1_text)
                v = parse_verdicts(res["raw"]) or {}
                # 植入项是 X5（mutated 版把 X5 处置改成虚假「已解释」）
                fails.append(v.get("X5") == "fail")
            except Exception:
                fails.append(False)
        ac2 = all(fails)

    # AC3 B-none 地板 / AC4 A-full vs B-2del-eo 区分度
    def cfg_mean(cfg, judge):
        vals = [
            score_of(k, judge)
            for k in results
            if k.startswith(cfg + "/") and score_of(k, judge) is not None
        ]
        return sum(vals) / len(vals) if vals else None

    ac3 = all(
        (m := cfg_mean("B-none", j)) is not None and m < 0.3
        for j in ("J1-strict-v2", "J2-lenient-v2")
    )
    diffs = []
    for j in ("J1-strict-v2", "J2-lenient-v2"):
        a, b = cfg_mean("A-full", j), cfg_mean("B-2del-eo", j)
        if a is not None and b is not None:
            diffs.append(a - b)
    ac4 = all(d >= 0.3 for d in diffs) if diffs else False

    receipt = {
        "kind": "rubric_v2_replay",
        "run_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "n_runs": len(results),
        "prompts_sha256_16": {k: v["sha256_16"] for k, v in PROMPTS["prompts"].items()},
        "per_run": results,
        "ac1_agreement": {"agree": agree_hit, "total": agree_total, "rate": ac1_rate, "threshold": 0.85, "pass": (ac1_rate or 0) >= 0.85},
        "ac2_positive_control_x5_both_fail": ac2,
        "ac3_bnone_floor_lt_0.3": ac3,
        "ac4_a_vs_2deol_diff_ge_0.3": ac4,
        "cfg_means": {
            cfg: {j: cfg_mean(cfg, j) for j in ("J1-strict-v2", "J2-lenient-v2")}
            for cfg in ("A-full", "B-none", "B-nofreeze", "B-2del-eo")
        },
        "overall_pass": (ac1_rate or 0) >= 0.85 and bool(ac2) and ac3 and ac4,
    }
    OUT.write_text(json.dumps(receipt, ensure_ascii=False, indent=1))
    print("\n=== 验收 ===")
    print(f"AC1 一致率: {ac1_rate if ac1_rate is None else round(ac1_rate,3)} ({agree_hit}/{agree_total}) ≥0.85 → {'PASS' if (ac1_rate or 0)>=0.85 else 'FAIL'}")
    print(f"AC2 阳性对照双 fail: {ac2}")
    print(f"AC3 B-none 地板 <0.3: {ac3}")
    print(f"AC4 A-2del-eo 差 ≥0.3: {ac4} (diffs={diffs})")
    print(f"OVERALL: {'PASS' if receipt['overall_pass'] else 'FAIL'} → {OUT}")


if __name__ == "__main__":
    main()
