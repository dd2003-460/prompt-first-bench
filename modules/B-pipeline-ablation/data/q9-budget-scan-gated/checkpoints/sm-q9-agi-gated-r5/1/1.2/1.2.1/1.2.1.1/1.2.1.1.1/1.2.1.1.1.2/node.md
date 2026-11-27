# N157: 基于 N138 确认的参数，计算单卡每 token KV Cache 显存占用公式：Bytes_per_token_per_card = (2 * num_hi

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

基于 N138 确认的参数，计算单卡每 token KV Cache 显存占用公式：Bytes_per_token_per_card = (2 * num_hidden_layers * num_key_value_heads * head_dim * dtype_bytes) / TP_size，其中 dtype_bytes=1 (FP8)，TP_size=4。

## Corrected Claim

基于 N138 确认的参数，计算单卡每 token KV Cache 显存占用公式：Bytes_per_token_per_card = (2 * num_hidden_layers * num_key_value_heads * head_dim * dtype_bytes) / TP_size，其中 dtype_bytes=1 (FP8)，TP_size=4。

## Evidence

先验知识/题面给定，逻辑校验通过
