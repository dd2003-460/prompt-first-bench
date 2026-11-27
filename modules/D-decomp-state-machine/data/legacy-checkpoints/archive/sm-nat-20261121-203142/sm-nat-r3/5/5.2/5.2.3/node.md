# N68: LFU 的计数器开销导致元数据占用缓存空间，128GB 中约 5-10% 被 LFU 频率计数器消耗，有效缓存容量降至 115-121GB，进一步压缩 LFU 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

LFU 的计数器开销导致元数据占用缓存空间，128GB 中约 5-10% 被 LFU 频率计数器消耗，有效缓存容量降至 115-121GB，进一步压缩 LFU 相对 LRU 的增益，需从 H_LFU 中扣除容量损失项 ΔH_capacity ≈ 5-10% * (1-H_LRU) [knowledge: 典型 LFU 实现开销]

## Corrected Claim

LFU 的计数器开销导致元数据占用缓存空间，128GB 中约 5-10% 被 LFU 频率计数器消耗，有效缓存容量降至 115-121GB，进一步压缩 LFU 相对 LRU 的增益，需从 H_LFU 中扣除容量损失项 ΔH_capacity ≈ 5-10% * (1-H_LRU) [knowledge: 典型 LFU 实现开销]

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点仅列举了5%和10%两个离散点，未能覆盖父节点中'5-10%'的连续区间（如中间值），导致完备性缺失；同时，两个子节点本质上是同一计算公式在不同参数下的实例化，属于高度冗余，应合并为通用公式并列出参数范围。）
