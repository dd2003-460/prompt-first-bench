# N122: Qwen3-27B 在 64K 上下文下的 KV Cache 显存占用计算公式：KV_64K = 2 × num_layers × num_kv_heads ×

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

Qwen3-27B 在 64K 上下文下的 KV Cache 显存占用计算公式：KV_64K = 2 × num_layers × num_kv_heads × head_dim × 64 × 1024 × bytes_per_elem，该值通常为 32K 占用量的 2 倍，需代入 N31 获取的架构参数得出具体 GB 值。

## Corrected Claim

Qwen3-27B 在 64K 上下文下的 KV Cache 显存占用计算公式：KV_64K = 2 × num_layers × num_kv_heads × head_dim × 64 × 1024 × bytes_per_elem，该值通常为 32K 占用量的 2 倍，需代入 N31 获取的架构参数得出具体 GB 值。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 显存占用与上下文长度成正比，64K 为 32K 的 2 倍符合线性关系，公式结构正确。
