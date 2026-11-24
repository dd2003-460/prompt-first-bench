# N125: SLA 赔偿条款具体化：公有云 CDN 通常承诺 99.9% 可用性，违约赔偿上限为月度服务费的 10%-30%，而非按毫秒线性赔偿；自建无外部 SLA，惩罚仅

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

SLA 赔偿条款具体化：公有云 CDN 通常承诺 99.9% 可用性，违约赔偿上限为月度服务费的 10%-30%，而非按毫秒线性赔偿；自建无外部 SLA，惩罚仅体现为内部机会成本（用户流失）。

## Corrected Claim

公有云 CDN 通常承诺 99.9% 或更高可用性，违约赔偿通常以月度服务费的一定比例（如50%-100%不等，视厂商而定）为上限，而非按毫秒线性赔偿；自建无外部 SLA，惩罚仅体现为内部机会成本（用户流失）。

## Evidence

[质询]具体数值区间（10%-30%）缺乏通用性，不同云厂商（如阿里云、AWS、Azure）的SLA赔偿上限差异巨大（有的仅为50%或固定金额，有的可达100%），且99.9%并非所有CDN产品的唯一标准（部分高端产品承诺99.95%或99.99%），该陈述将特定案例或平均值泛化为行业通用规则，存在以偏概全的风险。 | 来源[2]直接支持99.9%可用性承诺及存在服务信用索赔（即赔偿机制），但未明确支持'10%-30%'这一具体赔偿上限区间；来源[1]和[3]讨论了SLA设计陷阱和赔偿限制，但未提供具体的行业通用赔偿比例数据。逻辑上，'非按毫秒线性赔偿'和'自建无外部SLA'符合常识，但具体赔偿比例属于经验事实，缺乏多源一致的直接证据支持该特定区间。

## Search Query

Alibaba Cloud CDN SLA penalty clause maximum compensation percentage

## Retrieval Sources

- {'url': 'https://www.sre.wang/posts/sre-sla-design/&rut=3b17fd0a68c55f66d16151bbdb30d72b62c05c274803e2921e6fac592bc51c8c', 'type': 'ddg', 'title': '承诺 99.9% 赔了 0.7 元：Sla 条款拆解与内部设计的 6 个工程决策 | Sre工程实践'}
- {'url': 'https://www.alibabacloud.com/help/zh/legal/latest/content-delivery-network-service-level-agreement&rut=b204a44dcb369131155c400cc02c7f9c36ce6a921f1e6b2174fb2544606cb7bb', 'type': 'ddg', 'title': '了解 CDN 服务等级协议 - 内容分发网络 (CDN) -Alibaba Cloud'}
- {'url': 'https://blog.csdn.net/2509_93932836/article/details/156238377&rut=c31ed495366c0e11712c296d8b914d27179cdbe5d93ba35a19a440542f065497', 'type': 'ddg', 'title': '云服务SLA大揭秘：99.99%背后，是承诺还是文字游戏？_sla 99.99-CSDN博客'}
