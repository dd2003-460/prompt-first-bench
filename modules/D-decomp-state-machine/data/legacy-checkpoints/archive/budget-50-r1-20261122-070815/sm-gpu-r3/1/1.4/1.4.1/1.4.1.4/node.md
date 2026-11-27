# N181: 若强制在 48 GB 显存硬件 (如 RTX A6000) 上运行 Qwen3-27B，需将权重精度降至 FP8 (27.3 GB) 或 INT8 (27.3 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

若强制在 48 GB 显存硬件 (如 RTX A6000) 上运行 Qwen3-27B，需将权重精度降至 FP8 (27.3 GB) 或 INT8 (27.3 GB)，此时剩余显存 (48 - 27.3 - 2.15 - 1.0 ≈ 17.5 GB) 足以支持 32K 上下文，但需验证 FP8/INT8 的质量损失是否在可接受范围内。

## Corrected Claim

若强制在 48 GB 显存硬件 (如 RTX A6000) 上运行 Qwen3-27B，需将权重精度降至 FP8 (27.3 GB) 或 INT8 (27.3 GB)，此时剩余显存 (48 - 27.3 - 2.15 - 1.0 ≈ 17.5 GB) 足以支持 32K 上下文，但需验证 FP8/INT8 的质量损失是否在可接受范围内。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型在FP8/INT8下权重约27.3GB，加上KV Cache和激活值开销后，48GB显存剩余空间足以支撑32K上下文，数值量级与工程常识一致。

## Search Query

Qwen3-27B FP8 quantization quality degradation benchmark
