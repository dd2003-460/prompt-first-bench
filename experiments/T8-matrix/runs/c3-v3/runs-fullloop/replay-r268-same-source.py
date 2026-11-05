#!/usr/bin/env python3
"""r268 同源降级重放：qwen3.8-27b 对 pilot 18 份阶段工件做 J1/J2 双判。

动机（r266 回执 §4(c) 降级通道）：异源 judge 端点不可用（LM Studio/Ollama 端口 CLOSED，
无外部 API key），按 conf-0.2 降级用同源模型复判——目的不是给 T8 下最终结论，而是
(1) 算 J1/J2 的 κ（两个裁判去掉瞎蒙后的真实一致度，检验 rubric v3 双判是否站得住）；
(2) 复算 G2 spread（同 domain 内跨 3 config 的分数差）看信号是否仍 < 噪声；
(3) 为将来拿到非 Qwen key 后的异源复判留一份可对比基线。
所有产出标注 conf-0.2 + 同源偏差风险。

用法：python replay-r268-same-source.py [--limit N]
产出：runs-fullloop/receipt-r268-same-source-replay.json
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
OUT = HERE / "receipt-r268-same-source-replay.json"

NINFER_URL = "http://localhost:8787/v1/chat/completions"
MODEL = "qwen3.8-27b"
STAGES = ["stage01.md", "stage02.md", "stage03.md"]
CONFIGS = ["A-full", "B-nofreeze", "B-none"]
DOMAINS = ["D1-meeting-room", "D2-file-collab"]


def extract_items(art: str) -> list[str]:
    """与 replay-rubric-v3.py 同版正则策略（r246 对账冻结）。"""
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
        except Exception as e:  # noqa: BLE001
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
        if iid and v in ("pass", "fail"):
            out[iid] = v
    return out or None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=0, help="冒烟：只跑前 N 个 cell×stage")
    args = ap.parse_args()

    jobs = [(cfg, dom, st) for cfg in CONFIGS for dom in DOMAINS for st in STAGES]
    if args.limit:
        jobs = jobs[: args.limit]
    print(f"r268 同源重放：{len(jobs)} 工件 × 2 判官 (J1-strict-v3 / J2-lenient-v3) ...")

    results = {}
    errors = []
    for i, (cfg, dom, st) in enumerate(jobs, 1):
        art_path = HERE / "pilot" / cfg / dom / st
        art = art_path.read_text()
        items = extract_items(art)
        cell_key = f"{cfg}|{dom}"
        stage_num = st.replace("stage", "S")
        entry = results.setdefault(cell_key, {}).setdefault(stage_num, {})
        entry["item_count"] = len(items)
        for judge_name in ("J1", "J2"):
            prompt_key = "J1-strict-v3" if judge_name == "J1" else "J2-lenient-v3"
            r = call_ninfer(PROMPTS[prompt_key]["text"], art, items)
            verdicts = parse_verdicts(r["raw"]) if r.get("raw") else None
            entry[judge_name] = {
                "status": "ok" if verdicts is not None else "parse_fail",
                "latency_s": r.get("latency_s"),
                "error": r.get("error"),
                "verdicts": verdicts,
                "raw_head": (r.get("raw") or "")[:300],
            }
            if verdicts is None:
                errors.append(f"{cell_key}/{stage_num}/{judge_name}: {r.get('error') or 'JSON parse fail'}")
        passed = {j: sum(1 for v in (entry[j].get("verdicts") or {}).values() if v == "pass") for j in ("J1", "J2")}
        total = {j: len(entry[j].get("verdicts") or {}) for j in ("J1", "J2")}
        print(f"[{i}/{len(jobs)}] {cell_key} {stage_num}: items={len(items)} "
              f"J1={passed['J1']}/{total['J1']} J2={passed['J2']}/{total['J2']}")

    # ---- κ 计算（逐 cell×stage：J1 vs J2 在共同 id 上的一致度，去瞎蒙）----
    kappa_rows = []
    for cell_key, stages in results.items():
        for stage_num, entry in stages.items():
            v1 = entry.get("J1", {}).get("verdicts") or {}
            v2 = entry.get("J2", {}).get("verdicts") or {}
            common = sorted(set(v1) & set(v2))
            if len(common) < 4:
                continue
            a = sum(1 for k in common if v1[k] == v2[k])
            n = len(common)
            po = a / n
            p1_pass = sum(1 for k in common if v1[k] == "pass") / n
            p2_pass = sum(1 for k in common if v2[k] == "pass") / n
            pe = p1_pass * p2_pass + (1 - p1_pass) * (1 - p2_pass)
            kappa = (po - pe) / (1 - pe) if pe < 1 else 1.0
            kappa_rows.append({
                "cell": cell_key, "stage": stage_num, "n_common": n,
                "p_observed": round(po, 4), "kappa": round(kappa, 4),
            })
    avg_kappa = sum(r["kappa"] for r in kappa_rows) / len(kappa_rows) if kappa_rows else None

    # ---- G2 复算：每 (domain, stage, judge) 内跨 3 config 的 max-min spread ----
    def score(cell_key, stage_num, judge):
        entry = results.get(cell_key, {}).get(stage_num, {})
        v = entry.get(judge, {}).get("verdicts") or {}
        return sum(1 for x in v.values() if x == "pass") / len(v) if v else None

    g2 = {}
    for dom in DOMAINS:
        for stage_num in ("S01", "S02", "S03"):
            for judge in ("J1", "J2"):
                vals = []
                for cfg in CONFIGS:
                    s = score(f"{cfg}|{dom}", stage_num, judge)
                    if s is not None:
                        vals.append(s)
                spread = max(vals) - min(vals) if len(vals) == 3 else None
                g2[f"{dom}_{stage_num}_{judge}"] = {
                    "scores": {c: score(f"{c}|{dom}", stage_num, judge) for c in CONFIGS},
                    "spread": round(spread, 4) if spread is not None else None,
                    "verdict": "PASS" if spread is not None and spread > 0 else "FAIL",
                }

    receipt = {
        "receipt_id": "r268-same-source-replay",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "goal": "T8-C3-v3-fullloop-execution · 阶段 02.5 降级通道 (r266 回执 §4(c))",
        "channel": {
            "url": NINFER_URL,
            "model": MODEL,
            "conf_note": "conf-0.2 同源降级：judge 与生成器同族 (Qwen)，存在同源偏差风险，T8 结论须标注",
        },
        "rubric": "J1-strict-v3 / J2-lenient-v3 (judge-prompts-rubric-v3.json, frozen r249)",
        "cells_completed": [f"{c}|{d}" for c in CONFIGS for d in DOMAINS],
        "errors": errors,
        "scores": {
            ck: {
                sn: {j: f"{sum(1 for v in (e.get(j,{}).get('verdicts') or {}).values() if v=='pass')}/{len(e.get(j,{}).get('verdicts') or {})}"
                      for j in ("J1", "J2")}
                for sn, e in stages.items()
            }
            for ck, stages in results.items()
        },
        "inter_rater_reliability": {
            "metric": "Cohen's κ per cell×stage (J1 vs J2 on common ids, n≥4)",
            "rows": kappa_rows,
            "mean_kappa": round(avg_kappa, 4) if avg_kappa is not None else None,
            "note": "κ≥0.6 视为双判可用；<0.4 说明 rubric v3 双判区分口径分歧大，需先修 rubric 再谈消融",
        },
        "g2_recompute": {
            "definition": "spread = max-min pass-rate across 3 configs within (domain, stage, judge)",
            "results": g2,
            "pass_count": sum(1 for r in g2.values() if r["verdict"] == "PASS"),
            "compare_r265": "r265 为 1/12 PASS (仅 D1 S02 J2 spread=0.1111)——但注意口径不同：r265 用冻结 opportunity set（每 stage 固定 5-10 条），本重放用正则全量抽取（9-45 条），分数不可直接跨口径比较，只作方向性参考",
        },
    }
    OUT.write_text(json.dumps(receipt, ensure_ascii=False, indent=1))
    print(f"\nκ mean = {receipt['inter_rater_reliability']['mean_kappa']}")
    print(f"G2 = {receipt['g2_recompute']['pass_count']}/12 PASS")
    print(f"errors: {len(errors)}")
    print(f"→ {OUT}")


if __name__ == "__main__":
    main()