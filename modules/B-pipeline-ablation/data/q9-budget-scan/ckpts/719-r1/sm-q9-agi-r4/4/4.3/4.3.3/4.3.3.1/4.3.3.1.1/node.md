# N634: mpmath 与 NumPy 在矩阵乘法上的性能差距系数 k 随矩阵维度 d 变化，k(d) ≈ k_base × d^α，其中 k_base 在 d=100 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N226

## Claim

mpmath 与 NumPy 在矩阵乘法上的性能差距系数 k 随矩阵维度 d 变化，k(d) ≈ k_base × d^α，其中 k_base 在 d=100 时约为 50，α 约为 0.5-1.0，导致离线预计算时间 T_offline = k × T_Numpy 呈非线性增长

## Corrected Claim

mpmath 与 NumPy 在矩阵乘法上的性能差距系数 k 通常随矩阵维度 d 增加而增大，导致离线预计算时间 T_offline = k × T_Numpy 呈非线性增长，但具体系数 k_base 和指数 α 需根据实际基准测试确定。

## Evidence

[质询]该陈述包含具体的经验参数（k_base≈50, α≈0.5-1.0），这些数值并非第一性原理可推导，且缺乏来源支持，属于未经证实的经验断言。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

mpmath vs numpy matrix multiplication benchmark speedup ratio
