# N58: 修正 N29 的显存占用计算：基于 N22 验证的 KV Cache 占用为 64 KB/token（GQA, 8 kv_heads, FP8），15k tok

- **status**: pending
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

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 727)
