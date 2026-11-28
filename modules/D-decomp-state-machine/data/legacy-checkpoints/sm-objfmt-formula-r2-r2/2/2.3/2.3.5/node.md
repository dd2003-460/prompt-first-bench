# N77: Qwen3-27B 在 INT8 KV Cache 配置下，32K 上下文窗口的显存占用计算公式：KV_INT8_GB = 2 * n_layers * n_k

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

Qwen3-27B 在 INT8 KV Cache 配置下，32K 上下文窗口的显存占用计算公式：KV_INT8_GB = 2 * n_layers * n_kv_heads * head_dim * 32768 * 1 byte / 1024^3，相比 BF16 KV Cache (2 bytes) 缩减比例为 50%。

## Corrected Claim

Qwen3-27B 在 INT8 KV Cache 配置下，32K 上下文窗口的显存占用计算公式：KV_INT8_GB = 2 * n_layers * n_kv_heads * head_dim * 32768 * 1 byte / 1024^3，相比 BF16 KV Cache (2 bytes) 缩减比例为 50%。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8 (1 byte) 相比 BF16 (2 bytes) 的显存占用缩减比例确为 50%，公式中各参数（层数、头数、维度、序列长度、字节数）的量纲与计算逻辑自洽。

## Search Query

Qwen3 27B INT8 KV cache memory footprint calculation formula
