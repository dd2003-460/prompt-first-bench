# N178: RTX 4090 运行 Qwen3-27B FP8 量化时，单卡吞吐实测为 42 tokens/s (batch=1, seq=2048)，相比 INT8 提升

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

RTX 4090 运行 Qwen3-27B FP8 量化时，单卡吞吐实测为 42 tokens/s (batch=1, seq=2048)，相比 INT8 提升 50%，主要因 FP8 数据带宽减半且 Tensor Core 对 FP8 有原生加速支持，但 FP8 量化在 27B 模型上的质量损失需单独评估

## Corrected Claim

RTX 4090 运行 Qwen3-27B FP8 量化时，单卡吞吐通常显著高于 INT8（因 FP8 数据带宽减半且 Tensor Core 原生加速），具体数值（如 42 tokens/s）需视具体软件栈和实现而定，FP8 量化在 27B 模型上的质量损失需单独评估

## Evidence

[质询]具体数值（42 tokens/s）和性能提升比例（50%）属于特定硬件、软件栈及量化实现下的经验测量值，无法从第一性原理严格推导，且缺乏外部来源佐证其准确性。 | 先验知识/题面给定，逻辑校验通过：FP8相比INT8在带宽和Tensor Core支持上确有优势，量级合理，但具体实测数值为经验事实，缺来源支持。

## Search Query

RTX 4090 Qwen3-27B FP8 inference speed tokens per second
