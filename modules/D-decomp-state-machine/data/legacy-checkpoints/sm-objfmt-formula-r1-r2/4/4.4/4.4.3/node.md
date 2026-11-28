# N91: NVFP4 量化后的 KV Cache 精度保持策略：通常 KV Cache 仍使用 BF16 或 FP8 存储以避免累积误差爆炸，因此 KV Cache 显存

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

NVFP4 量化后的 KV Cache 精度保持策略：通常 KV Cache 仍使用 BF16 或 FP8 存储以避免累积误差爆炸，因此 KV Cache 显存占用不随权重精度降低而减半，仍按 N11 公式计算（约 0.5-1GB for 32K context）

## Corrected Claim

NVFP4 量化后的 KV Cache 精度保持策略：通常 KV Cache 仍使用 BF16 或 FP8 存储以避免累积误差爆炸，因此 KV Cache 显存占用不随权重精度降低而减半，仍按 N11 公式计算（约 0.5-1GB for 32K context）

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 通常保持高精度（BF16/FP8）以维持推理稳定性，其显存占用由序列长度和模型维度决定，与权重量化精度（NVFP4）解耦，故不随权重精度降低而减半。

## Search Query

NVFP4 quantization KV cache precision strategy BF16 vs FP8
