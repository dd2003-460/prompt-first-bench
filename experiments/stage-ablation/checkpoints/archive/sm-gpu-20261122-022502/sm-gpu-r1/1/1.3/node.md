# N8: 非典型方案统一内存容量：Apple M2 Ultra 192GB (BF16可行), M3 Ultra 512GB (BF16可行), 但内存带宽~800GB/

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

非典型方案统一内存容量：Apple M2 Ultra 192GB (BF16可行), M3 Ultra 512GB (BF16可行), 但内存带宽~800GB/s vs H100~3.35TB/s，推理吞吐量差距约4-5倍

## Corrected Claim

非典型方案统一内存容量：Apple M2 Ultra 192GB (BF16可行), M3 Ultra 512GB (BF16可行), 但内存带宽~800GB/s vs H100~3.35TB/s，推理吞吐量差距约4-5倍

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra带宽256GB/s，M3 Ultra带宽800GB/s，H100 SXM带宽3.35TB/s，带宽比约4.2-13倍，与陈述中4-5倍差距（可能指特定场景或保守估计）在量级上兼容，且内存容量数据准确。

## Search Query

Apple M2 Ultra memory bandwidth LLM inference throughput comparison H100
