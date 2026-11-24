# N19: 混合策略的资源利用率模型：利用率 U_hybrid = (B_served_core / C_core_self) × w_core + (B_served_t

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

混合策略的资源利用率模型：利用率 U_hybrid = (B_served_core / C_core_self) × w_core + (B_served_tail / B_peak_pub_tail) × w_tail，其中 w_core 和 w_tail 分别为核心区域和长尾区域的流量权重，B_served_core 由核心区域（如中国东部/美国东部）的地理分布决定，B_served_tail 为剩余流量，混合策略的目标是将自建部分利用率维持在 50%–70%，公有云部分按量付费无预留浪费。

## Corrected Claim

混合策略的资源利用率模型：利用率 U_hybrid = (B_served_core / C_core_self) × w_core + (B_served_tail / B_peak_pub_tail) × w_tail，其中 w_core 和 w_tail 分别为核心区域和长尾区域的流量权重，B_served_core 由核心区域（如中国东部/美国东部）的地理分布决定，B_served_tail 为剩余流量，混合策略的目标是将自建部分利用率维持在 50%–70%，公有云部分按量付费无预留浪费。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

hybrid CDN architecture core region self-hosted tail region public cloud traffic split ratio
