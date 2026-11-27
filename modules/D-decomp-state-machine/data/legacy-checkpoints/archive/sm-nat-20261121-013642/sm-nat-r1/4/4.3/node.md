# N17: 动态更新惩罚因子 δ = 1 - C_steady * (1 - P_hit_cold)，其中 P_hit_cold 为陈旧对象被请求时的命中概率（若更新后内容

- **status**: verified
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

先验知识/题面给定，逻辑校验通过
