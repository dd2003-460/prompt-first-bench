# N89: 混合策略月度总成本 C_total_hybrid = C_infra_self + C_bw_self + C_ops_self + C_bw_cloud + 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

混合策略月度总成本 C_total_hybrid = C_infra_self + C_bw_self + C_ops_self + C_bw_cloud + C_req_cloud，其中 C_infra_self 为自建10个POP的基础设施摊销，C_bw_self 为自建节点出网带宽成本，C_ops_self 为自建运维人力成本，C_bw_cloud 为公有云流量费，C_req_cloud 为公有云请求数费用。

## Corrected Claim

混合策略月度总成本 C_total_hybrid = C_infra_self + C_bw_self + C_ops_self + C_bw_cloud + C_req_cloud，其中 C_infra_self 为自建10个POP的基础设施摊销，C_bw_self 为自建节点出网带宽成本，C_ops_self 为自建运维人力成本，C_bw_cloud 为公有云流量费，C_req_cloud 为公有云请求数费用。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点清晰对应父节点公式中的5个成本分项，并额外增加了归一化指标（单位成本），各分项定义独立无重叠，且涵盖了从固定摊销到变动流量的所有关键成本维度，逻辑完备且无冗余。）
