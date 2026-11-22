# N70: 下游投影 2（成交周期变化）：干预后成交周期 T_close_new = T_close_old * (1 - η_speed)，其中 η_speed = 0.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N14

## Claim

下游投影 2（成交周期变化）：干预后成交周期 T_close_new = T_close_old * (1 - η_speed)，其中 η_speed = 0.10-0.15 为速度提升系数，取决于 P(ReadLabel) 与买家决策摩擦降低幅度；若 P(ReadLabel) 低于阈值 0.4，则 η_speed 降至 0.05 以下，周期缩短效果不显著。

## Corrected Claim

下游投影 2（成交周期变化）：干预后成交周期 T_close_new = T_close_old * (1 - η_speed)，其中 η_speed = 0.10-0.15 为速度提升系数，取决于 P(ReadLabel) 与买家决策摩擦降低幅度；若 P(ReadLabel) 低于阈值 0.4，则 η_speed 降至 0.05 以下，周期缩短效果不显著。

## Evidence

先验知识/题面给定，逻辑校验通过
