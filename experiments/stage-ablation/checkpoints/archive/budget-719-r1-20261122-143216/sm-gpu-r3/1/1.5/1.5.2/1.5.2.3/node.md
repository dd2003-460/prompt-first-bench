# N184: 在 HumanEval 代码生成任务上，Qwen3-27B NVFP4 量化模型的 Pass@1 通过率相比 BF16 基线通常下降 3.0% - 7.0%，主

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

在 HumanEval 代码生成任务上，Qwen3-27B NVFP4 量化模型的 Pass@1 通过率相比 BF16 基线通常下降 3.0% - 7.0%，主要源于 token 概率分布的离散化误差，若下降超过 7% 则判定为不可接受的质量损失

## Corrected Claim

在 HumanEval 代码生成任务上，Qwen3-27B NVFP4 量化模型的 Pass@1 通过率相比 BF16 基线通常会出现一定程度的下降（具体幅度取决于量化配置，常见范围可能在 3%-7% 左右），主要源于 token 概率分布的离散化误差；若下降幅度显著（如超过 7%），通常被视为不可接受的质量损失。

## Evidence

[质询]具体数值区间（3.0%-7.0%）及阈值（7%）属于特定实验条件下的经验数据，缺乏通用性，且不同量化实现（如校准集大小、校准算法）可能导致显著差异，直接断言'通常'下降该区间存在过度概括风险。 | source=knowledge，逻辑自洽（量化导致精度损失符合直觉，离散化误差是主要来源之一），但具体数值区间为经验事实，无外部来源直接支持，依据经验事实排除条款降级。

## Search Query

Qwen3 27B 4bit quantization HumanEval Pass@1 drop
