# N412: 腾讯云CDN阶梯结构与阿里云类似但阈值略有不同：第一阶梯0-5TB ¥0.26/GB，第二阶梯5-50TB ¥0.22/GB，第三阶梯50TB+ ¥0.16/G

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N143

## Claim

腾讯云CDN阶梯结构与阿里云类似但阈值略有不同：第一阶梯0-5TB ¥0.26/GB，第二阶梯5-50TB ¥0.22/GB，第三阶梯50TB+ ¥0.16/GB，需对比两家供应商在60TB流量下的实际成本差异以选择最优公有云供应商

## Corrected Claim

腾讯云CDN采用阶梯计费结构，具体阈值与单价需查阅最新官方定价页（如来源[1]），通常随用量增加单价递减；需对比阿里云在同等流量下的实际成本以选择最优供应商。

## Evidence

[质询]具体价格数值（如¥0.26/GB、¥0.22/GB等）属于经验事实，且CDN价格随时间、地域及促销活动频繁变动，参考来源摘要中未包含具体的阶梯价格数值，无法直接验证这些具体数字的准确性。 | 来源[1]和[2]确认了腾讯云和阿里云CDN存在计费对比及阶梯/流量包模式，但摘要中未提供具体的阶梯阈值和单价数值，属于经验事实缺来源直接支持。

## Search Query

Tencent Cloud CDN tiered pricing 2024

## Retrieval Sources

- {'url': 'https://buy.cloud.tencent.com/price/cdn&rut=8b12217b52d13da99b4933ecc75cfa4a8ac8bd87880c93a6d88ec92b6400052a', 'type': 'ddg', 'title': '内容分发网络 Cdn定价 _ 内容分发网络 Cdn价格 _ 内容分发网络 Cdn计费模式 - 腾讯云'}
- {'url': 'https://lieke-ai.com/articles/cdn-pricing-comparison-20260904.html&rut=b4c9c0fd2f3e6a26231289fd82ba62b3f065aea5edca0ac83ccdfabb7eb3d215', 'type': 'ddg', 'title': 'CDN价格对比2026：阿里云CDN vs 腾讯云CDN流量包哪个便宜'}
