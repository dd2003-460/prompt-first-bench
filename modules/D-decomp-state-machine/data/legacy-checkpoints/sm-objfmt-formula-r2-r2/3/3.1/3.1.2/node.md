# N92: Batch Size=1 时，每 Token 需读取的 KV Cache 字节数计算公式：KV_Read_Bytes_per_Token = 2 * n_lay

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

Batch Size=1 时，每 Token 需读取的 KV Cache 字节数计算公式：KV_Read_Bytes_per_Token = 2 * n_layers * n_kv_heads * head_dim * dtype_bytes，其中 dtype_bytes 取决于 KV Cache 精度（BF16=2, INT8/FP8=1）。

## Corrected Claim

Batch Size=1 时，每 Token 需读取的 KV Cache 字节数计算公式：KV_Read_Bytes_per_Token = 2 * n_layers * n_kv_heads * head_dim * dtype_bytes，其中 dtype_bytes 取决于 KV Cache 精度（BF16=2, INT8/FP8=1）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

per token KV cache read bytes calculation batch size 1 inference
