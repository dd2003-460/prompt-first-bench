# N66: KV Cache 在 Decode 阶段的带宽瓶颈系数：每生成一个 token，需读取之前所有 token 的 KV Cache 以计算 Attention。3

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

KV Cache 在 Decode 阶段的带宽瓶颈系数：每生成一个 token，需读取之前所有 token 的 KV Cache 以计算 Attention。32K 上下文下，单 token 需读取的 KV Cache 大小 = 32768 × (num_kv_heads × head_dim × 2 × 2 bytes)。若 num_kv_heads=8, head_dim=128，则单 token 读取量约 134 MB。带宽需求 = 134 MB / target_TPS。

## Corrected Claim

KV Cache 在 Decode 阶段的带宽瓶颈系数：每生成一个 token，需读取之前所有 token 的 KV Cache 以计算 Attention。32K 上下文下，单 token 需读取的 KV Cache 大小 = 32768 × (num_kv_heads × head_dim × 2 × 2 bytes)。若 num_kv_heads=8, head_dim=128，则单 token 读取量约 134 MB。带宽需求 = 134 MB / target_TPS。

## Evidence

先验知识/题面给定，逻辑校验通过：32768 * 8 * 128 * 2 * 2 = 134,217,728 bytes ≈ 134 MB，计算无误且符合KV Cache带宽瓶颈的基本原理。

## Search Query

KV cache memory bandwidth requirement per token long context inference
