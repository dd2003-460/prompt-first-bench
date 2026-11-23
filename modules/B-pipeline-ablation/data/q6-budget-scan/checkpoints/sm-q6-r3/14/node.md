# N221: 公有云CDN每千请求基础设施摊销成本 = (月度固定订阅费 + 月度峰值带宽预留费) / (月度总请求数 / 1000)；以阿里云为例，若月固定费¥0（按量付费

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

公有云CDN每千请求基础设施摊销成本 = (月度固定订阅费 + 月度峰值带宽预留费) / (月度总请求数 / 1000)；以阿里云为例，若月固定费¥0（按量付费）且峰值带宽费¥500，月请求2.19亿次，则每千请求基础设施成本 ≈ ¥500 / 219,000 ≈ ¥0.0023。

## Corrected Claim

在阿里云CDN按带宽峰值计费且无固定订阅费的假设场景下，若月度峰值带宽费用为¥500，月度总请求数为2.19亿次，则仅基于带宽费用的每千请求摊销成本约为¥0.0023。注意：此计算未包含流量费或请求数费等其他潜在计费项。

## Evidence

[质询]该陈述将“基础设施摊销成本”简化为仅包含“固定订阅费+峰值带宽费”，忽略了CDN计费中通常占比更大的“流量费”或“请求数费”（若按流量计费，带宽费可能为0或较低；若按请求计费，则有独立单价）。此外，¥500的峰值带宽费是假设值，并非阿里云标准定价的直接引用，属于特定场景下的估算而非通用事实。 | 来源[1]和[2]确认阿里云CDN支持按带宽峰值计费，且存在基础服务费，但未提供具体的¥500费用或2.19亿请求对应的标准摊销公式，该数值为特定假设下的计算，缺乏直接来源支持具体金额，故降级。

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-rules-of-basic-services&rut=8ac269fc0fd33361b507140bc77f95e7de5882f95004416a424fe1397b02bd86', 'type': 'ddg', 'title': '基础服务计费方式定价规则-cdn-阿里云-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
