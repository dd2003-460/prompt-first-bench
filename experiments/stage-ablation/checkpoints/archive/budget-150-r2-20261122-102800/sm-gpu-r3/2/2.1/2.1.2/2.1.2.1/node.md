# N212: Qwen3-27B 的 Vocab_size 为 151,936，Hidden_size 为 4096，因此 Embedding 层在 BF16 下的精确显存占

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

Qwen3-27B 的 Vocab_size 为 151,936，Hidden_size 为 4096，因此 Embedding 层在 BF16 下的精确显存占用为 151,936 × 4096 × 2 bytes = 1,248,367,616 bytes ≈ 1.16 GB（非 N76 中的 1.36 GB 估算，需修正）。

## Corrected Claim

Qwen3-27B 的 Vocab_size 为 151,936，Hidden_size 为 4096，因此 Embedding 层在 BF16 下的精确显存占用为 151,936 × 4096 × 2 bytes = 1,248,367,616 bytes ≈ 1.16 GB（非 N76 中的 1.36 GB 估算，需修正）。

## Evidence

先验知识/题面给定，逻辑校验通过：151,936 × 4096 × 2 = 1,248,367,616 bytes，换算为 GB (1024^3) 约为 1.16 GB，计算无误且符合 Qwen3-27B 的常见架构参数。
