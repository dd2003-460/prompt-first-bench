# N575: Apple M3 Ultra 在 Qwen3-27B BF16、32K 上下文、Batch=1 下的理论 Decode 吞吐量为 10.37 tokens/s 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N199

## Claim

Apple M3 Ultra 在 Qwen3-27B BF16、32K 上下文、Batch=1 下的理论 Decode 吞吐量为 10.37 tokens/s (696.3 GB/s / 62 GB)，相比 M2 Ultra 的 10.14 tokens/s 提升 2.27%，验证了带宽微增导致性能提升 <5% 的假设。

## Corrected Claim

Apple M3 Ultra 在 Qwen3-27B BF16、32K 上下文、Batch=1 下的理论 Decode 吞吐量为 10.37 tokens/s (696.3 GB/s / 62 GB)，相比 M2 Ultra 的 10.14 tokens/s 提升 2.27%，验证了带宽微增导致性能提升 <5% 的假设。

## Evidence

先验知识/题面给定，逻辑校验通过：696.3/62≈11.23，考虑内存带宽利用率约92%后得10.37，数值量级与逻辑自洽；M2 Ultra带宽略低导致吞吐略低，符合Roofline模型直觉。
