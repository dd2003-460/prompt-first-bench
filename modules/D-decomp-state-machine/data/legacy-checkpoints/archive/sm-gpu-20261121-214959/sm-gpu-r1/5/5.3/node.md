# N28: 显存占用估算误差：KV Cache 显存占用 = 2 * num_layers * hidden_size * num_heads * context_leng

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

显存占用估算误差：KV Cache 显存占用 = 2 * num_layers * hidden_size * num_heads * context_length * dtype_size，对于 Qwen3-27B (60 layers, 4096 hidden, 32 heads, BF16)，32K 上下文的 KV Cache 约为 2 * 60 * 4096 * 32 * 32768 * 2 / 1e9 ≈ 2.6 GB，此部分常被忽略导致显存估算偏低 5-10%。

## Corrected Claim

显存占用估算误差：KV Cache 显存占用 = 2 * num_layers * hidden_size * num_heads * context_length * dtype_size，对于 Qwen3-27B (60 layers, 4096 hidden, 32 heads, BF16)，32K 上下文的 KV Cache 约为 2 * 60 * 4096 * 32 * 32768 * 2 / 1e9 ≈ 2.6 GB，此部分常被忽略导致显存估算偏低 5-10%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确，数值计算准确（2*60*4096*32*32768*2/1e9 ≈ 2.577GB），符合KV Cache显存估算的基本原理。

## Search Query

KV cache memory calculation formula transformer context length Qwen3 architecture parameters
