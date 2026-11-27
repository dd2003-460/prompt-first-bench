#!/usr/bin/env python3
"""gen: score a single run file with the v3 judge (score.score_run) → runs-r293/scores-*.json.

用法:
    python3 score_single.py runs-r293/S8G-Q1-r1.json --out-name scores-S8G-Q1-r1.json
    python3 score_single.py runs-r293/S7V-Q4-r1.json   # out name derived from run tag

复用 score.py 的 v3 judge (M1/M4 LLM judge, conf_cap=0.7; M2/M3/M5 gates; M6 URL check)。
gold 路径来自 ablation_harness.QUESTIONS[qid]["gold_file"]。
"""
import argparse, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ablation_harness import QUESTIONS
from score import score_run


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_path", help="path to run JSON (e.g. runs-r293/S8G-Q1-r1.json)")
    ap.add_argument("--out-name", default=None, help="output filename in runs-r293/ (default: scores-<tag>.json)")
    args = ap.parse_args()

    path = args.run_path if os.path.isabs(args.run_path) else os.path.join(HERE, args.run_path)
    with open(path) as f:
        run = json.load(f)
    arm, qid, rep = run["arm"], run["qid"], run["rep"]
    if qid not in QUESTIONS:
        sys.exit(f"unknown qid {qid}")
    gold_path = QUESTIONS[qid]["gold_file"]
    if not os.path.exists(gold_path):
        sys.exit(f"gold not found: {gold_path}")
    gold_md = open(gold_path).read()

    # 重试整个评分直到成功（judge 偶发超时/网络抖动时 M1/M4 会记为 0，需重跑）
    for attempt in range(1, 4):
        print(f"scoring {os.path.basename(path)} ({arm}/{qid}/r{rep}) ... attempt {attempt}", flush=True)
        sc = score_run(path, gold_md, arm, qid, multi_n=1)
        failed = [n for n in sc.get("notes", []) if "judge failed" in n]
        if not failed:
            break
        print(f"  judge failure(s) detected: {failed}, retrying...", file=sys.stderr)
    print(json.dumps({k: sc[k] for k in ("scores", "total", "boundary_violation")}, ensure_ascii=False), flush=True)

    out_name = args.out_name or f"scores-{arm}-{qid}-r{rep}.json"
    out_dir = os.path.join(HERE, "runs-r293")
    out_path = os.path.join(out_dir, out_name)
    with open(out_path, "w") as f:
        json.dump(sc, f, ensure_ascii=False, indent=2)
    print(f"saved → {out_path}", flush=True)


if __name__ == "__main__":
    main()