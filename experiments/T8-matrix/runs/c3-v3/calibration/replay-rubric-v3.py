"""rubric v3 重放脚本：J1-strict-v3 / J2-lenient-v3 + id 锚定（条目清单注入 prompt）。

动机：r246 对账（RUBRIC-V2-RECONCILIATION.md）定位 v2 失败两根因——
① J1-v2 来源判据一刀切过严（AC3/AC4 区分度塌）；② 双判官自造 id 不对齐（AC1 被幻觉 id 拉低，35.2% 越界）。
v3 = J2 保留 v2 原文（已验证 0.978 无扰动）+ J1 来源判据三级化 + 双判官统一 id 锚定。

用法：python replay-rubric-v3.py [--limit N]（--limit 只跑前 N 个 run 做冒烟）
产出：receipt-r8-rubric-v3-replay.json（AC1-AC4 判定）
"""
from __future__ import annotations

import argparse
import json
import re
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS_R6 = HERE.parent / "runs-r6"
PROMPTS = json.loads((HERE / "judge-prompts-rubric-v3.json").read_text())["prompts"]
OUT = HERE / "receipt-r8-rubric-v3-replay.json"

NINFER_URL = "http://localhost:8787/v1/chat/completions"
MODEL = "qwen3.8-27b"


def extract_items(art: str) -> list[str]:
    """条目抽取器（与 r246 对账同版正则策略）：从工件正文抽统一 item 清单。"""
    ids = set()
    for m in re.finditer(r"\b([A-H]\d+(?:\.\d+)?)\b", art):
        ids.add(m.group(1))
    for m in re.finditer(r"\b(U\d+|K\d+|Q\d+|P\d+)\b", art):
        ids.add(m.group(1))
    for m in re.finditer(r"\bGAP-\d+\b", art):
        ids.add(m.group(0))
    for m in re.finditer(r"\bOQ-\d+\b", art):
        ids.add(m.group(0))
    for m in re.finditer(r"\bGap[- ]?[\w-]+\b", art):
        ids.add(m.group(0).replace(" ", "-"))
    for m in re.finditer(r"(?:主张|候选|方案|来源)\s*(\d+)", art):
        ids.add(f"Z{m.group(1)}")
    return sorted(ids)


def call_ninfer(prompt_text: str, artifact_text: str, item_list: list[str]) -> dict:
    user = (
        f"条目清单（只许评这些 id）：{json.dumps(item_list, ensure_ascii=False)}\n\n"
        f"请审计以下工件：\n\n{artifact_text}"
    )
    payload = {
        "model": MODEL,
        "temperature": 0,
        "max_tokens": 4096,
        "messages": [
            {"role": "system", "content": prompt_text},
            {"role": "user", "content": user},
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

    runs = sorted(
        rf
        for c in RUNS_R6.iterdir() if c.is_dir()
        for d in c.iterdir() if d.is_dir()
        for rf in d.iterdir()
        if rf.suffix == ".json" and rf.name.startswith("seed") and not re.search(r"-J\d", rf.name)
    )
    if args.limit:
        runs = runs[: args.limit]
    print(f"重放 {len(runs)} run × 2 判官 (v3 + id 锚定) ...")

    results = {}
    for i, rf in enumerate(runs, 1):
        key = str(rf.relative_to(RUNS_R6))[:-5]
        artifact = json.loads(rf.read_text()).get("output", "")
        canon = extract_items(artifact)
        entry = {"canon_ids": canon}
        for judge_key in ("J1-strict-v3", "J2-lenient-v3"):
            ptext = PROMPTS[judge_key]["text"]
            try:
                res = call_ninfer(ptext, artifact, canon)
                verdicts = parse_verdicts(res["raw"])
                off = [k for k in (verdicts or {}) if k not in set(canon)]
                entry[judge_key] = {
                    "score": (sum(v == "pass" for v in verdicts.values()) / len(verdicts))
                    if verdicts else None,
                    "n_items": len(verdicts) if verdicts else 0,
                    "verdicts": verdicts,
                    "out_of_canon_ids": off,
                    "latency_s": res["latency_s"],
                    "parse_ok": verdicts is not None,
                }
            except Exception as e:
                entry[judge_key] = {"error": repr(e)}
            print(f"  [{i}/{len(runs)}] {key} {judge_key}: done")
        results[key] = entry

    # ---- AC 计算（口径：只算两判官都落在 canonical 清单内的 id）----
    agree_total = agree_hit = 0
    for key, e in results.items():
        canon = set(e["canon_ids"])
        j1 = set((e.get("J1-strict-v3") or {}).get("verdicts") or {}) & canon
        j2 = set((e.get("J2-lenient-v3") or {}).get("verdicts") or {}) & canon
        common = j1 & j2
        agree_hit += sum(
            e["J1-strict-v3"]["verdicts"][k] == e["J2-lenient-v3"]["verdicts"][k]
            for k in common
        )
        agree_total += len(common)
    ac1_rate = agree_hit / agree_total if agree_total else None

    # AC2 阳性对照
    ac2 = None
    p1_path = HERE / "positive-control-x5-mutated.md"
    if p1_path.exists():
        p1_text = p1_path.read_text()
        fails = []
        for judge_key in ("J1-strict-v3", "J2-lenient-v3"):
            try:
                res = call_ninfer(PROMPTS[judge_key]["text"], p1_text, ["X5"])
                v = parse_verdicts(res["raw"]) or {}
                fails.append(v.get("X5") == "fail")
            except Exception:
                fails.append(False)
        ac2 = all(fails)

    def cfg_mean(cfg, judge):
        vals = [
            results[k][judge]["score"]
            for k in results
            if k.startswith(cfg + "/")
            and results[k].get(judge, {}).get("score") is not None
        ]
        return sum(vals) / len(vals) if vals else None

    ac3 = all(
        (m := cfg_mean("B-none", j)) is not None and m < 0.3
        for j in ("J1-strict-v3", "J2-lenient-v3")
    )
    diffs = []
    for j in ("J1-strict-v3", "J2-lenient-v3"):
        a, b = cfg_mean("A-full", j), cfg_mean("B-2del-eo", j)
        if a is not None and b is not None:
            diffs.append(a - b)
    ac4 = all(d >= 0.3 for d in diffs) if diffs else False

    receipt = {
        "kind": "rubric_v3_replay",
        "run_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "n_runs": len(results),
        "prompts_sha256_16": {k: v["sha256_16"] for k, v in PROMPTS.items()},
        "ac1_note": "口径：只统计两判官 verdict 都落在 canonical 抽取清单内的 id",
        "per_run": results,
        "ac1_agreement": {"agree": agree_hit, "total": agree_total, "rate": ac1_rate, "threshold": 0.85, "pass": (ac1_rate or 0) >= 0.85},
        "ac2_positive_control_x5_both_fail": ac2,
        "ac3_bnone_floor_lt_0.3": ac3,
        "ac4_a_vs_2deol_diff_ge_0.3": ac4,
        "cfg_means": {
            cfg: {j: cfg_mean(cfg, j) for j in ("J1-strict-v3", "J2-lenient-v3")}
            for cfg in ("A-full", "B-none", "B-nofreeze", "B-2del-eo")
        },
        "overall_pass": (ac1_rate or 0) >= 0.85 and bool(ac2) and ac3 and ac4,
    }
    OUT.write_text(json.dumps(receipt, ensure_ascii=False, indent=1))
    print("\n=== 验收 ===")
    print(f"AC1 一致率: {round(ac1_rate,3) if ac1_rate is not None else 'NA'} ({agree_hit}/{agree_total}) ≥0.85 → {'PASS' if (ac1_rate or 0)>=0.85 else 'FAIL'}")
    print(f"AC2 阳性对照双 fail: {ac2}")
    print(f"AC3 B-none 地板 <0.3: {ac3}")
    print(f"AC4 A-2del-eo 差 ≥0.3: {ac4} (diffs={diffs})")
    print(f"OVERALL: {'PASS' if receipt['overall_pass'] else 'FAIL'} → {OUT}")


if __name__ == "__main__":
    main()