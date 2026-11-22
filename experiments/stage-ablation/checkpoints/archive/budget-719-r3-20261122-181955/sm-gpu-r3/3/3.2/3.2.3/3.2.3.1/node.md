# N288: KV Cache 读取带宽占比 R_kv 的精确计算公式为 R_kv = (KV_Size_per_token * Seq_Len) / (Weights_Si

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N95

## Claim

KV Cache 读取带宽占比 R_kv 的精确计算公式为 R_kv = (KV_Size_per_token * Seq_Len) / (Weights_Size + KV_Size_per_token * Seq_Len)；在 32K 上下文、BF16 权重 (54GB) 下，R_kv = 536.87MB / (54GB + 536.87MB) ≈ 0.98，即 98%，远高于 N95 声称的 70-85%，表明长上下文下 KV Cache 是绝对瓶颈。

## Corrected Claim

KV Cache 读取带宽占比 R_kv 的精确计算公式为 R_kv = (KV_Size_per_token * Seq_Len) / (Weights_Size + KV_Size_per_token * Seq_Len)；在 32K 上下文、BF16 权重 (54GB) 下，R_kv = 536.87MB / (54GB + 536.87MB) ≈ 0.98，即 98%，远高于 N95 声称的 70-85%，表明长上下文下 KV Cache 是绝对瓶颈。

## Search Query

KV cache memory bandwidth bottleneck long context inference
