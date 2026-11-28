# N157: KV cache 显存占用的精确计算需考虑 Attention Head 的投影维度：对于 GQA (Grouped Query Attention) 架构，n

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

KV cache 显存占用的精确计算需考虑 Attention Head 的投影维度：对于 GQA (Grouped Query Attention) 架构，n_kv_heads 小于 n_heads，若误用 n_heads 会导致 KV 估算偏大 4 倍（假设 n_heads=32）。

## Corrected Claim

KV cache 显存占用的精确计算需考虑 Attention Head 的投影维度：对于 GQA (Grouped Query Attention) 架构，n_kv_heads 小于 n_heads，若误用 n_heads 会导致 KV 估算偏大 4 倍（假设 n_heads=32）。

## Evidence

先验知识/题面给定，逻辑校验通过：GQA中KV Cache大小正比于n_kv_heads，若误用n_heads且n_heads/n_kv_heads=4，则估算值确实偏大4倍，符合线性比例关系。

## Search Query

GQA grouped query attention KV cache calculation difference MHA
