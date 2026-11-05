#!/usr/bin/env python3
"""r269 本地降级双判官复判：arena 通道故障，用 qwen3.8-27b @ :8787 做 J1/J2。

与 r268 的区别：
- r268 是首次同源重放（receipt-r268-same-source-replay.json）
- r269 是 arena 故障后的独立复判（独立上下文 + temp=0），用于算 κ 和 G2 spread
- 产出 JSONL（与 arena 任务书同格式）+ summary（κ/G2/与 r268 对照）

用法：python replay-r269-local-dual-judge.py [--limit N]
产出：runs-fullloop/receipt-r269-local-dual-judge.jsonl + receipt-r269-local-dual-judge-summary.md
"""
from __future__ import annotations

import argparse
import json
import re
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROMPTS = json.loads((HERE.parent / "calibration" / "judge-prompts-rubric-v3.json").read_text())["prompts"]
R268 = HERE / "receipt-r268-same-source-replay.json"
OUT_JSONL = HERE / "receipt-r269-local-dual-judge.jsonl"
OUT_SUMMARY = HERE / "receipt-r269-local-dual-judge-summary.md"

NINFER_URL = "http://localhost:8787/v1/chat/completions"
MODEL = "qwen3.8-27b"
STAGES = ["stage01.md", "stage02.md", "stage03.md"]
CONFIGS = ["A-full", "B-nofreeze", "B-none"]
DOMAINS = ["D1-meeting-room", "D2-file-collab"]


def extract_items(art: str) -> list[str]:
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
    for m in re.finditer(r"(?:主张|来源)\s*(\d+)", art):
        ids.add(f"Z{m.group(1)}")
    for m in re.finditer(r"(?:方案|候选)\s*([A-Z])(?=[\s：:、，])", art):
        ids.add(f"P-{m.group(1)}")
    return sorted(ids)


def call_ninfer(prompt_text: str, artifact_text: str, item_list: list[str], retries: int = 2) -> dict:
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
    last_err = None
    for attempt in range(retries + 1):
        try:
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
        except Exception as e:
            last_err = repr(e)
            if attempt < retries:
                time.sleep(5 * (attempt + 1))
    return {"raw": None, "error": last_err}


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
        note = it.get("note", "")
        tests_failed = it.get("tests_failed", [])
        if iid and v in ("pass", "fail"):
            out[iid] = {"verdict": v, "note": note, "tests_failed": tests_failed}
    return out or None


def compute_kappa(v1: dict, v2: dict) -> dict | None:
    """Cohen's kappa on common ids. v1/v2 map id -> verdict string."""
    common = sorted(set(v1.keys()) & set(v2.keys()))
    if len(common) < 4:
        return None
    a = sum(1 for k in common if v1[k] == v2[k])
    n = len(common)
    po = a / n
    p1 = sum(1 for k in common if v1[k] == "pass") / n
    p2 = sum(1 for k in common if v2[k] == "pass") / n
    pe = p1 * p2 + (1 - p1) * (1 - p2)
    kappa = (po - pe) / (1 - pe) if pe < 1 else 1.0
    return {"n_common": n, "p_observed": round(po, 4), "kappa": round(kappa, 4)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=0, help="冒烟：只跑前 N 个 cell")
    args = ap.parse_args()

    jobs = [(cfg, dom, st) for cfg in CONFIGS for dom in DOMAINS for st in STAGES]
    if args.limit:
        jobs = jobs[: args.limit]
    print(f"r269 本地双判官：{len(jobs)} 工件 × 2 判官 ...")

    # Load r268 baseline for comparison
    r268_data = None
    if R268.exists():
        r268_data = json.loads(R268.read_text())
        print(f"r268 baseline loaded: {len(r268_data.get('scores', {}))} cells")

    results = []
    errors = []
    for i, (cfg, dom, st) in enumerate(jobs, 1):
        art_path = HERE / "pilot" / cfg / dom / st
        if not art_path.exists():
            errors.append(f"{cfg}/{dom}/{st}: artifact_missing")
            continue
        art = art_path.read_text()
        items = extract_items(art)
        if not items:
            errors.append(f"{cfg}/{dom}/{st}: no_items_extracted")
            continue

        stage_num = st.replace("stage", "S").replace(".md", "")
        cell_key = f"{cfg}/{dom}/{stage_num.lower()}"

        for judge_name in ("J1", "J2"):
            prompt_key = "J1-strict-v3" if judge_name == "J1" else "J2-lenient-v3"
            r = call_ninfer(PROMPTS[prompt_key]["text"], art, items)
            verdicts = parse_verdicts(r["raw"]) if r.get("raw") else None

            entry = {
                "cell": cell_key,
                "judge": prompt_key,
                "items": [],
                "summary": {},
                "model_identity": MODEL,
            }

            if verdicts is None:
                entry["error"] = r.get("error") or "parse_fail"
                entry["raw_head"] = (r.get("raw") or "")[:300]
                errors.append(f"{cell_key}/{judge_name}: {entry['error']}")
            else:
                entry["items"] = [
                    {"id": k, **v} for k, v in sorted(verdicts.items())
                ]
                passed = sum(1 for v in verdicts.values() if v["verdict"] == "pass")
                entry["summary"] = {"total": len(verdicts), "passed": passed}

            results.append(entry)
            status = f"{entry['summary'].get('passed','?')}/{entry['summary'].get('total','?')}" if "error" not in entry else f"ERR:{entry['error'][:30]}"
            print(f"  [{i}/{len(jobs)}] {cell_key} {judge_name}: {status} ({r.get('latency_s','?')}s)")

    # Write JSONL
    with open(OUT_JSONL, "w") as f:
        for entry in results:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(f"\nJSONL: {len(results)} rows → {OUT_JSONL}")

    # ---- κ computation (J1 vs J2 per cell) ----
    kappa_rows = []
    by_cell = {}
    for entry in results:
        if "error" in entry:
            continue
        ck = entry["cell"]
        jk = entry["judge"].split("-")[0]  # J1 or J2
        by_cell.setdefault(ck, {})[jk] = {it["id"]: it["verdict"] for it in entry["items"]}

    for ck, judges in by_cell.items():
        if "J1" in judges and "J2" in judges:
            k = compute_kappa(judges["J1"], judges["J2"])
            if k:
                kappa_rows.append({"cell": ck, **k})

    avg_kappa = sum(r["kappa"] for r in kappa_rows) / len(kappa_rows) if kappa_rows else None

    # ---- G2 spread ----
    def pass_rate(cell, judge):
        for entry in results:
            if entry["cell"] == cell and entry["judge"] == judge and "error" not in entry:
                s = entry["summary"]
                return s["passed"] / s["total"] if s["total"] else None
        return None

    g2 = {}
    for dom in DOMAINS:
        for sn in ("S01", "S02", "S03"):
            for judge in ("J1-strict-v3", "J2-lenient-v3"):
                vals = {}
                for cfg in CONFIGS:
                    cell = f"{cfg}/{dom}/s{sn[1:].lower()}"
                    s = pass_rate(cell, judge)
                    if s is not None:
                        vals[cfg] = round(s, 4)
                spread = max(vals.values()) - min(vals.values()) if len(vals) == 3 else None
                g2[f"{dom}_{sn}_{judge.split('-')[0]}"] = {
                    "scores": vals,
                    "spread": round(spread, 4) if spread is not None else None,
                    "verdict": "PASS" if spread is not None and spread > 0 else "FAIL",
                }

    # ---- Compare with r268 ----
    r268_compare = []
    if r268_data:
        r268_scores = r268_data.get("scores", {})
        for entry in results:
            if "error" in entry:
                continue
            ck = entry["cell"]
            jk = entry["judge"].split("-")[0]
            # Map to r268 format: "cfg|dom" key, stage S01/S02/S03
            parts = ck.split("/")
            cfg, dom, stage = parts[0], parts[1], "S" + parts[2][5:7]
            r268_key = f"{cfg}|{dom}"
            r268_stage = r268_scores.get(r268_key, {}).get(stage, {})
            r268_val = r268_stage.get(jk, "?")
            my_summary = entry["summary"]
            my_str = f"{my_summary.get('passed','?')}/{my_summary.get('total','?')}"
            r268_compare.append({
                "cell": ck, "judge": jk,
                "r269": my_str, "r268": r268_val,
            })

    # ---- Summary markdown ----
    lines = [
        "# r269 本地降级双判官复判 summary",
        "",
        f"- 生成时间: {time.strftime('%Y-%m-%dT%H:%M:%S%z')}",
        f"- 模型: {MODEL} @ {NINFER_URL}",
        f"- 通道: 本地 vLLM（arena 故障降级）",
        f"- conf: 0.2（同源偏差风险，judge 与生成器同族 Qwen）",
        f"- 工件数: {len(jobs)}, 完成: {sum(1 for e in results if 'error' not in e)}, 错误: {len(errors)}",
        "",
        "## κ (J1 vs J2 per cell)",
        "",
        "| Cell | n | P(obs) | κ |",
        "|------|---|--------|---|",
    ]
    for r in kappa_rows:
        lines.append(f"| {r['cell']} | {r['n_common']} | {r['p_observed']} | {r['kappa']} |")
    lines.append(f"| **mean** | | | **{avg_kappa:.4f}** |" if avg_kappa else "| mean | | | N/A |")

    lines += ["", "## G2 spread (cross-config within domain×stage×judge)", ""]
    lines.append("| Key | A-full | B-nofreeze | B-none | Spread | Verdict |")
    lines.append("|-----|--------|------------|--------|--------|---------|")
    for k, v in g2.items():
        sc = v["scores"]
        lines.append(
            f"| {k} | {sc.get('A-full','-')} | {sc.get('B-nofreeze','-')} | {sc.get('B-none','-')} "
            f"| {v['spread'] if v['spread'] is not None else 'N/A'} | {v['verdict']} |"
        )
    g2_pass = sum(1 for v in g2.values() if v["verdict"] == "PASS")
    lines.append(f"\nG2: {g2_pass}/12 PASS")

    if r268_compare:
        lines += ["", "## 与 r268 逐格对照", ""]
        lines.append("| Cell | Judge | r269 | r268 | Δ |")
        lines.append("|------|-------|------|------|---|")
        for c in r268_compare:
            delta = ""
            try:
                p269 = int(c["r269"].split("/")[0]) / int(c["r269"].split("/")[1])
                p268_str = c["r268"]
                if "/" in p268_str:
                    p268 = int(p268_str.split("/")[0]) / int(p268_str.split("/")[1])
                    delta = f"{p269-p268:+.4f}"
            except Exception:
                pass
            lines.append(f"| {c['cell']} | {c['judge']} | {c['r269']} | {c['r268']} | {delta} |")

    if errors:
        lines += ["", "## Errors", ""]
        for e in errors:
            lines.append(f"- {e}")

    OUT_SUMMARY.write_text("\n".join(lines))
    print(f"Summary → {OUT_SUMMARY}")
    print(f"κ mean = {avg_kappa:.4f}" if avg_kappa else "κ mean = N/A")
    print(f"G2 = {g2_pass}/12 PASS")
    print(f"errors: {len(errors)}")


if __name__ == "__main__":
    main()