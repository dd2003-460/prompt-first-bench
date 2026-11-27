# N104: LRU 缓存驻留对象数量 K 的解析表达式：K = floor(128GB / E[s|C])，其中 E[s|C] 是条件截断 Pareto 分布的期望大小，需

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

LRU 缓存驻留对象数量 K 的解析表达式：K = floor(128GB / E[s|C])，其中 E[s|C] 是条件截断 Pareto 分布的期望大小，需通过数值积分计算以替代固定 K 值假设。

## Corrected Claim

LRU 缓存驻留对象数量 K 的解析表达式：K = floor(128GB / E[s|C])，其中 E[s|C] 是条件截断 Pareto 分布的期望大小，需通过数值积分计算以替代固定 K 值假设。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU缓存驻留对象数量K由总容量除以平均对象大小决定，公式K = floor(Capacity / E[size])在量纲和逻辑上自洽，且使用条件截断分布的期望值替代固定值假设符合统计建模原则。
