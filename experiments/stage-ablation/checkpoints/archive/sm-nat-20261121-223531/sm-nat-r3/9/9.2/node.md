# N80: 容量受限下 LFU 相对 LRU 的增益上限公式：ΔH_max = H_LFU - H_LRU，其中 H_LFU 基于频率阈值 h_th 保留对象，h_th 由

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

容量受限下 LFU 相对 LRU 的增益上限公式：ΔH_max = H_LFU - H_LRU，其中 H_LFU 基于频率阈值 h_th 保留对象，h_th 由缓存容量 C 和对象大小-频率联合分布确定；增益源于 LFU 优先保留高频对象，即使其大小较大，而 LRU 可能因时间局部性不足淘汰高频但近期未访问的对象。

## Corrected Claim

容量受限下 LFU 相对 LRU 的增益上限公式：ΔH_max = H_LFU - H_LRU，其中 H_LFU 基于频率阈值 h_th 保留对象，h_th 由缓存容量 C 和对象大小-频率联合分布确定；增益源于 LFU 优先保留高频对象，即使其大小较大，而 LRU 可能因时间局部性不足淘汰高频但近期未访问的对象。

## Evidence

先验知识/题面给定，逻辑校验通过
