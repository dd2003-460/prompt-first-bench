# N186: 标准 Attention 层的 KV Cache 字节数精确计算：Bytes_attn = 2 * L_attn * num_kv_heads (8) * he

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

标准 Attention 层的 KV Cache 字节数精确计算：Bytes_attn = 2 * L_attn * num_kv_heads (8) * head_dim (128) * seq_len (32768) * dtype_size (2 for FP16)，其中 L_attn = L_total - L_delta。

## Corrected Claim

标准 Attention 层的 KV Cache 字节数精确计算：Bytes_attn = 2 * L_attn * num_kv_heads (8) * head_dim (128) * seq_len (32768) * dtype_size (2 for FP16)，其中 L_attn = L_total - L_delta。

## Evidence

先验知识/题面给定，逻辑校验通过
