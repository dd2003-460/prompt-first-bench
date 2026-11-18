# N285: Apple M2 Ultra 运行 Qwen3-27B BF16 时的理论吞吐上限计算：Throughput_BF16 = Memory_Bandwidth /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N111

## Claim

Apple M2 Ultra 运行 Qwen3-27B BF16 时的理论吞吐上限计算：Throughput_BF16 = Memory_Bandwidth / Weight_Size = 800 GB/s / (27e9 * 2 bytes) ≈ 14.81 tokens/s (Batch=1, Decode阶段)。此数值修正了 N60 中基于 54B 模型折算的错误逻辑，直接针对 27B 模型计算。

## Corrected Claim

Apple M2 Ultra 运行 Qwen3-27B BF16 时的理论吞吐上限计算：Throughput_BF16 = Memory_Bandwidth / Weight_Size = 800 GB/s / (27e9 * 2 bytes) ≈ 14.81 tokens/s (Batch=1, Decode阶段)。此数值修正了 N60 中基于 54B 模型折算的错误逻辑，直接针对 27B 模型计算。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 内存带宽约 800GB/s，27B 模型 BF16 权重约 54GB，计算 800/54 ≈ 14.81 tokens/s，符合内存带宽瓶颈下的理论吞吐上限公式。
