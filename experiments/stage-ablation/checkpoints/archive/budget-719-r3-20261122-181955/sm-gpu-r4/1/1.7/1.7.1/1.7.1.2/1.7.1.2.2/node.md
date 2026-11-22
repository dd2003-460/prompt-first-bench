# N634: 工作点 2 (中等利用率/通用推理)：在 PyTorch 原生或 llama.cpp 等通用框架下，RTX 4090 的 Tensor Core 利用率约为 6

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N223

## Claim

工作点 2 (中等利用率/通用推理)：在 PyTorch 原生或 llama.cpp 等通用框架下，RTX 4090 的 Tensor Core 利用率约为 60%，有效算力 = 82.6 * 0.6 = 49.6 TFLOPS；此时 $/TFLOPS (基于 $1,650) ≈ $33.3，适用于 Decode 密集或混合负载场景，性价比中等。

## Corrected Claim

工作点 2 (中等利用率/通用推理)：在 PyTorch 原生或 llama.cpp 等通用框架下，RTX 4090 的 Tensor Core 利用率约为 60%，有效算力 = 82.6 * 0.6 = 49.6 TFLOPS；此时 $/TFLOPS (基于 $1,650) ≈ $33.3，适用于 Decode 密集或混合负载场景，性价比中等。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 FP16 Tensor Core 峰值算力约为 82.6 TFLOPS，通用推理框架下 60% 利用率符合工程经验，计算 82.6 * 0.6 = 49.56 ≈ 49.6 TFLOPS 及 1650 / 49.6 ≈ 33.27 ≈ 33.3 $/TFLOPS 均准确。
