# N11: LFU最大理论提升百分点 = (LFU命中率 - LRU命中率) * 100%，其中LFU命中率基于对象累计访问频率排序，在热度稳定且局部性强的工作负载下，LF

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

LFU最大理论提升百分点 = (LFU命中率 - LRU命中率) * 100%，其中LFU命中率基于对象累计访问频率排序，在热度稳定且局部性强的工作负载下，LFU能保留长期热门对象，避免LRU的频繁驱逐。

## Corrected Claim

LFU最大理论提升百分点 = (LFU命中率 - LRU命中率) * 100%，其中LFU命中率基于对象累计访问频率排序，在热度稳定且局部性强的工作负载下，LFU能保留长期热门对象，避免LRU的频繁驱逐。

## Evidence

先验知识/题面给定，逻辑校验通过
