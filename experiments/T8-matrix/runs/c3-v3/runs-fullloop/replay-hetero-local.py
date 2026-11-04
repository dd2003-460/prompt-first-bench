#!/usr/bin/env python3
"""本地异源 judge 复判：qwen3.8-27b @ :8787 对 18 fullloop 工件做 J1+J2 双判。

动机：arena 通道不可用（ego-browser 会话页面加载异常），降级到本地自答。
虽然与 r268 同源（都是 qwen3.8-27b），但独立上下文 + temp=0 能算：
(1) J1/J2 的 κ（检验 rubric v3 双判在独立调用下是否站得住）
(2) G2 spread（同 domain 内跨 config 的分数差）
(3) 与 r268 逐格对照（Δ 列）→ 量化同源 judge 的 run-to-run 噪声

产出：arena-hetero-judge-results.jsonl + receipt-hetero-local-replay.json
"""
import json, re, time, urllib.request, sys
from pathlib import Path
from datetime import datetime, timezone, timedelta

HERE = Path(__file__).resolve().parent
PROMPTS = json.loads((HERE.parent / "calibration" / "judge-prompts-rubric-v3.json").read_text())["prompts"]
OUT_JSONL = HERE / "arena-hetero-judge-results.jsonl"
OUT_RECEIPT = HERE / "receipt-hetero-local-replay.json"

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
    for m in re.finditer(r"\b(GAP-\d+)\b", art):
        ids.add(m.group(1))
    for m in re.finditer(r"\b(OQ-\d+)\b", art):
        ids.add(m.group(1))
    for m in re.finditer(r"\bGap[- ]?[\w-]+\b", art):
        ids.add(m.group(0).replace(" ", "-"))
    for m in re.finditer(r"(?:主张|来源)\s*(\d+)", art):
        ids.add(f"Z{m.group(1)}")
    for m in re.finditer(r"(?:方案|候选)\s*([A-Z])(?=[\s：:、，])", art):
        ids.add(f"P-{m.group(1)}")
    return sorted(ids)


def call_judge(judge_name: str, artifact_text: str, items: list[str]) -> dict:
    """Call the LLM judge and parse JSON response."""
    prompt_text = PROMPTS[judge_name]["text"]
    item_list = ", ".join(items)
    user_msg = f"{artifact_text}\n\n条目清单：{item_list}"
    
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": prompt_text},
            {"role": "user", "content": user_msg}
        ],
        "temperature": 0,
        "max_tokens": 4096
    }
    
    req = urllib.request.Request(
        NINFER_URL,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read())
    
    raw = data["choices"][0]["message"]["content"].strip()
    
    # Parse JSON (handle markdown code blocks)
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1]
        if raw.endswith("```"):
            raw = raw[:-3]
        raw = raw.strip()
        if raw.startswith("json"):
            raw = raw[4:].strip()
    
    try:
        result = json.loads(raw)
    except json.JSONDecodeError:
        # Try to find JSON in the text
        match = re.search(r'\{.*\}', raw, re.DOTALL)
        if match:
            result = json.loads(match.group(0))
        else:
            raise ValueError(f"Cannot parse judge response: {raw[:200]}")
    
    return result


def main():
    results = []
    total_cells = len(CONFIGS) * len(DOMAINS) * len(STAGES)
    done = 0
    
    # Resume support: skip cells already in jsonl
    existing_cells = set()
    if OUT_JSONL.exists():
        for line in OUT_JSONL.read_text().strip().split('\n'):
            if line.strip():
                try:
                    r = json.loads(line)
                    existing_cells.add((r['cell'], r['judge']))
                except:
                    pass
    
    for cfg in CONFIGS:
        for dom in DOMAINS:
            for stage_file in STAGES:
                cell_id = f"{cfg}/{dom}/{stage_file.replace('.md','')}"
                fpath = HERE / "pilot" / cfg / dom / stage_file
                
                if not fpath.exists():
                    print(f"SKIP {cell_id}: artifact missing")
                    continue
                
                artifact_text = fpath.read_text()
                items = extract_items(artifact_text)
                
                if not items:
                    print(f"SKIP {cell_id}: no items extracted")
                    continue
                
                for judge_name in ["J1-strict-v3", "J2-lenient-v3"]:
                    key = (cell_id, judge_name)
                    if key in existing_cells:
                        print(f"RESUME {cell_id} {judge_name}: already done")
                        continue
                    
                    done += 1
                    print(f"[{done}/{total_cells*2}] Judging {cell_id} with {judge_name} ({len(items)} items)...", flush=True)
                    
                    try:
                        result = call_judge(judge_name, artifact_text, items)
                        entry = {
                            "cell": cell_id,
                            "judge": judge_name,
                            "items": result.get("items", []),
                            "summary": result.get("summary", {}),
                            "model_identity": "qwen3.8-27b (same-source, independent context)",
                            "timestamp": datetime.now(timezone(timedelta(hours=8))).isoformat()
                        }
                        # Append to jsonl
                        with open(OUT_JSONL, "a") as f:
                            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
                        results.append(entry)
                        
                        s = result.get("summary", {})
                        print(f"  → {s.get('passed', '?')}/{s.get('total', '?')} passed", flush=True)
                    except Exception as e:
                        print(f"  ERROR: {e}", flush=True)
                        entry = {
                            "cell": cell_id,
                            "judge": judge_name,
                            "error": str(e),
                            "model_identity": "qwen3.8-27b",
                            "timestamp": datetime.now(timezone(timedelta(hours=8))).isoformat()
                        }
                        with open(OUT_JSONL, "a") as f:
                            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
                    
                    time.sleep(1)  # Rate limit
    
    # Compute summary statistics
    print(f"\n{'='*60}")
    print(f"Done. {len(results)} successful judgments.")
    
    # Per-cell pass rates
    cell_scores = {}
    for r in results:
        if "error" in r:
            continue
        s = r["summary"]
        total = s.get("total", 0)
        passed = s.get("passed", 0)
        rate = passed / total if total > 0 else 0
        cell_scores.setdefault(r["cell"], {})[r["judge"]] = rate
    
    # G2 spread: same domain, across configs
    print(f"\nG2 Spread (same domain, cross-config J1 mean diff):")
    for dom in DOMAINS:
        j1_scores = {}
        j2_scores = {}
        for cfg in CONFIGS:
            j1_vals = []
            j2_vals = []
            for stage in ["stage01", "stage02", "stage03"]:
                cell = f"{cfg}/{dom}/{stage}"
                if cell in cell_scores:
                    if "J1-strict-v3" in cell_scores[cell]:
                        j1_vals.append(cell_scores[cell]["J1-strict-v3"])
                    if "J2-lenient-v3" in cell_scores[cell]:
                        j2_vals.append(cell_scores[cell]["J2-lenient-v3"])
            j1_scores[cfg] = sum(j1_vals)/len(j1_vals) if j1_vals else None
            j2_scores[cfg] = sum(j2_vals)/len(j2_vals) if j2_vals else None
        
        if all(v is not None for v in j1_scores.values()):
            spread_j1 = max(j1_scores.values()) - min(j1_scores.values())
            print(f"  {dom}: J1 spread = {spread_j1:.4f} ({j1_scores})")
        if all(v is not None for v in j2_scores.values()):
            spread_j2 = max(j2_scores.values()) - min(j2_scores.values())
            print(f"  {dom}: J2 spread = {spread_j2:.4f} ({j2_scores})")
    
    # Kappa between J1 and J2 (per item)
    print(f"\nκ (Cohen's kappa, J1 vs J2, per-item agreement):")
    j1_verdicts = {}
    j2_verdicts = {}
    for r in results:
        if "error" in r:
            continue
        for item in r.get("items", []):
            key = f"{r['cell']}:{item['id']}"
            verdict = "pass" if item.get("verdict") == "pass" else "fail"
            if r["judge"] == "J1-strict-v3":
                j1_verdicts[key] = verdict
            else:
                j2_verdicts[key] = verdict
    
    common_keys = set(j1_verdicts.keys()) & set(j2_verdicts.keys())
    if common_keys:
        tp = sum(1 for k in common_keys if j1_verdicts[k] == j2_verdicts[k] == "pass")
        tf = sum(1 for k in common_keys if j1_verdicts[k] == j2_verdicts[k] == "fail")
        p = sum(1 for k in common_keys if j1_verdicts[k] != j2_verdicts[k])
        n = len(common_keys)
        
        pe = ((tp+p)/n) * ((tp+p)/n) + ((tf+p)/n) * ((tf+p)/n)
        po = (tp + tf) / n
        kappa = (po - pe) / (1 - pe) if pe < 1 else 0
        
        print(f"  n={n} common items, agreement={po:.3f}, κ={kappa:.3f}")
    
    # Write receipt
    receipt = {
        "generated_at": datetime.now(timezone(timedelta(hours=8))).isoformat(),
        "channel": f"{MODEL} @ localhost:8787 (same-source, independent context)",
        "conf": "0.2 (same-source bias risk)",
        "cells_judged": len(results),
        "cells_total": total_cells * 2,
        "cell_scores": cell_scores,
        "g2_spread": {},
        "kappa_j1_j2": None,
        "notes": "Local replay due to arena channel unavailable. Same model as r268 but independent context."
    }
    OUT_RECEIPT.write_text(json.dumps(receipt, indent=2, ensure_ascii=False))
    print(f"\nReceipt written: {OUT_RECEIPT}")


if __name__ == "__main__":
    main()
