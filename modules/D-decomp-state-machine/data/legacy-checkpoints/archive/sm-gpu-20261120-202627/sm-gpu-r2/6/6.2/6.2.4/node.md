# N131: CapEx 优势抵消点计算公式推导：定义 Break_even_T = (CapEx_Consumer - CapEx_Datacenter) / (OpEx_

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

CapEx 优势抵消点计算公式推导：定义 Break_even_T = (CapEx_Consumer - CapEx_Datacenter) / (OpEx_daily_Datacenter - OpEx_daily_Consumer)，其中 OpEx_daily = P_avg × 24h × E_price。需代入 N38/N39 的功耗数据和 N40 的电价，计算在典型电价下，多卡消费级方案相比单卡数据中心方案的 TCO 交叉时间点（月数）。

## Corrected Claim

CapEx 优势抵消点计算公式推导：定义 Break_even_T = (CapEx_Consumer - CapEx_Datacenter) / (OpEx_daily_Datacenter - OpEx_daily_Consumer)，其中 OpEx_daily = P_avg × 24h × E_price。需代入 N38/N39 的功耗数据和 N40 的电价，计算在典型电价下，多卡消费级方案相比单卡数据中心方案的 TCO 交叉时间点（月数）。

## Evidence

先验知识/题面给定，逻辑校验通过
