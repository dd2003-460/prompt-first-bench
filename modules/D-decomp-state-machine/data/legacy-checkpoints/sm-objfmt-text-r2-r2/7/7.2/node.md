# N107: RTX 5090 的 FP8 峰值算力为 2048 TFLOPS，RTX 4090 为 826 TFLOPS；在 Qwen3-27B 推理中，若计算受限而非带宽

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

RTX 5090 的 FP8 峰值算力为 2048 TFLOPS，RTX 4090 为 826 TFLOPS；在 Qwen3-27B 推理中，若计算受限而非带宽受限，5090 的理论算力优势为 2.48x，但受限于显存容量 (32GB vs 24GB)，实际加速比需结合 KV Cache 占用计算。

## Corrected Claim

RTX 5090 的 FP8 峰值算力为 2048 TFLOPS，RTX 4090 为 826 TFLOPS；在 Qwen3-27B 推理中，若计算受限而非带宽受限，5090 的理论算力优势为 2.48x，但受限于显存容量 (32GB vs 24GB)，实际加速比需结合 KV Cache 占用计算。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 (Blackwell) 与 RTX 4090 (Ada) 的 FP8 算力比值约为 2.48x (2048/826 ≈ 2.48)，符合硬件架构升级的预期量级；显存容量 32GB vs 24GB 及 KV Cache 对推理加速比的限制符合大模型推理的基本原理。
