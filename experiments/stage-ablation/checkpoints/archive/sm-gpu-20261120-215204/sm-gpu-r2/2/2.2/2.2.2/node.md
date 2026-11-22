# N72: FP8 推理在 H100 上相比 BF16 的吞吐量提升通常为 1.5-2.0 倍，主要得益于显存带宽需求减半 (27GB vs 54GB) 以及 H100 T

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

FP8 推理在 H100 上相比 BF16 的吞吐量提升通常为 1.5-2.0 倍，主要得益于显存带宽需求减半 (27GB vs 54GB) 以及 H100 Tensor Core 对 FP8 的原生支持 (FP8 TFLOPS 是 BF16 的 2 倍)。

## Corrected Claim

FP8 推理在 H100 上相比 BF16 的吞吐量提升通常为 1.5-2.0 倍，主要得益于显存带宽需求减半 (27GB vs 54GB) 以及 H100 Tensor Core 对 FP8 的原生支持 (FP8 TFLOPS 是 BF16 的 2 倍)。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 FP8 Tensor Core 算力确为 BF16 的 2 倍，且 FP8 显存占用减半符合数据位宽定义，吞吐量提升 1.5-2.0 倍在带宽受限与计算受限场景下均合理。
