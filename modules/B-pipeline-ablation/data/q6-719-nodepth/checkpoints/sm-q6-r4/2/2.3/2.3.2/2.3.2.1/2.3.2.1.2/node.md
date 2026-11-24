# N653: 阿里云CDN中国内地HTTPS请求费的计费周期为按小时汇总、按天出账、按月结算，不存在跨月累计阶梯折扣（与流量费不同），即无论月请求量多大，单价恒定为 ¥0.0

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N224, N225, N226

## Claim

阿里云CDN中国内地HTTPS请求费的计费周期为按小时汇总、按天出账、按月结算，不存在跨月累计阶梯折扣（与流量费不同），即无论月请求量多大，单价恒定为 ¥0.04/万次，无‘量大价优’机制

## Corrected Claim

阿里云CDN中国内地HTTPS请求费通常按固定单价（如¥0.04/万次）计费，不同于流量费的阶梯累进模式，但具体计费周期（按小时/天/月）及是否绝对无跨月优惠需以阿里云官方最新计费文档为准。

## Evidence

[质询]参考来源中未包含关于HTTPS请求费具体计费周期（按小时/天/月）及是否存在阶梯折扣的明确描述，无法通过现有来源直接验证‘按小时汇总、按天出账’及‘无阶梯折扣’这一具体计费机制细节，存在来源覆盖不足的风险。 | 来源[2]和[3]仅提及流量和带宽的阶梯计费，未涉及HTTPS请求费；来源[1]仅提及出账延迟。虽然逻辑上HTTPS请求费通常按固定单价计费且无阶梯（符合行业惯例），但作为search节点，缺乏直接来源支持具体计费周期和‘无阶梯’的明确陈述，依据经验事实排除条款降级。

## Search Query

阿里云 CDN 请求数计费 阶梯 折扣 月度 结算 规则

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}
