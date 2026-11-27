# N85: LTV_seller 的计算模型：LTV_seller = Σ_{t=1}^{T} (Commission * GMV_seller(t) - C_servic

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

LTV_seller 的计算模型：LTV_seller = Σ_{t=1}^{T} (Commission * GMV_seller(t) - C_service(t)) * (1 - d)^t，其中 T 为卖家预期留存期，GMV_seller(t) 为第 t 期卖家成交额，C_service(t) 为第 t 期服务成本，d 为折现率

## Corrected Claim

LTV_seller 的计算模型：LTV_seller = Σ_{t=1}^{T} (Commission * GMV_seller(t) - C_service(t)) * (1 - d)^t，其中 T 为卖家预期留存期，GMV_seller(t) 为第 t 期卖家成交额，C_service(t) 为第 t 期服务成本，d 为折现率

## Evidence

先验知识/题面给定，逻辑校验通过
