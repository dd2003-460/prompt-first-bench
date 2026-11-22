# N55: Top 1% 对象阈值大小 S_1% 的计算：S_1% = S_min * (1 - 0.01)^(1/(1-α))，代入 α=1.1, S_min=1KB 得

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15

## Claim

Top 1% 对象阈值大小 S_1% 的计算：S_1% = S_min * (1 - 0.01)^(1/(1-α))，代入 α=1.1, S_min=1KB 得 S_1% ≈ 1KB * (0.99)^(-10) ≈ 1.1KB，需验证该阈值下 Top 1% 对象的实际字节占比

## Corrected Claim

Top 1% 对象阈值大小 S_1% 的计算：S_1% = S_min * (1 - 0.01)^(1/(1-α))，代入 α=1.1, S_min=1KB 得 S_1% ≈ 1KB * (0.99)^(-10) ≈ 1.1KB，需验证该阈值下 Top 1% 对象的实际字节占比

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合幂律分布累积分布函数逆运算逻辑，数值计算 (0.99)^(-10) ≈ 1.1046 准确，量级合理。

## Search Query

Pareto distribution quantile formula alpha=1.1
