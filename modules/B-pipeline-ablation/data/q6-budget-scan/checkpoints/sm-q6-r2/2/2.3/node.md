# N13: 回源路径延迟 $L_{backhaul}$ 受 POP 点覆盖范围影响：自建 POP 若覆盖核心区域，回源距离缩短，$L_{backhaul}$ 降低；公有云 

- **status**: pending
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

父节点级核验未通过：不完备（子节点之间存在明显的逻辑层级错位和概念混淆。父节点讨论的是‘回源路径延迟’（Origin Pull），但子节点2和3计算的是‘用户到POP’的接入延迟（Access Latency），而非POP到源站的回源延迟。此外，子节点4和5虽然涉及排队延迟，但未明确区分是接入链路还是回源链路的排队，导致与父节点核心概念‘回源’脱节。）

## Search Query

CDN backhaul latency comparison self-hosted vs public cloud
