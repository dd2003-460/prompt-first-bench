#!/usr/bin/env python3
"""Re-run P4 synthesis + judge from an existing node-tree JSON, without re-running the SM.

Usage: python3 synth_only.py <run_json> [qid_override]
  run_json: path to runs-s5-sm-{qid}.json (contains nodes + question)
  qid_override: optional, defaults to the qid field in run_json

Writes runs-s5-sm-{qid}-synth.json (same format as --synth flag).
"""
import json
import sys
import time
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from s5_state_machine import synthesize_answer, NodeRecord


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 synth_only.py <run_json> [qid_override]")
        sys.exit(1)

    run_path = sys.argv[1]
    with open(run_path) as f:
        d = json.load(f)

    qid = sys.argv[2] if len(sys.argv) > 2 else d.get("qid", "gpu")
    question = d["question"]
    nodes_raw = d["nodes"]

    print(f"[synth_only] Loaded {len(nodes_raw)} nodes from {run_path} (qid={qid})", flush=True)

    # Convert raw dicts to NodeRecord objects (synthesize_answer expects .level, .id, etc.)
    nodes = [NodeRecord(**n) for n in nodes_raw]

    t0 = time.time()
    s = synthesize_answer(question, nodes, qid)
    elapsed = time.time() - t0

    out_path = f"runs-s5-sm-{qid}-synth.json"
    with open(out_path, "w") as f:
        json.dump({
            "qid": qid,
            "n_nodes": len(nodes),
            "final_state": d.get("final_state"),
            "answer": s["answer"],
            "judge": s["judge"],
            "coverage": s["coverage"],
            "depth_score": s["depth"],
            "source_run": run_path,
            "synth_elapsed_s": round(elapsed, 1),
        }, f, ensure_ascii=False, indent=2)

    print(f"[synth_only] Saved → {out_path} | coverage={s['coverage']} depth={s['depth']} | {elapsed:.0f}s", flush=True)


if __name__ == "__main__":
    main()
