# N462: Qwen3-27B 在 INT4 (AWQ/GPTQ) 量化后 GSM8K 准确率为 87.0% - 89.0%，绝对下降幅度 ΔGSM8K 为 2-4 个百分

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N191

## Claim

Qwen3-27B 在 INT4 (AWQ/GPTQ) 量化后 GSM8K 准确率为 87.0% - 89.0%，绝对下降幅度 ΔGSM8K 为 2-4 个百分点；主要归因于 4-bit 权重量化导致的注意力头数值截断误差在长链推理中累积，参考 Llama-2-70B INT4 AWQ 在 GSM8K 上约 3% 的性能损失 [时效待核]。

## Corrected Claim

Qwen3-27B 在 INT4 (AWQ/GPTQ) 量化后 GSM8K 准确率通常维持在较高水平（约 85%-90% 区间），绝对下降幅度约为 2-4 个百分点；性能损失主要归因于 4-bit 权重量化引入的数值误差在长链推理中的累积效应。

## Evidence

[质询]具体数值（87.0%-89.0%）及归因机制（注意力头数值截断误差累积）属于特定模型版本的经验性观测结果，无法从第一性原理严格推导，且不同量化实现（AWQ vs GPTQ）及评测设置可能导致数值波动，缺乏直接来源支持具体区间。 | 先验知识/题面给定，逻辑校验通过；但具体准确率区间及归因细节为经验事实，无外部来源直接支持，依据经验事实排除条款降级。

## Search Query

Qwen3 INT4 AWQ GSM8K accuracy drop
