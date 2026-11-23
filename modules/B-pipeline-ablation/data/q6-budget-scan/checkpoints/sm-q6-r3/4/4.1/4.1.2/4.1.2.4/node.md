# N250: 自建节点P99延迟风险项中的最后1公里延迟 T_last_mile_P99_self：若自建节点未接入本地运营商骨干网，仅通过公网互联，P99延迟比公有云CDN

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77, N78, N79

## Claim

自建节点P99延迟风险项中的最后1公里延迟 T_last_mile_P99_self：若自建节点未接入本地运营商骨干网，仅通过公网互联，P99延迟比公有云CDN（多运营商BGP接入）高20-50ms；具体数值取决于用户地理分布，核心城市（如北上广深）自建节点若接入双运营商，P99延迟可控制在30-50ms，与公有云持平；长尾城市若仅单运营商接入，P99延迟可能达60-80ms。

## Corrected Claim

自建节点P99延迟风险项中的最后1公里延迟 T_last_mile_P99_self：若自建节点未接入本地运营商骨干网，仅通过公网互联，P99延迟比公有云CDN（多运营商BGP接入）高20-50ms；具体数值取决于用户地理分布，核心城市（如北上广深）自建节点若接入双运营商，P99延迟可控制在30-50ms，与公有云持平；长尾城市若仅单运营商接入，P99延迟可能达60-80ms。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

self-hosted edge node last mile latency vs public CDN BGP access
