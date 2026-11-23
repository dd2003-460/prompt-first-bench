# N13: 回源路径延迟 $L_{backhaul}$ 受 POP 点覆盖范围影响：自建 POP 若覆盖核心区域，回源距离缩短，$L_{backhaul}$ 降低；公有云 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

回源路径延迟 $L_{backhaul}$ 受 POP 点覆盖范围影响：自建 POP 若覆盖核心区域，回源距离缩短，$L_{backhaul}$ 降低；公有云 CDN 通常有更深层次的 POP 覆盖，回源延迟更稳定，但成本更高。需量化不同拓扑下的 RTT 差异（如自建 20ms vs 公有云 10ms）。

## Corrected Claim

回源路径延迟 $L_{backhaul}$ 受 POP 点覆盖范围影响：自建 POP 若覆盖核心区域，回源距离缩短，$L_{backhaul}$ 降低；公有云 CDN 通常有更深层次的 POP 覆盖，回源延迟更稳定，但成本更高。需量化不同拓扑下的 RTT 差异（如自建 20ms vs 公有云 10ms）。

## Evidence

先验知识/题面给定，逻辑校验通过：POP覆盖范围与回源距离/延迟呈负相关符合网络物理规律，公有云因规模效应通常具备更优的节点分布和稳定性，虽成本更高但延迟更稳定，逻辑自洽且数值量级（20ms vs 10ms）在合理范围内。

## Search Query

CDN backhaul latency comparison self-hosted vs public cloud
