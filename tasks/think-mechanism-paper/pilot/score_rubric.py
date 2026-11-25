#!/usr/bin/env python3
"""TASK-T4b mechanical rubric scorer. 0/1 per run, keyword/structure existence only.
Bilingual matching (model may answer in Chinese). Writes scores.json (supplementary,
for results.md generation); does NOT modify runs.json."""
import json, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
RUNS_JSON = os.path.join(BASE, "runs.json")
SCORES_JSON = os.path.join(BASE, "scores.json")

# Flag words (extra recording, not scored)
FLAG_WORDS = ["needs measurement", "cheapest probe", "special case",
              "需要测量", "最便宜的探针", "特例"]

def norm(t):
    return (t or "").lower()

def has_any(t, patterns):
    tl = norm(t)
    return any(re.search(p, tl) for p in patterns)

# ---------- per-template mechanical checks ----------
# Each check: (name, regex list). All required checks must hit for score=1
# (per rubric: 三项全有 / 两项全有 / 二选一).

def check_T1(t):
    """cost model (formula/itemized cost list) + premises statement + special-case verification sentence"""
    cost = has_any(t, [r"o\(log", r"log\s*n", r"cost model", r"代价模型", r"时间复杂度",
                       r"comparisons", r"比较次数", r"itemized", r"逐项"])
    premises = has_any(t, [r"premises?\b", r"assumptions?\b", r"assumes?\b", r"前提",
                           r"假设", r"holds when", r"under the (assumption|premise)"])
    special = has_any(t, [r"special case", r"特例", r"degenerat", r"退化",
                          r"instance of", r"reduces to"])
    return {"cost_model": cost, "premises": premises, "special_case": special}, \
           [cost, premises, special]

def check_T2(t):
    """single formula/analogy covering >=2 methods + degeneration conditions per method"""
    unified = has_any(t, [r"unified", r"single formula", r"one formula", r"common (form|framework|view|analogy)",
                          r"统一", r"统一公式", r"共同", r"covers? (all|both|the three)",
                          r"gradient", r"information gain", r"channel"])
    # need at least two method names present (coverage evidence)
    methods = sum(1 for m in [r"gradient descent", r"newton", r"evolutionar",
                              r"梯度下降", r"牛顿", r"进化策略"] if re.search(m, norm(t)))
    unified = unified and methods >= 2
    degeneracy = has_any(t, [r"degenerat", r"退化", r"reduces? (to|into)", r"collapses?",
                             r"fails? when", r"breaks? when", r"失效", r"退化为"])
    return {"unified_formula": unified, "degeneration_conditions": degeneracy}, \
           [unified, degeneracy]

def check_T3(t):
    """testable number (unit-bearing number/formula/expected value) OR explicit 'needs measurement' + cheapest probe design"""
    quant = has_any(t, [r"\d+(\.\d+)?\s*(percent|%|accuracy|bits|samples|epochs|params|parameters)",
                        r"accuracy\s*(of|improves?|rises?)", r"power\s*=", r"n\s*=\s*\d+",
                        r"success rate", r"success-rate", r"期望", r"样本量", r"准确率",
                        r"formula", r"公式", r"expected number", r"预期"])
    needs_meas = has_any(t, [r"needs measurement", r"需要测量", r"cannot be quantified without",
                             r"无法量化", r"requires (measuring|empirical)"])
    probe = has_any(t, [r"cheapest probe", r"probe", r"最便宜", r"探针", r"minimal experiment",
                        r"smallest experiment", r"cheap(est)? (experiment|test|measurement)",
                        r"pilot study", r"小规模实验", r"最小实验"])
    branch_a = quant
    branch_b = needs_meas and probe
    return {"quantitative_number": quant, "needs_measurement": needs_meas,
            "probe_design": probe}, [branch_a, branch_b]

def check_T4(t):
    """dimension-by-dimension condition-gap check (>=3 dims listed) + borrow/don't-borrow conclusion"""
    dim_markers = len(re.findall(r"dimension|dim\b|维度|方面|facet|aspect", norm(t)))
    numbered_dims = len(re.findall(r"^\s*(\d+[\.\)、]|[-•*])\s", t, re.M))
    dims_ok = dim_markers >= 3 or numbered_dims >= 3
    conclusion = has_any(t, [r"do not borrow", r"should not (borrow|accept)", r"reject",
                             r"不(应|宜|可)(借用|采纳|接受)", r"不应借用", r"拒绝",
                             r"accept (with|this) (analogy|lesson)", r"can be borrowed",
                             r"可以借用", r"值得借鉴", r"conclusion", r"结论",
                             r"verdict", r"判定"])
    return {"dimensions_listed": dims_ok, "borrow_conclusion": conclusion}, \
           [dims_ok, conclusion]

def check_T5(t):
    """name which step lacks cheap ground truth + closing fix (synthetic domain / executable verification / pre-registration)"""
    step = has_any(t, [r"judge", r"评判", r"评审", r"evaluation step", r"verification step",
                       r"bottleneck", r"瓶颈", r"literature search", r"文献检索",
                       r"idea generation", r"idea 生成", r"experiment step", r"实验环节"])
    ground_truth = has_any(t, [r"ground truth", r"ground-truth", r"真值", r"groundtruth",
                               r"reliable (signal|feedback|criterion)", r"可靠(的)?(信号|判据|标准)"])
    closing = has_any(t, [r"synthetic", r"executable verification", r"pre-registr",
                          r"合成域", r"合成数据", r"可执行验证", r"预注册", r"closed world",
                          r"close the world", r"闭合", r"unit test", r"单元测试",
                          r"verifiable", r"可验证"])
    step_named = step and ground_truth
    return {"step_with_ground_truth_gap": step_named, "closing_fix": closing}, \
           [step_named, closing]

CHECKS = {"T1": check_T1, "T2": check_T2, "T3": check_T3, "T4": check_T4, "T5": check_T5}

def main():
    with open(RUNS_JSON) as f:
        runs = json.load(f)
    scores = []
    for r in runs:
        entry = {"run_id": r["run_id"], "prompt_id": r["prompt_id"],
                 "condition": r["condition"], "template": r["template"],
                 "status": r["status"], "score": None, "checks": {},
                 "flag_words": {}, "finish_reason": r["finish_reason"],
                 "completion_tokens": r["completion_tokens"]}
        if r["status"] == "ok" and r["full_text"]:
            t = r["full_text"]
            checks, required = CHECKS[r["template"]](t)
            entry["checks"] = checks
            entry["score"] = 1 if all(required) else 0
            entry["flag_words"] = {w: len(re.findall(re.escape(w), norm(t))) for w in FLAG_WORDS}
        scores.append(entry)
    with open(SCORES_JSON, "w") as f:
        json.dump(scores, f, ensure_ascii=False, indent=2)
    for e in scores:
        print(f"{e['run_id']}: status={e['status']} score={e['score']} checks={e['checks']}")

if __name__ == "__main__":
    main()
