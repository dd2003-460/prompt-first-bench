# N58: Cloudflare CDN月度基础成本计算：Cloudflare Pro/Enterprise计划通常包含基础带宽（如Pro $20/月含不限流量但有限速，E

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14, N15, N16

## Claim

Cloudflare CDN月度基础成本计算：Cloudflare Pro/Enterprise计划通常包含基础带宽（如Pro $20/月含不限流量但有限速，Enterprise定制），按量计费模式（如Free/Basic）下，若按$0.08/GB估算（需查证具体阶梯），月度成本 = 60,000GB * $0.08 * 7.2 (汇率) = ¥34,560/月；但Cloudflare主要按请求数或带宽峰值计费，实际成本可能因请求数（400万-4000万次/日）而异，需进一步分解请求单价。

## Corrected Claim

Cloudflare Pro/Enterprise计划通常采用固定月费或定制报价，而非简单的按GB计费。若假设存在按量计费场景（如特定API或旧版计划），需查证具体阶梯单价；当前参考来源未提供$0.08/GB的依据，月度成本估算需基于实际订阅费用或官方最新按量计费标准重新计算。

## Evidence

[质询]陈述中引用的具体单价（$0.08/GB）和计费模式（按量计费）与Cloudflare当前主流定价模型（Pro/Business为固定月费，无按GB计费；Enterprise为定制）存在潜在冲突，且参考来源未提供该具体数值支持，属于缺乏来源支撑的经验性估算。 | 来源[1][2]确认Pro/Enterprise为订阅制，未提及$0.08/GB的按量计费标准；来源[3]仅提及定价拆解但未提供具体数值。该事实为经验性成本估算，逻辑自洽但缺乏直接来源支持，且计费模式描述可能与实际订阅制不符，故降级。

## Search Query

Cloudflare CDN pricing per GB request based 2024

## Retrieval Sources

- {'url': 'https://www.cloudflare.com/zh-cn/plans/pro/&rut=982444a875615c3446d3eb08f6ec77d8ea77d9c54be2e138a9a12f32818c7717', 'type': 'ddg', 'title': 'Pro 计划概览 | 功能与定价 | Cloudflare'}
- {'url': 'https://www.cloudflare.com/zh-tw/plans/pro/&rut=6f8f746acb41e1454b6ea653337d8497a55bd2c008c7e4570e77479a1576e547', 'type': 'ddg', 'title': 'Pro 方案概觀 | 功能和定價 | Cloudflare'}
- {'url': 'https://www.plumephp.com/cloudflare-pricing-guide/&rut=dfbef2d090f81b790f54b8b338e79f9fda10ccbaceb217a2fef5afed9c0038bf', 'type': 'ddg', 'title': 'Cloudflare 定价详解：Free / Pro / Business / Enterprise 四档拆解与成本优化'}
