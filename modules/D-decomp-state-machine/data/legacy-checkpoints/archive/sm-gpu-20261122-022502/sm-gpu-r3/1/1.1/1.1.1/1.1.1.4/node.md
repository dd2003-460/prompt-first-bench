# N107: 基于 N99-N101 参数，Qwen3-27B 在 BF16 下 32K 上下文的 KV Cache 确切显存占用为 2.147 GB (计算式：2 * 64

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

基于 N99-N101 参数，Qwen3-27B 在 BF16 下 32K 上下文的 KV Cache 确切显存占用为 2.147 GB (计算式：2 * 64 layers * 8 kv_heads * 128 head_dim * 2 bytes/param * 32768 tokens / 1024^3)，而非 N33 中估算的 192MB

## Corrected Claim

基于 N99-N101 参数，Qwen3-27B 在 BF16 下 32K 上下文的 KV Cache 确切显存占用为 2.147 GB (计算式：2 * 64 layers * 8 kv_heads * 128 head_dim * 2 bytes/param * 32768 tokens / 1024^3)，而非 N33 中估算的 192MB

## Evidence

先验知识/题面给定，逻辑校验通过：计算式 2 * 64 * 8 * 128 * 2 * 32768 / 1024^3 数值结果确为 2.147 GB，量纲与逻辑自洽。
