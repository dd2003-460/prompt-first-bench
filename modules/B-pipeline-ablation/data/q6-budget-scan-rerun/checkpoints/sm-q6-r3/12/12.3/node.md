# N409: SLA赔付率的具体量化：基于公有云CDN SLA条款（如阿里云/Cloudflare），赔付率通常为月服务费的 5%-30%（视故障时长和频率），而非固定10%

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N130

## Claim

SLA赔付率的具体量化：基于公有云CDN SLA条款（如阿里云/Cloudflare），赔付率通常为月服务费的 5%-30%（视故障时长和频率），而非固定10%；需查询具体SLA文档确定赔付阶梯（如连续故障>5分钟赔付10%，>30分钟赔付30%），并计算期望赔付额 E_penalty = Σ(P_fault_duration_j × penalty_rate_j)

## Corrected Claim

SLA赔付率通常基于月度服务可用性未达标程度进行阶梯式赔偿（具体比例需查阅最新SLA文档，阿里云CDN通常按月费的一定比例赔付），而非固定比例；需查询具体SLA文档确定赔付阶梯，并计算期望赔付额 E_penalty = Σ(P_fault_duration_j × penalty_rate_j)。

## Evidence

[质询]陈述中给出的具体赔付阶梯数值（如“连续故障>5分钟赔付10%，>30分钟赔付30%”）属于经验事实，且与阿里云CDN SLA通常基于“月度服务可用性百分比”而非“单次故障时长”进行阶梯赔付的常见逻辑存在潜在冲突，参考来源摘要未直接证实该具体数值阶梯。 | 来源[1][2]确认了阿里云CDN SLA存在赔偿方案，但摘要未提供具体的赔付率数值（5%-30%）或基于故障时长的具体阶梯（>5min/10%等），属于经验事实缺直接来源支持，逻辑上期望值公式自洽。

## Search Query

Alibaba Cloud CDN SLA penalty rate Cloudflare SLA compensation terms

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/support/alibaba-cloud-cdn-sla&rut=3956d40b61723b624586e57a9ca801bbecb2bb04169a8328aa7a4c0cbff04394', 'type': 'ddg', 'title': 'Cdn服务等级协议sla的服务可用性指标与赔偿方案-cdn-阿里云'}
- {'url': 'http://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud201803050950_21147.html&rut=4ea3dffc5b57a36309cd0a05201504fd407668bd99f18ab73a0500d16bf07fb8', 'type': 'ddg', 'title': 'CDN服务等级协议 - aliyun.com'}
- {'url': 'https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud201804111508_13381.html&rut=8100621ccca4fa704fda5070914f5756708eb2af10288c1296c2e32c7e194bdd', 'type': 'ddg', 'title': '全站加速服务等级协议 - aliyun.com'}
