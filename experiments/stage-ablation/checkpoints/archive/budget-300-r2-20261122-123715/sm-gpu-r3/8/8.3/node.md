# N109: GQA 下 KV Cache 显存精确计算公式：KV_GB = (2 * num_layers * num_kv_heads * head_dim * seq_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26, N27

## Claim

GQA 下 KV Cache 显存精确计算公式：KV_GB = (2 * num_layers * num_kv_heads * head_dim * seq_len * dtype_size) / 1024^3

## Corrected Claim

GQA 下 KV Cache 显存精确计算公式：KV_GB = (2 * num_layers * num_kv_heads * head_dim * seq_len * dtype_size) / 1024^3

## Evidence

先验知识/题面给定，逻辑校验通过：公式中 2 代表 Key 和 Value 两个张量，num_layers * num_kv_heads * head_dim * seq_len 为单个张量的元素总数，乘以 dtype_size 得到字节数，除以 1024^3 转换为 GB，量纲与逻辑均正确。
