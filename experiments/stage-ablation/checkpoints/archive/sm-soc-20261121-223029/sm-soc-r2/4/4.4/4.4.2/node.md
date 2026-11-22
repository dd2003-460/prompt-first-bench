# N87: 卖家利润损失中成交量补偿效应：价格透明化使成交周期 T_cycle 缩短，单位时间成交量 Q_unit_time 提升，估计 Q_unit_time_post 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

卖家利润损失中成交量补偿效应：价格透明化使成交周期 T_cycle 缩短，单位时间成交量 Q_unit_time 提升，估计 Q_unit_time_post = Q_unit_time_pre * (T_pre / T_post)，若 T_post = 0.7 * T_pre，则 Q_unit_time 提升约 43%。

## Corrected Claim

卖家利润损失中成交量补偿效应：价格透明化使成交周期 T_cycle 缩短，单位时间成交量 Q_unit_time 提升，估计 Q_unit_time_post = Q_unit_time_pre * (T_pre / T_post)，若 T_post = 0.7 * T_pre，则 Q_unit_time 提升约 43%。

## Evidence

先验知识/题面给定，逻辑校验通过：根据定义 Q = 1/T，若 T_post = 0.7 * T_pre，则 Q_post = 1/(0.7 * T_pre) = (1/0.7) * Q_pre ≈ 1.4286 * Q_pre，提升幅度为 1/0.7 - 1 ≈ 42.86%，四舍五入为 43%，数学推导自洽。

## Search Query

transaction cycle reduction impact on unit time sales volume
