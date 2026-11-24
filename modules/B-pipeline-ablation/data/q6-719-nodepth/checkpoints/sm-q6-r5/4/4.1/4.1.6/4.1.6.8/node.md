# N258: 公有云请求费计费模型修正：阿里云 CDN 请求费通常按 10 万次请求为一个阶梯，单价 ¥0.04/万次（非 ¥0.01/千次）；日均 1.34 亿请求，月请求

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82, N83, N84

## Claim

公有云请求费计费模型修正：阿里云 CDN 请求费通常按 10 万次请求为一个阶梯，单价 ¥0.04/万次（非 ¥0.01/千次）；日均 1.34 亿请求，月请求数 40.2 亿，请求费 = (40.2 * 10^8 / 10^5) * 0.04 = ¥16,080/月，远高于 N84 估算的 ¥402/月，需重新核算。

## Corrected Claim

阿里云 CDN 请求费按阶梯计费，若单价为 ¥0.04/万次，则月请求费约为 ¥16,080；具体单价需以阿里云官网实时报价为准。

## Evidence

[质询]单价数值（¥0.04/万次）及阶梯划分属于具体商业定价经验事实，参考来源摘要中未直接列出该具体数值，存在定价随时间或区域变化的风险，无法仅凭逻辑推导确认当前准确单价。 | 逻辑计算自洽（40.2亿/10万 * 0.04 = 16080），但来源[1][2][3]仅确认存在请求数计费模式，未直接提供¥0.04/万次这一具体单价数据，属经验事实缺直接来源支持。

## Search Query

Alibaba Cloud CDN request fee pricing per 10000 requests

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/faq-about-the-billing-of-requests&rut=1c0f34c295fef609fa2c9cd791f27c8a0d38981f255ffe5287fbcef0089b7011', 'type': 'ddg', 'title': '关于请求数计费的常见问题有哪些-cdn (Cdn)-阿里云帮助中心'}
