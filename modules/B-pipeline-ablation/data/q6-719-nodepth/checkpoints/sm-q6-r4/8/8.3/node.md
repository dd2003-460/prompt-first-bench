# N181: 单 POP 峰值带宽需求 B_peak_pop (Mbps) 的计算：B_peak_pop = (B_avg * K_peak) / N_pop * (1 + 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N46

## Claim

单 POP 峰值带宽需求 B_peak_pop (Mbps) 的计算：B_peak_pop = (B_avg * K_peak) / N_pop * (1 + H_miss * Overhead)，其中 H_miss 为缓存未命中率，Overhead 为协议开销（TCP/IP 头部等，约 5-10%）。

## Corrected Claim

单 POP 峰值带宽需求 B_peak_pop (Mbps) 的计算：B_peak_pop = (B_avg * K_peak) / N_pop * (1 + H_miss * Overhead)，其中 H_miss 为缓存未命中率，Overhead 为协议开销（TCP/IP 头部等，约 5-10%）。

## Evidence

父节点级核验未通过：不完备（子节点仅提供了对象大小参数，而父节点公式中明确包含 K_peak（峰值因子）、N_pop（POP数量）以及 H_miss（缓存未命中率）和 Overhead（协议开销）等关键变量。子节点未能覆盖这些核心计算因子，导致分解不完备。此外，子节点提供的是输入参数而非公式本身的分解逻辑。）

## Search Query

CDN POP bandwidth sizing formula cache miss overhead
