# N294: Qwen3-27B 在 W4 量化下于 HumanEval 简单函数子集的 Pass@1 基准值为 82.0%（假设 BF16 基线为 86-87%），损失 3

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N93, N94, N96

## Claim

Qwen3-27B 在 W4 量化下于 HumanEval 简单函数子集的 Pass@1 基准值为 82.0%（假设 BF16 基线为 86-87%），损失 3-4% 的量化依据是：W4 量化将权重精度降低至 4 比特，导致激活值分布的长尾部分被截断，简单函数中虽对精度要求较低，但截断误差仍足以改变某些边界条件判断，导致通过率下降。

## Corrected Claim

Qwen3-27B 在 W4 量化下于 HumanEval 简单函数子集的 Pass@1 基准值预计会有所下降（例如损失 3-4%），具体数值需参考官方或第三方评测报告。

## Evidence

[质询]具体数值（82.0%、86-87%）及特定模型（Qwen3-27B）在特定量化配置下的基准测试结果为经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B W4 quantization HumanEval simple functions Pass@1 accuracy benchmark
