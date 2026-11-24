# N392: L2 节点到源站的回源带宽需求 B_origin：B_origin = B_avg * K_peak * (1 - Hit_rate_L1) * (1 - Hi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N121

## Claim

L2 节点到源站的回源带宽需求 B_origin：B_origin = B_avg * K_peak * (1 - Hit_rate_L1) * (1 - Hit_rate_L2)。由于 (1 - Hit_rate_L2) 极小（1-5%），源站出口带宽需求仅为总流量的 1-10%，显著低于单级缓存架构。

## Corrected Claim

L2 节点到源站的回源带宽需求 B_origin：B_origin = B_avg * K_peak * (1 - Hit_rate_L1) * (1 - Hit_rate_L2)。由于 (1 - Hit_rate_L2) 极小（1-5%），源站出口带宽需求仅为总流量的 1-10%，显著低于单级缓存架构。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN origin server bandwidth requirement two-tier cache architecture
