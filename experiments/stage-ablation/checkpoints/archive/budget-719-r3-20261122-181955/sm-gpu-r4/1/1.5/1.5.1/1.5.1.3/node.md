# N199: Apple M3 Ultra (256GB) 在 Qwen3-27B BF16 下的理论 Decode 上限计算：相比 M2 Ultra，内存容量增加允许更长的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

Apple M3 Ultra (256GB) 在 Qwen3-27B BF16 下的理论 Decode 上限计算：相比 M2 Ultra，内存容量增加允许更长的 KV Cache 或更大的 Batch Size，但带宽仅微增（800 -> 819.2 GB/s）。计算在相同 32K 上下文、Batch=1 情况下的 tokens/s 差异，量化 M3 Ultra 相对于 M2 Ultra 的性能提升百分比（预计 <5%）。

## Corrected Claim

Apple M3 Ultra (256GB) 在 Qwen3-27B BF16 下的理论 Decode 上限计算：相比 M2 Ultra，内存容量增加允许更长的 KV Cache 或更大的 Batch Size，但带宽仅微增（800 -> 819.2 GB/s）。计算在相同 32K 上下文、Batch=1 情况下的 tokens/s 差异，量化 M3 Ultra 相对于 M2 Ultra 的性能提升百分比（预计 <5%）。

## Evidence

先验知识/题面给定，逻辑校验通过：M3 Ultra带宽(819.2GB/s)相比M2 Ultra(800GB/s)提升约2.4%，在Decode阶段（带宽受限）且Batch=1时，理论吞吐量提升比例与带宽提升比例一致，符合<5%的预期。
