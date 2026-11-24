# N302: 公有云CDN最小灰度粒度为1%流量（基于权重配置），支持按地域/IP/UA多维组合，实际最小可控单元为1%总流量，即500万日活中5万用户。

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N114

## Claim

公有云CDN最小灰度粒度为1%流量（基于权重配置），支持按地域/IP/UA多维组合，实际最小可控单元为1%总流量，即500万日活中5万用户。

## Corrected Claim

主流公有云CDN通常支持基于权重的流量灰度，最小粒度常见为1%（具体依厂商而定），在500万日活场景下，1%流量约对应5万用户。

## Evidence

[质询]「公有云CDN」并非单一标准产品，不同厂商（如阿里云、腾讯云、AWS CloudFront）的灰度粒度、配置方式（权重/地域/UA）及最小可控单元存在差异，且1%流量对应5万用户是基于500万日活的特定假设，并非通用物理或逻辑常数，属于具体产品经验参数。 | source=knowledge，逻辑自洽（1% * 500万 = 5万），但具体产品参数（最小粒度1%、多维组合支持）属于经验事实，缺乏通用性，且无外部来源验证特定厂商是否均支持此粒度，故降级。

## Search Query

Cloudflare weighted load balancing minimum percentage
