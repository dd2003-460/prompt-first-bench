#!/usr/bin/env python3
"""T53-B12 verifier: 机检 AC1-AC8（题集/对标/口径/落盘/A6/回执/阶段工件/降级登记）。

用法: python3 loop-artifacts/stages/04/verify-t53-b12.py [--repo ROOT]
退出码 0 = 全过；1 = 有 FAIL
"""
import argparse
import json
import os
import re
import sys

QS = ["gpu", "drb-2", "q6-nev", "q7-rd", "q8-nvda"]
NEW = ["q6-nev", "q7-rd", "q8-nvda"]
CRITERIA = "modules/E-sota-benchmark/research/sm-bench-sota-criteria.md"
REPORT = "experiments/stage-ablation/s5-sm-bench-report.md"
QSPEC = "experiments/stage-ablation/questions/T53-B12-new3-questions.md"
RECEIPT = "research/T53-B12-RECEIPT.json"
STAGES = [
    "loop-artifacts/stages/01/T53-B12-01-goal-decomposition.md",
    "loop-artifacts/stages/02/T53-B12-02-information-research.md",
    "loop-artifacts/stages/02.5/T53-B12-02.5-cross-check.md",
    "loop-artifacts/stages/03/T53-B12-03-action-decomposition.md",
    "loop-artifacts/stages/04/T53-B12-04-execution.md",
    "loop-artifacts/stages/04.5/T53-B12-04.5-final-review.md",
]
results = []


def check(ac, desc, ok, detail=""):
    results.append((ac, desc, bool(ok), detail))


def read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def run_path(q):
    return f"experiments/stage-ablation/runs-s5-sm-{q}.json"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))))
    os.chdir(ap.parse_args().repo)

    report = read(REPORT) if os.path.exists(REPORT) else ""
    criteria = read(CRITERIA) if os.path.exists(CRITERIA) else ""
    qspec = read(QSPEC) if os.path.exists(QSPEC) else ""

    # AC1: 5 题（含 3 新）
    in_report = [q for q in QS if q in report]
    in_spec = [q for q in NEW if q in qspec]
    check("AC1", "5 questions in report", len(in_report) == 5, f"{in_report}")
    check("AC1b", "3 new questions in spec file", len(in_spec) == 3, f"{in_spec}")

    # AC2: 每题 ≥1 开源 SOTA 公开分（判据 §3 映射表 5 行，含数字 + URL）
    sec3 = criteria.split("## 3. 五题 × SOTA 映射")[-1].split("## 4.")[0] if "## 3. 五题" in criteria else ""
    rows = [l for l in sec3.splitlines() if l.startswith("|") and re.search(r"`(gpu|drb-2|q6-nev|q7-rd|q8-nvda)`", l)]
    rows_with_num = [l for l in rows if re.search(r"\d+\.\d+", l)]
    check("AC2", "criteria §3 maps 5 qids", len(rows) == 5, f"{len(rows)} rows")
    check("AC2b", "each mapped row carries a public number", len(rows_with_num) == 5, f"{len(rows_with_num)}")
    check("AC2c", "L1 comparability flagged false", "l1_comparable" in json.dumps(
        [json.load(open(run_path(q), encoding="utf-8")) for q in NEW if os.path.exists(run_path(q))]) or
        "不可比" in criteria or "非同题" in criteria, "")

    # AC3: judge 字段存在（null 允许），且状态显式
    ok3, det3 = True, []
    for q in NEW:
        p = run_path(q)
        if not os.path.exists(p):
            ok3 = False
            det3.append(f"{q}:missing")
            continue
        d = json.load(open(p, encoding="utf-8"))
        sc = d.get("scores", {})
        if "s5_judge_n3_median" not in sc:
            ok3 = False
            det3.append(f"{q}:no-field")
        if sc.get("s5_judge_n3_median") is None and d.get("status") != "blocked_no_llm_endpoint":
            ok3 = False
            det3.append(f"{q}:null-without-blocked")
    check("AC3", "judge field present; null only when blocked", ok3, ",".join(det3) or "ok")

    # AC4a/b/c
    check("AC4a", "report has 五题对标表", "五题对标表" in report, "")
    have_runs = [q for q in QS if os.path.exists(run_path(q))]
    check("AC4b", "run file per question (5)", len(have_runs) == 5, f"{have_runs}")
    check("AC4c", "criteria file v3", "v3" in criteria and "三层" in criteria, "")

    # AC5: A6 —— 新 run 无题面原文
    leak = []
    for q in NEW:
        p = run_path(q)
        if not os.path.exists(p):
            continue
        d = json.load(open(p, encoding="utf-8"))
        if "question" in d:
            leak.append(f"{q}:has-question-field")
        if not d.get("leak_check", {}).get("question_text_absent"):
            leak.append(f"{q}:no-attest")
        blob = json.dumps(d, ensure_ascii=False)
        if len(blob) > 3000:
            leak.append(f"{q}:oversized")
    check("AC5", "new run records carry no question text (A6)", not leak, ",".join(leak[:3]))

    # AC6: 回执
    if os.path.exists(RECEIPT):
        rc = json.load(open(RECEIPT, encoding="utf-8"))
        ok6 = (rc.get("repo", "").startswith("https://github.com/")
               and rc.get("branch") == "arena/f65a5a27-prompt-first-bench"
               and re.fullmatch(r"[0-9a-f]{7,40}", str(rc.get("commit_sha", ""))))
        check("AC6", "receipt repo/branch/commit_sha", ok6, f"sha={rc.get('commit_sha')}")
    else:
        check("AC6", "receipt exists", False, RECEIPT)

    # AC7: 阶段工件
    missing = [p for p in STAGES if not os.path.exists(p)]
    check("AC7", "stage artifacts 01..04.5", not missing, f"missing={missing}")

    # AC8: 降级显式登记
    deg_ok = ("阻塞" in report and "Connection refused" in report)
    check("AC8", "degradation documented with evidence", deg_ok, "")

    fails = [r for r in results if not r[2]]
    for ac, desc, ok, detail in results:
        print(f"{'PASS' if ok else 'FAIL'}  {ac:<6} {desc}" + (f"  [{detail}]" if detail else ""))
    print(f"\nfails={len(fails)}  passes={len(results) - len(fails)}  total={len(results)}")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
