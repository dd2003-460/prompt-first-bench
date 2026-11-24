# N162: D2 成本排序中的基础设施成本占比 C_infra_share = C_infra / C_total_per_1000req，对于公有云 CDN 策略，C_i

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

D2 成本排序中的基础设施成本占比 C_infra_share = C_infra / C_total_per_1000req，对于公有云 CDN 策略，C_infra 通常包含节点资源摊销（若包月）或纯请求计费（若按量），需明确区分是‘资源成本’还是‘请求成本’，避免与带宽成本重复计算

## Corrected Claim

D2 成本排序中的基础设施成本占比 C_infra_share = C_infra / C_total_per_1000req，对于公有云 CDN 策略，C_infra 通常包含节点资源摊销（若包月）或纯请求计费（若按量），需明确区分是‘资源成本’还是‘请求成本’，避免与带宽成本重复计算

## Evidence

先验知识/题面给定，逻辑校验通过
