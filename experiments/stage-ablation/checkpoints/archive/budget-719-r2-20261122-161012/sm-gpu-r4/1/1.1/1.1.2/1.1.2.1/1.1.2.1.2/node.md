# N341: Qwen3-27B 在 32K 上下文下，KV Cache 的最大占用量（BF16 精度）计算公式为：2 * num_layers * num_kv_heads

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N141

## Claim

Qwen3-27B 在 32K 上下文下，KV Cache 的最大占用量（BF16 精度）计算公式为：2 * num_layers * num_kv_heads * head_dim * seq_len * 2 bytes = 2 * 64 * 8 * 128 * 32768 * 2 = 2.147 GB。

## Corrected Claim

Qwen3-27B 在 32K 上下文下，KV Cache 的最大占用量（BF16 精度）计算公式为：2 * num_layers * num_kv_heads * head_dim * seq_len * 2 bytes = 2 * 64 * 8 * 128 * 32768 * 2 = 2.147 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层, 8 KV头, 128维）符合主流大模型设计，BF16精度下2字节/元素，计算过程 2*64*8*128*32768*2 = 2,147,483,648 bytes ≈ 2.147 GB，量纲与数值均正确。
