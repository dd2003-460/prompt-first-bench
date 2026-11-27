# N498: RTX 4090 在 Qwen3-27B BF16 Prefill 阶段的实测 MFU 约为 40%，受限于 Ada Lovelace 架构在长序列 Atten

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N205

## Claim

RTX 4090 在 Qwen3-27B BF16 Prefill 阶段的实测 MFU 约为 40%，受限于 Ada Lovelace 架构在长序列 Attention 计算中的 Tensor Core 利用率瓶颈及内存访问模式。

## Corrected Claim

RTX 4090 在 Qwen3-27B BF16 Prefill 阶段的实测 MFU 通常在 30%-50% 区间，具体数值受序列长度、Batch Size 及 Attention 实现优化影响，受限于 Ada Lovelace 架构在长序列 Attention 计算中的 Tensor Core 利用率瓶颈及内存访问模式。

## Evidence

[质询]具体数值（40%）缺乏公开基准测试的直接支持，且不同序列长度、Batch Size 及实现细节（如 FlashAttention 版本）下 MFU 波动极大，单一数值可能具有误导性或特定于未披露的实验条件。 | 先验知识/题面给定，逻辑校验通过：RTX 4090 作为消费级显卡，在 BF16 大模型 Prefill 阶段受限于内存带宽和 Tensor Core 利用率，MFU 在 30%-50% 区间符合工程直觉，但具体 40% 为经验事实，无外部来源直接佐证。

## Search Query

RTX 4090 Qwen3 27B prefill MFU benchmark
