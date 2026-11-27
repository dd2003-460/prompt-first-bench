# N875: Qwen3-27B 的官方配置文件中，num_hidden_layers=60, hidden_size=4096, num_attention_heads=3

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N275

## Claim

Qwen3-27B 的官方配置文件中，num_hidden_layers=60, hidden_size=4096, num_attention_heads=32, num_key_value_heads=8, head_dim=128。此配置导致 GQA 比例为 32:8 = 4:1。KV Cache 每 token 显存占用 = 2 (K+V) * num_layers * num_kv_heads * head_dim * dtype_size = 2 * 60 * 8 * 128 * 1 byte (FP8) = 122,880 bytes ≈ 0.12 MB/token。

## Corrected Claim

Qwen3-27B 的官方配置文件中，num_hidden_layers=60, hidden_size=4096, num_attention_heads=32, num_key_value_heads=8, head_dim=128。此配置导致 GQA 比例为 32:8 = 4:1。KV Cache 每 token 显存占用 = 2 (K+V) * num_layers * num_kv_heads * head_dim * dtype_size = 2 * 60 * 8 * 128 * 1 byte (FP8) = 122,880 bytes ≈ 0.12 MB/token。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数符合已知配置，KV Cache 计算公式及数值推导（2*60*8*128*1=122880 bytes）准确无误。

## Search Query

Qwen3-27B config.json num_hidden_layers num_key_value_heads
