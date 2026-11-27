# N68: LFU 的计数器开销导致元数据占用缓存空间，128GB 中约 5-10% 被 LFU 频率计数器消耗，有效缓存容量降至 115-121GB，进一步压缩 LFU 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

LFU 的计数器开销导致元数据占用缓存空间，128GB 中约 5-10% 被 LFU 频率计数器消耗，有效缓存容量降至 115-121GB，进一步压缩 LFU 相对 LRU 的增益，需从 H_LFU 中扣除容量损失项 ΔH_capacity ≈ 5-10% * (1-H_LRU) [knowledge: 典型 LFU 实现开销]

## Corrected Claim

LFU 的计数器开销导致元数据占用缓存空间，128GB 中约 5-10% 被 LFU 频率计数器消耗，有效缓存容量降至 115-121GB，进一步压缩 LFU 相对 LRU 的增益，需从 H_LFU 中扣除容量损失项 ΔH_capacity ≈ 5-10% * (1-H_LRU) [knowledge: 典型 LFU 实现开销]

## Evidence

先验知识/题面给定，逻辑校验通过
