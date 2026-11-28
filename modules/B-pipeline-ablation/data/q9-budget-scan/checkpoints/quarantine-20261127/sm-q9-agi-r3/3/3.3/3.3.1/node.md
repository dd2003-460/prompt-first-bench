# N67: Redis 热数据层存储最近 24h 的中间推理状态，键空间大小受限于 16GB 内存，最大支持约 200万条 8KB 记录，超出后触发 LRU 淘汰策略。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

Redis 热数据层存储最近 24h 的中间推理状态，键空间大小受限于 16GB 内存，最大支持约 200万条 8KB 记录，超出后触发 LRU 淘汰策略。

## Corrected Claim

Redis 热数据层存储最近 24h 的中间推理状态，键空间大小受限于 16GB 内存，最大支持约 200万条 8KB 记录，超出后触发 LRU 淘汰策略。

## Evidence

先验知识/题面给定，逻辑校验通过：16GB内存除以8KB单条记录大小，理论上限约为200万条（16*1024*1024/8 = 2,097,152），数值量级与逻辑自洽。
