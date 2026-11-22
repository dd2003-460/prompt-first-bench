# N291: Qwen3-27B 在 INT8 量化下于 HumanEval 简单函数子集（如 LeetCode Easy 级别或基础算法）的 Pass@1 基准值为 85.

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N93, N94, N96

## Claim

Qwen3-27B 在 INT8 量化下于 HumanEval 简单函数子集（如 LeetCode Easy 级别或基础算法）的 Pass@1 基准值为 85.0%（假设 BF16 基线为 86-87%），损失 1-2% 的量化依据是：该子集主要依赖局部上下文和简单语法结构，对权重梯度的敏感度低，量化噪声在解码时被概率分布平滑效应抵消。

## Corrected Claim

Qwen3-27B 在 INT8 量化下于 HumanEval 简单函数子集的 Pass@1 基准值预计会有轻微下降（通常约 1-2%），具体数值需参考官方或第三方评测报告，假设 BF16 基线为 86-87% 时，量化后可能在 84-85% 左右。

## Evidence

[质询]该陈述包含具体的经验性基准数值（85.0%）和特定的量化损失幅度（1-2%），属于经验事实。虽然量化导致性能轻微下降的逻辑在理论上成立，但具体的数值（85.0%）和针对特定子集（HumanEval简单函数）的精确损失幅度无法从第一性原理推导，且缺乏外部来源支持。 | 经验事实，逻辑自洽但缺来源支持。INT8量化通常会导致轻微性能下降，但具体数值85.0%及1-2%的损失幅度属于特定实验结果，无法仅凭逻辑推导验证，且本轮检索无可用来源。

## Search Query

Qwen3-27B INT8 quantization HumanEval simple functions Pass@1 accuracy benchmark
