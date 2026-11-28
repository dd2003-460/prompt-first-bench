# N75: Qwen3-27B 在 FP8 KV Cache 配置下，32K 上下文窗口的显存占用计算公式：KV_FP8_GB = 2 * n_layers * n_kv_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

Qwen3-27B 在 FP8 KV Cache 配置下，32K 上下文窗口的显存占用计算公式：KV_FP8_GB = 2 * n_layers * n_kv_heads * head_dim * 32768 * 1 byte / 1024^3，相比 BF16 KV Cache (2 bytes) 缩减比例为 50%。

## Corrected Claim

Qwen3-27B 在 FP8 KV Cache 配置下，32K 上下文窗口的显存占用计算公式：KV_FP8_GB = 2 * n_layers * n_kv_heads * head_dim * 32768 * 1 byte / 1024^3，相比 BF16 KV Cache (2 bytes) 缩减比例为 50%。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8为单字节精度，BF16为双字节精度，显存占用与数据位宽成正比，故缩减比例为50%，公式量纲与逻辑自洽。

## Search Query

Qwen3 27B FP8 KV cache memory footprint calculation formula
