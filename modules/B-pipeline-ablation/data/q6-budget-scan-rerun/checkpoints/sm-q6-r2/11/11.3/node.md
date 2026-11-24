# N182: 单POP故障期间的用户体验惩罚成本 C_penalty 量化：C_penalty = (U_impact * DAU * ARPU_daily * Downti

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

单POP故障期间的用户体验惩罚成本 C_penalty 量化：C_penalty = (U_impact * DAU * ARPU_daily * Downtime_Hours / 24) / Q_day * 1000，其中 ARPU_daily 为日均每用户收入（基于DAU 500万和平台变现模型估算，如广告+会员），Downtime_Hours 为实际不可用小时数。

## Corrected Claim

单POP故障期间的用户体验惩罚成本 C_penalty 量化：C_penalty = (U_impact * DAU * ARPU_daily * Downtime_Hours / 24) / Q_day * 1000，其中 ARPU_daily 为日均每用户收入（基于DAU 500万和平台变现模型估算，如广告+会员），Downtime_Hours 为实际不可用小时数。

## Evidence

先验知识/题面给定，逻辑校验通过
