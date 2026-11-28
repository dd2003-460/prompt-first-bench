# N519: 单卡 KV Cache 可存储的最大 token 数 = 11.6GB / 8KB/token ≈ 1.47M tokens，但受 max_model_len=

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N185

## Claim

单卡 KV Cache 可存储的最大 token 数 = 11.6GB / 8KB/token ≈ 1.47M tokens，但受 max_model_len=262144 限制，实际单序列上限为 262K tokens

## Corrected Claim

单卡 KV Cache 可存储的最大 token 数 = 11.6GB / 8KB/token ≈ 1.47M tokens，但受 max_model_len=262144 限制，实际单序列上限为 262K tokens

## Evidence

先验知识/题面给定，逻辑校验通过：11.6GB / 8KB ≈ 1.47M tokens 计算正确，且 max_model_len 作为硬性上限逻辑自洽
