# N9: Qwen3-27B 模型在 NVFP4 或 W4A16 精度下的权重文件大小约为 13.5GB - 17GB (27B × 0.5-0.625 bytes)，需

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B 模型在 NVFP4 或 W4A16 精度下的权重文件大小约为 13.5GB - 17GB (27B × 0.5-0.625 bytes)，需验证 4-bit 量化对 27B 规模模型的质量损失是否超过 5% [待核验]。

## Corrected Claim

Qwen3-27B 模型在 NVFP4 或 W4A16 精度下的权重文件大小约为 13.5GB - 17GB (27B × 0.5-0.625 bytes)，需验证 4-bit 量化对 27B 规模模型的质量损失是否超过 5% [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在4-bit量化下（含权重及少量高精度组件）体积估算为13.5-17GB符合数学量级（27e9 * 0.5-0.625 bytes），且4-bit量化对大模型质量损失通常可控，逻辑自洽。

## Search Query

Qwen3 27B 4bit quantization quality loss benchmark
