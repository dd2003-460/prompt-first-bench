# N372: 修正N126错误：N126中'KV Cache per token = 128KB'及'可支持68个token'计算错误。基于Qwen3-27B正确参数（num

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N126

## Claim

修正N126错误：N126中'KV Cache per token = 128KB'及'可支持68个token'计算错误。基于Qwen3-27B正确参数（num_layers=64, n_kv_heads=8, head_dim=128, BF16），KV Cache per token = 2 * 64 * 8 * 128 * 2 bytes = 256 KB。PagedAttention不改变总KV Cache大小，仅优化内存碎片，8.5GB显存可支持 8.5GB / 256KB = 34,000 tokens的KV Cache，足以覆盖32K上下文（32,768 tokens）单请求需求。

## Corrected Claim

修正N126错误：N126中'KV Cache per token = 128KB'及'可支持68个token'计算错误。基于Qwen3-27B正确参数（num_layers=64, n_kv_heads=8, head_dim=128, BF16），KV Cache per token = 2 * 64 * 8 * 128 * 2 bytes = 256 KB。PagedAttention不改变总KV Cache大小，仅优化内存碎片，8.5GB显存可支持 8.5GB / 256KB = 34,000 tokens的KV Cache，足以覆盖32K上下文（32,768 tokens）单请求需求。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache计算公式正确（2*64*8*128*2=256KB），容量估算合理（8.5GB/256KB≈34000 tokens > 32768 tokens）
