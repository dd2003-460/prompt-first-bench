# N442: 高码率工作点的带宽成本增量：C_bw_high = (8.0 MB / 8) * 2TB_daily * (1 - 0.65) * P_bw = 700GB *

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N142

## Claim

高码率工作点的带宽成本增量：C_bw_high = (8.0 MB / 8) * 2TB_daily * (1 - 0.65) * P_bw = 700GB * P_bw；相比标准工作点（400GB * P_bw）成本增加 75%，而非 100%，因为缓存命中率下降（65% vs 80%）部分抵消了对象大小增加的影响。

## Corrected Claim

高码率工作点的带宽成本增量：C_bw_high = (8.0 MB / 8) * 2TB_daily * (1 - 0.65) * P_bw = 700GB * P_bw；相比标准工作点（400GB * P_bw）成本增加 75%，而非 100%，因为缓存命中率下降（65% vs 80%）部分抵消了对象大小增加的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (8/8)*2000*(1-0.65)=700GB 正确，700/400-1=75% 正确，逻辑自洽。
