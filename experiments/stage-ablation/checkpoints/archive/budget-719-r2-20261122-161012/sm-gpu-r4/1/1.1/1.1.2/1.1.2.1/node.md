# N141: KV Cache 最大占用量计算：KV_Cache_Max = 2 (K+V) * num_layers * num_kv_heads * head_dim *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

KV Cache 最大占用量计算：KV_Cache_Max = 2 (K+V) * num_layers * num_kv_heads * head_dim * seq_len * dtype_size。对于 Qwen3-27B，需获取 num_kv_heads 和 head_dim 以计算 32K 上下文下的确切 GB 数值

## Corrected Claim

KV Cache 最大占用量计算：KV_Cache_Max = 2 (K+V) * num_layers * num_kv_heads * head_dim * seq_len * dtype_size。对于 Qwen3-27B，需获取 num_kv_heads 和 head_dim 以计算 32K 上下文下的确切 GB 数值

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且互斥：节点1提供基础架构参数（num_kv_heads, head_dim等），节点2基于标准精度（BF16）计算基准值，节点3探讨量化优化场景（FP8/INT4）。三者分别对应‘参数获取’、‘基准计算’和‘优化变体’，无内容重叠或矛盾，且共同完整覆盖了父节点关于计算KV Cache最大占用量的需求。）
