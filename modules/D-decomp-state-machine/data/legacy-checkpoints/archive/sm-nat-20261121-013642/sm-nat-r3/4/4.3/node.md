# N17: 动态更新惩罚因子 δ = 1 - C_steady * (1 - P_hit_cold)，其中 P_hit_cold 为陈旧对象被请求时的命中概率（若更新后内容

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

动态更新惩罚因子 δ = 1 - C_steady * (1 - P_hit_cold)，其中 P_hit_cold 为陈旧对象被请求时的命中概率（若更新后内容不同则 miss，P_hit_cold≈0 若内容完全替换）

## Corrected Claim

动态更新惩罚因子 δ = 1 - C_steady * (1 - P_hit_cold)，其中 P_hit_cold 为陈旧对象被请求时的命中概率（若更新后内容不同则 miss，P_hit_cold≈0 若内容完全替换）

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是对同一参数 P_hit_cold 在不同取值（0, 1, 0.5）下的特例展示，属于参数实例化而非正交的概念分解，存在冗余。此外，父节点中明确定义的另一个关键变量 C_steady（稳态成本/权重）未被单独分解或解释，导致对公式中各分量作用的覆盖不全。）
