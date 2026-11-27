# N161: 工作点 1 (高并发短上下文) 显存占用量化：在 num_key_value_heads=8 前提下，max_num_seqs=8, seq_len=2048 

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

工作点 1 (高并发短上下文) 显存占用量化：在 num_key_value_heads=8 前提下，max_num_seqs=8, seq_len=2048 时，总 KV 需求 = 8 * 2048 * 48 KB = 768 MB/卡，占 11.125 GB 可用显存的 6.9%，远低于 N81 声称的 2GB (19%)，判定为安全。

## Corrected Claim

工作点 1 (高并发短上下文) 显存占用量化：在 num_key_value_heads=8 前提下，max_num_seqs=8, seq_len=2048 时，总 KV 需求 = 8 * 2048 * 48 KB = 768 MB/卡，占 11.125 GB 可用显存的 6.9%，远低于 N81 声称的 2GB (19%)，判定为安全。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 8*2048*48KB=768MB 正确，占比 768/11125≈6.9% 正确，且 768MB < 2GB 符合逻辑。
