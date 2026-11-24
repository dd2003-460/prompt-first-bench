# N530: 地理分布从集中（80/20）变为分散（50/50）时，混合策略固定成本摊销 C_fixed_per_req 的上升幅度：C_fixed_per_req_mix 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N174

## Claim

地理分布从集中（80/20）变为分散（50/50）时，混合策略固定成本摊销 C_fixed_per_req 的上升幅度：C_fixed_per_req_mix 从 (C_fixed_self / Q_core) 变为 (C_fixed_self / (0.5*Q_total))，即固定成本分摊基数减半，导致单位请求固定成本翻倍，这是混合策略在长尾流量增加时成本劣势的核心机制。

## Corrected Claim

地理分布从集中（80/20）变为分散（50/50）时，混合策略固定成本摊销 C_fixed_per_req 的上升幅度：C_fixed_per_req_mix 从 (C_fixed_self / Q_core) 变为 (C_fixed_self / (0.5*Q_total))，即固定成本分摊基数减半，导致单位请求固定成本翻倍，这是混合策略在长尾流量增加时成本劣势的核心机制。

## Evidence

先验知识/题面给定，逻辑校验通过：固定成本总额不变，分摊基数从 Q_core 变为 0.5*Q_total，若 Q_core 与 Q_total 量级相当或 Q_core 接近 Q_total 的 50% 以上，则单位固定成本确实显著上升（接近翻倍），符合成本摊销的基本经济逻辑。
