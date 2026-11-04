#!/usr/bin/env python3
"""C2: Local re-run with aligned rubric via :8787 vLLM (qwen3.8-27b).
Uses the updated JUDGE_PROMPT from cross_judge.py."""
import json, os, sys, time, urllib.request, re
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cross_judge import JUDGE_PROMPT, GOLD_FILES

VLLM_URL = "http://127.0.0.1:8787/v1/chat/completions"
OUT_PATH = os.path.join(HERE, "runs", "local-rerun-aligned.jsonl")

def call_vllm(prompt_text):
    """Call local vLLM for judge scoring."""
    payload = {
        "model": "qwen3.8-27b",
        "messages": [{"role": "user", "content": prompt_text}],
        "temperature": 0.0,
        "max_tokens": 500,
    }
    req = urllib.request.Request(VLLM_URL, data=json.dumps(payload).encode(),
                                  headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        d = json.loads(resp.read())
    return d["choices"][0]["message"]["content"]

def extract_json(text):
    """Extract JSON from LLM response."""
    # Try direct
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        pass
    # Find JSON in text
    m = re.search(r'\{[^{}]*"m1"[^{}]*\}', text)
    if m:
        try:
            return json.loads(m.group(0))
        except json.JSONDecodeError:
            pass
    return None

def main():
    arms = ["S0", "S1", "S2", "S3", "S4", "S5"]
    qs = ["Q1", "Q2", "Q3", "Q4", "Q5"]
    
    # Resume support
    done_tags = set()
    results = []
    if os.path.exists(OUT_PATH):
        with open(OUT_PATH) as f:
            for line in f:
                r = json.loads(line)
                if r.get("m1") is not None:
                    done_tags.add(r["tag"])
                    results.append(r)
        print(f"Resuming: {len(done_tags)} already done")
    
    total = 0
    for qid in qs:
        gold_path = GOLD_FILES.get(qid)
        if not gold_path or not os.path.exists(gold_path):
            print(f"[skip] {qid}: no gold file at {gold_path}")
            continue
        gold = open(gold_path).read()
        
        for arm in arms:
            for rep in [1, 2, 3]:
                tag = f"{arm}-{qid}-r{rep}"
                if tag in done_tags:
                    continue
                
                run_path = os.path.join(HERE, "runs", f"{arm}-{qid}-r{rep}.json")
                if not os.path.exists(run_path):
                    continue
                
                d = json.load(open(run_path))
                answer = d.get("output_text", "")
                
                prompt = JUDGE_PROMPT.format(gold=gold[:4000], answer=answer[:6000])
                
                print(f"[judge] {tag}...", flush=True)
                try:
                    raw = call_vllm(prompt)
                    verdict = extract_json(raw)
                    if verdict and verdict.get("m1") is not None:
                        m1 = float(verdict["m1"])
                        result = {
                            "tag": tag, "arm": arm, "qid": qid, "rep": rep,
                            "m1": m1,
                            "claims_checked": verdict.get("claims_checked", 0),
                            "claims_correct": verdict.get("claims_correct", 0),
                            "notes": verdict.get("notes", "")[:200],
                            "timestamp": datetime.now(timezone.utc).isoformat(),
                        }
                    else:
                        # Retry once
                        time.sleep(2)
                        raw = call_vllm(prompt)
                        verdict = extract_json(raw)
                        if verdict and verdict.get("m1") is not None:
                            m1 = float(verdict["m1"])
                            result = {
                                "tag": tag, "arm": arm, "qid": qid, "rep": rep,
                                "m1": m1,
                                "claims_checked": verdict.get("claims_checked", 0),
                                "claims_correct": verdict.get("claims_correct", 0),
                                "notes": verdict.get("notes", "")[:200],
                                "timestamp": datetime.now(timezone.utc).isoformat(),
                            }
                        else:
                            result = {"tag": tag, "arm": arm, "qid": qid, "rep": rep,
                                      "m1": None, "notes": f"parse_failed: {raw[:150]}"}
                except Exception as e:
                    result = {"tag": tag, "arm": arm, "qid": qid, "rep": rep,
                              "m1": None, "notes": f"error: {str(e)[:150]}"}
                
                results.append(result)
                total += 1
                
                # Append-only write
                with open(OUT_PATH, "a") as f:
                    f.write(json.dumps(result, ensure_ascii=False) + "\n")
                
                status = f"M1={result['m1']:.2f}" if result.get("m1") is not None else "FAILED"
                print(f"  {status} ({result.get('notes','')[:50]})", flush=True)
                time.sleep(1)  # gentle rate limit
    
    print(f"\nDone. {total} new judgments, {len(results)} total → {OUT_PATH}")
    
    # Quick stats
    valid = [r for r in results if r.get("m1") is not None]
    if valid:
        print(f"Valid: {len(valid)}/{len(results)}, mean M1 = {sum(r['m1'] for r in valid)/len(valid):.3f}")

if __name__ == "__main__":
    main()