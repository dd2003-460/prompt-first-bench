#!/usr/bin/env python3
"""ICL hack 复现：β=0 vs β=3 判据提取。

从 runs json 提取 quotient 占比（r14 口径：>30% = hack 显著），
对比 β=0 臂（gpu-beta0）和 β=3 对照臂（gpu-formula-r2）。

用法：
    python3 extract-hack-metrics.py
    # 跑完 β=0 臂后执行，输出对比表 + 判定

判据来源：modules/B-pipeline-ablation/research/r14-results.md
    r13（无 structural test）: 63/70 = 90% hack
    r14（加 structural test）: 12.4% 正常（≤20%）
    阈值：>30% = hack 显著，≤20% = 正常
"""
import json
import sys
from collections import Counter
from pathlib import Path

ABLATION_DIR = Path(__file__).resolve().parents[3] / "experiments" / "stage-ablation"

# β=0 臂（本实验新跑）
BETA0_FILE = ABLATION_DIR / "runs-s5-sm-gpu-beta0.json"
# β=3 对照臂（现有数据，r14 时代跑的）
BETA3_FILE = ABLATION_DIR / "runs-s5-sm-gpu-formula-r2.json"

HACK_THRESHOLD = 30.0   # quotient 占比 >30% = hack 显著
NORMAL_THRESHOLD = 20.0  # ≤20% = 正常


def extract_metrics(path: Path) -> dict:
    """从 runs json 提取 hack 判据。"""
    if not path.exists():
        return {"file": str(path), "error": "文件不存在"}
    d = json.load(open(path))
    nodes = d.get("nodes", [])
    if not nodes:
        return {"file": str(path), "error": "无 nodes 字段或为空"}
    et = [n.get("edge_type") for n in nodes if n.get("edge_type")]
    n_et = len(et)
    n_quotient = et.count("quotient")
    quotient_pct = 100 * n_quotient / n_et if n_et else 0
    # 节点状态分布
    status = Counter(n.get("status") for n in nodes)
    return {
        "file": str(path.name),
        "n_nodes": len(nodes),
        "n_with_edge_type": n_et,
        "n_quotient": n_quotient,
        "quotient_pct": round(quotient_pct, 1),
        "status_dist": dict(status),
        "final_state": d.get("final_state"),
        "n_rounds": d.get("n_rounds"),
        "verdict": (
            "HACK 显著" if quotient_pct > HACK_THRESHOLD
            else "正常" if quotient_pct <= NORMAL_THRESHOLD
            else "灰区（20-30%，需更多样本）"
        ),
    }


def main():
    print("=" * 60)
    print("ICL hack 复现：β=0 vs β=3 对比")
    print("=" * 60)
    m0 = extract_metrics(BETA0_FILE)
    m3 = extract_metrics(BETA3_FILE)

    for label, m in [("β=0（无冗余惩罚，复现 v13）", m0),
                     ("β=3（当前默认，对照）", m3)]:
        print(f"\n【{label}】")
        if "error" in m:
            print(f"  ⚠ {m['error']}")
            continue
        print(f"  文件: {m['file']}")
        print(f"  节点数: {m['n_nodes']}")
        print(f"  quotient: {m['n_quotient']}/{m['n_with_edge_type']} = {m['quotient_pct']}%")
        print(f"  状态分布: {m['status_dist']}")
        print(f"  终止状态: {m['final_state']} (轮次 {m['n_rounds']})")
        print(f"  判定: {m['verdict']}")

    # 对比判定
    if "error" not in m0 and "error" not in m3:
        delta = m0["quotient_pct"] - m3["quotient_pct"]
        print(f"\n{'=' * 60}")
        print(f"对比: β=0 比 β=3 高 {delta:+.1f}pp")
        if delta > 10:
            print("结论: β=0 显著刷分 → 冗余惩罚必要（复现成功）")
        elif delta < -10:
            print("结论: β=0 反而更低 → 假设被推翻，structural test 可能足够")
        else:
            print("结论: 差异不显著 → 需更多样本或检查其他变量")
        print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
