# N49: KV Cache 精确计算公式：KV_Cache_GB = (2 × num_layers × num_kv_heads × head_dim × seq_le

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8, N9, N10

## Claim

KV Cache 精确计算公式：KV_Cache_GB = (2 × num_layers × num_kv_heads × head_dim × seq_len × dtype_bytes) / (1024^3)，其中 head_dim = hidden_size / num_attention_heads = 128。

## Corrected Claim

KV Cache 精确计算公式：KV_Cache_GB = (2 × num_layers × num_kv_heads × head_dim × seq_len × dtype_bytes) / (1024^3)，其中 head_dim = hidden_size / num_attention_heads = 128。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合Transformer KV Cache存储原理（Key和Value各一份，故系数为2；维度乘积正确；单位换算正确），head_dim=128是常见架构参数，逻辑自洽。

## Search Query

KV cache memory calculation formula GQA head_dim
