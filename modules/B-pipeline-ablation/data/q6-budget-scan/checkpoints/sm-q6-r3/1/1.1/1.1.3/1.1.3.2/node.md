# N119: 地理熵对回源率 p_miss 的边际影响公式：Δp_miss/ΔH_geo = k_entropy * (1 - H_edge_max)，其中 k_entrop

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

地理熵对回源率 p_miss 的边际影响公式：Δp_miss/ΔH_geo = k_entropy * (1 - H_edge_max)，其中 k_entropy 为熵敏感度系数（通常 0.05-0.1），H_edge_max 为理论最大命中率；当 H_geo 从 3.0 增至 4.0 bits 时，p_miss 增加约 2-4%，对应带宽成本增加 ¥40-80/月（基于 2TB 日均流量）。

## Corrected Claim

在特定缓存架构下，地理熵对回源率的边际影响可近似表示为 Δp_miss/ΔH_geo ≈ k_entropy * (1 - H_edge_max)，其中 k_entropy 为经验敏感度系数（典型值 0.05-0.1）；当 H_geo 从 3.0 增至 4.0 bits 时，p_miss 预计增加约 2-4%，对应带宽成本增加约 ¥40-80/月（基于 2TB 日均流量估算）。

## Evidence

[质询]该公式及具体数值（k_entropy 0.05-0.1, 成本 ¥40-80/月）缺乏通用理论或行业标准支持，属于特定场景下的经验拟合参数，存在口径混淆风险（如将特定业务场景的统计结果泛化为通用公式）。 | 先验知识/题面给定，逻辑校验通过（量纲与量级在工程估算中合理），但作为经验事实缺乏外部来源直接支持，故降级。

## Search Query

geographic entropy impact on CDN cache miss rate marginal cost bandwidth
