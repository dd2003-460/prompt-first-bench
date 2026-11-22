# N464: 性能/成本归一化项计算：Norm_Perf_Cost = (Throughput_i / Cost_3yr_TCO_i) / max(Throughput_j 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N151, N152, N153

## Claim

性能/成本归一化项计算：Norm_Perf_Cost = (Throughput_i / Cost_3yr_TCO_i) / max(Throughput_j / Cost_3yr_TCO_j)，其中 max 取自所有通过 N151 可行性过滤的候选硬件集合，确保该项在 [0,1] 区间且最优硬件得分为 1.0 [knowledge]

## Corrected Claim

性能/成本归一化项计算：Norm_Perf_Cost = (Throughput_i / Cost_3yr_TCO_i) / max(Throughput_j / Cost_3yr_TCO_j)，其中 max 取自所有通过 N151 可行性过滤的候选硬件集合，确保该项在 [0,1] 区间且最优硬件得分为 1.0 [knowledge]

## Evidence

先验知识/题面给定，逻辑校验通过：归一化公式结构正确，除以最大值确保结果在[0,1]区间且最优值为1.0，符合数学定义。
