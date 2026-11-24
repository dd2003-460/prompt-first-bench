# N78: 混合策略总基础设施成本 C_infra_mix 为自建部分与公有云部分的加权平均，即 C_infra_mix = P_core * C_infra_self_p

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

混合策略总基础设施成本 C_infra_mix 为自建部分与公有云部分的加权平均，即 C_infra_mix = P_core * C_infra_self_per_req + (1-P_core) * C_infra_cloud_per_req，其中 P_core 为核心区域流量占比。

## Corrected Claim

混合策略总基础设施成本 C_infra_mix 为自建部分与公有云部分的加权平均，即 C_infra_mix = P_core * C_infra_self_per_req + (1-P_core) * C_infra_cloud_per_req，其中 P_core 为核心区域流量占比。

## Evidence

先验知识/题面给定，逻辑校验通过
