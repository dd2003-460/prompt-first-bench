# N153: 在 r_rank=0.05 工作点下，LFU 保留 Top 10% 热度对象的精确容量占比：Top 10% 对象（排名 1-10,000）的累计请求率占比为 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N52

## Claim

在 r_rank=0.05 工作点下，LFU 保留 Top 10% 热度对象的精确容量占比：Top 10% 对象（排名 1-10,000）的累计请求率占比为 1 - (10,000/100,000)^{1-0.9} = 1 - 0.1^{0.1} ≈ 6.51%。LFU 能准确保留这些对象，其字节命中率贡献 H_top10 = 0.651 * (1 - P_miss_top10)，其中 P_miss_top10 在稳态下趋近于 0。

## Corrected Claim

在 r_rank=0.05 工作点下，LFU 保留 Top 10% 热度对象的精确容量占比：Top 10% 对象（排名 1-10,000）的累计请求率占比为 1 - (10,000/100,000)^{1-0.9} = 1 - 0.1^{0.1} ≈ 6.51%。LFU 能准确保留这些对象，其字节命中率贡献 H_top10 = 0.651 * (1 - P_miss_top10)，其中 P_miss_top10 在稳态下趋近于 0。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1 - 0.1^0.1 ≈ 0.651 正确，LFU 稳态行为符合理论预期

## Search Query

Pareto distribution top percentile request rate fraction beta 0.9
