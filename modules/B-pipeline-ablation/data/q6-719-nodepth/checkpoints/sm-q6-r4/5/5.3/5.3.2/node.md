# N141: Cloudflare的请求计费在Free和Pro套餐中为 $0（无限请求），仅在Enterprise套餐中按自定义合同计费（通常 <$0.01/1000 req

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35

## Claim

Cloudflare的请求计费在Free和Pro套餐中为 $0（无限请求），仅在Enterprise套餐中按自定义合同计费（通常 <$0.01/1000 requests），因此对于C端平台，Cloudflare的请求边际成本近似为0

## Corrected Claim

Cloudflare的Free和Pro套餐通常包含无限的基础请求（Web请求）而不额外收费，但特定高级产品或功能可能按量计费；对于基础Web流量，C端平台的边际成本极低。

## Evidence

[质询]来源未直接提供具体的计费数值（如$0或<$0.01/1000），且Cloudflare的计费模型复杂，不同产品（如Workers, R2, KV等）可能有不同的请求计费逻辑，仅凭通用计划页面无法确证所有请求边际成本近似为0。 | 经验事实，逻辑自洽但缺来源支持。来源[2]和[3]确认了Free/Pro计划的存在，但未明确列出请求计费为$0的具体条款；来源[1]仅说明计费原理，未给出具体数值。

## Search Query

Cloudflare request pricing Free Pro Enterprise 2024

## Retrieval Sources

- {'url': 'https://developers.cloudflare.com/billing/understand/how-charges-accrue/&rut=827d289a8b7d483e5f28d82dc7441c747f5289fb87d9e56776d44ed7df32d90f', 'type': 'ddg', 'title': 'How charges accrue · Cloudflare Billing docs'}
- {'url': 'https://www.cloudflare.com/zh-cn/plans/&rut=129c23725ca678adf98669a07a56e5f8ed4d74206f871eb48919e18bef9e81fd', 'type': 'ddg', 'title': 'Cloudflare 产品_服务列表_收费计划_服务定价_Cloudflare 中国官网'}
- {'url': 'https://www.cloudflare.com/zh-cn/plans/pro/&rut=982444a875615c3446d3eb08f6ec77d8ea77d9c54be2e138a9a12f32818c7717', 'type': 'ddg', 'title': 'Pro 计划概览 | 功能与定价 | Cloudflare'}
