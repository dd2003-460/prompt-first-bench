# N226: Cloudflare Pro Plan $20/月费用包含的出站流量上限：尽管官方声称'无限出站流量'，但公平使用政策（Fair Use Policy）实际上限

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N76, N77, N78

## Claim

Cloudflare Pro Plan $20/月费用包含的出站流量上限：尽管官方声称'无限出站流量'，但公平使用政策（Fair Use Policy）实际上限为月均10TB出站流量，超出后可能被限速或要求升级至Business Plan（$200/月），需量化日均2TB流量（月均60TB）是否触发限速风险

## Corrected Claim

Cloudflare Pro Plan ($20/月) 虽声称无限流量，但受公平使用政策限制。若月均出站流量达60TB（日均2TB），极大概率超出Pro Plan的隐性或显性公平使用阈值（通常远低于此量级），存在被限速或要求升级至更高阶计划（如Business Plan）的风险。

## Evidence

[质询]具体数值（10TB上限、$200 Business Plan价格）属于经验事实，参考来源仅包含Pro Plan的通用介绍，未提供具体的公平使用政策数值或Business Plan定价，无法通过现有来源直接验证具体阈值。 | 逻辑自洽（60TB > 10TB 确实触发风险），但参考来源[1]-[3]仅描述Pro Plan定位，未包含具体流量上限数值或Business Plan价格，属于经验事实且缺乏直接来源支持。

## Search Query

Cloudflare Pro plan fair use policy monthly bandwidth limit 2024

## Retrieval Sources

- {'url': 'https://www.cloudflare.com/plans/pro/&rut=5dea87418d1c945fc160c8cc624da5a766380e03d681a44eea354aed068e6b0b', 'type': 'ddg', 'title': 'Pro Plan Overview | Features & Pricing | Cloudflare'}
- {'url': 'https://www.cloudflare.com/zh-tw/plans/pro/&rut=6f8f746acb41e1454b6ea653337d8497a55bd2c008c7e4570e77479a1576e547', 'type': 'ddg', 'title': 'Pro 方案概觀 | 功能和定價 | Cloudflare'}
- {'url': 'https://www.cloudflare-cn.com/plans/pro/&rut=ff5b1e0167a8e0a5babf0fb04d615d1365c383ec8b16bbe628a26130b6aa0fee', 'type': 'ddg', 'title': 'Pro 计划概览 | 功能与定价 | Cloudflare'}
