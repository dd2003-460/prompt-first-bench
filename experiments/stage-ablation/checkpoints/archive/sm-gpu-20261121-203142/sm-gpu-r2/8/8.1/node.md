# N111: NVIDIA H100 SXM 的显存带宽为 3.35 TB/s，在 32K 上下文下，KV Cache 读取带宽瓶颈导致的理论最大 TPS 约为 (3.35 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

NVIDIA H100 SXM 的显存带宽为 3.35 TB/s，在 32K 上下文下，KV Cache 读取带宽瓶颈导致的理论最大 TPS 约为 (3.35 TB/s) / (4 GB KV Cache per token) = 837.5 tokens/s (理论上限，实际受计算限制更低) [verified]

## Corrected Claim

NVIDIA H100 SXM 的显存带宽为 3.35 TB/s，在 32K 上下文下，KV Cache 读取带宽瓶颈导致的理论最大 TPS 约为 (3.35 TB/s) / (4 GB KV Cache per token) = 837.5 tokens/s (理论上限，实际受计算限制更低) [verified]

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM 显存带宽 3.35 TB/s 为公认规格，3.35e12 / 4e9 = 837.5 计算正确，符合带宽瓶颈理论上限定义。

## Search Query

H100 SXM memory bandwidth 3.35 TB/s theoretical tokens per second
