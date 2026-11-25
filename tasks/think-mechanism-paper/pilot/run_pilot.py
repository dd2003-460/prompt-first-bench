#!/usr/bin/env python3
"""TASK-T4b pilot runner: 5 prompts x 2 conditions = 10 serial API calls.
Incremental append to runs.json after EACH run (anti-truncation protocol).
Raw API responses saved to raw/<run_id>.json for no-fabrication audit."""
import json, os, time, sys
import requests

BASE = os.path.dirname(os.path.abspath(__file__))
RUNS_JSON = os.path.join(BASE, "runs.json")
RAW_DIR = os.path.join(BASE, "raw")
os.makedirs(RAW_DIR, exist_ok=True)

ENDPOINT = "http://127.0.0.1:8787/v1/chat/completions"
MODEL = "qwen3.8-27b-mtp"
TEMPERATURE = 0.7
MAX_TOKENS = 1500
TIMEOUT_S = 300

T1_T5 = """T1 Cost model: when you solve a concrete problem or are asked "is X optimal?", write down the cost model (what cost is computed, under what premises) and a unified form; verify the original solution is a special case. If you cannot derive it, name the missing premise.
T2 Unified coverage: when facing several seemingly unrelated methods/systems, find one formula or analogy that covers all of them (compression ratio / info gain per cost / channel bandwidth), and write the degeneration conditions of each.
T3 Quantitative landing: when giving a qualitative conclusion, immediately quantify it into a testable number (success-rate formula / bandwidth lower bound / expected number of tests). If you cannot quantify, mark "needs measurement" and design the cheapest probe.
T4 Analogy audit: when borrowing a historical case/analogy/prior, check condition gaps delta and conclusion sensitivity s_k dimension by dimension; if sensitive and mismatched, do not borrow; attach an epsilon*uniform floor against confident errors.
T5 Criterion bottleneck: when a framework takes shape, find the "criterion bottleneck" — the step in the loop lacking cheap reliable ground truth; that step is the real bottleneck, not the architecture. Prefer "closing the world" (synthetic domains / executable verification) as the fix."""

SYS_A = "You are a helpful assistant."
SYS_B = "Follow these five thinking disciplines in your answer:\n" + T1_T5

PROMPTS = {
    "P1": ("T1", "Is binary search the fastest way to find an element in a sorted array of N items? What is the cost model behind your answer, and under what premises does it hold?"),
    "P2": ("T2", "Compare gradient descent, Newton's method, and evolutionary strategies as optimizers. Is there a single formula or analogy that covers all three, and under what conditions does each degenerate?"),
    "P3": ("T3", "People say large language models generalize better with more data. Turn this qualitative claim into a testable quantitative prediction, or state exactly what measurement is needed and design the cheapest probe."),
    "P4": ("T4", "Someone suggests borrowing the lesson from TCP congestion control (slow start) to design LLM agent retry policies. Audit this analogy dimension by dimension before accepting it."),
    "P5": ("T5", "We are building an automated research pipeline: idea generation -> literature search -> experiment -> judge. Which step is the true bottleneck, and what is the cheapest way to make the system verifiable?"),
}

def load_runs():
    if os.path.exists(RUNS_JSON):
        with open(RUNS_JSON) as f:
            return json.load(f)
    return []

def save_runs(runs):
    tmp = RUNS_JSON + ".tmp"
    with open(tmp, "w") as f:
        json.dump(runs, f, ensure_ascii=False, indent=2)
    os.replace(tmp, RUNS_JSON)

def call_api(system, user, max_retries=2):
    payload = {
        "model": MODEL,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS,
    }
    last_err = None
    for attempt in range(max_retries + 1):
        t0 = time.time()
        try:
            r = requests.post(ENDPOINT, json=payload, timeout=TIMEOUT_S)
            latency = time.time() - t0
            if r.status_code != 200:
                last_err = f"HTTP {r.status_code}: {r.text[:300]}"
                print(f"    attempt {attempt+1} failed: {last_err}", flush=True)
                if attempt < max_retries:
                    time.sleep(2)
                    continue
                return None, latency, last_err
            data = r.json()
            choice = data["choices"][0]
            return {
                "text": choice["message"]["content"],
                "finish_reason": choice.get("finish_reason"),
                "usage": data.get("usage", {}),
                "raw": data,
            }, latency, None
        except Exception as e:
            latency = time.time() - t0
            last_err = f"{type(e).__name__}: {e}"
            print(f"    attempt {attempt+1} exception: {last_err}", flush=True)
            if attempt < max_retries:
                time.sleep(2)
    return None, latency, last_err

def main():
    runs = load_runs()
    done_ids = {r["run_id"] for r in runs}
    order = [(pid, cond) for pid in PROMPTS for cond in ("A", "B")]
    for i, (pid, cond) in enumerate(order):
        rid = f"{pid}-{cond}"
        if rid in done_ids:
            print(f"[{i+1}/10] {rid} already in runs.json, skip", flush=True)
            continue
        template, user = PROMPTS[pid]
        system = SYS_A if cond == "A" else SYS_B
        print(f"[{i+1}/10] {rid} ({template}) calling...", flush=True)
        result, latency, err = call_api(system, user)
        rec = {
            "run_id": rid,
            "prompt_id": pid,
            "condition": cond,
            "template": template,
            "system_prompt": system,
            "user_prompt": user,
            "model": MODEL,
            "temperature": TEMPERATURE,
            "max_tokens": MAX_TOKENS,
            "status": "ok" if result else "error",
            "error": err,
            "latency_s": round(latency, 3),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "finish_reason": None,
            "full_text": None,
            "prompt_tokens": None,
            "completion_tokens": None,
            "total_tokens": None,
        }
        if result:
            rec["finish_reason"] = result["finish_reason"]
            rec["full_text"] = result["text"]
            u = result["usage"]
            rec["prompt_tokens"] = u.get("prompt_tokens")
            rec["completion_tokens"] = u.get("completion_tokens")
            rec["total_tokens"] = u.get("total_tokens")
            with open(os.path.join(RAW_DIR, f"{rid}.json"), "w") as f:
                json.dump(result["raw"], f, ensure_ascii=False, indent=2)
        runs.append(rec)
        save_runs(runs)  # incremental append, anti-truncation
        print(f"    -> status={rec['status']} finish={rec['finish_reason']} "
              f"tokens={rec['completion_tokens']} latency={rec['latency_s']}s "
              f"(saved to runs.json)", flush=True)
        if i < len(order) - 1:
            time.sleep(1)
    ok = sum(1 for r in runs if r["status"] == "ok")
    print(f"DONE: {ok}/{len(runs)} ok", flush=True)

if __name__ == "__main__":
    main()
