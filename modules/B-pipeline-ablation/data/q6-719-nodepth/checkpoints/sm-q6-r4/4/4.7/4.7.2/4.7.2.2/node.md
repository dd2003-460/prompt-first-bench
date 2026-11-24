# N405: 自建POP节点内存缓存查找时间 T_mem 的P99估算值为 1-2ms，基于DRAM随机访问延迟 100ns 及单次请求平均 10k 次内存访问的计算：T_m

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N126

## Claim

自建POP节点内存缓存查找时间 T_mem 的P99估算值为 1-2ms，基于DRAM随机访问延迟 100ns 及单次请求平均 10k 次内存访问的计算：T_mem = 10k * 100ns = 1ms。

## Corrected Claim

自建POP节点内存缓存查找时间 T_mem 的P99估算值为 1-2ms，基于DRAM随机访问延迟 100ns 及单次请求平均 10k 次内存访问的计算：T_mem = 10k * 100ns = 1ms。

## Evidence

先验知识/题面给定，逻辑校验通过：10,000次访问 * 100ns/次 = 1,000,000ns = 1ms，计算无误且符合DRAM延迟量级常识。
