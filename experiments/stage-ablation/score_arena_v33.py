#!/usr/bin/env python3
"""Score arena execution logs with v3.3 judge (methodology-type: public facts)."""
import json, re, sys, os
sys.path.insert(0, '.')
from score import detect_gold_type, judge_m1, score_run

def extract_execution_log(path):
    """Read an arena execution log markdown file."""
    with open(path) as f:
        return f.read()

def score_arena_file(log_path, gold_path, output_json_path):
    """Score a single arena run and save results."""
    output = extract_execution_log(log_path)
    gold = open(gold_path).read()
    
    gt = detect_gold_type(gold)
    print(f"  Gold type: {gt}")
    print(f"  Output length: {len(output)} chars")
    
    m, t, note = judge_m1(output[:12000], gold)
    m1 = m/t if t > 0 else 0
    print(f"  M1: {m}/{t} = {m1:.3f}")
    print(f"  Note: {note[:200]}")
    
    result = {
        "source": log_path,
        "gold": gold_path,
        "gold_type": gt,
        "M1": round(m1, 4),
        "M1_matched": m,
        "M1_total_decidable": t,
        "M1_note": note[:500],
    }
    with open(output_json_path, 'w') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"  Saved: {output_json_path}")
    return result

if __name__ == "__main__":
    # Usage: score_arena_v33.py <log.md> <gold.md> <output.json>
    if len(sys.argv) != 4:
        print("Usage: score_arena_v33.py <execution-log.md> <gold/Q*.md> <output.json>")
        sys.exit(1)
    score_arena_file(sys.argv[1], sys.argv[2], sys.argv[3])
