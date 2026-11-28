# N133: 在 max_num_seqs=8 且每序列均为 262k tokens 的极端满载工况下，系统总 KV 显存需求为 8 * 524.288 MB = 4.19 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

在 max_num_seqs=8 且每序列均为 262k tokens 的极端满载工况下，系统总 KV 显存需求为 8 * 524.288 MB = 4.19 GB，分摊到 4 张卡每卡仅 1.05 GB，显存利用率约为 9.4% (1.05/11.125)，证实存在大量闲置显存。

## Corrected Claim

在 max_num_seqs=8 且每序列均为 262k tokens 的极端满载工况下，系统总 KV 显存需求为 8 * 524.288 MB = 4.19 GB，分摊到 4 张卡每卡仅 1.05 GB，显存利用率约为 9.4% (1.05/11.125)，证实存在大量闲置显存。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（8*524.288=4194.304MB≈4.19GB；4.19/4=1.0475GB≈1.05GB；1.05/11.125≈9.43%），量级合理，符合KV Cache显存计算的基本逻辑。
