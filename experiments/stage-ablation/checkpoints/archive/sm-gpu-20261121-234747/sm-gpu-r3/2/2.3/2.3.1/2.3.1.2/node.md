# N243: H100 SXM5 的 FP8 计算峰值 3958 TFLOPS 仅在 Prefill 阶段（计算密集）可达，Decode 阶段（内存密集）的实际算力利用率低于

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

H100 SXM5 的 FP8 计算峰值 3958 TFLOPS 仅在 Prefill 阶段（计算密集）可达，Decode 阶段（内存密集）的实际算力利用率低于 10%，因此 FP8 对 Decode 延迟的改善主要源于显存占用减半（27GB vs 54GB）带来的 KV Cache 容量增加，而非算力提升

## Corrected Claim

H100 SXM5 的 FP8 计算峰值 3958 TFLOPS 仅在 Prefill 阶段（计算密集）可达，Decode 阶段（内存密集）的实际算力利用率低于 10%，因此 FP8 对 Decode 延迟的改善主要源于显存占用减半（27GB vs 54GB）带来的 KV Cache 容量增加，而非算力提升

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 FP8峰值算力约3958 TFLOPS符合官方规格；Decode阶段受内存带宽限制，算力利用率极低（通常<10%）符合LLM推理基本物理直觉；FP8将权重和KV Cache精度减半从而增加KV Cache容量是标准工程事实，逻辑自洽且无内部矛盾。
