# N220: Cloudflare Pro 套餐的流量上限与超额费用：Pro 套餐包含 50TB/月流量，超出部分按 $0.05/GB 计费，对于 60TB/月流量，超额 1

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75

## Claim

Cloudflare Pro 套餐的流量上限与超额费用：Pro 套餐包含 50TB/月流量，超出部分按 $0.05/GB 计费，对于 60TB/月流量，超额 10TB 成本为 $10 \times 1000 \times 0.05 = 500$ 美元，总成本需叠加基础套餐费。

## Corrected Claim

Cloudflare Pro 套餐通常提供无限流量（Unmetered），不收取超额流量费用；具体计费规则需参考最新官方定价页。

## Evidence

[质询]Cloudflare Pro 套餐通常包含无限流量（Unmetered），不存在 50TB 的硬性流量上限及 $0.05/GB 的超额计费标准，该陈述混淆了套餐类型或引用了过时/错误的定价模型。 | 来源 [1] 和 [2] 为 Cloudflare 官方 Pro 计划页面，但摘要未提及具体流量上限和超额费用；来源 [3] 指出 Cloudflare 以“免费无限带宽”闻名，暗示 Pro 计划可能无硬性流量上限，与陈述中的 50TB 上限矛盾。经验事实，逻辑自洽但缺来源支持且与常识/来源暗示矛盾。

## Search Query

Cloudflare Pro plan overage charges 2024

## Retrieval Sources

- {'url': 'https://www.cloudflare.com/zh-cn/plans/pro/&rut=982444a875615c3446d3eb08f6ec77d8ea77d9c54be2e138a9a12f32818c7717', 'type': 'ddg', 'title': 'Pro 计划概览 | 功能与定价 | Cloudflare'}
- {'url': 'https://www.cloudflare.com/zh-tw/plans/pro/&rut=6f8f746acb41e1454b6ea653337d8497a55bd2c008c7e4570e77479a1576e547', 'type': 'ddg', 'title': 'Pro 方案概觀 | 功能和定價 | Cloudflare'}
- {'url': 'https://www.plumephp.com/cloudflare-pricing-guide/&rut=dfbef2d090f81b790f54b8b338e79f9fda10ccbaceb217a2fef5afed9c0038bf', 'type': 'ddg', 'title': 'Cloudflare 定价详解：Free / Pro / Business / Enterprise 四档拆解与成本优化'}
