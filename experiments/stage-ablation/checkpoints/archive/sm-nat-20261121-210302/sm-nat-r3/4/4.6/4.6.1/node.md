# N59: 在 128GB 容量约束下，确定 LFU 热点集合大小 N_hot 的优化目标函数：Maximize P_hot_bytes(N_hot) = (Sum_{i=

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

在 128GB 容量约束下，确定 LFU 热点集合大小 N_hot 的优化目标函数：Maximize P_hot_bytes(N_hot) = (Sum_{i=1}^{N_hot} S_i * P_i) / (N * E[S])，其中 S_i 为第 i 热门对象大小，P_i 为热度，E[S] 为总体平均大小

## Corrected Claim

在 128GB 容量约束下，确定 LFU 热点集合大小 N_hot 的优化目标函数：Maximize P_hot_bytes(N_hot) = (Sum_{i=1}^{N_hot} S_i * P_i) / (N * E[S])，其中 S_i 为第 i 热门对象大小，P_i 为热度，E[S] 为总体平均大小

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应目标函数的分子（字节量计算）、分母（平均大小计算）、最优解的一阶条件（边际分析）以及约束条件（容量限制）。这四个维度在数学优化问题中是正交的，且共同构成了确定 N_hot 的完整逻辑链条，无冗余。）
