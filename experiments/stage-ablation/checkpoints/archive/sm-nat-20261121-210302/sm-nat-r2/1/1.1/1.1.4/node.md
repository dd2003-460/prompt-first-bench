# N27: 在 X_min=1KB, S_max=100MB, α=1.1 假设下，计算截断后的 S_mean ≈ 1.1/0.1 * 1KB * (1 - (1KB/10

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

在 X_min=1KB, S_max=100MB, α=1.1 假设下，计算截断后的 S_mean ≈ 1.1/0.1 * 1KB * (1 - (1KB/100MB)^0.1) ≈ 11KB * (1 - 0.1) ≈ 9.9KB，从而 N_cap = 128GB / 9.9KB ≈ 13,100,000 个对象。

## Corrected Claim

在 X_min=1KB, S_max=100MB, α=1.1 假设下，计算截断后的 S_mean ≈ 1.1/0.1 * 1KB * (1 - (1KB/100MB)^0.1) ≈ 11KB * (1 - 0.1) ≈ 9.9KB，从而 N_cap = 128GB / 9.9KB ≈ 13,100,000 个对象。

## Evidence

先验知识/题面给定，逻辑校验通过：截断帕累托分布均值公式应用正确，数值量级（11KB * 0.9 ≈ 9.9KB）及最终对象数量（128GB / 9.9KB ≈ 13.1M）计算无误。
