# N41: 在 max_model_len=262144 且 max_num_seqs=8 的极端负载下，理论最大 KV Cache 需求为 8 * 262144 * 12

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

在 max_model_len=262144 且 max_num_seqs=8 的极端负载下，理论最大 KV Cache 需求为 8 * 262144 * 128KB ≈ 256GB

## Corrected Claim

在 max_model_len=262144 且 max_num_seqs=8 的极端负载下，理论最大 KV Cache 需求为 8 * 262144 * 128KB ≈ 256GB

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 8 * 262144 * 128KB = 268,435,456 KB = 256 GB，数值量级与算术逻辑完全自洽。
