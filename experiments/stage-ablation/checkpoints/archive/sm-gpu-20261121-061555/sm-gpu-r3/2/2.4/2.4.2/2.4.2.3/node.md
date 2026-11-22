# N202: Qwen3-27B 在 FP8/INT8 精度下的运行时开销（Overhead）显存占用：与 BF16 类似，取保守值 3.5 GB (≈ 3.26 GiB)，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

Qwen3-27B 在 FP8/INT8 精度下的运行时开销（Overhead）显存占用：与 BF16 类似，取保守值 3.5 GB (≈ 3.26 GiB)，因为 CUDA 上下文和部分中间缓冲仍可能使用 FP16/FP32 或固定大小。

## Corrected Claim

Qwen3-27B 在 FP8/INT8 精度下的运行时开销（Overhead）显存占用：与 BF16 类似，取保守值 3.5 GB (≈ 3.26 GiB)，因为 CUDA 上下文和部分中间缓冲仍可能使用 FP16/FP32 或固定大小。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数模型在量化后权重显存大幅降低，但CUDA上下文、KV Cache及中间缓冲（常为FP16/FP32）确实会占用数GB固定开销，3.5GB量级符合工程直觉。
