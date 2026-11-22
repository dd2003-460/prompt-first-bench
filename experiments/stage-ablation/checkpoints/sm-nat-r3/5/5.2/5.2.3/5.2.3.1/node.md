# N224: LFU 的缓存保留集合 S_LFU 由频率阈值 f_threshold 决定，该阈值是满足容量约束 Σ_{i∈S_LFU} s_i ≤ 128GB 的最小频率，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

LFU 的缓存保留集合 S_LFU 由频率阈值 f_threshold 决定，该阈值是满足容量约束 Σ_{i∈S_LFU} s_i ≤ 128GB 的最小频率，其具体数值取决于 Pareto(β=0.9) 热度分布的截断参数 r_max 和对象大小分布的联合耦合。

## Corrected Claim

LFU 的缓存保留集合 S_LFU 由频率阈值 f_threshold 决定，该阈值是满足容量约束 Σ_{i∈S_LFU} s_i ≤ 128GB 的最小频率，其具体数值取决于 Pareto(β=0.9) 热度分布的截断参数 r_max 和对象大小分布的联合耦合。

## Evidence

先验知识/题面给定，逻辑校验通过：LFU 基于频率排序，在固定容量约束下，保留集合确实由满足容量上限的最小频率阈值决定，且该阈值数值依赖于热度分布（Pareto）和大小分布的联合统计特性，逻辑自洽且符合缓存理论基本原理。

## Search Query

LFU cache frequency threshold calculation Pareto distribution
