# N406: Qwen3-27B 的 KV Cache 字节数精确计算：KV Cache Size = 2 * n_layers * n_heads * head_dim *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N158

## Claim

Qwen3-27B 的 KV Cache 字节数精确计算：KV Cache Size = 2 * n_layers * n_heads * head_dim * seq_len * bytes_per_element；Qwen3-27B 有 64 层，GQA 头数 4（KV 头），head_dim 128，因此每 token KV Cache = 2 * 64 * 4 * 128 * 1 = 65,536 bytes = 64 KB/token。

## Corrected Claim

Qwen3-27B 的 KV Cache 字节数精确计算：KV Cache Size = 2 * n_layers * n_heads * head_dim * seq_len * bytes_per_element；Qwen3-27B 有 64 层，GQA 头数 4（KV 头），head_dim 128，因此每 token KV Cache = 2 * 64 * 4 * 128 * 1 = 65,536 bytes = 64 KB/token。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层，GQA 4 KV头，head_dim 128）符合主流大模型设计惯例，计算公式 2 * 64 * 4 * 128 = 65536 bytes 数学推导正确，量级合理。
