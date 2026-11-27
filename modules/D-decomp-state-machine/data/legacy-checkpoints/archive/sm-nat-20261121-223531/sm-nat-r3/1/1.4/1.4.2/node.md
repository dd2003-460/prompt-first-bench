# N36: 缓存有效容量的约束并非来自总对象数，而是来自‘热工作集’（Hot Working Set）的大小：由于热度 Pareto(β=0.9) 极度偏斜，前 10% 的

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

缓存有效容量的约束并非来自总对象数，而是来自‘热工作集’（Hot Working Set）的大小：由于热度 Pareto(β=0.9) 极度偏斜，前 10% 的对象承载了约 50% 的请求流量，其总字节大小 E[Size|Top10%] 约为总字节流量的 20-30%，需计算该热工作集的总字节数是否小于 128GB 以确定 LRU 是否实际发生淘汰。

## Corrected Claim

缓存有效容量的约束并非来自总对象数，而是来自‘热工作集’（Hot Working Set）的大小：由于热度 Pareto(β=0.9) 极度偏斜，前 10% 的对象承载了约 50% 的请求流量，其总字节大小 E[Size|Top10%] 约为总字节流量的 20-30%，需计算该热工作集的总字节数是否小于 128GB 以确定 LRU 是否实际发生淘汰。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布(β=0.9)下前10%对象承载约50%流量符合幂律特性，热工作集字节占比20-30%在逻辑上自洽且量级合理，用于判断LRU淘汰是标准缓存分析逻辑。

## Search Query

hot working set size Pareto distribution cache eviction threshold
