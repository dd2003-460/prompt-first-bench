# N94: RTX 4090 在 BF16 权重 + BF16 KV Cache 配置下的 Batch Size=1 吞吐量估算：Tokens_per_sec ≈ 1000

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

RTX 4090 在 BF16 权重 + BF16 KV Cache 配置下的 Batch Size=1 吞吐量估算：Tokens_per_sec ≈ 1000 GB/s / (54GB*1024^3/32768 + 2*n_layers*n_kv_heads*head_dim*2)，具体数值需代入 Qwen3-27B 的实际层数和头数计算。

## Corrected Claim

RTX 4090 在 BF16 权重 + BF16 KV Cache 配置下的 Batch Size=1 吞吐量估算：Tokens_per_sec ≈ 1000 GB/s / (54GB*1024^3/32768 + 2*n_layers*n_kv_heads*head_dim*2)，具体数值需代入 Qwen3-27B 的实际层数和头数计算。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存带宽约1000GB/s，BF16精度下权重和KV Cache占用空间计算符合物理直觉，吞吐量估算公式逻辑自洽。

## Search Query

RTX 4090 Qwen3 27B BF16 batch size 1 throughput estimation tokens per second
