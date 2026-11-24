# N278: 公有云 CDN 请求数单价 P_req 的验证：阿里云 CDN 通常不单独按请求数计费（包含在流量包中或极低），而 Cloudflare 等按请求计费；若使用阿

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N92

## Claim

公有云 CDN 请求数单价 P_req 的验证：阿里云 CDN 通常不单独按请求数计费（包含在流量包中或极低），而 Cloudflare 等按请求计费；若使用阿里云，C_req_cloud 可能为 0 或极低（<¥100/月）；若使用 Cloudflare，P_req ≈ $0.005/1000 requests = ¥0.000036/req，C_req_cloud = 1.34e9 * 30 * 0.000036 ≈ ¥1,447,200/月，远高于流量费，故需明确厂商选择。

## Corrected Claim

阿里云CDN对静态HTTPS请求数单独计费（作为增值服务），而Cloudflare等按请求计费；若使用阿里云，需考虑HTTPS请求数费用；若使用Cloudflare，P_req需根据实际厂商定价确定，C_req_cloud的计算依赖于该单价，需明确厂商选择及具体费率。

## Evidence

[质询]阿里云CDN并非完全不按请求数计费，而是将静态HTTPS请求数作为独立的增值服务计费项，且Cloudflare的具体单价（$0.005/1000 requests）属于经验事实，参考来源未提供该数值支持，存在参数不准确的风险。 | 来源[1]和[2]直接反驳了'阿里云通常不单独按请求数计费'的说法，指出静态HTTPS请求数是独立计费项；Cloudflare单价无来源支持，属经验事实，逻辑自洽但缺来源直接支持。

## Search Query

Cloudflare CDN pricing per 1000 requests vs Alibaba Cloud CDN request billing

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-of-https-requests-for-static-content&rut=b2a9e93598935bbcc4bb8023df740c51e7ee06804c384188e45cda294fd47011', 'type': 'ddg', 'title': '静态https请求数的计费标准及示例-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/faq-about-the-billing-of-requests&rut=1c0f34c295fef609fa2c9cd791f27c8a0d38981f255ffe5287fbcef0089b7011', 'type': 'ddg', 'title': '关于请求数计费的常见问题有哪些-cdn (Cdn)-阿里云帮助中心'}
