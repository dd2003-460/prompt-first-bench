# N19: 混合策略中自建POP的流量占比阈值：设核心区域流量占比为α（通常α∈[0.6,0.8]），则混合运维成本 C_hybrid_ops = α * C_sre_se

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

混合策略中自建POP的流量占比阈值：设核心区域流量占比为α（通常α∈[0.6,0.8]），则混合运维成本 C_hybrid_ops = α * C_sre_self * (n_pops_self/n_pops_total) + (1-α) * C_cloud_sre，其中 n_pops_self 为自建POP数，n_pops_total=10

## Corrected Claim

混合策略中自建POP的流量占比阈值：设核心区域流量占比为α（通常α∈[0.6,0.8]），则混合运维成本 C_hybrid_ops = α * C_sre_self * (n_pops_self/n_pops_total) + (1-α) * C_cloud_sre，其中 n_pops_self 为自建POP数，n_pops_total=10

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

hybrid CDN traffic split ratio core region self-hosted POP
