# N181: 单 POP 峰值带宽需求 B_peak_pop (Mbps) 的计算：B_peak_pop = (B_avg * K_peak) / N_pop * (1 + 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

单 POP 峰值带宽需求 B_peak_pop (Mbps) 的计算：B_peak_pop = (B_avg * K_peak) / N_pop * (1 + H_miss * Overhead)，其中 H_miss 为缓存未命中率，Overhead 为协议开销（TCP/IP 头部等，约 5-10%）。

## Corrected Claim

单 POP 峰值带宽需求 B_peak_pop (Mbps) 的计算：B_peak_pop = (B_avg * K_peak) / N_pop * (1 + H_miss * Overhead)，其中 H_miss 为缓存未命中率，Overhead 为协议开销（TCP/IP 头部等，约 5-10%）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN POP bandwidth sizing formula cache miss overhead
