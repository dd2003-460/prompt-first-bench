# N209: Prefill阶段算力受限下的吞吐量上限计算：对于RTX 4090 (BF16 330.4 TFLOPS)，Prefill阶段吞吐量 = Peak_FLOPS 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

Prefill阶段算力受限下的吞吐量上限计算：对于RTX 4090 (BF16 330.4 TFLOPS)，Prefill阶段吞吐量 = Peak_FLOPS / FLOPs_per_token = 330.4e9 / 54.2e9 ≈ 6.1 tokens/ms (即6100 tokens/s)；对于A100 (BF16 312 TFLOPS)，吞吐量 ≈ 312e9 / 54.2e9 ≈ 5.76 tokens/ms。两者在Prefill阶段性能接近，差异主要源于显存带宽在Decode阶段的影响。

## Corrected Claim

Prefill阶段算力受限下的吞吐量上限计算：对于RTX 4090 (BF16 330.4 TFLOPS)，Prefill阶段吞吐量 = Peak_FLOPS / FLOPs_per_token = 330.4e9 / 54.2e9 ≈ 6.1 tokens/ms (即6100 tokens/s)；对于A100 (BF16 312 TFLOPS)，吞吐量 ≈ 312e9 / 54.2e9 ≈ 5.76 tokens/ms。两者在Prefill阶段性能接近，差异主要源于显存带宽在Decode阶段的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 BF16峰值算力约330 TFLOPS，A100 BF16峰值算力约312 TFLOPS，数值量级准确；Prefill阶段为计算密集型，吞吐量近似等于峰值算力除以单Token计算量，逻辑自洽；Decode阶段受显存带宽限制，故两者Prefill性能接近而Decode差异大，符合LLM推理基本原理。
