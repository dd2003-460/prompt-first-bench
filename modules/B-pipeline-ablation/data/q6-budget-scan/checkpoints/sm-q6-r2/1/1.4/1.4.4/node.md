# N51: 自建节点的带宽预留策略需基于 $B_{peak}$ 而非 $B_{avg}$，且需预留 20%-30% 的带宽余量以应对突发流量，即实际采购带宽 $B_{pur

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10, N11, N12

## Claim

自建节点的带宽预留策略需基于 $B_{peak}$ 而非 $B_{avg}$，且需预留 20%-30% 的带宽余量以应对突发流量，即实际采购带宽 $B_{purchase} = B_{peak} \times 1.25$。

## Corrected Claim

自建节点的带宽预留策略需基于 $B_{peak}$ 而非 $B_{avg}$，且需预留 20%-30% 的带宽余量以应对突发流量，即实际采购带宽 $B_{purchase} = B_{peak} \times 1.25$。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

self-hosted CDN bandwidth overprovisioning best practice
