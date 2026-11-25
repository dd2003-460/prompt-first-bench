#!/usr/bin/env python3
"""T-REPAIR-1 4 臂析因分析（纯 CPU, 不碰 vLLM）

数据: modules/B-pipeline-ablation/data/t-repair1/arms/{baseline,fixA,fixAB,fixB}/{arm}-r{1,2,3}-*.json
基线: 同目录 t-repair1-stats.json（执行器逐 rep 落的统计, 交叉验证用）
外部参照: q6-budget-scan/q6-300-r{1,2,3}*.json（未修改 SM 的 Q6-300 3 reps, 11-23 跑的）
        + 80-run corpus 节点级 3.7%（repair-closure-dryrun.py 固化 a1d42814c）

预注册预测（repair-loop-design-20261124.md）:
  P-A:  Fix-A 后 value_mismatch 修复率 > 2.4% 基线（事件级, 22/932, 80-run corpus）
  P-B:  Fix-B 后整体节点级修复率 > 3.7% 基线（节点级, 331/8870）
  P-A+B: 正交 → A+B ≥ max(A,B); 亚/超可加 = 交互新发现
  判别: A、B 都不升 → 瓶颈在 fixer 能力或 contradiction 证据

PREREG 效度注记（2026-11-25 11:00 分析前核查）:
  Q6-300 基线 rework 事件 mode 全为 angle(167), value_mismatch=0 →
  P-A 主判别（value_mismatch 修复率）在 Q6 域分母=0, 不可直接测。
  处理: P-A 降级为间接观察（angle mode 修复率 + 节点级修复率是否随 A 升）;
  正式测 P-A 需 gpu 域补臂（follow-up 登记, 不阻塞本批）。
  本脚本对分母=0 的 mode 标 UNTESTABLE 而非输出 0%/NaN（鉴别力: 防空判别）。

统计口径（设计文档 §验收）:
  - 节点级修复率 = rework_count>0 且最终 status==verified 的比例（strict, 与 dryrun 同口径）
  - n=3 臂内 → bootstrap CI (B=2000, 节点级重采样); n=3 只 suggestive, 正式 claim 需 n≥5
  - 等效性: 声称"无效"需 TOST（预设最小效应 0.10, T-PR-17 先例; 0.05 在 n=150 下不可行, 见 MIN_EFFECT 注释）
"""
import json, glob, os, sys, math, re
import random

DATA = "/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/t-repair1"
ARMS = ["baseline", "fixA", "fixAB", "fixB"]
MIN_EFFECT = 0.10  # TOST 预设最小效应（T-PR-17 先例 ±0.1 半宽）。
# 2026-11-25 功效核算: 曾收紧到 0.05, 但 n=150/臂 p≈0.06 时差值 CI 宽≈0.107 > 2*0.05=0.10
# → margin=0.05 下 TOST 等效结论永不触发, "无效"与"不显著"无法区分。恢复 0.10 使 TOST 可行。
BOOT_B = 2000
RNG = random.Random(20261125)


def load_arm_runs(arm, rep_rc):
    """自动发现某臂的 3 个 runs json（按 mtime 取最新, 防重跑残留）。
    rep_rc: {(arm,rep): rc} 从 executor log 解析; rc!=0 的 rep 排除
    （SM 失败时不写 runs json, executor 复制的是上一个成功 rep 的旧文件——
    不排除会把旧数据当新 rep 用, 空验证）。"""
    pat = os.path.join(DATA, "arms", arm, f"{arm}-r*.json")
    fs = [f for f in glob.glob(pat) if "-r1-" in f or "-r2-" in f or "-r3-" in f]
    by_rep = {}
    for f in fs:
        for rep in (1, 2, 3):
            if f"-r{rep}-" in f:
                by_rep[rep] = f  # glob 按文件名排序, 同名后写的覆盖=最新
    out = {}
    for rep, f in sorted(by_rep.items()):
        rc = rep_rc.get((arm, rep))
        if rc is not None and rc != 0:
            continue  # executor 记录该 rep 失败, 文件是旧数据
        out[rep] = json.load(open(f))
    return out


def parse_rep_rc(log_path):
    """从 executor log 提取 {(arm,rep): rc}。行格式: arm=X rep=Y rc=N wall_s=M out=..."""
    rc = {}
    if not os.path.exists(log_path):
        return rc
    for line in open(log_path):
        m = re.match(r"\[[\d:]+\] arm=(\w+) rep=(\d+) rc=(\d+) ", line)
        if m:
            rc[(m.group(1), int(m.group(2)))] = int(m.group(3))
    return rc


def node_repair(d):
    """节点级: (n_rework_nodes, n_fixed_strict, n_corrected)"""
    nodes = d.get("nodes", [])
    rc = [n for n in nodes if (int(n.get("rework_count", 0) or 0)) > 0]
    fixed = [n for n in rc if n.get("status") == "verified"]
    corrected = [n for n in rc if (n.get("corrected_claim") or "").strip()]
    return len(rc), len(fixed), len(corrected)


def event_modes(d):
    """事件级: mode → (n_events, n_fixed)。fixed = 该事件 node_id 最终 verified。"""
    nodes = {n.get("id"): n for n in d.get("nodes", [])}
    ev = {}
    for e in d.get("rework_events", []):
        mode = e.get("mode")
        if not mode:
            continue  # parent-review 事件(无 mode)不进 rework 模式统计
        nid = e.get("node_id")
        fixed = nodes.get(nid, {}).get("status") == "verified" if nid else False
        a, fx = ev.get(mode, (0, 0))
        ev[mode] = (a + 1, fx + (1 if fixed else 0))
    return ev


def rate(num, den):
    return (num / den) if den else None


def bootstrap_ci(fixed, total, b=BOOT_B, seed=20261125):
    """节点级重采样 bootstrap CI（臂内合并所有 rep 的节点）。"""
    if total == 0:
        return None
    p = fixed / total
    rng = random.Random(seed)
    ests = []
    # 用 0/1 向量重采样
    vec = [1] * fixed + [0] * (total - fixed)
    for _ in range(b):
        s = sum(rng.choice(vec) for _ in range(total))
        ests.append(s / total)
    ests.sort()
    return (ests[int(0.025 * b)], ests[int(0.975 * b)])


def tost(diff, ci_lo, ci_hi, margin=MIN_EFFECT):
    """TOST: 差值 CI ⊂ [-margin, +margin] → 等效。"""
    if ci_lo is None:
        return None
    return ci_lo > -margin and ci_hi < margin


def main():
    out = {"arms": {}, "predictions": {}, "caveats": []}
    out["caveats"].append(
        "P-A 主判别(value_mismatch 修复率)在 Q6 域分母=0(基线 mode 全 angle) → 降级间接观察; "
        "正式测 P-A 需 gpu 域补臂(follow-up)")

    # executor log 里的 per-rep rc（rc!=0 的 rep 排除, 防旧文件冒充新 rep）
    sa_logs = "/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation/logs"
    exec_logs = sorted(glob.glob(os.path.join(sa_logs, "t-repair1-4arm-*.log")))
    rep_rc = {}
    for lf in exec_logs:
        rep_rc.update(parse_rep_rc(lf))
    if rep_rc:
        bad = {k: v for k, v in rep_rc.items() if v != 0}
        if bad:
            out["caveats"].append(f"executor log 记录 {len(bad)} 个 rep 失败(rc!=0), 已从分析排除: {bad}")

    arm_stats = {}
    for arm in ARMS:
        runs = load_arm_runs(arm, rep_rc)
        reps = sorted(runs.keys())
        if len(reps) < 3:
            out["caveats"].append(f"臂 {arm} 只有 {len(reps)} reps(<3), 结果不可用")
            continue
        n_rw = n_fx = n_cc = 0
        all_vec = []  # 节点 0/1 向量(bootstrap 用)
        ev_agg = {}
        rep_rates = []  # 每 rep 节点级修复率 (rep 间方差监控用)
        for rep in reps:
            d = runs[rep]
            rw, fx, cc = node_repair(d)
            n_rw += rw; n_fx += fx; n_cc += cc
            if rw:
                rep_rates.append(fx / rw)
            nodes = d.get("nodes", [])
            rc_nodes = [n for n in nodes if (int(n.get("rework_count", 0) or 0)) > 0]
            all_vec += [1 if n.get("status") == "verified" else 0 for n in rc_nodes]
            for mode, (a, f) in event_modes(d).items():
                ea, ef = ev_agg.get(mode, (0, 0))
                ev_agg[mode] = (ea + a, ef + f)
        ci = bootstrap_ci(n_fx, n_rw)
        spread = (max(rep_rates) - min(rep_rates)) if len(rep_rates) >= 2 else None
        arm_stats[arm] = {
            "n_reps": len(reps),
            "node": {"n_rework": n_rw, "n_fixed": n_fx, "n_corrected": n_cc,
                     "repair_rate": rate(n_fx, n_rw),
                     "ci95": ci,
                     "per_rep_rates": rep_rates, "rep_spread": spread},
            "events": {m: {"n": a, "fixed": f, "rate": rate(f, a)} for m, (a, f) in sorted(ev_agg.items())},
        }
        # rep 间方差监控: spread 超过池化 CI 宽度的一半 → 节点级 bootstrap 低估真实不确定性
        if spread is not None and ci is not None:
            ci_w = ci[1] - ci[0]
            if spread > 0.5 * ci_w:
                out["caveats"].append(
                    f"臂 {arm} rep 间修复率 spread={spread:.3f} (per-rep={rep_rates}) 超过池化 CI 宽度 {ci_w:.3f} 的一半 → "
                    f"节点级 bootstrap 把 rep 当独立样本, 低估真实不确定性; TOST/显著性读法降权, 以 rep 级方向一致性为准")
        out["arms"][arm] = arm_stats[arm]

    if len(arm_stats) < 4:
        print(json.dumps(out, ensure_ascii=False, indent=1))
        print("FATAL: 臂数不足 4, 析因不可做")
        sys.exit(1)

    b, a, ab, bb = (arm_stats[x]["node"]["repair_rate"] for x in ARMS)
    b_ci, a_ci, ab_ci, bb_ci = (arm_stats[x]["node"]["ci95"] for x in ARMS)

    # P-B: fixB vs baseline 节点级修复率
    pb_diff = (bb - b) if (bb is not None and b is not None) else None
    out["predictions"]["P-B"] = {
        "claim": "Fix-B 后节点级修复率 > 3.7% 基线",
        "baseline_corpus": 0.037,
        "baseline_q6_same_seed": b,
        "fixB_rate": bb, "fixB_ci95": bb_ci,
        "delta_vs_baseline_arm": pb_diff,
        "tost_equivalent_to_baseline": tost(pb_diff,
                                            (bb_ci[0] - b_ci[1]) if bb_ci and b_ci else None,
                                            (bb_ci[1] - b_ci[0]) if bb_ci and b_ci else None),
    }
    # P-A: value_mismatch 事件级（Q6 域分母=0 → 间接观察）
    vm_b = arm_stats["baseline"]["events"].get("value_mismatch")
    vm_a = arm_stats["fixA"]["events"].get("value_mismatch")
    out["predictions"]["P-A"] = {
        "claim": "Fix-A 后 value_mismatch 修复率 > 2.4% 基线",
        "baseline_corpus": 0.024,
        "baseline_q6_vm": vm_b, "fixA_q6_vm": vm_a,
        "testable": bool(vm_a and vm_a["n"] > 0),
        "indirect": {
            "note": "Q6 域 value_mismatch 分母=0 → 看 angle mode + 节点级是否随 A 升",
            "angle_baseline": arm_stats["baseline"]["events"].get("angle"),
            "angle_fixA": arm_stats["fixA"]["events"].get("angle"),
            "node_rate_baseline": b, "node_rate_fixA": a,
        },
    }
    # P-A+B: 交互
    if None not in (b, a, ab, bb):
        additive = a + bb - b  # 可加预期
        out["predictions"]["P-A+B"] = {
            "claim": "正交 → A+B ≥ max(A,B)",
            "max_ab": max(a, bb), "a_plus_b": ab,
            "additive_expectation": round(additive, 4),
            "interaction": "orthogonal" if ab >= max(a, bb) else
                           ("superadditive" if ab > additive else "subadditive"),
        }
    # 判别: A、B 都不升
    if None not in (b, a, bb):
        out["predictions"]["discriminant"] = {
            "rule": "A、B 节点级修复率都不升(差<0 或 TOST 等效) → 瓶颈在 fixer 能力/contradiction 证据",
            "A_up": a > b, "B_up": bb > b,
            "both_not_up": not (a > b) and not (bb > b),
        }

    print(json.dumps(out, ensure_ascii=False, indent=1))
    with open(os.path.join(DATA, "t-repair1-analysis.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"\n[saved] {os.path.join(DATA, 't-repair1-analysis.json')}", file=sys.stderr)


if __name__ == "__main__":
    main()
