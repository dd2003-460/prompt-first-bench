# N8: 非典型方案统一内存容量：Apple M2 Ultra 192GB (BF16可行), M3 Ultra 512GB (BF16可行), 但内存带宽~800GB/

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

非典型方案统一内存容量：Apple M2 Ultra 192GB (BF16可行), M3 Ultra 512GB (BF16可行), 但内存带宽~800GB/s vs H100~3.35TB/s，推理吞吐量差距约4-5倍

## Corrected Claim

非典型方案统一内存容量：Apple M2 Ultra 192GB (BF16可行), M3 Ultra 512GB (BF16可行), 但内存带宽~800GB/s vs H100~3.35TB/s，推理吞吐量差距约4-5倍

## Evidence

父节点级核验未通过：有冗余（子节点在结构上重复了相同的带宽对比逻辑和吞吐量推导过程，仅数值（192GB/800GB/s vs 512GB/819GB/s）和结论侧重点（基础吞吐 vs 容量过剩/性价比）不同。这属于同一分析框架下的参数变体，而非正交的不同维度。）

## Search Query

Apple M2 Ultra memory bandwidth LLM inference throughput comparison H100
