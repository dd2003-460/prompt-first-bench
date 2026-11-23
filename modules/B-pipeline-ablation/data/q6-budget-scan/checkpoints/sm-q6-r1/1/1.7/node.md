# N12: 混合策略每千请求总成本计算公式为 C_total_hybrid = (Q_core / Q_total) * C_per_req_self + (Q_tail 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

混合策略每千请求总成本计算公式为 C_total_hybrid = (Q_core / Q_total) * C_per_req_self + (Q_tail / Q_total) * C_per_req_cloud，其中 Q_core 和 Q_tail 分别为核心区域和长尾区域的请求量占比，C_per_req_self 和 C_per_req_cloud 分别为自建和公有云的每千请求成本。

## Corrected Claim

混合策略每千请求总成本计算公式为 C_total_hybrid = (Q_core / Q_total) * C_per_req_self + (Q_tail / Q_total) * C_per_req_cloud，其中 Q_core 和 Q_tail 分别为核心区域和长尾区域的请求量占比，C_per_req_self 和 C_per_req_cloud 分别为自建和公有云的每千请求成本。

## Evidence

先验知识/题面给定，逻辑校验通过
