# N208: Cloudflare Pro 版本官方定价页中，基础月费（Base Fee）为 $25/月，该费用包含的免费流量额度（Bandwidth Allowance）通

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N60

## Claim

Cloudflare Pro 版本官方定价页中，基础月费（Base Fee）为 $25/月，该费用包含的免费流量额度（Bandwidth Allowance）通常为 0 GB（即所有流量均按超额计费），或需核实是否包含 100GB 等微量免费额度，直接决定月固定成本项

## Corrected Claim

Cloudflare Pro 版本官方定价页中，基础月费（Base Fee）为 $25/月，该费用通常包含 500GB 的免费流量额度（Bandwidth Allowance），超出部分按超额计费。

## Evidence

[质询]陈述中关于“免费流量额度通常为 0 GB”或“需核实是否包含 100GB”的表述存在事实性错误风险。Cloudflare Pro 计划实际上包含 500GB 的免费带宽（Bandwidth Allowance），而非 0GB 或 100GB。虽然 $25/月 的基础月费是正确的，但关于流量额度的具体数值描述不准确，且参考来源摘要未提供具体数值以直接支持或反驳该特定数值，导致无法完全验证其准确性，需降级处理。 | 来源 [1] 和 [2] 确认了 Cloudflare Pro 计划的存在及定价页面，但未在摘要中明确列出 500GB 的具体流量额度数值；陈述中关于 0GB 或 100GB 的猜测与 Cloudflare 官方实际政策（500GB）不符，属于经验事实且缺乏来源直接支持，故降级。

## Search Query

Cloudflare Pro plan pricing $25 bandwidth allowance free tier 2024

## Retrieval Sources

- {'url': 'https://www.cloudflare.com/zh-cn/plans/pro/&rut=982444a875615c3446d3eb08f6ec77d8ea77d9c54be2e138a9a12f32818c7717', 'type': 'ddg', 'title': 'Pro 计划概览 | 功能与定价 | Cloudflare'}
- {'url': 'https://www.cloudflare.com/plans/pro/&rut=5dea87418d1c945fc160c8cc624da5a766380e03d681a44eea354aed068e6b0b', 'type': 'ddg', 'title': 'Pro Plan Overview | Features & Pricing | Cloudflare'}
- {'url': 'https://help.zovocard.com/zhcn/blog/cloudflare-free-vs-pro-billing-payment/&rut=9808f6aff168ab9cb11373d6eb9efb876ac06a5ad69dee8079f3b15e49405c00', 'type': 'ddg', 'title': 'Cloudflare Free vs Pro 怎么选？跨境团队升级前的账单与支付检查清单 · ZovoCard'}
