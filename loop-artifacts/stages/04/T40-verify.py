#!/usr/bin/env python3
"""Offline arithmetic/leaf audit for T40. Not a benchmark or a reviewer."""

from decimal import Decimal as D
from pathlib import Path
import re

I, O = D(2000), D(500)  # explicitly hypothetical, NOT measured usage
PRICES = {
    "Mistral-2501": ("0.05", "0.08"),
    "GLM-0414-ZAI": ("0.10", "0.10"),
    "Qwen3-32B": ("0.08", "0.28"),
    "Llama-3.3-70B": ("0.10", "0.32"),
    "Qwen2.5-Coder-32B": ("0.66", "1.00"),
}
EXPECTED_CENTS = [D(14), D(25), D(30), D(36), D(182)]


def dollars_per_attempt(pair):
    pin, pout = (D(v) for v in pair)
    return (I * pin + O * pout) / D(1_000_000)


def main():
    attempts = {model: dollars_per_attempt(pair) for model, pair in PRICES.items()}
    cents = {model: D(100_000) * cost for model, cost in attempts.items()}
    assert list(cents.values()) == EXPECTED_CENTS, cents
    assert cents["Mistral-2501"] / D("0.4") == D(35)
    assert cents["GLM-0414-ZAI"] / D("0.8") == D("31.25")
    assert D(236) * D(4) / D(8) == D(118)  # ideal W4 storage in decimal GB

    print("[估计, conf 0.2] i=2000, o=500 tokens/attempt; published list prices; F, tests, tax=excluded")
    base = attempts["Mistral-2501"]
    for model, cost in attempts.items():
        ratio = cost / base
        threshold = base / cost
        print(
            f"{model}: ${cost}/attempt, C_API={cents[model]}/q cents/1k_acc; "
            f"cost-ratio-to-M={ratio:.6f}, sufficient-q_M>{threshold:.6f}; "
            f"equal-q GPU threshold at $0.89/GPU-h={D('0.89') / cost:.2f} attempts/h"
        )
    print(f"Llama 2-GPU equal-q threshold: {D('1.78') / attempts['Llama-3.3-70B']:.2f} attempts/h")

    doc = Path(__file__).with_name("execution-log.md")
    if not doc.exists():
        print("No execution-log.md yet; arithmetic assertions passed")
        return
    text = doc.read_text(encoding="utf-8")
    tree = text.split("## 三、ASCII 定量树", 1)[1].split("## 四、叶子卡片", 1)[0]
    cards = text.split("## 四、叶子卡片", 1)[1].split("## 五、计算与敏感性", 1)[0]
    tree_ids = re.findall(r"\bL\d{2}\b", tree)
    node_lines = [line for line in tree.splitlines() if "├─" in line or "└─" in line]
    node_count = 1 + len(node_lines)  # root plus all visibly connected ASCII branches
    depths = []
    for line in node_lines:
        if re.search(r"\bL\d{2}\b", line):
            prefix = line.split("├─", 1)[0] if "├─" in line else line.split("└─", 1)[0]
            depths.append(len(prefix) // 3 + 1)  # 3-column groups per level
    assert node_count >= 15 and min(depths) >= 3 and max(depths) >= 4, (node_count, depths)
    rows = re.findall(r"(?m)^\| (L\d{2}) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$", cards)
    card_ids = [row[0] for row in rows]
    expected = {f"L{i:02d}" for i in range(1, 53)}
    assert len(tree_ids) == len(set(tree_ids)) == 52, "tree leaf duplicate/missing"
    assert len(card_ids) == len(set(card_ids)) == 52, "leaf card duplicate/missing"
    assert set(tree_ids) == set(card_ids) == expected, (set(tree_ids) ^ expected, set(card_ids) ^ expected)
    for leaf_id, value, source, sensitivity in rows:
        assert re.search(r"\d", value), (leaf_id, "missing numeric value")
        assert any(u in value for u in ("%", "token", "$/", "GB", "GPU", "B 参数", "布尔", "次")), (leaf_id, "missing unit")
        assert "https://" in source or "Q2-model-selection.md" in source, (leaf_id, "missing URL/path")
        assert sensitivity.strip(), (leaf_id, "missing sensitivity")
    assert "[GAP]" in text
    assert all(h in text for h in ("## 一、根节点", "## 二、正交维度", "## 六、双源交叉", "## 七、缺口清单", "## 八、结论"))
    print(
        f"Tree audit passed: {node_count} nodes, depth {min(depths)}–{max(depths)} edges; "
        f"{len(tree_ids)} unique numeric leaves with source and sensitivity; tree/card IDs match"
    )


if __name__ == "__main__":
    main()
