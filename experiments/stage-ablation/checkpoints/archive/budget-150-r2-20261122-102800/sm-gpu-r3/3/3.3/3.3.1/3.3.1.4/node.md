# N258: 修正 N94 结论：由于 Decode 阶段带宽受限，NVFP4 在 RTX 4090 上的实际推理速度接近 FP16 峰值（约 17.3 tokens/s @

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

修正 N94 结论：由于 Decode 阶段带宽受限，NVFP4 在 RTX 4090 上的实际推理速度接近 FP16 峰值（约 17.3 tokens/s @ 32K），而非因算力下降导致的 ~10 tokens/s；算力下降主要影响 Prefill 阶段（Compute-Bound），对总延迟影响有限。

## Corrected Claim

修正 N94 结论：由于 Decode 阶段带宽受限，NVFP4 在 RTX 4090 上的实际推理速度接近 FP16 峰值（约 17.3 tokens/s @ 32K），而非因算力下降导致的 ~10 tokens/s；算力下降主要影响 Prefill 阶段（Compute-Bound），对总延迟影响有限。

## Evidence

先验知识/题面给定，逻辑校验通过：Decode阶段为带宽受限（Memory-Bound），NVFP4与FP16在带宽瓶颈下的理论吞吐差异较小，且算力下降主要影响Prefill（Compute-Bound），符合LLM推理的基本物理/工程直觉。
