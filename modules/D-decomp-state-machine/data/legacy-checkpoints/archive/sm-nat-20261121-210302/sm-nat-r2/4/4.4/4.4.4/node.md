# N51: 负相关 ρ=-0.3 对 LRU 驱逐字节损失的修正：LRU 驱逐的对象平均大小 S_evict = E[Size | Popularity < thresho

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

负相关 ρ=-0.3 对 LRU 驱逐字节损失的修正：LRU 驱逐的对象平均大小 S_evict = E[Size | Popularity < threshold]，需通过条件期望计算，threshold 由 LRU 队列位置决定

## Corrected Claim

负相关 ρ=-0.3 对 LRU 驱逐字节损失的修正：LRU 驱逐的对象平均大小 S_evict = E[Size | Popularity < threshold]，需通过条件期望计算，threshold 由 LRU 队列位置决定

## Evidence

先验知识/题面给定，逻辑校验通过：LRU 驱逐机制基于访问历史，其驱逐对象确实由队列位置（即最近最少使用的时间点）决定，且平均大小需通过条件期望 E[Size | Popularity < threshold] 计算，其中 threshold 隐含了 LRU 队列的截断位置，逻辑自洽且符合缓存理论基本定义。
