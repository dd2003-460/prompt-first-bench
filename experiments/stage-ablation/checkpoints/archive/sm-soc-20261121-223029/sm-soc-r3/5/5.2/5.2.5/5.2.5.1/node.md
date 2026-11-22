# N311: 成交速度指标 Velocity 的量化定义：Velocity_t = N_deals_t / N_listings_active_t，其中 N_deals_t 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

成交速度指标 Velocity 的量化定义：Velocity_t = N_deals_t / N_listings_active_t，其中 N_deals_t 为第 t 小时内的成交笔数，N_listings_active_t 为第 t 小时处于活跃状态（未下架且未成交）的商品数；需计算 24 小时内的平均 Velocity_avg 及其标准差。

## Corrected Claim

成交速度指标 Velocity 的量化定义：Velocity_t = N_deals_t / N_listings_active_t，其中 N_deals_t 为第 t 小时内的成交笔数，N_listings_active_t 为第 t 小时处于活跃状态（未下架且未成交）的商品数；需计算 24 小时内的平均 Velocity_avg 及其标准差。

## Evidence

先验知识/题面给定，逻辑校验通过
