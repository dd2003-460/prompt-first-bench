#!/usr/bin/env python3
"""rule-injection-bench 分析：臂间对比 + 压缩安全性判断。

读 results/ 下所有单 run json，输出：
1. 臂 × 题 平均分表
2. 臂级总平均分
3. A1(压缩) vs A2(全文) 逐题差异 + 是否在噪声范围内
4. 结论：压缩是否安全

噪声阈值 ±1.5 的出处：decomp T17 先例"重复 run 噪声 ±1.5 ≥ 域间差 → 排序不可信"
（projects/decomp 四域泛化实验，2026-11 落盘）。复用该阈值，标注来源。
"""
import json, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
NOISE = 1.5  # 噪声阈值，来源见文件头


def load():
    out = []
    for fn in os.listdir(RESULTS):
        if fn.endswith(".json") and fn != "scores.json":
            with open(os.path.join(RESULTS, fn)) as f:
                out.append(json.load(f))
    return out


def main():
    results = load()
    if not results:
        print("无结果")
        return

    # 臂 × 题 聚合
    agg = defaultdict(list)
    for r in results:
        agg[(r["arm"], r["task"])].append(r["score"])

    print(f"总 run 数: {len(results)}")
    print(f"\n{'臂':<4} {'题':<4} {'n':<3} {'mean':<6} {'min':<4} {'max':<4}")
    print("-" * 30)
    for (arm, task), scores in sorted(agg.items()):
        print(f"{arm:<4} {task:<4} {len(scores):<3} {sum(scores)/len(scores):<6.2f} {min(scores):<4} {max(scores):<4}")

    # 臂级总平均
    arm_scores = defaultdict(list)
    for r in results:
        arm_scores[r["arm"]].append(r["score"])
    print(f"\n{'臂':<4} {'mean':<6} {'n':<4}")
    print("-" * 16)
    arm_mean = {}
    for arm in sorted(arm_scores):
        s = arm_scores[arm]
        arm_mean[arm] = sum(s) / len(s)
        print(f"{arm:<4} {arm_mean[arm]:<6.2f} {len(s):<4}")

    # A1 vs A2 逐题差异
    print(f"\n=== A1(压缩) vs A2(全文) 逐题差异（噪声阈值 ±{NOISE}）===")
    print(f"{'题':<4} {'A1':<6} {'A2':<6} {'Δ(A1-A2)':<10} {'判断'}")
    print("-" * 40)
    n_safe, n_drop = 0, 0
    for task in sorted(set(r["task"] for r in results)):
        a1 = agg.get(("A1", task), [])
        a2 = agg.get(("A2", task), [])
        if not a1 or not a2:
            continue
        m1, m2 = sum(a1)/len(a1), sum(a2)/len(a2)
        diff = m1 - m2
        # 压缩安全 = A1 不低于 A2 超过噪声阈值
        if diff >= -NOISE:
            verdict = "安全(压缩未显著降低)"
            n_safe += 1
        else:
            verdict = f"⚠️ 下降超噪声(差{diff:.2f})"
            n_drop += 1
        print(f"{task:<4} {m1:<6.2f} {m2:<6.2f} {diff:<+10.2f} {verdict}")

    # 结论
    print(f"\n=== 结论 ===")
    print(f"逐题: {n_safe} 题压缩安全, {n_drop} 题下降超噪声")
    d_total = arm_mean.get("A1", 0) - arm_mean.get("A2", 0)
    if n_drop == 0:
        print(f"臂级总差 A1-A2 = {d_total:+.2f} → 压缩安全，1022ch 小便签够用")
    else:
        drops = [t for t in sorted(set(r['task'] for r in results))
                 if agg.get(('A1',t)) and agg.get(('A2',t))
                 and sum(agg[('A1',t)])/len(agg[('A1',t)]) - sum(agg[('A2',t)])/len(agg[('A2',t)]) < -NOISE]
        print(f"臂级总差 A1-A2 = {d_total:+.2f} → 部分规则下降，需加回: {drops}")


if __name__ == "__main__":
    main()
