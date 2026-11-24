# N381: Cloudflare 现行定价模型修正：Pro 计划（$20/月）提供无限流量（受 Fair Use 限制），无 $0.09/GB 超额计费；日均 2TB 场景

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N121

## Claim

Cloudflare 现行定价模型修正：Pro 计划（$20/月）提供无限流量（受 Fair Use 限制），无 $0.09/GB 超额计费；日均 2TB 场景下月成本锁定为 $20（≈144 元），原 N121 中 $5,375 的计算基于已废弃的旧版计费结构，需废弃该节点并采用新基线。

## Corrected Claim

Cloudflare Pro 计划采用订阅制，提供高流量支持（受公平使用政策限制），不再采用旧版按 GB 超额计费模式；具体月费及流量上限需以官方最新定价页为准，原基于 $0.09/GB 的计算已失效。

## Evidence

[质询]参考来源摘要中未明确列出 Pro 计划的具体价格（$20/月）及“无限流量”的具体条款细节，仅提供了计划定位和对比链接，缺乏直接数值支持。 | 来源 [1] 和 [2] 确认了 Pro 计划的存在及定位，来源 [3] 提及了 2026 年价格对比，但摘要均未直接陈述 $20/月 及无限流量的具体参数，属于间接支持；逻辑上 Cloudflare 转向订阅制且取消按量计费符合行业趋势，但具体数值需依赖外部直接证据。

## Search Query

Cloudflare Pro plan pricing 2024 unlimited bandwidth overage fee

## Retrieval Sources

- {'url': 'https://www.cloudflare.com/zh-tw/plans/pro/&rut=6f8f746acb41e1454b6ea653337d8497a55bd2c008c7e4570e77479a1576e547', 'type': 'ddg', 'title': 'Pro 方案概觀 | 功能和定價 | Cloudflare'}
- {'url': 'https://www.cloudflare-cn.com/plans/pro/&rut=ff5b1e0167a8e0a5babf0fb04d615d1365c383ec8b16bbe628a26130b6aa0fee', 'type': 'ddg', 'title': 'Pro 计划概览 | 功能与定价 | Cloudflare'}
- {'url': 'https://eastondev.com/blog/zh/posts/dev/20251201-cloudflare-pricing-compare/&rut=ddc25e749bddb07a3b4857bd1d65886dac9de81430b649fd86d26f1a6af26454', 'type': 'ddg', 'title': 'Cloudflare Free Plan Limits 2026：免费、Pro、Business怎么选'}
