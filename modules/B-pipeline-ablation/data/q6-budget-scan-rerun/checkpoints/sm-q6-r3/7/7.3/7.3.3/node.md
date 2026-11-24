# N373: 长尾区域公有云缓存命中率 CHR_pub_tail 的修正计算：CHR_pub_tail = CHR_pub_global × (1 - Δ_tail_pena

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N118

## Claim

长尾区域公有云缓存命中率 CHR_pub_tail 的修正计算：CHR_pub_tail = CHR_pub_global × (1 - Δ_tail_penalty)，其中 CHR_pub_global 为 N116 中的典型值 92%，Δ_tail_penalty 为长尾内容热度惩罚项，若长尾区域内容热度分布更分散（Zipf α 从 1.2 升至 1.5），命中率降低约 2%，即 CHR_pub_tail ≈ 90%。

## Corrected Claim

长尾区域公有云缓存命中率 CHR_pub_tail 的修正计算：CHR_pub_tail = CHR_pub_global × (1 - Δ_tail_penalty)，其中 CHR_pub_global 为 N116 中的典型值 92%，Δ_tail_penalty 为长尾内容热度惩罚项，若长尾区域内容热度分布更分散（Zipf α 从 1.2 升至 1.5），命中率降低约 2%，即 CHR_pub_tail ≈ 90%。

## Evidence

先验知识/题面给定，逻辑校验通过：92% * (1 - 2%) = 90.16% ≈ 90%，数值计算自洽，且符合长尾内容热度分散导致缓存命中率下降的直觉。
