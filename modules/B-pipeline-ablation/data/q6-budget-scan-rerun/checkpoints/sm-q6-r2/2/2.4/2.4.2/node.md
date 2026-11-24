# N60: Cloudflare Pro 计费模式：基础月费 $25/月（修正 N13 原 $5 为 Free 版，Pro 版为 $25），超额流量单价 $0.08/GB，

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

Cloudflare Pro 计费模式：基础月费 $25/月（修正 N13 原 $5 为 Free 版，Pro 版为 $25），超额流量单价 $0.08/GB，日均 2TB 下载流量月成本 ≈ $25 + (2000GB×30×0.08) = $485 ≈ ¥3,500（按汇率 7.2 计算）

## Corrected Claim

Cloudflare Pro 计费模式：基础月费 $25/月（来源 [3] 确认），超额流量单价需参考官方最新定价页（通常约为 $0.08/GB，但具体以官方为准），日均 2TB 下载流量月成本估算约为 $485（基于 $0.08/GB 假设），约合 ¥3,500（按汇率 7.2 计算）。

## Evidence

[质询]超额流量单价 $0.08/GB 缺乏来源支持，且 Cloudflare 通常按 10GB 块计费，实际成本可能因取整规则略有差异；此外，$25 月费仅覆盖基础服务，未包含可能产生的其他增值费用。 | 来源 [3] 直接支持 Pro 版月费 $25，但未提供超额流量单价 $0.08/GB 的具体数据，该部分属于经验事实且缺来源支持，故降级。

## Search Query

Cloudflare Pro plan pricing 2024 monthly fee overage traffic per GB

## Retrieval Sources

- {'url': 'https://www.cloudflare.com/zh-cn/plans/pro/&rut=982444a875615c3446d3eb08f6ec77d8ea77d9c54be2e138a9a12f32818c7717', 'type': 'ddg', 'title': 'Pro 计划概览 | 功能与定价 | Cloudflare'}
- {'url': 'https://www.cloudflare.com/plans/pro/&rut=5dea87418d1c945fc160c8cc624da5a766380e03d681a44eea354aed068e6b0b', 'type': 'ddg', 'title': 'Pro Plan Overview | Features & Pricing | Cloudflare'}
- {'url': 'https://ftdesign.tw/how-much-does-cloudflare-cost-from-free-to-commercial-plan/&rut=35e2ee209217c0c07dbd92c389c34c9c403256ffde4d40ee7afcd8bbec595d9e', 'type': 'ddg', 'title': 'Cloudflare 費用多少？免費到商用方案價格一次看懂 | 丰田設計 FT Design'}
