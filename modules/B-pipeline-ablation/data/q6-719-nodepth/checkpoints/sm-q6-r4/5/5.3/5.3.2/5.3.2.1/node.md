# N291: 单POP月度出网流量需求 Q_pop = (Total_Daily_Download * 30 * (1 - H_pop)) / 10，其中 Total_Dai

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N96

## Claim

单POP月度出网流量需求 Q_pop = (Total_Daily_Download * 30 * (1 - H_pop)) / 10，其中 Total_Daily_Download = 2TB，H_pop 为单POP稳态缓存命中率（假设85%），计算得 Q_pop ≈ 900GB/月。

## Corrected Claim

单POP月度出网流量需求 Q_pop = (Total_Daily_Download * 30 * (1 - H_pop)) / 10，其中 Total_Daily_Download = 2TB，H_pop 为单POP稳态缓存命中率（假设85%），计算得 Q_pop ≈ 900GB/月。

## Evidence

先验知识/题面给定，逻辑校验通过：2TB * 30 * (1 - 0.85) / 10 = 60TB * 0.15 / 10 = 9TB / 10 = 0.9TB = 900GB，计算无误。
