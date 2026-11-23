# N187: 跨域路径总跳数 N_hops 的分布模型：N_hops = N_intra_city + N_backbone + N_target_region，其中 N_i

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

跨域路径总跳数 N_hops 的分布模型：N_hops = N_intra_city + N_backbone + N_target_region，其中 N_intra_city≈1-2, N_backbone≈1-3, N_target_region≈1-2，总跳数 P99 约为 4-6 跳，直接决定 T_switch_total = N_hops * T_switch_per_hop

## Corrected Claim

跨域路径总跳数 N_hops 的分布模型：N_hops = N_intra_city + N_backbone + N_target_region，其中 N_intra_city≈1-2, N_backbone≈1-3, N_target_region≈1-2，总跳数 P99 约为 4-6 跳，直接决定 T_switch_total = N_hops * T_switch_per_hop

## Evidence

先验知识/题面给定，逻辑校验通过：跨域路径分解符合网络拓扑常识，跳数量级（1-2+1-3+1-2=3-7，P99 4-6）合理，公式 T_switch_total = N_hops * T_switch_per_hop 线性关系自洽。

## Search Query

ISP backbone network hop count distribution China cross-region latency
