#!/usr/bin/env python3
"""
DRB RACE judge: score target articles against reference articles.

Usage:
    # Local qwen2.5-7b judge (lower-bound estimate):
    python drb_race_judge.py --judge local --judge-url http://localhost:1234/v1 --judge-model qwen2.5-7b-original

    # OpenRouter GPT-5.5 judge (official, needs OPENROUTER_API_KEY):
    python drb_race_judge.py --judge openrouter

Inputs:
    - Target articles: runs-s5-sm-gpu/gptr-bench/*.md  (or --target-dir)
    - Reference articles: /tmp/drbench/data/test_data/cleaned_data/reference.jsonl
    - Criteria: /tmp/drbench/data/criteria_data/criteria.jsonl
    - Queries: /tmp/drbench/data/prompt_data/query.jsonl

Output:
    runs-s5-sm-gpu/drb-race-scores.json
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

# Add DRB repo to path for utils
DRB_DIR = "/tmp/drbench"
sys.path.insert(0, DRB_DIR)

from utils.score_calculator import calculate_weighted_scores
from utils.json_extractor import extract_json_from_markdown


def load_jsonl(path):
    items = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items


def build_maps(query_path, criteria_path, reference_path):
    queries = {q["prompt"]: q for q in load_jsonl(query_path)}
    criteria = {c["prompt"]: c for c in load_jsonl(criteria_path)}
    references = {r["prompt"]: r["article"] for r in load_jsonl(reference_path)}
    return queries, criteria, references


def format_criteria_list(criteria_data):
    """Format criteria for prompt (no weights)."""
    criteria_for_prompt = {}
    for dim, criterions in criteria_data.get("criterions", {}).items():
        if not isinstance(criterions, list):
            continue
        criteria_for_prompt[dim] = [
            {"criterion": c["criterion"], "explanation": c["explanation"]}
            for c in criterions if isinstance(c, dict) and "criterion" in c
        ]
    return json.dumps(criteria_for_prompt, ensure_ascii=False, indent=2)


def build_score_prompt(task_prompt, article_1, article_2, criteria_list, language="en"):
    """Build the merged score prompt."""
    if language == "zh":
        from prompt.score_prompt_zh import generate_merged_score_prompt as tpl
    else:
        from prompt.score_prompt_en import generate_merged_score_prompt as tpl
    return tpl.format(
        task_prompt=task_prompt,
        article_1=article_1,
        article_2=article_2,
        criteria_list=criteria_list,
    )


def call_local_judge(prompt, base_url, model, max_tokens=8192, timeout=300):
    """Call local OpenAI-compatible API."""
    import urllib.request
    url = f"{base_url}/chat/completions"
    payload = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a strict research article evaluation expert."},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": max_tokens,
        "temperature": 0,
    }).encode()
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.loads(resp.read())
    return data["choices"][0]["message"]["content"]


def call_openrouter_judge(prompt, api_key, model="openai/gpt-5.5", max_tokens=8192, timeout=300):
    """Call OpenRouter API."""
    import urllib.request
    url = "https://openrouter.ai/api/v1/chat/completions"
    payload = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a strict research article evaluation expert."},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": max_tokens,
    }).encode()
    req = urllib.request.Request(url, data=payload, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.loads(resp.read())
    return data["choices"][0]["message"]["content"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--judge", choices=["local", "openrouter"], default="local")
    parser.add_argument("--judge-url", default="http://localhost:1234/v1")
    parser.add_argument("--judge-model", default="qwen2.5-7b-original")
    parser.add_argument("--openrouter-key", default=os.environ.get("OPENROUTER_API_KEY", ""))
    parser.add_argument("--openrouter-model", default="openai/gpt-5.5")
    parser.add_argument("--target-dir", default="archive/root-runs/runs-s5-sm-gpu/gptr-bench")
    parser.add_argument("--query-path", default=f"{DRB_DIR}/data/prompt_data/query.jsonl")
    parser.add_argument("--criteria-path", default=f"{DRB_DIR}/data/criteria_data/criteria.jsonl")
    parser.add_argument("--reference-path", default=f"{DRB_DIR}/data/test_data/cleaned_data/reference.jsonl")
    parser.add_argument("--output", default="archive/root-runs/runs-s5-sm-gpu/drb-race-scores.json")
    parser.add_argument("--ids", type=str, default="", help="Comma-separated question IDs to evaluate (empty = all found)")
    args = parser.parse_args()

    queries, criteria, references = build_maps(args.query_path, args.criteria_path, args.reference_path)

    # Load target articles
    target_dir = Path(args.target_dir)
    targets = {}
    for f in sorted(target_dir.glob("*.md")):
        text = f.read_text()
        # Try to match by filename or content
        targets[f.stem] = text

    # Map target filenames to query prompts
    # gptr_bench_run.py saves as q{N}.md where N is index in QUESTIONS list
    # We need to map back to DRB query IDs
    all_queries = load_jsonl(args.query_path)
    id_to_prompt = {q["id"]: q["prompt"] for q in all_queries}
    prompt_to_id = {q["prompt"]: q["id"] for q in all_queries}

    # Determine which IDs to evaluate
    if args.ids:
        eval_ids = [int(x) for x in args.ids.split(",")]
    else:
        eval_ids = list(id_to_prompt.keys())

    results = []
    for qid in eval_ids:
        prompt = id_to_prompt.get(qid)
        if not prompt:
            print(f"[SKIP] ID {qid}: not in query file")
            continue
        if prompt not in criteria:
            print(f"[SKIP] ID {qid}: no criteria")
            continue
        if prompt not in references:
            print(f"[SKIP] ID {qid}: no reference article")
            continue

        # Find target article — try multiple naming conventions
        target_text = None
        for stem, text in targets.items():
            # Match by ID in filename (e.g., q58.md, q_58.md, 58.md)
            if str(qid) in stem:
                target_text = text
                break
        if target_text is None:
            # Try matching by first few words of prompt in filename
            key_words = prompt[:20].replace(" ", "_")
            for stem, text in targets.items():
                if key_words.lower() in stem.lower():
                    target_text = text
                    break
        if target_text is None:
            print(f"[SKIP] ID {qid}: no target article found in {args.target_dir}")
            results.append({"id": qid, "error": "no_target_article"})
            continue

        ref_text = references[prompt]
        crit_data = criteria[prompt]
        language = "zh" if any('\u4e00' <= c <= '\u9fff' for c in prompt[:50]) else "en"

        print(f"\n{'='*60}")
        print(f"Evaluating ID {qid} ({language}): {prompt[:60]}...")
        print(f"Target: {len(target_text)} chars | Reference: {len(ref_text)} chars")

        # Build and call judge
        criteria_list = format_criteria_list(crit_data)
        score_prompt = build_score_prompt(prompt, target_text, ref_text, criteria_list, language)

        t0 = time.time()
        try:
            if args.judge == "local":
                raw = call_local_judge(score_prompt, args.judge_url, args.judge_model)
            else:
                raw = call_openrouter_judge(score_prompt, args.openrouter_key, args.openrouter_model)
        except Exception as e:
            print(f"  JUDGE ERROR: {e}")
            results.append({"id": qid, "error": f"judge_failed: {e}"})
            continue

        elapsed = time.time() - t0
        print(f"  Judge response: {len(raw)} chars in {elapsed:.1f}s")

        # Extract JSON
        try:
            scores_json = extract_json_from_markdown(raw)
        except Exception as e:
            print(f"  JSON EXTRACTION FAILED: {e}")
            print(f"  Raw response head: {raw[:500]}")
            results.append({"id": qid, "error": "json_extraction_failed", "raw_head": raw[:500]})
            continue

        # Calculate weighted scores
        try:
            weighted = calculate_weighted_scores(scores_json, crit_data, language)
        except Exception as e:
            print(f"  SCORE CALCULATION FAILED: {e}")
            results.append({"id": qid, "error": f"score_calc_failed: {e}"})
            continue

        target_total = weighted["target"]["total"]
        ref_total = weighted["reference"]["total"]
        margin = target_total - ref_total

        print(f"  TARGET: {target_total:.3f} | REFERENCE: {ref_total:.3f} | MARGIN: {margin:+.3f}")
        for dim, val in weighted["target"]["dims"].items():
            print(f"    {dim}: {val:.3f}")

        results.append({
            "id": qid,
            "prompt": prompt[:80],
            "target_total": round(target_total, 4),
            "reference_total": round(ref_total, 4),
            "margin": round(margin, 4),
            "target_dims": {k: round(v, 4) for k, v in weighted["target"]["dims"].items()},
            "ref_dims": {k: round(v, 4) for k, v in weighted["reference"]["dims"].items()},
            "judge": args.judge_model,
            "judge_type": args.judge,
            "elapsed_s": round(elapsed, 1),
        })

    # Summary
    valid = [r for r in results if "target_total" in r]
    wins = sum(1 for r in valid if r["margin"] > 0)
    losses = sum(1 for r in valid if r["margin"] < 0)
    ties = len(valid) - wins - losses
    avg_margin = sum(r["margin"] for r in valid) / len(valid) if valid else 0

    print(f"\n{'='*60}")
    print(f"SUMMARY ({args.judge_model}, {args.judge})")
    print(f"  Valid: {len(valid)}/{len(results)}")
    print(f"  Wins: {wins} | Losses: {losses} | Ties: {ties}")
    print(f"  Avg margin: {avg_margin:+.4f}")
    for r in valid:
        status = "WIN" if r["margin"] > 0 else ("LOSS" if r["margin"] < 0 else "TIE")
        print(f"  ID {r['id']:3d} [{status}] target={r['target_total']:.3f} ref={r['reference_total']:.3f} margin={r['margin']:+.3f}")

    # Save
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump({
            "judge_model": args.judge_model,
            "judge_type": args.judge,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "results": results,
            "summary": {
                "valid": len(valid),
                "wins": wins,
                "losses": losses,
                "ties": ties,
                "avg_margin": round(avg_margin, 4),
            },
        }, f, indent=2, ensure_ascii=False)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()