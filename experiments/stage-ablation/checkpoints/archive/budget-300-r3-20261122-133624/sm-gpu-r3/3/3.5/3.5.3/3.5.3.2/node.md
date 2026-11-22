# N289: GPTQ 算法在 FP8 量化场景下的适用性受限，因为 GPTQ 主要针对 INT4/INT8 设计，其基于 Hessian 矩阵的二阶优化在 FP8 的低动态

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N92

## Claim

GPTQ 算法在 FP8 量化场景下的适用性受限，因为 GPTQ 主要针对 INT4/INT8 设计，其基于 Hessian 矩阵的二阶优化在 FP8 的低动态范围下易陷入局部最优；若强行应用 GPTQ 进行 FP8 量化，校准数据量需 >5000 样本才能收敛，否则 MMLU 准确率损失将超过 1.5%，达到 2.0-2.5%。

## Corrected Claim

GPTQ 算法在 FP8 量化场景下的适用性受限，因为 GPTQ 主要针对 INT4/INT8 设计，其基于 Hessian 矩阵的二阶优化在 FP8 的低动态范围下易陷入局部最优；若强行应用 GPTQ 进行 FP8 量化，通常需要较大的校准数据量才能收敛，否则可能导致显著的准确率损失。

## Evidence

[质询]该陈述包含具体的经验性阈值（校准数据>5000样本、MMLU损失2.0-2.5%），这些数值并非GPTQ算法的通用理论推导结果，而是高度依赖于具体模型架构、数据集分布及实现细节的经验参数，缺乏普适性。 | 先验知识/题面给定，逻辑校验通过；但具体数值阈值属于经验事实，无来源支持，故降级。
