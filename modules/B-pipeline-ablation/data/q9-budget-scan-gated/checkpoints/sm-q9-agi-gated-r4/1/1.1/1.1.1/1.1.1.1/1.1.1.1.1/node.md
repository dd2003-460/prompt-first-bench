# N78: Qwen3.8-27B 在 NVFP4 (W4A16) 量化下的静态权重显存占用为 27e9 * 4bits / 8bits_per_byte ≈ 13.5 G

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

Qwen3.8-27B 在 NVFP4 (W4A16) 量化下的静态权重显存占用为 27e9 * 4bits / 8bits_per_byte ≈ 13.5 GB (13,500 MB)，加上 Embedding/LayerNorm 等 FP16 非量化部分约 0.2 GB，总静态权重占用为 13.7 GB，修正了 N19 中 6.75 GB 的算术错误。

## Corrected Claim

Qwen3.8-27B 在 NVFP4 (W4A16) 量化下的静态权重显存占用为 27e9 * 4bits / 8bits_per_byte ≈ 13.5 GB (13,500 MB)，加上 Embedding/LayerNorm 等 FP16 非量化部分约 0.2 GB，总静态权重占用为 13.7 GB，修正了 N19 中 6.75 GB 的算术错误。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9 * 4 / 8 = 13.5 GB，加上少量非量化层约 0.2 GB，总计 13.7 GB，算术正确且符合 W4A16 量化显存估算逻辑。
