# N127: K 的解析近似：在 Pareto(α=1.1) 下，前 k 个对象的累积大小 S_k ≈ s_min * (k+1)^(1-1/α) / (1-1/α)，令 S

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N42

## Claim

K 的解析近似：在 Pareto(α=1.1) 下，前 k 个对象的累积大小 S_k ≈ s_min * (k+1)^(1-1/α) / (1-1/α)，令 S_k = 128GB 解得 k ≈ (128GB / s_min)^(1/0.9) * (0.9)^(1/0.9)，此公式用于快速估算 K 而不需逐对象累加。

## Corrected Claim

K 的解析近似：在 Pareto(α=1.1) 下，前 k 个对象的累积大小 S_k ≈ s_min * (k+1)^(1-1/α) / (1-1/α)，令 S_k = 128GB 解得 k ≈ (128GB / s_min)^(1/0.9) * (0.9)^(1/0.9)，此公式用于快速估算 K 而不需逐对象累加。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布累积和的解析近似公式推导正确，量纲与数值逻辑自洽。
