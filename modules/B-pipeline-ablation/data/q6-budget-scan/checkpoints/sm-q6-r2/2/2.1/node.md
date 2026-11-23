# N11: 每千请求总成本公式：C_total/1000req = (C_infra + C_bandwidth + C_ops) / (R_daily / 1000)，其

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

每千请求总成本公式：C_total/1000req = (C_infra + C_bandwidth + C_ops) / (R_daily / 1000)，其中R_daily为日请求总数

## Corrected Claim

每千请求总成本公式：C_total/1000req = (C_infra + C_bandwidth + C_ops) / (R_daily / 1000)，其中R_daily为日请求总数

## Evidence

父节点级核验未通过：不完备（子节点仅描述了一种特定的架构方案（全自建边缘节点），未能覆盖父节点公式中涉及的通用成本构成（基础设施、带宽、运维）及其与请求量的通用关系。父节点是一个通用的成本计算模型，而子节点是一个具体的实例化场景，导致内容严重缺失。）
