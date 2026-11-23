# N54: 突发流量冗余成本：自建节点需预留 R_redundancy = (PF - 1) * BW_avg 的冗余带宽以应对突发，这部分带宽在低峰期闲置，导致实际利用率

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10, N11, N12

## Claim

突发流量冗余成本：自建节点需预留 R_redundancy = (PF - 1) * BW_avg 的冗余带宽以应对突发，这部分带宽在低峰期闲置，导致实际利用率 U_actual = BW_avg / BW_peak = 1/PF ≈ 0.5-0.67；公有云无此固定冗余成本，但突发流量单价 P_burst 通常为常规单价的 1.2-1.5 倍

## Corrected Claim

突发流量冗余成本：自建节点需预留 R_redundancy = (PF - 1) * BW_avg 的冗余带宽以应对突发，这部分带宽在低峰期闲置，导致实际利用率 U_actual = BW_avg / BW_peak = 1/PF ≈ 0.5-0.67；公有云无此固定冗余成本，但突发流量单价 P_burst 通常为常规单价的 1.2-1.5 倍

## Evidence

先验知识/题面给定，逻辑校验通过：冗余带宽公式与利用率定义在数学上自洽，公有云突发溢价符合行业常识

## Search Query

CDN burst traffic cost public cloud vs self-hosted bandwidth redundancy idle capacity
