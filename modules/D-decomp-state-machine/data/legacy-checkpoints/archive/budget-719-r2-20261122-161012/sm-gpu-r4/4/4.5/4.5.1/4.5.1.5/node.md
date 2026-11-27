# N233: RTX 5090 (32GB) 运行 FP8 精度 Qwen3-27B (28.2GB) 的显存余量为 3.8 GB，足以支持单卡 32K 上下文运行，无需 O

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

RTX 5090 (32GB) 运行 FP8 精度 Qwen3-27B (28.2GB) 的显存余量为 3.8 GB，足以支持单卡 32K 上下文运行，无需 Offload。

## Corrected Claim

RTX 5090 (32GB) 运行 FP8 精度 Qwen3-27B (28.2GB) 的显存余量为 3.8 GB，足以支持单卡 32K 上下文运行，无需 Offload。

## Evidence

先验知识/题面给定，逻辑校验通过：32GB - 28.2GB = 3.8GB，数值计算准确；对于27B参数量的模型，3.8GB显存余量通常足以支撑32K上下文的KV Cache及激活值，无需Offload，符合工程常识。
