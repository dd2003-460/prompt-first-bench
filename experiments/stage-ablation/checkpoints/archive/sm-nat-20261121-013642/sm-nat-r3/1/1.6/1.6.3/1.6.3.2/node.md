# N144: ΔCache 的对象数量占比工作点 2（小对象主导）：ΔCache 中对象数量占比 P_count_diff = |ΔCache| / N，在 β=0.9 平缓

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

ΔCache 的对象数量占比工作点 2（小对象主导）：ΔCache 中对象数量占比 P_count_diff = |ΔCache| / N，在 β=0.9 平缓热度下，该值可能高达 20-30%，表明 LFU 与 LRU 在对象集合上有显著差异，但字节影响小。

## Corrected Claim

ΔCache 的对象数量占比工作点 2（小对象主导）：ΔCache 中对象数量占比 P_count_diff = |ΔCache| / N，在 β=0.9 平缓热度下，该值可能高达 20-30%，表明 LFU 与 LRU 在对象集合上有显著差异，但字节影响小。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cache set difference object count ratio
