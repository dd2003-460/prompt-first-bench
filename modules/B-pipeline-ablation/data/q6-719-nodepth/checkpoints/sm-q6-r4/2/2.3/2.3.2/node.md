# N67: 公有云 CDN 月请求数成本 Request_Cost = Total_Monthly_Requests × Unit_Price_Per_10k_Req，其中

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14

## Claim

公有云 CDN 月请求数成本 Request_Cost = Total_Monthly_Requests × Unit_Price_Per_10k_Req，其中 Total_Monthly_Requests = DAU 500万 × 人均请求 20次 × 30天 = 30亿次 = 300,000 (万)，Unit_Price_Per_10k_Req 取阿里云 HTTP/HTTPS 请求费 ¥0.04/万次，计算得 Request_Cost ≈ 300,000 × 0.04 = ¥12,000/月 [时效待核]。

## Corrected Claim

公有云 CDN 月请求数成本估算：若采用按请求数计费模式（如阿里云静态HTTPS请求），假设单价为 ¥0.04/万次，则 30亿次请求的成本约为 ¥12,000/月。注意：阿里云CDN默认按流量计费，按请求数计费通常仅适用于HTTPS等特定场景，具体单价需以官方最新价目表为准。

## Evidence

[质询]阿里云CDN基础计费默认按流量或带宽，而非按请求数；按请求数计费通常仅针对HTTPS请求或特定增值服务，且具体单价（¥0.04/万次）属于经验参数，需核实是否为当前最新刊例价及是否适用于所有HTTP/HTTPS请求。 | 来源[1]和[2]确认阿里云CDN存在按请求数计费项（如静态HTTPS请求），但未直接提供¥0.04/万次的具体数值支持；该数值为经验事实，逻辑自洽但缺直接来源支持，故降级。

## Search Query

Aliyun CDN request price per 10000 requests 2024 Cloudflare request pricing

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://cloud.tencent.com/document/product/228/75562&rut=c32a82b203ae6be2bdb86af74ab9bc57d1f406852b20720b260f9360274c5f9f', 'type': 'ddg', 'title': '内容分发网络 Cdn 基础服务计费_腾讯云'}
