# N58: 修正 N29 的显存占用计算：基于 N22 验证的 KV Cache 占用为 64 KB/token（GQA, 8 kv_heads, FP8），15k tok

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

修正 N29 的显存占用计算：基于 N22 验证的 KV Cache 占用为 64 KB/token（GQA, 8 kv_heads, FP8），15k tokens 的上下文占用显存为 15,000 * 64 KB = 960 MB (0.96 GB)，而非原估的 '60% of 25k budget'（该比例基于错误的 16KB/token 或单头假设）。

## Corrected Claim

修正 N29 的显存占用计算：基于 N22 验证的 KV Cache 占用为 64 KB/token（GQA, 8 kv_heads, FP8），15k tokens 的上下文占用显存为 15,000 * 64 KB = 960 MB (0.96 GB)，而非原估的 '60% of 25k budget'（该比例基于错误的 16KB/token 或单头假设）。

## Evidence

先验知识/题面给定，逻辑校验通过：15,000 tokens × 64 KB/token = 960,000 KB = 937.5 MiB ≈ 0.96 GB，计算无误且符合GQA显存估算逻辑。
