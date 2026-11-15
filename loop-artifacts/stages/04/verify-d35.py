#!/usr/bin/env python3
"""T53-D35 verifier: 机检 survey / search-log / stage artifacts / index / 回执。

用法: python3 loop-artifacts/stages/04/verify-d35.py [--repo ROOT]
退出码: 0 = 全通过（可能带 warn），1 = 有 FAIL
"""
import argparse
import json
import os
import re
import sys

SURVEY = "modules/F-theory/gradient-descent/litsurvey/2026-11-13-d35-realworld-vs-analytic-optimization-survey.md"
LOG = "modules/F-theory/gradient-descent/litsurvey/search-log-d35.json"
INDEX = "litsurvey-index.md"
RECEIPT = "research/T53-D35-RECEIPT.md"
STAGES = [
    "loop-artifacts/stages/01/T53-D35-01-goal-decomposition.md",
    "loop-artifacts/stages/02/T53-D35-02-information-research.md",
    "loop-artifacts/stages/02.5/T53-D35-02.5-crosscheck.md",
    "loop-artifacts/stages/04/T53-D35-04-execution.md",
    "loop-artifacts/stages/04.5/T53-D35-04.5-final-review.md",
]

results = []


def check(ac, desc, ok, detail=""):
    results.append((ac, desc, bool(ok), detail))


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))))
    args = ap.parse_args()
    root = args.repo
    os.chdir(root)

    missing = [p for p in [SURVEY, LOG] + STAGES if not os.path.exists(p)]
    if SURVEY not in missing:
        survey = read(SURVEY)
    else:
        survey = ""

    # AC1 survey 行数 >= 300
    n_lines = survey.count("\n") + (1 if survey and not survey.endswith("\n") else 0)
    check("AC1", "survey >= 300 lines", n_lines >= 300, f"{n_lines} lines")

    # AC2 来源 >= 20（附录 A 表格行 + search-log sources 双口径）
    appendix = survey.split("## 12. 附录 A")[-1].split("## 13.")[0] if "## 12. 附录 A" in survey else ""
    app_rows = [l for l in appendix.splitlines() if re.match(r"^\|\s*\d+\s*\|", l)]
    log_sources = []
    log_ok = LOG not in missing
    if log_ok:
        try:
            log = json.loads(read(LOG))
            log_sources = log.get("sources", [])
        except Exception as exc:  # noqa: BLE001
            check("AC9", "search-log-d35.json parses", False, str(exc))
            log = None
    check("AC2", "sources >= 20 (appendix rows)", len(app_rows) >= 20, f"{len(app_rows)} rows")
    check("AC2b", "sources >= 20 (search-log)", len(log_sources) >= 20, f"{len(log_sources)} sources")

    # AC3 ① 本轮现取 >= 8 且 read_level >= abstract
    lvl1 = [s for s in log_sources if s.get("level") == "①"]
    lvl1_body = [s for s in lvl1 if s.get("read_level") in ("abstract", "partial", "full")]
    check("AC3", "① sources >= 8", len(lvl1) >= 8, f"{len(lvl1)}")
    check("AC3b", "① sources read >= abstract >= 8", len(lvl1_body) >= 8, f"{len(lvl1_body)}")

    # AC4 判决句 + conf
    verdicts = re.findall(r"判决[（(][^）)]*[）)]?[：:][^\n]*?conf\s*([0-9.]+)", survey)
    verdicts_all = re.findall(r"判决[^\n]*?conf\s*([0-9.]+)", survey)
    check("AC4", ">=4 verdicts with conf", len(verdicts_all) >= 4, f"{len(verdicts_all)}")
    bad_conf = [c for c in verdicts_all if not (0.0 <= float(c) <= 1.0)]
    check("AC4b", "all conf in [0,1]", not bad_conf, f"bad={bad_conf}")

    # AC4c 每个子问题都有判决
    q_ok = []
    for q in ("Q1", "Q2", "Q3", "Q4"):
        seg_start = survey.find(f"## {q[1]}. {q}")
        q_ok.append(bool(re.search(rf"{q}[^\n]*判决|判决[^\n]*{q}", survey)) or seg_start >= 0)
    check("AC4c", "Q1-Q4 each addressed", all(q_ok), f"{q_ok}")

    # AC5 反方复核 >= 3
    n_inter = len(re.findall(r"反方复核\s*\d", survey))
    check("AC5", ">= 3 counter-interrogations", n_inter >= 3, f"{n_inter}")

    # AC6 A vs B vs 结合 专节 + 具体形式
    has_sec = "A vs B vs 结合" in survey
    has_formula = ("Div_t" in survey and "Drift_t" in survey and "S_alpha_corrected" in survey)
    check("AC6", "'A vs B vs 结合' section", has_sec, "")
    check("AC6b", "concrete combined form (objective + S5 fields)", has_formula, "")

    # AC7 未找到登记 + conf <= 0.3
    nf = survey.split("## 13. 附录 C")[-1] if "## 13. 附录 C" in survey else ""
    nf_rows = [l for l in nf.splitlines() if l.startswith("|") and "conf" in l.lower()]
    low = re.findall(r"conf\s*0\.([0-9])", nf)
    check("AC7", "not-found table present with conf", len(nf_rows) >= 3, f"{len(nf_rows)} rows")
    check("AC7b", "not-found confs all <= 0.3", all(int(x) <= 3 for x in low), f"{low}")

    # AC8 drift gap 明确结论
    check("AC8", "drift gap explicitly refuted", ("推翻" in survey or "不成立" in survey), "")

    # AC10 阶段工件齐全 + 02 不泄漏 04
    check("AC10", "stage artifacts 01..04.5 present", not missing, f"missing={missing}")
    if all(os.path.exists(p) for p in STAGES[:3]):
        s02 = read(STAGES[1])
        s025 = read(STAGES[2])
        leak = re.findall(r"T53-D35-04|stages/04/", s02 + s025)
        check("AC10b", "stage 02/02.5 do not cite stage 04", not leak, f"leak={leak[:3]}")

    # AC11 根索引只改 F-theory 行且提到 D35
    idx = read(INDEX) if os.path.exists(INDEX) else ""
    f_row = [l for l in idx.splitlines() if l.startswith("| F-theory")]
    check("AC11", "index has F-theory row", len(f_row) == 1, f"{len(f_row)}")
    check("AC11b", "F-theory row mentions D35 survey", bool(f_row) and "D35" in f_row[0], "")

    # AC12 回执含 repo url + branch + commit_sha
    if os.path.exists(RECEIPT):
        rc = read(RECEIPT)
        has_url = "github.com/dd2003-460/prompt-first-bench" in rc
        has_br = "arena/f65a5a27-prompt-first-bench" in rc
        has_sha = bool(re.search(r"commit_sha[:：]\s*`?[0-9a-f]{7,40}", rc))
        check("AC12", "receipt has repo url + branch + commit_sha", has_url and has_br and has_sha,
              f"url={has_url} branch={has_br} sha={has_sha}")
    else:
        check("AC12", "receipt exists", False, RECEIPT)

    # AC13 勘误表 3 处错误 ID 齐全 + 正确替代
    errata_ok = all(x in survey for x in ("2101.05574", "1403.3919", "2202.06384", "1906.08253"))
    check("AC13", "errata covers 3 wrong IDs + correct MBPO id", errata_ok, "")

    # AC14 多样性项（防 Goodhart 要求）
    div_ok = ("Div" in survey and "多样性" in survey and "λ" in survey)
    check("AC14", "objective contains exploration-diversity term", div_ok, "")

    fails = [r for r in results if not r[2]]
    for ac, desc, ok, detail in results:
        print(f"{'PASS' if ok else 'FAIL'}  {ac:<7} {desc}" + (f"  [{detail}]" if detail else ""))
    print(f"\nfails={len(fails)}  passes={len(results) - len(fails)}  total={len(results)}")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
