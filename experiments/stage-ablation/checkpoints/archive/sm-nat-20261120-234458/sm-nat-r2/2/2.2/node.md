# N10: LFU 增益的热度分布特征：当 β < 1.5 时，LFU 显著优于 LRU；当 β > 2 时，LFU 优势缩小；β=0.9 属于强头部集中，LFU 增益上限

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

LFU 增益的热度分布特征：当 β < 1.5 时，LFU 显著优于 LRU；当 β > 2 时，LFU 优势缩小；β=0.9 属于强头部集中，LFU 增益上限 ≈ (1 - F(0.1)) / (1 - F(0.5)) * 100%，F 为热度 Pareto CDF

## Corrected Claim

LFU 增益的热度分布特征：当 β < 1.5 时，LFU 显著优于 LRU；当 β > 2 时，LFU 优势缩小；β=0.9 属于强头部集中，LFU 增益上限 ≈ (1 - F(0.1)) / (1 - F(0.5)) * 100%，F 为热度 Pareto CDF

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU LRU performance Pareto exponent threshold
