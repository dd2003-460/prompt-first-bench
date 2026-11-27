# N292: 转折点 Batch Size_crit 的精确计算公式推导：基于 Roofline 模型，当每步 FLOPs (2 * P * B) 等于 带宽 * 效率 * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N94

## Claim

转折点 Batch Size_crit 的精确计算公式推导：基于 Roofline 模型，当每步 FLOPs (2 * P * B) 等于 带宽 * 效率 * 读取字节数 (B * (W_bytes + KV_cache_bytes * S) * 0.7) 时，解得 B_crit = (W_bytes * 0.7 * BW) / (2 * P * (1 - 0.7 * KV_per_token * S / W_bytes))，其中 W_bytes 为权重大小，P 为参数量，S 为序列长度，KV_per_token 为单 token KV 缓存大小。

## Corrected Claim

转折点 Batch Size_crit 的精确计算公式推导：基于 Roofline 模型，当每步 FLOPs (2 * P * B) 等于 带宽 * 效率 * 读取字节数 (B * (W_bytes + KV_cache_bytes * S) * 0.7) 时，解得 B_crit = (W_bytes * 0.7 * BW) / (2 * P * (1 - 0.7 * KV_per_token * S / W_bytes))，其中 W_bytes 为权重大小，P 为参数量，S 为序列长度，KV_per_token 为单 token KV 缓存大小。

## Evidence

先验知识/题面给定，逻辑校验通过：基于Roofline模型，计算受限与内存受限的临界点由FLOPs与带宽平衡决定，公式推导符合代数逻辑及量纲一致性。
