#!/usr/bin/env python3
"""q7 719 档 curve JSON 回填脚本 (2026-11-24, v2 含 fit 重估).

背景: q7-budget-response-curve.json 是手工维护的 (无自动重生成脚本)。
队列跑完每个 rep 会自动把分数 append 到 q7-scan-scores.json (q7_budget_scan_queue.sh L39-55),
watcher 也会自动跑 post-run 协议 + replication-check, 但都不碰 curve JSON。
所以 719 档 r3 落盘后, 需要把 curve JSON 的 719 行从 n=2 升到 n=3 —— 本脚本做这件事,
消除手工算术错误风险 (300-r2 复制污染正是手工口径错误的教训)。

v2 修正 (2026-11-24 23:4x 发现): curve JSON 不止 rows 一处依赖 719 ——
  fits (log_saturation / linear 的 5 点拟合)、marginal_gains、per_unit_efficiency、
  conclusion 文字里的 719 数值, 当初都在 r1 单点 (0.6635) 上算的, 719 行升到 n=2 (0.6539)
  后没跟着重估 → curve JSON 内部不一致 (行是 n=2, 拟合/结论文字还是 n=1)。
本脚本一并重估这些字段, 保证回填后整份 curve JSON 口径一致。

数据源 (权威):
  - q7-scan-scores.json : 每个 rep 的 judge.total / judge.depth / judge.cov / wall_s (队列自动 append)
  - q7-719-r*.json      : 每个 rep 的 run 文件, 用于 claim-set 去重 (排除字节级复制污染)
  - q7-budget-response-curve.json 自身的 50/100/150/300 行 (这些档不随 719 变, 直接取均值)

去重逻辑: 同一 budget 下, 两个 run 文件的 claim-set (节点 claim 集合 sha1) 相同 = 一个是另一个的
字节级复制 (如 300-r2 = 300-r1 复制), 剔除后者。719 档 r1/r2 已核验 SHA 独立, r3 落盘后应为第三
个独立 claim-set。

用法:
  python3 q7-curve-backfill-719.py            # dry-run: 只打印将写入的值, 不改文件
  python3 q7-curve-backfill-719.py --apply    # 实际写入 curve JSON

幂等: 可重复运行; 每次从 q7-scan-scores.json + run 文件重算 719 行 + 重估拟合, 结果一致。
拟合方法: OLS (log_saturation: jt = a + b*ln(budget); linear: jt = a + b*budget),
  已验证能精确复现当前 curve 里的拟合参数 (-0.1280/0.1219/0.9883), 方法无误。
conclusion 文字: 对 719 依赖的数值 token 做受保护替换 (只在找到旧值时才替换, 漏配则 WARN 让 Lead 人工核)。
"""
import glob, json, os, sys, math, hashlib, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
CURVE = os.path.join(HERE, "q7-budget-response-curve.json")
SCORES = os.path.join(HERE, "q7-scan-scores.json")
BUDGET = 719
OTHER_BUDGETS = [50, 100, 150, 300]


def claim_set(run_file):
    """节点 claim 集合 sha1 (与 watcher post-run 协议同口径)."""
    d = json.load(open(run_file))
    cs = hashlib.sha1("|".join(sorted(nd.get("claim", "")[:40] for nd in d["nodes"])).encode()).hexdigest()[:12]
    return cs, len(d["nodes"])


def ols(xs, ys):
    """简单 OLS, 返回 (intercept, slope, r2)."""
    n = len(xs)
    sx, sy = sum(xs), sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))
    slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    intercept = (sy - slope * sx) / n
    ybar = sy / n
    ss_res = sum((y - (intercept + slope * x)) ** 2 for x, y in zip(xs, ys))
    ss_tot = sum((y - ybar) ** 2 for y in ys)
    r2 = 1 - ss_res / ss_tot if ss_tot else float("nan")
    return intercept, slope, r2


def main():
    apply = "--apply" in sys.argv
    scores = json.load(open(SCORES))
    curve = json.load(open(CURVE))

    # ---- 719 行: 从 scores + run 文件重算 (claim-set 去重) ----
    by_rep = {rec.get("rep"): rec for rec in scores if rec.get("budget") == BUDGET}
    runs = sorted(glob.glob(os.path.join(HERE, f"q7-{BUDGET}-r*.json")))
    seen_cs, kept, dropped = {}, [], []
    for f in runs:
        base = os.path.basename(f)
        try:
            rep = int(base.split("-r")[1].split("-")[0])
        except (IndexError, ValueError):
            continue
        cs, n = claim_set(f)
        if cs in seen_cs:
            dropped.append((rep, base, seen_cs[cs])); continue
        seen_cs[cs] = base
        kept.append((rep, base, cs, n))

    reps_with_score = []
    for rep, base, cs, n in kept:
        rec = by_rep.get(rep)
        if rec is None:
            print(f"[warn] rep {rep} ({base}) 在 q7-scan-scores.json 无分数记录 — 跳过 (r3 落盘后队列会自动 append)")
            continue
        reps_with_score.append((rep, rec, base, n))
    if not reps_with_score:
        print("[abort] 719 档无可用 rep — 不写"); return

    jts = [r[1]["judge"]["total"] for r in reps_with_score]
    covs = [r[1]["judge"]["cov"] for r in reps_with_score]
    depths = [r[1]["judge"].get("depth") for r in reps_with_score if r[1]["judge"].get("depth") is not None]
    walls = [r[1]["wall_s"] for r in reps_with_score]
    n_reps = len(reps_with_score)
    new_jt = round(sum(jts) / n_reps, 4)
    new_cov = round(sum(covs) / n_reps, 4)

    new_row_vals = {
        "n_reps": n_reps,
        "judge_total_mean": new_jt,
        "judge_total_min": round(min(jts), 4),
        "judge_total_max": round(max(jts), 4),
        "cov_mean": new_cov,
    }
    if depths: new_row_vals["depth_mean"] = round(sum(depths) / len(depths), 3)
    if walls: new_row_vals["wall_s_mean"] = round(sum(walls) / len(walls))

    # ---- 其他档 jt 均值 (不随 719 变, 从 curve rows 直接取) ----
    jt_by_budget = {row["budget"]: row["judge_total_mean"] for row in curve["rows"]}
    all_budgets = OTHER_BUDGETS + [BUDGET]
    all_jt = [jt_by_budget[b] for b in OTHER_BUDGETS] + [new_jt]

    # ---- 重估 fits ----
    li, ls, lr2 = ols([math.log(b) for b in all_budgets], all_jt)
    xi, xs, xr2 = ols(all_budgets, all_jt)
    new_fits = {
        "log_saturation": {
            "formula": "jt = intercept + slope*ln(budget)",
            "intercept": round(li, 4), "slope": round(ls, 4), "r2": round(lr2, 4), "n_pts": len(all_budgets),
            "pred_note": f"719 实测 {new_jt} 残差 {new_jt - (li + ls * math.log(BUDGET)):+.3f}, 拟合内",
        },
        "linear": {
            "formula": "jt = intercept + slope*budget",
            "intercept": round(xi, 4), "slope": round(xs, 6), "r2": round(xr2, 4), "n_pts": len(all_budgets),
        },
    }

    # ---- 重估 marginal_gains + per_unit_efficiency 的 300->719 ----
    jt_300 = jt_by_budget[300]
    new_marg = round(new_jt - jt_300, 4)
    new_pue = round((new_jt - jt_300) / (BUDGET - 300), 6)
    new_lin_pred = round(xi + xs * BUDGET, 2)

    # ---- conclusion 文字的 719 依赖 token (受保护替换: 只在找到旧值时替换) ----
    # 旧值取自当前 curve (可能是 n=1 或 n=2 时代), 新值按 new_jt 重算。
    old_fits = curve.get("fits", {})
    old_log = old_fits.get("log_saturation", {})
    old_li, old_ls = old_log.get("intercept"), old_log.get("slope")
    old_jt_719 = next((r["judge_total_mean"] for r in curve["rows"] if r.get("budget") == BUDGET), None)
    old_res = round(old_jt_719 - (old_li + old_ls * math.log(BUDGET)), 3) if None not in (old_jt_719, old_li, old_ls) else None
    old_r2_5pt = old_log.get("r2")
    old_pue_300_719 = curve.get("per_unit_efficiency", {}).get("300->719")
    old_marg_txt = None  # 结论文字里的 "+0.079" 来自 n=1 时代 (0.6635-0.5846), 单独处理
    old_lin_pred_txt = None

    # 结论文字里已知 719 依赖 token 的候选旧值 (按当前 curve 实际值优先, 否则用 n=1 时代已知值)
    cand_old_jt = [old_jt_719, 0.6635]
    cand_old_res = [old_res, -0.032]
    cand_old_r2 = [old_r2_5pt, 0.988]
    cand_old_pue = [old_pue_300_719, 0.00019]
    cand_old_marg = [round(old_jt_719 - jt_300, 3), 0.079]
    cand_old_linpred = [0.98]

    conclusion = curve.get("conclusion", "")
    repl = [
        (f"719 实测点 ({c})", f"719 实测点 ({new_jt})") for c in cand_old_jt
    ] + [
        (f"残差 {c:+.3f}".replace("+", "").replace("-", "-"), f"残差 {new_jt - (li + ls * math.log(BUDGET)):+.3f}".replace("+", "")) for c in cand_old_res
    ] + [
        (f"R^2={c}", f"R^2={round(lr2, 3)}") for c in cand_old_r2
    ] + [
        (f"300→719={c}", f"300→719={new_pue:.5f}") for c in cand_old_pue
    ] + [
        (f"只 +{c}", f"只 +{new_marg:.3f}") for c in cand_old_marg
    ] + [
        (f"pred 719≈{c}", f"pred 719≈{new_lin_pred}") for c in cand_old_linpred
    ] + [
        (f"719 档当前 n={c}", f"719 档当前 n={n_reps} (已回填)") for c in [1, 2]
    ]
    new_conclusion, missed = conclusion, []
    for old, new in repl:
        if old in new_conclusion:
            new_conclusion = new_conclusion.replace(old, new, 1)
        # 不在此处判 missed (同一语义可能有多个候选旧值, 命中其一即可)
    # 判断每个语义是否至少命中一个候选
    sem_groups = {
        "jt 实测点": [f"719 实测点 ({c})" for c in cand_old_jt],
        "residual": [f"残差 {c:+.3f}".replace("+", "").replace("-", "-") for c in cand_old_res],
        "r2": [f"R^2={c}" for c in cand_old_r2],
        "pue": [f"300→719={c}" for c in cand_old_pue],
        "marg": [f"只 +{c}" for c in cand_old_marg],
        "linpred": [f"pred 719≈{c}" for c in cand_old_linpred],
        "n": [f"719 档当前 n={c}" for c in [1, 2]],
    }
    for sem, olds in sem_groups.items():
        if not any(o in conclusion for o in olds):
            missed.append(sem)

    # ---- 打印 ----
    print(f"=== 719 档回填 (dry-run={'NO' if apply else 'YES'}) ===")
    print(f"独立 rep: {[(r[0], 'n='+str(r[3])) for r in reps_with_score]}")
    if dropped: print(f"剔除复制: {[(r[0], 'cs 同 '+r[2]) for r in dropped]}")
    print(f"719 行: jt {new_jt} (min {round(min(jts),4)}/max {round(max(jts),4)}), cov {new_cov}, n={n_reps}")
    print(f"  逐 rep judge.total={[round(x,4) for x in jts]}, cov={[round(x,4) for x in covs]}")
    print(f"fits.log_saturation: intercept={round(li,4)} slope={round(ls,4)} r2={round(lr2,4)} (719 残差 {new_jt-(li+ls*math.log(BUDGET)):+.3f})")
    print(f"fits.linear:        intercept={round(xi,4)} slope={round(xs,6)} r2={round(xr2,4)} (pred 719≈{new_lin_pred})")
    print(f"marginal 300->719 = {new_marg}; per_unit 300->719 = {new_pue}")
    if missed:
        print(f"[WARN] conclusion 文字以下语义未找到旧 token, 未自动替换, 请 Lead 人工核: {missed}")
    else:
        print("conclusion 文字: 719 依赖 token 全部命中并替换")

    if not apply:
        print("\n[dry-run] 未写文件。确认后加 --apply 写入。")
        return

    # ---- 应用 ----
    for row in curve["rows"]:
        if row.get("budget") == BUDGET:
            row.update(new_row_vals)
            row["note"] = (
                f"n={n_reps} 独立 rep (claim-set 去重); 逐 rep judge.total="
                f"{[round(x,4) for x in jts]} cov={[round(x,4) for x in covs]}; "
                f"回填时间 {datetime.datetime.now().astimezone().isoformat(timespec='seconds')} (q7-curve-backfill-719.py v2)"
            )
            break
    curve["fits"] = new_fits
    mg = curve.setdefault("marginal_gains", {})
    mg["300->719"] = new_marg
    pue = curve.setdefault("per_unit_efficiency", {})
    pue["300->719"] = new_pue
    curve["conclusion"] = new_conclusion
    curve["updated_at"] = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    curve["pending"] = f"719 档已回填 n={n_reps} (r1/r2/r3 独立); 300 档 n=2 独立 rep 不变 (r2 复制已剔除)"
    curve["source"] = f"q7-scan-scores.json ({len(scores)} 条; 719 n={n_reps} 独立 claim-set, 300-r2 复制剔除)"
    json.dump(curve, open(CURVE, "w"), ensure_ascii=False, indent=1)
    print(f"\n[applied] curve JSON 已写: {CURVE}")
    if missed:
        print(f"[applied] 但 conclusion 有 {len(missed)} 个语义未自动替换 ({missed}), 请人工核。")

if __name__ == "__main__":
    main()
