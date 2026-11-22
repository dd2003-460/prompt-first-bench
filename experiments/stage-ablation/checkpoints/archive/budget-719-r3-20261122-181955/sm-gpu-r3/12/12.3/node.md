# N380: RTX 5090 32GB 显存中，扣除 54GB BF16 权重后显存不足，必须使用 INT4/FP8 量化；若使用 INT4 (13.5GB 权重)，剩余 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N128

## Claim

RTX 5090 32GB 显存中，扣除 54GB BF16 权重后显存不足，必须使用 INT4/FP8 量化；若使用 INT4 (13.5GB 权重)，剩余 18.5GB 显存可支持约 18.5GB / (KV Cache per token) 的并发请求或更长上下文，具体需结合 KV Cache 大小计算。

## Corrected Claim

RTX 5090 32GB 显存中，若加载 54GB BF16 权重，显存严重不足（需多卡或量化）；若使用 INT4 量化（约 13.5GB 权重），剩余约 18.5GB 显存可用于 KV Cache，具体并发数需结合 KV Cache per token 大小计算。

## Evidence

[质询]数值量级严重错误：RTX 5090 显存为 32GB，而陈述中声称扣除 '54GB BF16 权重'，54GB 远大于 32GB，导致逻辑前提（'扣除后显存不足'）在算术上不成立（32 - 54 < 0），且暗示模型权重本身已超出单卡容量，与后续讨论单卡剩余显存支持 KV Cache 的语境矛盾。 | 逻辑校验失败：32GB 显存无法容纳 54GB 权重，陈述内部数值自相矛盾。
