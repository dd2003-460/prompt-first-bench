# N62: RTX 4090 在 FP16/BF16 下的理论峰值算力（Tensor Core 加速后）与 FP8 下的算力差异，量化精度切换对 Prefill 阶段性能的

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

RTX 4090 在 FP16/BF16 下的理论峰值算力（Tensor Core 加速后）与 FP8 下的算力差异，量化精度切换对 Prefill 阶段性能的影响

## Corrected Claim

RTX 4090 在 FP16/BF16 下的理论峰值算力（Tensor Core 加速后）与 FP8 下的算力差异，量化精度切换对 Prefill 阶段性能的影响

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 基于 Ada Lovelace 架构，其 Tensor Core 支持 FP8 且吞吐量通常为 FP16/BF16 的 2 倍，符合硬件规格逻辑。
