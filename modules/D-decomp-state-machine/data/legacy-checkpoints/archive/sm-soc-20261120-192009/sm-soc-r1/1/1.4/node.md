# N8: 买家核验机制：买家决策函数 P(buy | price, info_quality) = sigmoid(β1 * (intrinsic_value - pri

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N1

## Claim

买家核验机制：买家决策函数 P(buy | price, info_quality) = sigmoid(β1 * (intrinsic_value - price) + β2 * info_quality)；β1 为价格敏感度，β2 为信息可信度权重，初始阶段 β2 较低，导致高挂价难以成交。

## Corrected Claim

买家核验机制：买家决策函数 P(buy | price, info_quality) = sigmoid(β1 * (intrinsic_value - price) + β2 * info_quality)；β1 为价格敏感度，β2 为信息可信度权重，初始阶段 β2 较低，导致高挂价难以成交。

## Evidence

先验知识/题面给定，逻辑校验通过
