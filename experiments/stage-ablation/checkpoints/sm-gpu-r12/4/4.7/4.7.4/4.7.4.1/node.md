# N251: Qwen3-27B BF16 模型在 Apple M2 Ultra 上的理论吞吐量上限计算：Throughput = Memory_Bandwidth / Mo

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

Qwen3-27B BF16 模型在 Apple M2 Ultra 上的理论吞吐量上限计算：Throughput = Memory_Bandwidth / Model_Size_in_Bytes = 800 GB/s / 54 GB ≈ 14.8 tokens/s。修正自矛盾检测：N60 声称 13 tokens/s 更接近实际值，N111 的 57 tokens/s 计算错误（可能误用了容量而非带宽作为分母或单位错误）

## Corrected Claim

Qwen3-27B BF16 模型在 Apple M2 Ultra 上的理论吞吐量上限计算：Throughput = Memory_Bandwidth / Model_Size_in_Bytes = 800 GB/s / 54 GB ≈ 14.8 tokens/s。修正自矛盾检测：N60 声称 13 tokens/s 更接近实际值，N111 的 57 tokens/s 计算错误（可能误用了容量而非带宽作为分母或单位错误）

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 带宽 800GB/s 与 27B BF16 模型约 54GB 大小符合常识，计算 800/54≈14.8 正确，且对 N111 错误值的归因逻辑合理。
