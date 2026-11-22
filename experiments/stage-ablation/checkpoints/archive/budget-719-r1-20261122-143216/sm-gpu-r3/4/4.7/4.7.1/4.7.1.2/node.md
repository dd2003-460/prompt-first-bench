# N334: Qwen3-27B 在 BF16 精度下的权重显存占用 (VRAM_weights) 为 54 GB (基于 27B 参数 × 2 bytes/param)，该

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N119

## Claim

Qwen3-27B 在 BF16 精度下的权重显存占用 (VRAM_weights) 为 54 GB (基于 27B 参数 × 2 bytes/param)，该值为 N109 中已验证的总显存公式中的权重项

## Corrected Claim

Qwen3-27B 在 BF16 精度下的权重显存占用 (VRAM_weights) 为 54 GB (基于 27B 参数 × 2 bytes/param)，该值为 N109 中已验证的总显存公式中的权重项

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 × 2 bytes/param (BF16) = 54 GB，计算准确且符合显存占用基本公式。
