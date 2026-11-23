# N186: 阿里云CDN请求数计费模式及单价：除流量计费外，阿里云CDN还支持按请求数计费，单价约为¥0.04/万次请求；日均请求量2,193,000次，月度请求数 = 2

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

阿里云CDN请求数计费模式及单价：除流量计费外，阿里云CDN还支持按请求数计费，单价约为¥0.04/万次请求；日均请求量2,193,000次，月度请求数 = 2,193,000 * 30 = 65,790,000次，月度请求成本 = 6,579 * ¥0.04 = ¥263/月；若采用流量+请求混合计费模式，总成本 = 流量成本 + 请求成本，需对比两种计费模式的总成本以选择最优方案。

## Corrected Claim

阿里云CDN默认按流量计费，请求数计费通常适用于HTTPS等增值服务。若按¥0.04/万次估算，日均2,193,000次请求的月度成本约为¥263，实际费用需根据具体计费项（如是否启用HTTPS）及官方最新价目表确定。

## Evidence

[质询]单价数值（¥0.04/万次）属于具体经验参数，参考来源中未提供该确切数值，且阿里云CDN基础计费通常按流量/带宽，请求数计费多用于HTTPS等增值服务，直接将其作为基础计费模式之一并给出固定单价缺乏来源直接支持。 | 来源[3]确认了按流量计费是默认方式，请求数计费主要涉及增值服务（如HTTPS），但未提供¥0.04/万次这一具体基础单价，属于经验事实缺来源直接支持。

## Search Query

阿里云CDN 请求数计费 单价 万次请求 月度成本 2024

## Retrieval Sources

- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
