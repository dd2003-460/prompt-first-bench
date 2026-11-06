#!/usr/bin/env python3
"""gen: S7F 近似臂 runner — S5 全流程 prompt, 无 research hook, 无两遍核验 (纯 prompt).

任务卡 tasks/s8g-generalization.md G4 定义: "S7F = 全流程无核验无 hook (纯 prompt)"。
ablation_harness.build_prompt("S7F") 实际是 S6-style fuzzy heuristic + filtered sources
注入 (T31), 与任务卡口径不符; arms_new/ 目录里也没有现成的 S7F arm 定义。
因此按硬约束第 3 条降级: 用 S5 prompt 减去 research_hook 作为 S7F 近似, 并在此记录。

输出: runs-r293/S7F-{qid}-r{rep}.json (schema 与 ablation_harness run 文件一致)。
"""
import argparse, json, os, sys, time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ablation_harness import (
    QUESTIONS, LLM_MODEL, LLM_MAX_TOKENS,
    read_file, extract_question, call_llm, build_prompt,
)

RUNS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "runs-r293")


def run_one(qid, rep, dry_run=False):
    tag = f"S7F-{qid}-r{rep}"
    q = QUESTIONS[qid]
    question = extract_question(read_file(q["prompt_file"]))
    prompt = build_prompt("S5", qid)  # 全流程, 不注入 sources (无 hook)
    print(f"[{tag}] prompt={len(prompt)} chars, calling {LLM_MODEL}...", flush=True)

    record = {
        "arm": "S7F", "qid": qid, "rep": rep,
        "model": LLM_MODEL, "params": {"temp": 0, "max_tokens": LLM_MAX_TOKENS},
        "output_text": "", "sources": [],
        "wall_s": 0, "tokens": {"in": 0, "out": 0},
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "note": "S7F approximation per task card G4: S5 full pipeline, no research hook, no two-pass verification (pure prompt). Harness 'S7F' arm is T31 filtered-sources variant, not used.",
    }
    if dry_run:
        print(f"[{tag}] DRY RUN — prompt head:\n{prompt[:400]}...")
        return record

    t0 = time.time()
    output, tokens = call_llm(prompt, seed=None, temperature=0)
    wall = round(time.time() - t0, 1)
    print(f"[{tag}] done in {wall}s, {tokens['out']} tokens out", flush=True)
    record.update({"output_text": output, "wall_s": wall, "tokens": tokens})

    os.makedirs(RUNS_DIR, exist_ok=True)
    path = os.path.join(RUNS_DIR, f"{tag}.json")
    with open(path, "w") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)
    print(f"[{tag}] saved → {path}", flush=True)
    return record


def main():
    ap = argparse.ArgumentParser(description="S7F approximation pilot (S5 pure prompt)")
    ap.add_argument("--qs", default="Q1,Q4,Q5", help="comma-separated: Q1,Q4,Q5")
    ap.add_argument("--reps", type=int, default=1)
    ap.add_argument("--rep", type=int, default=None, help="run only this specific rep")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    qs = [q.strip().upper() for q in args.qs.split(",")]
    reps = [args.rep] if args.rep else list(range(1, args.reps + 1))
    print(f"S7F approximation: {len(qs)} questions × {len(reps)} reps, hook=off by definition")
    for qid in qs:
        for rep in reps:
            run_one(qid, rep, dry_run=args.dry_run)
    print("S7F complete.")


if __name__ == "__main__":
    main()