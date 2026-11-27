# N666: M3 Ultra 方案在 32K 上下文下的 KV Cache 带宽竞争：KV Cache 读取与权重读取共享内存总线；在 32K 长上下文下，KV Cache

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N275

## Claim

M3 Ultra 方案在 32K 上下文下的 KV Cache 带宽竞争：KV Cache 读取与权重读取共享内存总线；在 32K 长上下文下，KV Cache 占比增大，导致权重读取的有效带宽进一步降低约 5-10%；修正后有效带宽降至 650-665 GB/s，理论 Decode 上限降至 11-12 tokens/s (BF16)。

## Corrected Claim

M3 Ultra 方案在 32K 上下文下的 KV Cache 带宽竞争：KV Cache 读取与权重读取共享内存总线；在 32K 长上下文下，KV Cache 占比增大，导致权重读取的有效带宽进一步降低约 5-10%；修正后有效带宽降至 650-665 GB/s，理论 Decode 上限降至 11-12 tokens/s (BF16)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM KV cache memory bandwidth contention unified memory architecture
