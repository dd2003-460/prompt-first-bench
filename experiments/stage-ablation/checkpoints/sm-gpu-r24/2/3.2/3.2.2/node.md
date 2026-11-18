# N39: KV Cache 大小计算公式：2 * L * H_kv * head_dim * seq_len * bytes_per_element，其中 2 代表 K 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

KV Cache 大小计算公式：2 * L * H_kv * head_dim * seq_len * bytes_per_element，其中 2 代表 K 和 V 两个矩阵

## Corrected Claim

KV Cache 大小计算公式：2 * L * H_kv * head_dim * seq_len * bytes_per_element，其中 2 代表 K 和 V 两个矩阵

## Evidence

先验知识/题面给定，逻辑校验通过
