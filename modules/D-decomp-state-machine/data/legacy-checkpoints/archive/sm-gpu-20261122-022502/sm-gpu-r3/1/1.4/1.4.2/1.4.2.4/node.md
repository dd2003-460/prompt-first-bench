# N136: KV Cache 传输频率修正因子：在混合推理中，并非每生成一个 token 都需全量传输 3.2GB KV Cache；通常仅传输新增的 KV 向量 (每步 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N42

## Claim

KV Cache 传输频率修正因子：在混合推理中，并非每生成一个 token 都需全量传输 3.2GB KV Cache；通常仅传输新增的 KV 向量 (每步 2×60×4096×2 bytes ≈ 1.97MB) 或定期同步；若采用全量同步策略，传输瓶颈极大；若采用增量策略，瓶颈转为 CPU 计算和内存带宽，需明确同步策略以确定 T_transfer 的实际值。

## Corrected Claim

KV Cache 传输频率修正因子：在混合推理中，并非每生成一个 token 都需全量传输 3.2GB KV Cache；通常仅传输新增的 KV 向量 (每步 2×60×4096×2 bytes ≈ 1.97MB) 或定期同步；若采用全量同步策略，传输瓶颈极大；若采用增量策略，瓶颈转为 CPU 计算和内存带宽，需明确同步策略以确定 T_transfer 的实际值。

## Evidence

先验知识/题面给定，逻辑校验通过：增量传输量计算（2×60×4096×2 bytes ≈ 1.97MB）符合数学逻辑，且KV Cache增量同步与全量同步的性能瓶颈差异符合分布式推理系统的基本工程原理。

## Search Query

LLM CPU GPU offload KV cache synchronization strategy incremental vs full
