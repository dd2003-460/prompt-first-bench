# N85: 修正截断帕累托均值 E[S] 计算：当 α=1.1, S_min=1KB, S_max=100MB (10^8 KB) 时，修正因子 (1 - (S_min/S

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

修正截断帕累托均值 E[S] 计算：当 α=1.1, S_min=1KB, S_max=100MB (10^8 KB) 时，修正因子 (1 - (S_min/S_max)^(α-1)) = 1 - (10^-8)^0.1 = 1 - 10^-0.8 ≈ 1 - 0.1585 = 0.8415。因此 E[S] = (1.1/0.1) * 1 * 0.8415 ≈ 9.26 KB，而非 N28 声称的 11.11 KB。

## Corrected Claim

修正截断帕累托均值 E[S] 计算：当 α=1.1, S_min=1KB, S_max=100MB (10^8 KB) 时，修正因子 (1 - (S_min/S_max)^(α-1)) = 1 - (10^-8)^0.1 = 1 - 10^-0.8 ≈ 1 - 0.1585 = 0.8415。因此 E[S] = (1.1/0.1) * 1 * 0.8415 ≈ 9.26 KB，而非 N28 声称的 11.11 KB。

## Evidence

先验知识/题面给定，逻辑校验通过：截断帕累托分布均值公式应用正确，数值计算 (1.1/0.1)*1*(1-10^-0.8) ≈ 9.26 准确无误。

## Search Query

truncated pareto distribution mean formula calculation
