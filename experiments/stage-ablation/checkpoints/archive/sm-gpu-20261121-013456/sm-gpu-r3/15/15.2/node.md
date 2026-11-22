# N305: L40S 支持原生 FP8 加速，其 FP8 推理吞吐量预期为 BF16 的 1.8-2.0 倍，基于 A100 BF16 吞吐量 ~45 tokens/s 估

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N126

## Claim

L40S 支持原生 FP8 加速，其 FP8 推理吞吐量预期为 BF16 的 1.8-2.0 倍，基于 A100 BF16 吞吐量 ~45 tokens/s 估算，L40S FP8 吞吐量约为 81-90 tokens/s [待核验]，显著高于 A100 的 FP8 软件模拟性能。

## Corrected Claim

L40S 支持原生 FP8 加速，其 FP8 推理吞吐量预期为 BF16 的 1.8-2.0 倍，显著高于 A100 的 FP8 软件模拟性能。

## Evidence

[质询]吞吐量数值（81-90 tokens/s）高度依赖于具体的模型规模、序列长度及硬件配置，缺乏具体上下文时，该绝对数值缺乏普适性；且L40S与A100的架构差异（Ada Lovelace vs Ampere）使得直接基于A100 BF16吞吐量线性外推L40S FP8吞吐量存在方法论上的简化风险。 | 先验知识/题面给定，逻辑校验通过：L40S确实支持原生FP8，且FP8通常比BF16快约2倍，量级合理；但具体吞吐量数值为经验事实，无外部来源直接支持，故降级。

## Search Query

NVIDIA L40S FP8 inference performance benchmark tokens per second
