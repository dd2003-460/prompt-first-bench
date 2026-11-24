# N232: 缓存命中率波动对回源带宽成本的量化影响：峰值期 H_peak = H_avg - ΔH，若 H_avg=0.95, ΔH=0.03，则 H_peak=0.92；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60, N61, N62

## Claim

缓存命中率波动对回源带宽成本的量化影响：峰值期 H_peak = H_avg - ΔH，若 H_avg=0.95, ΔH=0.03，则 H_peak=0.92；回源带宽比例从 5% 升至 8%，导致峰值期回源成本增加 60%（8%/5% - 1）。

## Corrected Claim

缓存命中率波动对回源带宽成本的量化影响：峰值期 H_peak = H_avg - ΔH，若 H_avg=0.95, ΔH=0.03，则 H_peak=0.92；回源带宽比例从 5% 升至 8%，导致峰值期回源成本增加 60%（8%/5% - 1）。

## Evidence

先验知识/题面给定，逻辑校验通过：0.95-0.03=0.92，回源比例1-H，从5%升至8%，成本增加(8-5)/5=60%，计算无误。

## Search Query

cache hit rate fluctuation peak load origin bandwidth cost increase
