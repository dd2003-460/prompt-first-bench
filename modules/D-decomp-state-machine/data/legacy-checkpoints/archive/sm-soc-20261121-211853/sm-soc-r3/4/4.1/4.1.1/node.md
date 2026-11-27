# N38: 品类近30天成交均价 $AvgDealPrice$ 的计算公式：$AvgDealPrice = \frac{\sum_{i=1}^{n} P_{deal,i}}

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

品类近30天成交均价 $AvgDealPrice$ 的计算公式：$AvgDealPrice = \frac{\sum_{i=1}^{n} P_{deal,i}}{n}$，其中 $n$ 为过去30天内该品类所有成功交易的数量；若 $n < 30$，则需引入置信区间或采用加权平均（按时间衰减权重 $w_t = e^{-\lambda t}$）来平滑数据波动，避免小样本偏差。

## Corrected Claim

品类近30天成交均价 $AvgDealPrice$ 的计算公式：$AvgDealPrice = \frac{\sum_{i=1}^{n} P_{deal,i}}{n}$，其中 $n$ 为过去30天内该品类所有成功交易的数量；若 $n < 30$，则需引入置信区间或采用加权平均（按时间衰减权重 $w_t = e^{-\lambda t}$）来平滑数据波动，避免小样本偏差。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

moving average price calculation small sample bias correction time decay weight
