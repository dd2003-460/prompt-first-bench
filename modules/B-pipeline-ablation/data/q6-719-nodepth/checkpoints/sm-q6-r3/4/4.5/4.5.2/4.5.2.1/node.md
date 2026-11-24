# N376: POP-L1 缓存命中率 H_L1_self 的计算公式为 H_L1_self = 1 - (Miss_Rate_L1)，其中 Miss_Rate_L1 基于对

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N116

## Claim

POP-L1 缓存命中率 H_L1_self 的计算公式为 H_L1_self = 1 - (Miss_Rate_L1)，其中 Miss_Rate_L1 基于对象访问频率分布（Zipf 分布参数 s_zipf）与 L1 缓存容量 C_pop_L1 (GB) 及平均对象大小 s_weighted 的比值计算，典型值为 0.7-0.85。

## Corrected Claim

POP-L1 缓存命中率 H_L1_self 的计算公式为 H_L1_self = 1 - (Miss_Rate_L1)，其中 Miss_Rate_L1 基于对象访问频率分布（Zipf 分布参数 s_zipf）与 L1 缓存容量 C_pop_L1 (GB) 及平均对象大小 s_weighted 的比值计算，典型值为 0.7-0.85。

## Evidence

先验知识/题面给定，逻辑校验通过：命中率与失效率互补关系成立，Zipf分布下L1缓存命中率0.7-0.85符合典型工程经验量级
