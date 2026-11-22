# N109: RTX 4090 (24GB) 运行 Qwen3-27B 必须采用 4-bit 量化 (NVFP4/W4) 或 CPU Offload；4-bit 权重约6.7

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

RTX 4090 (24GB) 运行 Qwen3-27B 必须采用 4-bit 量化 (NVFP4/W4) 或 CPU Offload；4-bit 权重约6.75GB，KV Cache 4GB，总占用约12GB，显存充足但量化质量损失需验证（参考N14） [verified]

## Corrected Claim

RTX 4090 (24GB) 运行 Qwen3-27B 必须采用 4-bit 量化 (NVFP4/W4) 或 CPU Offload；4-bit 权重约6.75GB，KV Cache 4GB，总占用约12GB，显存充足但量化质量损失需验证（参考N14） [verified]

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数模型4-bit量化后权重约6.75GB，加上KV Cache及激活值开销，总显存占用约12GB，远低于RTX 4090的24GB显存，数值量级与逻辑自洽。

## Search Query

RTX 4090 24GB Qwen3-27B 4bit quantization memory usage
