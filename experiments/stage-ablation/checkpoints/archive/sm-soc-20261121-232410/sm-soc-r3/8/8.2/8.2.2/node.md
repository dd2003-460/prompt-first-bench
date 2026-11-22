# N219: Chow test 结构性断裂检验：将时间序列分为前后两段（如干预前后），计算 F 统计量 F = ((RSS_pooled - (RSS_1 + RSS_2)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

Chow test 结构性断裂检验：将时间序列分为前后两段（如干预前后），计算 F 统计量 F = ((RSS_pooled - (RSS_1 + RSS_2)) / k) / ((RSS_1 + RSS_2) / (n1 + n2 - 2k))；若 F < F_critical (p > 0.1)，则断言 CVR 无结构性断裂，支持稳定性结论。

## Corrected Claim

Chow test 结构性断裂检验：将时间序列分为前后两段（如干预前后），计算 F 统计量 F = ((RSS_pooled - (RSS_1 + RSS_2)) / k) / ((RSS_1 + RSS_2) / (n1 + n2 - 2k))；若 F < F_critical (p > 0.1)，则断言 CVR 无结构性断裂，支持稳定性结论。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Chow test structural break F-statistic conversion rate time series
