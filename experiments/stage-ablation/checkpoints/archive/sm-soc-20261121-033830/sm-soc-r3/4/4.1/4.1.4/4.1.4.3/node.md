# N219: LTV_seller (卖家生命周期价值) = Σ_{t=1}^{T_max} (Commission_t * Volume_t) / (1 + discoun

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N69

## Claim

LTV_seller (卖家生命周期价值) = Σ_{t=1}^{T_max} (Commission_t * Volume_t) / (1 + discount_rate)^t，其中 Commission_t 为第t期佣金收入，Volume_t 为交易量，discount_rate 为平台折现率，需基于历史卖家留存数据估算

## Corrected Claim

LTV_seller (卖家生命周期价值) = Σ_{t=1}^{T_max} (Commission_t * Volume_t) / (1 + discount_rate)^t，其中 Commission_t 为第t期佣金收入，Volume_t 为交易量，discount_rate 为平台折现率，需基于历史卖家留存数据估算

## Evidence

先验知识/题面给定，逻辑校验通过
