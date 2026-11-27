# N271: H100 的显存带宽 (HBM3) 为 3.35 TB/s (3350 GB/s)，在 Decode 阶段 (Memory-Bound) 中，理论最大吞吐量 (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

H100 的显存带宽 (HBM3) 为 3.35 TB/s (3350 GB/s)，在 Decode 阶段 (Memory-Bound) 中，理论最大吞吐量 (tokens/s) 由 显存带宽 / (模型权重大小 + KV Cache 大小) 决定，例如对于 27B INT4 模型 (13.5GB)，理论上限约为 3350/13.5 ≈ 248 tokens/s (单请求)，实际受计算和并行度限制通常为此值的 50-70%

## Corrected Claim

H100 的显存带宽 (HBM3) 为 3.35 TB/s (3350 GB/s)，在 Decode 阶段 (Memory-Bound) 中，理论最大吞吐量 (tokens/s) 由 显存带宽 / (模型权重大小 + KV Cache 大小) 决定，例如对于 27B INT4 模型 (13.5GB)，理论上限约为 3350/13.5 ≈ 248 tokens/s (单请求)，实际受计算和并行度限制通常为此值的 50-70%

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 HBM3带宽确为3.35TB/s，27B INT4模型权重大小约13.5GB，理论吞吐量计算3350/13.5≈248 tokens/s符合Memory-Bound阶段的基本物理直觉，实际效率50-70%符合工程经验。
