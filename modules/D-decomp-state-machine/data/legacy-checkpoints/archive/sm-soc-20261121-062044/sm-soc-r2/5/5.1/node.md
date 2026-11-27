# N86: 皮尔逊相关系数 r 的显著性检验：给定样本量 n，计算 t-statistic = r * √(n-2) / √(1-r²)，若 r > 0.5 且 n > 3

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

皮尔逊相关系数 r 的显著性检验：给定样本量 n，计算 t-statistic = r * √(n-2) / √(1-r²)，若 r > 0.5 且 n > 30，需验证 p-value < 0.05 以排除统计噪声，确认‘逆向筛选’假设的统计显著性。

## Corrected Claim

皮尔逊相关系数 r 的显著性检验：给定样本量 n，计算 t-statistic = r * √(n-2) / √(1-r²)，若 r > 0.5 且 n > 30，需验证 p-value < 0.05 以排除统计噪声，确认‘逆向筛选’假设的统计显著性。

## Evidence

先验知识/题面给定，逻辑校验通过：t统计量公式正确，且当n>30且r>0.5时，t值远大于临界值，p值必然小于0.05，逻辑自洽。
