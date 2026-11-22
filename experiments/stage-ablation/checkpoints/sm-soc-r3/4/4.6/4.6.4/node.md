# N85: LTV_seller 的计算模型：LTV_seller = Σ_{t=1}^{T} (Commission * GMV_seller(t) - C_servic

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

LTV_seller 的计算模型：LTV_seller = Σ_{t=1}^{T} (Commission * GMV_seller(t) - C_service(t)) * (1 - d)^t，其中 T 为卖家预期留存期，GMV_seller(t) 为第 t 期卖家成交额，C_service(t) 为第 t 期服务成本，d 为折现率

## Corrected Claim

LTV_seller 的计算模型：LTV_seller = Σ_{t=1}^{T} (Commission * GMV_seller(t) - C_service(t)) * (1 - d)^t，其中 T 为卖家预期留存期，GMV_seller(t) 为第 t 期卖家成交额，C_service(t) 为第 t 期服务成本，d 为折现率

## Evidence

父节点级核验未通过：不完备（子节点分别描述了模型中的时间参数T、折现率d和成本/收益参数，彼此之间正交且不重复。然而，父节点公式中的核心变量 GMV_seller(t)（卖家成交额）未在子节点中定义或给出典型分布/估算方法，导致模型无法实际计算，存在关键要素缺失。）
