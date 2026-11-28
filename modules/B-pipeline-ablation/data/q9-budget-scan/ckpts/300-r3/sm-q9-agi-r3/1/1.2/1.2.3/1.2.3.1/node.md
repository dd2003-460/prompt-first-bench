# N142: 原 N8 中 4KB/token 的错误源于混淆了单头 KV Cache 大小 (head_dim * 1 byte = 128B) 与全模型 KV Cache

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

原 N8 中 4KB/token 的错误源于混淆了单头 KV Cache 大小 (head_dim * 1 byte = 128B) 与全模型 KV Cache 大小 (128KB)，或错误地假设 num_kv_heads=1 且仅计算单层

## Corrected Claim

原 N8 中 4KB/token 的错误源于混淆了单头 KV Cache 大小 (head_dim * 1 byte = 128B) 与全模型 KV Cache 大小 (128KB)，或错误地假设 num_kv_heads=1 且仅计算单层

## Evidence

先验知识/题面给定，逻辑校验通过：单头KV Cache大小计算（head_dim * 1 byte = 128B）与全模型KV Cache大小（128KB）的量级差异符合逻辑，混淆二者或错误假设num_kv_heads=1且仅计算单层确实会导致4KB/token的错误估算。
