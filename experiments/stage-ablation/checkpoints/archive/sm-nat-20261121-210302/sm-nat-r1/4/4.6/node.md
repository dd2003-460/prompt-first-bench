# N14: LFU 热点对象稳定保留机制：LFU 基于访问频率排序，热点对象（Pareto 头部）因频率高而长期驻留，其保留数量 N_hot 由频率阈值 F_th 决定，F

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

LFU 热点对象稳定保留机制：LFU 基于访问频率排序，热点对象（Pareto 头部）因频率高而长期驻留，其保留数量 N_hot 由频率阈值 F_th 决定，F_th 对应 Pareto 分布的分位数，需计算 F_th 使得前 N_hot 个对象覆盖的字节数最大化

## Corrected Claim

LFU 热点对象稳定保留机制：LFU 基于访问频率排序，热点对象（Pareto 头部）因频率高而长期驻留，其保留数量 N_hot 由频率阈值 F_th 决定，F_th 对应 Pareto 分布的分位数，需计算 F_th 使得前 N_hot 个对象覆盖的字节数最大化

## Evidence

先验知识/题面给定，逻辑校验通过：LFU 的核心机制即基于访问频率排序，高频对象（Pareto 头部）因频率高而长期驻留，保留数量由频率阈值决定，符合缓存替换算法的基本原理。

## Search Query

LFU frequency threshold hot object retention Pareto distribution
