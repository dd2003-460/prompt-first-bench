# N271: 流量分配比例 F_self 的确定公式：F_self = (Traffic_core_regions / Total_Traffic)，其中 Traffic_c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N90

## Claim

流量分配比例 F_self 的确定公式：F_self = (Traffic_core_regions / Total_Traffic)，其中 Traffic_core_regions 为覆盖在自建 POP 辐射半径（如 200km）内的用户请求量；基于中国一线及新一线城市用户占比约 35%-40%，假设 F_self ∈ [0.35, 0.40]，F_cloud = 1 - F_self。

## Corrected Claim

流量分配比例 F_self 的确定公式：F_self = (Traffic_core_regions / Total_Traffic)，其中 Traffic_core_regions 为覆盖在自建 POP 辐射半径（如 200km）内的用户请求量；基于中国一线及新一线城市用户占比约 35%-40%，假设 F_self ∈ [0.35, 0.40]，F_cloud = 1 - F_self。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

China mobile internet user distribution tier 1 and new tier 1 cities percentage 2024
