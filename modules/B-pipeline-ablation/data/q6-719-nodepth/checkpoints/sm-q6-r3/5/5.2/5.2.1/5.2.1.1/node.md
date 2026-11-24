# N438: 单 POP 峰值带宽需求 Q_peak_pop_Mbps 的计算公式：Q_peak_pop_Mbps = (B_avg_Mbps * K_peak * W_po

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N137

## Claim

单 POP 峰值带宽需求 Q_peak_pop_Mbps 的计算公式：Q_peak_pop_Mbps = (B_avg_Mbps * K_peak * W_pop) * (1 + H_miss * Overhead)，其中 W_pop 为该 POP 承载的流量权重（通常 1/N_pop），H_miss 为缓存未命中率，Overhead 为协议开销（约 5-10%）。

## Corrected Claim

单 POP 峰值带宽需求 Q_peak_pop_Mbps 的计算公式：Q_peak_pop_Mbps = (B_avg_Mbps * K_peak * W_pop) * (1 + H_miss * Overhead)，其中 W_pop 为该 POP 承载的流量权重（通常 1/N_pop），H_miss 为缓存未命中率，Overhead 为协议开销（约 5-10%）。

## Evidence

先验知识/题面给定，逻辑校验通过
