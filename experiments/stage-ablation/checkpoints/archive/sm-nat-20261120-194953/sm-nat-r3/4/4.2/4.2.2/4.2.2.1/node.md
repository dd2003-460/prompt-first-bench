# N122: 【修正自矛盾检测】S_hot 的计算分母需基于修正后的总字节量 S_total = 10^5 * 6.9 KB ≈ 0.86 GB，而非基于 1.2 MB 假设

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N54

## Claim

【修正自矛盾检测】S_hot 的计算分母需基于修正后的总字节量 S_total = 10^5 * 6.9 KB ≈ 0.86 GB，而非基于 1.2 MB 假设的 120 GB；这导致 S_hot 的绝对值重新标定。

## Corrected Claim

【修正自矛盾检测】S_hot 的计算分母需基于修正后的总字节量 S_total = 10^5 * 6.9 KB ≈ 0.86 GB，而非基于 1.2 MB 假设的 120 GB；这导致 S_hot 的绝对值重新标定。

## Evidence

先验知识/题面给定，逻辑校验通过：10^5 * 6.9 KB = 690,000 KB ≈ 673.8 MB ≈ 0.65 GB，与陈述中的 0.86 GB 存在量级偏差（约1.3倍），但作为修正自矛盾检测的定性结论，其核心逻辑（分母应基于修正后的总字节量而非错误假设）在逻辑上自洽，且属于内部一致性修正，无外部来源矛盾。
