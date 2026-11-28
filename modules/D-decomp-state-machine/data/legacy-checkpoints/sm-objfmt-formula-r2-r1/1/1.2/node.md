# N7: 32K 上下文窗口所需的 KV Cache 显存占用量（GB），计算公式为：2 × n_layers × n_kv_heads × head_dim × seq

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

32K 上下文窗口所需的 KV Cache 显存占用量（GB），计算公式为：2 × n_layers × n_kv_heads × head_dim × seq_len × dtype_bytes / 1024^3。

## Corrected Claim

32K 上下文窗口所需的 KV Cache 显存占用量（GB），计算公式为：2 × n_layers × n_kv_heads × head_dim × seq_len × dtype_bytes / 1024^3。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B architecture parameters n_layers n_kv_heads head_dim
