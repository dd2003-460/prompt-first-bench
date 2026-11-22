# N333: Qwen3-27B 在 FP8 精度下的权重显存占用 (VRAM_weights) 为 27 GB (基于 27B 参数 × 1 byte/param)，该值为

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N119

## Claim

Qwen3-27B 在 FP8 精度下的权重显存占用 (VRAM_weights) 为 27 GB (基于 27B 参数 × 1 byte/param)，该值为 N110 中已验证的总显存公式中的权重项

## Corrected Claim

Qwen3-27B 在 FP8 精度下的权重显存占用 (VRAM_weights) 为 27 GB (基于 27B 参数 × 1 byte/param)，该值为 N110 中已验证的总显存公式中的权重项

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8精度下（1字节/参数）占用27GB显存，计算逻辑自洽且符合基本物理/工程直觉。
