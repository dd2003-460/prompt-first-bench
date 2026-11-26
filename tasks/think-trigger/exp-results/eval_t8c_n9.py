#!/usr/bin/env python3
# origin: ai
# T8c n=9 三判据评估（预注册 §3 W1+W2+W3 + §4 Stage 1 判决映射，判据冻结 commit 8c168c2a4）
# 用法: python3 eval_t8c_n9.py [raw_outputs_t8c.json] [输出路径，默认 t8c-n9-eval.json]
#       python3 eval_t8c_n9.py --selftest   # 合成 18 行数据 3 场景自测（不碰真实数据）
# 口径全部复用 eval_t8c_smoke.py（同目录）：
#   - evaluate() 返回 18 行（9/臂）：arm∈{"A'","B'"}, run, label, s, depth, truncated, ...
#   - 截断样本：s=0、depth=None、不进三型分布比较（预注册 §1）
#   - W1（方向）: mean(s_B') > mean(s_A')，strict，只用非截断行
#   - W2（显著）: 2×2 表（断点/无断点 × 臂）双侧 Fisher exact p < 0.05；
#     95%CI = 比例差正常近似（Wald+CC），W2 不过时随 decision 报告
#   - W3（结构）: mean(d_B') > mean(d_A')，strict；d=None 的行剔除，
#     某臂无有效 d → W3 不可判（按不过处理，decision 如实标注）
# 判决映射（预注册 L155-160，优先级从高到低）：
#   W1 不过            → 'H1 不成立（W1 方向不满足）'
#   W1 过 W3 不过      → '结构未赢（W3 不满足）'
#   W1 过 W2 过 W3 过  → 'H1 成立（三判据全过，claim 限定 27b+本题面+73728 预算）'
#   W1 过 W2 不过 W3 过→ '方向性证据，检验力不足（W2 不满足，报观测 p 与 95%CI）'
import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "../../../modules/B-pipeline-ablation/research"))
from eval_t8c_smoke import evaluate
from scipy import stats

PREREG = "t8c-preregistration.md (8c168c2a4) §3"
ALPHA = 0.05


def _valid(rows, arm):
    """非截断行（预注册 §1：截断样本不进三型分布比较）"""
    return [r for r in rows if r["arm"] == arm and not r["truncated"]]


def _depths(rows, arm):
    """有效 d（None 剔除：截断行 + 复合/未知标签行）"""
    return [r["depth"] for r in _valid(rows, arm) if r["depth"] is not None]


def prop_diff_ci(rows, arm_x, arm_y, alpha=ALPHA):
    """比例差 mean(s_x)-mean(s_y) 的 95%CI（Wald + 连续性校正，双侧）"""
    xs = [r["s"] for r in _valid(rows, arm_x)]
    ys = [r["s"] for r in _valid(rows, arm_y)]
    nx, ny = len(xs), len(ys)
    if not nx or not ny:
        return None, None
    px, py = sum(xs) / nx, sum(ys) / ny
    diff = px - py
    se = (px * (1 - px) / nx + py * (1 - py) / ny) ** 0.5
    z = stats.norm.ppf(1 - alpha / 2)
    cc = z / 2 * (1 / nx + 1 / ny)
    return diff, [diff - z * se - cc, diff + z * se + cc]


def evaluate_w123(rows):
    va, vb = _valid(rows, "A'"), _valid(rows, "B'")
    n_per_arm = {"A": len(va), "B": len(vb)}
    if not va or not vb:
        return {"input": None, "n_per_arm": n_per_arm,
                "w1": {"pass": False, "mean_s_a": None, "mean_s_b": None},
                "w2": {"pass": False, "p": None, "table": None, "ci95_diff_s": None},
                "w3": {"pass": False, "indeterminate": True,
                       "mean_d_a": None, "mean_d_b": None},
                "decision": "不可判（有效样本不足）", "prereg": PREREG}
    # W1 方向（strict）
    sa = sum(r["s"] for r in va) / len(va)
    sb = sum(r["s"] for r in vb) / len(vb)
    w1 = sb > sa
    # W2 双侧 Fisher exact：表 [[n_A_break, n_A_nobreak],[n_B_break, n_B_nobreak]]，break=(s==0)
    ab = sum(1 for r in va if r["s"] == 0)
    bb = sum(1 for r in vb if r["s"] == 0)
    table = [[ab, len(va) - ab], [bb, len(vb) - bb]]
    _, p = stats.fisher_exact(table, alternative="two-sided")
    w2 = p < ALPHA
    ci_diff, ci_lo_hi = prop_diff_ci(rows, "B'", "A'")
    # W3 结构深度（strict；d=None 剔除；某臂无有效 d → 不可判）
    da = _depths(rows, "A'")
    db = _depths(rows, "B'")
    if not da or not db:
        w3_pass, w3_indet = False, True
        mda = mdb = None
    else:
        mda, mdb = sum(da) / len(da), sum(db) / len(db)
        w3_pass, w3_indet = mdb > mda, False
    # 判决映射（优先级：W1 不过 > W3 不过 > 三过 > W2 不过）
    if not w1:
        decision = "H1 不成立（W1 方向不满足）"
    elif not w3_pass:
        decision = "结构未赢（W3 不满足）" + ("，W3 不可判" if w3_indet else "")
    elif w1 and w2 and w3_pass:
        decision = "H1 成立（三判据全过，claim 限定 27b+本题面+73728 预算）"
    else:
        decision = "方向性证据，检验力不足（W2 不满足，报观测 p 与 95%CI）"
    return {"input": None, "n_per_arm": n_per_arm,
            "w1": {"pass": w1, "mean_s_a": sa, "mean_s_b": sb},
            "w2": {"pass": w2, "p": p, "table": table,
                   "ci95_diff_s": [ci_diff, ci_lo_hi]},
            "w3": {"pass": w3_pass, "indeterminate": w3_indet,
                   "mean_d_a": mda, "mean_d_b": mdb},
            "decision": decision, "prereg": PREREG}


def make_row(arm, run, label, truncated=False):
    """合成行（结构与 evaluate() 输出一致；depth 按 smoke DEPTH 口径）。
    截断是独立标志（finish_reason=length），与非截断 indeterminate（s=1,d=4）区分。"""
    from eval_t8c_smoke import DEPTH
    if truncated:
        s, depth = 0, None
    else:
        s = 1 if label == "indeterminate" else 0
        depth = DEPTH.get(label)
    return {"arm": arm, "run": run, "label": label, "s": s, "depth": depth,
            "truncated": truncated, "note": "", "completion_tokens": 0,
            "finish": "stop", "repeat5_max": 0}


def _f(x, spec=".3f"):
    return format(x, spec) if isinstance(x, float) else str(x)


def selftest():
    """合成 18 行（9/臂）3 场景；断言 decision 符合预注册映射，FAIL 则退出码 1"""
    def mk(arm, labels):
        return [make_row(arm, i + 1, lab) for i, lab in enumerate(labels)]
    scenarios = [
        ("①三判据全过（A' 全 A1、B' 全 indeterminate）",
         mk("A'", ["A1"] * 9) + mk("B'", ["indeterminate"] * 9),
         "H1 成立（三判据全过，claim 限定 27b+本题面+73728 预算）"),
        ("②W1 过 W2 不过（A' 2 断点、B' 1 断点，p≥0.05；W3 亦过）",
         mk("A'", ["A3", "A3"] + ["indeterminate"] * 7)
         + mk("B'", ["A3"] + ["indeterminate"] * 8),
         "方向性证据，检验力不足（W2 不满足，报观测 p 与 95%CI）"),
        ("③W3 不过（方向正但 B' 断点分布更浅：s_B>s_A 且 d_B<d_A；"
         "注：B' 断点更深与 W1 过在数学上不可共存——indeterminate d=4 最深，"
         "故 W3 负只能靠 B' 断点更浅(A1) vs A' 断点更深(A3) 构造）",
         mk("A'", ["A3"] * 3 + ["indeterminate"] * 6)
         + mk("B'", ["A1"] * 2 + ["indeterminate"] * 7),
         "结构未赢（W3 不满足）"),
    ]
    fails = 0
    for name, rows, expected in scenarios:
        out = evaluate_w123(rows)
        ok = out["decision"] == expected
        fails += (not ok)
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        print(f"      W1: s_A={_f(out['w1']['mean_s_a'])} s_B={_f(out['w1']['mean_s_b'])} pass={out['w1']['pass']}")
        ci = out["w2"]["ci95_diff_s"]
        cis = f"[{round(ci[1][0],3)}, {round(ci[1][1],3)}]" if ci else "NA"
        print(f"      W2: table={out['w2']['table']} p={_f(out['w2']['p'],'.4f')} pass={out['w2']['pass']} ci95(diff s_B'-s_A')={cis}")
        print(f"      W3: d_A={out['w3']['mean_d_a']} d_B={out['w3']['mean_d_b']} pass={out['w3']['pass']}")
        print(f"      decision: {out['decision']}")
        if not ok:
            print(f"      expected: {expected}")
    print(f"\n自测结果: {'3/3 PASS' if fails == 0 else f'{fails} FAIL'}")
    return 0 if fails == 0 else 1


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--selftest":
        sys.exit(selftest())
    base = os.path.dirname(os.path.abspath(__file__))
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(base, "raw_outputs_t8c.json")
    outpath = sys.argv[2] if len(sys.argv) > 2 else os.path.join(base, "t8c-n9-eval.json")
    data = json.load(open(path))
    rows = evaluate(data)
    out = evaluate_w123(rows)
    out["input"] = path
    json.dump(out, open(outpath, "w"), ensure_ascii=False, indent=2)
    print(f"{'臂':<3}{'run':<5}{'label':<18}{'s':<3}{'d':<4}{'trunc':<6}")
    for r in rows:
        print(f"{r['arm']:<3}{str(r['run']):<5}{r['label']:<18}{r['s']:<3}"
              f"{str(r['depth']):<4}{str(r['truncated']):<6}")
    print(f"\n有效样本: A'={out['n_per_arm']['A']}  B'={out['n_per_arm']['B']}")
    print(f"W1: s_A={_f(out['w1']['mean_s_a'])} s_B={_f(out['w1']['mean_s_b'])} pass={out['w1']['pass']}")
    ci = out["w2"]["ci95_diff_s"]
    cis = f"[{round(ci[1][0],3)}, {round(ci[1][1],3)}]" if ci else "NA"
    print(f"W2: table={out['w2']['table']} p={_f(out['w2']['p'],'.4f')} pass={out['w2']['pass']} ci95={cis}")
    print(f"W3: d_A={out['w3']['mean_d_a']} d_B={out['w3']['mean_d_b']} pass={out['w3']['pass']}")
    print(f"判决: {out['decision']}")
    print(f"输出: {outpath}")
    sys.exit(0)


if __name__ == "__main__":
    main()
