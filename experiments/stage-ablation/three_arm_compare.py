#!/usr/bin/env python3
"""三臂对比：M0(minimal) / M1(method) / M2(method_challenge)
从 runs-s5-sm-gpu-*.json 提取指标，输出对比表。
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

ARMS = [
    ("M0 (minimal)", "runs-s5-sm-gpu-minimal.json"),
    ("M1 (method)", "runs-s5-sm-gpu-method.json"),
    ("M2 (method_challenge)", "runs-s5-sm-gpu-method-challenge.json"),
]

def load_arm(path):
    """加载一臂的 run 数据，返回指标 dict。"""
    full = os.path.join(HERE, path)
    if not os.path.isfile(full):
        return None
    with open(full) as f:
        d = json.load(f)
    nodes = d.get("nodes", [])
    total = len(nodes)
    if total == 0:
        return None
    statuses = {}
    for n in nodes:
        s = n.get("status", "unknown")
        statuses[s] = statuses.get(s, 0) + 1
    verified = statuses.get("verified", 0)
    degraded = statuses.get("degraded", 0)
    pending = statuses.get("pending", 0)
    failed = statuses.get("failed", 0)
    # edge types
    edge_types = {}
    for n in nodes:
        et = n.get("edge_type", "unknown")
        edge_types[et] = edge_types.get(et, 0) + 1
    quotient = edge_types.get("quotient", 0)
    cartesian = edge_types.get("cartesian", 0)
    # reworks
    reworks = len(d.get("rework_events", []))
    # leaks
    leaks = d.get("leak_count", 0)
    # rounds
    rounds = len(d.get("rounds", []))
    # final state
    final_state = d.get("final_state", "unknown")
    # gain trajectory
    gains = []
    for r in d.get("rounds", []):
        g = r.get("gain")
        if g is not None:
            gains.append(g)
    return {
        "total": total,
        "verified": verified,
        "degraded": degraded,
        "pending": pending,
        "failed": failed,
        "verified_rate": verified / total * 100,
        "degraded_rate": degraded / total * 100,
        "quotient": quotient,
        "cartesian": cartesian,
        "quotient_pct": quotient / total * 100 if total else 0,
        "reworks": reworks,
        "leaks": leaks,
        "rounds": rounds,
        "final_state": final_state,
        "gains": gains,
    }

def main():
    print("=" * 70)
    print("S5 SM 三臂对比（gpu 题）")
    print("=" * 70)
    print()
    # header
    print(f"{'指标':<25} {'M0 (minimal)':>15} {'M1 (method)':>15} {'M2 (challenge)':>15}")
    print("-" * 70)

    results = {}
    for label, fname in ARMS:
        r = load_arm(fname)
        results[label] = r
        if r is None:
            print(f"  {label}: {fname} 不存在或无数据")

    # only print rows if at least one arm has data
    any_data = any(r is not None for r in results.values())
    if not any_data:
        print("  无数据可对比。等待 run 完成。")
        return

    def fmt(val, fmt_str="{}"):
        if val is None:
            return "—"
        return fmt_str.format(val)

    rows = [
        ("总节点数", lambda r: r["total"], "{}"),
        ("verified 数", lambda r: r["verified"], "{}"),
        ("verified 率", lambda r: r["verified_rate"], "{:.1f}%"),
        ("degraded 数", lambda r: r["degraded"], "{}"),
        ("degraded 率", lambda r: r["degraded_rate"], "{:.1f}%"),
        ("pending 数", lambda r: r["pending"], "{}"),
        ("failed 数", lambda r: r["failed"], "{}"),
        ("quotient 边", lambda r: r["quotient"], "{}"),
        ("cartesian 边", lambda r: r["cartesian"], "{}"),
        ("quotient 占比", lambda r: r["quotient_pct"], "{:.1f}%"),
        ("rework 事件", lambda r: r["reworks"], "{}"),
        ("泄漏数", lambda r: r["leaks"], "{}"),
        ("轮次", lambda r: r["rounds"], "{}"),
        ("终态", lambda r: r["final_state"], "{}"),
    ]

    for name, getter, fmt_str in rows:
        vals = []
        for label, _ in ARMS:
            r = results.get(label)
            if r is None:
                vals.append("—")
            else:
                vals.append(fmt(getter(r), fmt_str))
        print(f"{name:<25} {vals[0]:>15} {vals[1]:>15} {vals[2]:>15}")

    # gain trajectory
    print()
    print("gain 轨迹:")
    for label, _ in ARMS:
        r = results.get(label)
        if r is None:
            print(f"  {label}: —")
        else:
            gains = r["gains"]
            if gains:
                print(f"  {label}: {' → '.join(f'{g:.3f}' for g in gains)}")
            else:
                print(f"  {label}: (无 gain 数据)")

    # summary
    print()
    print("=" * 70)
    print("判读:")
    print("- M1 > M0 → 软注入（习惯声明）有效")
    print("- M2 > M1 → 结构机制（反方质询）有效")
    print("- 都 < M0 → 注入有害（稀释信号）")
    print("- 差异 < 2pp → 噪声，需 n>1")
    print("=" * 70)

if __name__ == "__main__":
    main()
