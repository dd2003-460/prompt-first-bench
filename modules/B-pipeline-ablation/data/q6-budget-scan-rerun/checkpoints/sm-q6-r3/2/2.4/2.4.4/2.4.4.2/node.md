# N234: Cloudflare Enterprise Plan SLA赔付条款：若P99延迟超过承诺值（如150ms）持续5分钟以上，赔付当月带宽费用的10%-50%，具

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

Cloudflare Enterprise Plan SLA赔付条款：若P99延迟超过承诺值（如150ms）持续5分钟以上，赔付当月带宽费用的10%-50%，具体比例取决于SLA等级

## Corrected Claim

Cloudflare Enterprise Plan包含服务等级协议（SLA），具体服务（如R2等）可能有独立的Service-Specific SLA，但通用Enterprise SLA摘要未明确列出P99延迟150ms及10%-50%带宽费用赔付的具体条款，需查阅具体服务条款或定制合同以确认延迟相关赔付细节。

## Evidence

[质询]具体数值（P99 150ms、持续5分钟、赔付10%-50%）在提供的参考来源摘要中未出现，且Cloudflare SLA通常针对可用性（Uptime）而非特定延迟值（Latency），延迟SLA通常属于特定服务（如R2或特定企业定制条款），通用Enterprise SLA摘要未涵盖此细节，存在将特定服务条款或虚构数值误植为通用条款的风险。 | 参考来源[1]和[2]确认存在Enterprise SLA及Service-Specific SLA机制，但摘要中未包含具体的延迟阈值（150ms）、持续时间（5分钟）及赔付比例（10%-50%）等经验性参数，无法直接支持该具体陈述，故降级。

## Search Query

Cloudflare Enterprise SLA penalty P99 latency

## Retrieval Sources

- {'url': 'https://www.cloudflare.com/enterprise-support-sla/&rut=5d295d8b39466cec9b57d01acf91f975c754095fd690ccd8a800451fbd10defa', 'type': 'ddg', 'title': 'Enterprise Subscription Service Level Agreement | Cloudflare'}
- {'url': 'https://www.cloudflare.com/r2-service-level-agreement/&rut=bac3d42d3bc7eca5af17e5083b30f98f99d09269f2f0261694f1e29a782977da', 'type': 'ddg', 'title': 'Enterprise Subscription Service Level Agreement | Cloudflare'}
- {'url': 'https://www.cloudflare-cn.com/enterpriseterms/&rut=37c786d7a205bd12e407502f1903990648b627c38d9197b8559bbc5de0700758', 'type': 'ddg', 'title': 'ENTERPRISE SUBSCRIPTION u2028TERMS OF SERVICE | Cloudflare'}
