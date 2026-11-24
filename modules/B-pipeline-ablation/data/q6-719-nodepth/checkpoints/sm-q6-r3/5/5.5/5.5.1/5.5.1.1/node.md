# N465: 运维人员配置比例 1人/3个POP (N_ops = N_pop/3) 是基于每个 POP 点日均处理请求量 Q_pop 与故障响应 SLA（MTTR < 30

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N148

## Claim

运维人员配置比例 1人/3个POP (N_ops = N_pop/3) 是基于每个 POP 点日均处理请求量 Q_pop 与故障响应 SLA（MTTR < 30min）的工作负载模型推导，当 N_pop < 6 时，由于最低人力成本约束，实际配置需向上取整至 2 人，导致人均管理 POP 数 > 3，边际运维效率下降。

## Corrected Claim

运维人员配置比例 1人/3个POP (N_ops = N_pop/3) 是基于每个 POP 点日均处理请求量 Q_pop 与故障响应 SLA（MTTR < 30min）的工作负载模型推导，当 N_pop < 6 时，由于最低人力成本约束，实际配置需向上取整至 2 人，导致人均管理 POP 数 > 3，边际运维效率下降。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN operations staff ratio per POP node MTTR SLA
