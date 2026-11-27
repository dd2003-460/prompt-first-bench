# N124: Qwen3-27B KV Cache 在 FP16 精度下的精确字节数计算公式：Bytes = 2 * L_eff * num_kv_heads * head_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35, N36, N37

## Claim

Qwen3-27B KV Cache 在 FP16 精度下的精确字节数计算公式：Bytes = 2 * L_eff * num_kv_heads * head_dim * seq_len * batch_size，其中 L_eff 为 N37 确定的有效注意力层数，num_kv_heads=8, head_dim=128, seq_len=32768, batch_size=1。

## Corrected Claim

Qwen3-27B KV Cache 在 FP16 精度下的精确字节数计算公式：Bytes = 2 * L_eff * num_kv_heads * head_dim * seq_len * batch_size，其中 L_eff 为 N37 确定的有效注意力层数，num_kv_heads=8, head_dim=128, seq_len=32768, batch_size=1。

## Evidence

先验知识/题面给定，逻辑校验通过
