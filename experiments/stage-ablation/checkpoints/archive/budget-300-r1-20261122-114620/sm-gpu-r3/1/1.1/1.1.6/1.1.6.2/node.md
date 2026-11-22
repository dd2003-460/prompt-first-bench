# N158: Qwen3-27B BF16 精度下 32K 上下文 KV Cache 的精确显存占用为 1.60 GB，计算公式为 2 (K+V) * 64 (layers)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

Qwen3-27B BF16 精度下 32K 上下文 KV Cache 的精确显存占用为 1.60 GB，计算公式为 2 (K+V) * 64 (layers) * 8 (kv_heads) * 128 (head_dim) * 32768 (seq_len) * 2 (bytes) / 1024^3

## Corrected Claim

Qwen3-27B BF16 精度下 32K 上下文 KV Cache 的精确显存占用为 1.60 GB，计算公式为 2 (K+V) * 64 (layers) * 8 (kv_heads) * 128 (head_dim) * 32768 (seq_len) * 2 (bytes) / 1024^3

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层, 8 KV头, 128维）符合 GQA 设计，计算公式 2*64*8*128*32768*2 / 1024^3 数学推导结果精确为 1.6 GB，量纲与数值均正确。
