# N247: Cloudflare Pro 计划超出免费额度后的精确计费单价 P_request_cf_overage 为 $0.00005/request，需转换为人民币单

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N69, N70, N71

## Claim

Cloudflare Pro 计划超出免费额度后的精确计费单价 P_request_cf_overage 为 $0.00005/request，需转换为人民币单价 P_request_cf_cny = $0.00005 * ExchangeRate_USDCNY，并确认 ExchangeRate_USDCNY 在 2024-2025 年的典型区间（如 7.1-7.3）。

## Corrected Claim

Cloudflare Pro 计划超出免费额度后的计费单价约为 $0.00005/request（需以官方最新定价为准），人民币单价需根据实时汇率（2024-2025 年典型区间约 7.1-7.3）进行动态换算。

## Evidence

[质询]Cloudflare 的计费模式复杂，Pro 计划通常包含固定的请求额度，超出后的计费可能涉及不同的层级或按量付费（Pay-as-you-go）的不同单价，且汇率是动态变化的，固定区间 7.1-7.3 可能无法覆盖 2024-2025 全年的波动（例如 2024 年初曾低于 7.1，2025 年可能进一步波动），且 $0.00005/request 这一具体数值需确认是否为当前最新定价（Cloudflare 经常调整定价策略）。 | source=knowledge，逻辑自洽（单价量级符合 CDN 行业惯例，汇率区间符合近期市场常识），但缺乏外部来源直接支持具体单价数值及汇率精确区间，依据经验事实排除条款及无可用来源情况，降级为 degraded。
