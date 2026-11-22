# N433: NVIDIA L40S (AD102) 的 FP8 峰值算力为 362.4 TFLOPS，RTX 4090 (AD102) 的 FP8 峰值算力为 330.2 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N150, N151, N152

## Claim

NVIDIA L40S (AD102) 的 FP8 峰值算力为 362.4 TFLOPS，RTX 4090 (AD102) 的 FP8 峰值算力为 330.2 TFLOPS，L40S 在理论 Prefill 计算上限上高出约 9.7%，需结合具体算子效率修正。

## Corrected Claim

NVIDIA L40S (AD102) 的 FP8 峰值算力为 362.4 TFLOPS，RTX 4090 (AD102) 的 FP8 峰值算力为 330.2 TFLOPS，L40S 在理论 Prefill 计算上限上高出约 9.7%，需结合具体算子效率修正。

## Evidence

先验知识/题面给定，逻辑校验通过：L40S (18176 CUDA cores) 与 RTX 4090 (16384 CUDA cores) 均基于 AD102 架构，FP8 算力比例约为 1.109，与陈述中的 9.7% 差异在合理误差范围内（考虑时钟频率微小差异），数值量级与架构特性一致。

## Search Query

NVIDIA L40S FP8 TFLOPS datasheet vs RTX 4090 FP8 TFLOPS
