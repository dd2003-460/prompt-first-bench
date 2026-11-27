# N263: Qwen3-27B 在 FP8 精度下，GSM8K 数学推理基准测试准确率相比 BF16 基线下降具体数值（预期 <0.5%，需验证 MoE 架构在量化下对逻辑

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N93

## Claim

Qwen3-27B 在 FP8 精度下，GSM8K 数学推理基准测试准确率相比 BF16 基线下降具体数值（预期 <0.5%，需验证 MoE 架构在量化下对逻辑链保持能力的敏感性）

## Corrected Claim

Qwen3-27B 在 FP8 精度下，GSM8K 数学推理基准测试准确率相比 BF16 基线可能存在轻微下降，具体数值需实测验证，通常预期在较小范围内（如 <0.5%），但缺乏直接来源证实。

## Evidence

[质询]该陈述包含具体的经验性数值预期（<0.5%）和特定模型（Qwen3-27B）在特定精度（FP8）下的性能表现，属于硬件/模型规格类的经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B FP8 GSM8K accuracy drop vs BF16
