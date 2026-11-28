# N286: 代码执行时间 T_exec 的分布特征：对于纯 Python/Numpy 数值模拟，T_exec 服从对数正态分布，中位数 < 0.5s，但 95th 百分位 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

代码执行时间 T_exec 的分布特征：对于纯 Python/Numpy 数值模拟，T_exec 服从对数正态分布，中位数 < 0.5s，但 95th 百分位 (P95) 可达 5-10s（涉及大型矩阵运算或迭代求解时），取保守值 T_exec_p95 = 8s 用于最坏情况延迟估算。

## Corrected Claim

代码执行时间 T_exec 的分布特征：对于纯 Python/Numpy 数值模拟，T_exec 服从对数正态分布，中位数 < 0.5s，但 95th 百分位 (P95) 可达 5-10s（涉及大型矩阵运算或迭代求解时），取保守值 T_exec_p95 = 8s 用于最坏情况延迟估算。

## Evidence

先验知识/题面给定，逻辑校验通过
