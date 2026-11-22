# N141: 长窗口低污染工作点（Long-T/Low-Pollution）：当时间窗口 T 远大于 LRU 驱逐周期（T >> T_evict）时，被驱逐对象在 T 内再次

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

长窗口低污染工作点（Long-T/Low-Pollution）：当时间窗口 T 远大于 LRU 驱逐周期（T >> T_evict）时，被驱逐对象在 T 内再次被访问的概率趋近于 0，P_pollution ≈ 0，此时 LFU 相比 LRU 的增益主要来自长期频率差异而非短期重复访问，ΔH 趋近于 0，代表污染损失可忽略的状态。

## Corrected Claim

长窗口低污染工作点（Long-T/Low-Pollution）：当时间窗口 T 远大于 LRU 驱逐周期（T >> T_evict）时，被驱逐对象在 T 内再次被访问的概率趋近于 0，P_pollution ≈ 0，此时 LFU 相比 LRU 的增益主要来自长期频率差异而非短期重复访问，ΔH 趋近于 0，代表污染损失可忽略的状态。

## Evidence

先验知识/题面给定，逻辑校验通过：当时间窗口远大于驱逐周期时，LRU驱逐的对象在窗口内复访概率极低，污染损失趋近于0，LFU优势源于长期频率差异，符合缓存替换算法的基本原理。
