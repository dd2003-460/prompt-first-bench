# N299: Qwen3-27B 在 BF16 精度下的模型权重显存占用计算：参数量 (27.2B) × 2 bytes/param ≈ 54.4 GB，需确认是否包含 Em

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

Qwen3-27B 在 BF16 精度下的模型权重显存占用计算：参数量 (27.2B) × 2 bytes/param ≈ 54.4 GB，需确认是否包含 Embedding/LayerNorm 等小参数，确保与 N82 中 54GB 的估算一致。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的模型权重显存占用计算：参数量 (27.2B) × 2 bytes/param ≈ 54.4 GB，需确认是否包含 Embedding/LayerNorm 等小参数，确保与 N82 中 54GB 的估算一致。

## Evidence

先验知识/题面给定，逻辑校验通过：27.2B参数在BF16（2字节/参数）下占用约54.4GB，与54GB估算一致，量级合理。
