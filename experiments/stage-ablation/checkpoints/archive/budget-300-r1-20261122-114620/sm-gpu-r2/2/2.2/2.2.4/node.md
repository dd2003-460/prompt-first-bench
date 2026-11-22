# N61: AMD MI250X (128GB) 推理性能基准：ROCm 5.7 环境下 Qwen3-27B BF16 吞吐 45 tokens/s (batch=1)，比

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

AMD MI250X (128GB) 推理性能基准：ROCm 5.7 环境下 Qwen3-27B BF16 吞吐 45 tokens/s (batch=1)，比 H100 低 42%；128GB HBM3 显存可容纳 BF16 权重 + 64K KV cache (3.2GB) + 框架开销，但 ROCm 生态成熟度导致优化空间受限

## Corrected Claim

AMD MI250X (128GB) 在 ROCm 5.7 环境下运行 Qwen3-27B BF16 的推理性能通常低于 H100，具体吞吐量和差距取决于优化程度；128GB HBM3 显存足以容纳该模型权重及长上下文 KV cache，但 ROCm 生态成熟度可能限制其性能上限。

## Evidence

[质询]具体数值（45 tokens/s, 42%差距）属于特定硬件、软件版本及模型配置下的经验测量数据，无法从第一性原理推导，且缺乏来源支持，存在数值不准确或口径混淆的风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

AMD MI250X Qwen3-27B BF16 inference ROCm benchmark
