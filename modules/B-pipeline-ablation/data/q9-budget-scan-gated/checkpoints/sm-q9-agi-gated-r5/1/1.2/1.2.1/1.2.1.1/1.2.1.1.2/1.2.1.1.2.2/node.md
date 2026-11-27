# N162: 工作点 3 (低并发长上下文) 显存占用量化：在 num_key_value_heads=8 前提下，max_num_seqs=1, seq_len=32768

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

工作点 3 (低并发长上下文) 显存占用量化：在 num_key_value_heads=8 前提下，max_num_seqs=1, seq_len=32768 时，总 KV 需求 = 1 * 32768 * 48 KB = 1.5 GB/卡，占 11.125 GB 可用显存的 13.5%，远低于 N81 声称的 4GB (38%)，判定为安全且余量充足。

## Corrected Claim

工作点 3 (低并发长上下文) 显存占用量化：在 num_key_value_heads=8 前提下，max_num_seqs=1, seq_len=32768 时，总 KV 需求 = 1 * 32768 * 48 KB = 1.5 GB/卡，占 11.125 GB 可用显存的 13.5%，远低于 N81 声称的 4GB (38%)，判定为安全且余量充足。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 1 * 32768 * 48KB = 1,572,864 KB ≈ 1.5 GB，占比 1.5/11.125 ≈ 13.5%，数值量级与算术逻辑自洽。
