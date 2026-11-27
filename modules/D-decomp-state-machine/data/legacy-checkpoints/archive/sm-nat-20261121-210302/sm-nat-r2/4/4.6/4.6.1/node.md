# N59: 在 128GB 容量约束下，确定 LFU 热点集合大小 N_hot 的优化目标函数：Maximize P_hot_bytes(N_hot) = (Sum_{i=

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

在 128GB 容量约束下，确定 LFU 热点集合大小 N_hot 的优化目标函数：Maximize P_hot_bytes(N_hot) = (Sum_{i=1}^{N_hot} S_i * P_i) / (N * E[S])，其中 S_i 为第 i 热门对象大小，P_i 为热度，E[S] 为总体平均大小

## Corrected Claim

在 128GB 容量约束下，确定 LFU 热点集合大小 N_hot 的优化目标函数：Maximize P_hot_bytes(N_hot) = (Sum_{i=1}^{N_hot} S_i * P_i) / (N * E[S])，其中 S_i 为第 i 热门对象大小，P_i 为热度，E[S] 为总体平均大小

## Evidence

先验知识/题面给定，逻辑校验通过：该公式在数学上自洽，分子表示热点集合的加权字节数，分母表示总数据量，符合缓存优化中最大化热点覆盖率的定义。
