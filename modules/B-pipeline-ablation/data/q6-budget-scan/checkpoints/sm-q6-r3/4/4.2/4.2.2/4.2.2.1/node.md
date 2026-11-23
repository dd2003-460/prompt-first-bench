# N239: 阿里云 CDN 95th 带宽计费的最小起租带宽限制通常为 10Gbps 或更高，若实际 $B_{95th} < 10\text{Gbps}$，则计费按最低门槛

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82

## Claim

阿里云 CDN 95th 带宽计费的最小起租带宽限制通常为 10Gbps 或更高，若实际 $B_{95th} < 10\text{Gbps}$，则计费按最低门槛计算，导致小流量场景下 95th 计费单价 $P_{95}^{eff}$ 远高于流量计费单价。

## Corrected Claim

阿里云 CDN 95th 带宽计费可能存在最小起租带宽限制，若实际 $B_{95th}$ 低于该限制，则计费按最低门槛计算，可能导致小流量场景下 95th 计费单价 $P_{95}^{eff}$ 高于流量计费单价。具体最小起租带宽限制需参考阿里云官方最新定价文档。

## Evidence

[质询]具体数值“10Gbps”缺乏来源直接支持，且阿里云CDN 95带宽计费通常有最低消费门槛（如按带宽峰值计费时的最低带宽限制），但具体是否为10Gbps或更高，以及是否导致小流量场景下单价远高于流量计费，需要更精确的官方定价文档支持。 | 来源[2]确认了阿里云CDN支持月结95带宽峰值计费，但未提及具体的最小起租带宽限制（如10Gbps）；来源[1]和[3]主要介绍计费模式和价格表，未明确说明95带宽计费的最小起租带宽限制。逻辑上，若存在最低起租带宽限制，小流量场景下确实可能导致有效单价升高，但具体数值需进一步验证。

## Search Query

Alibaba Cloud CDN 95th percentile bandwidth minimum billing threshold 10Gbps

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1712489&rut=9ac11fc059ec63ddd1ce104c3b0e7d9ac1b1e8c3823c8a667dafda6ca3e1bda1', 'type': 'ddg', 'title': '2026阿里云cdn 计费全攻略：按流量 / 带宽 / 95 峰值 + 基础服务费 + 增值服务价格表'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-rules-of-basic-services&rut=8ac269fc0fd33361b507140bc77f95e7de5882f95004416a424fe1397b02bd86', 'type': 'ddg', 'title': '基础服务计费方式定价规则-cdn-阿里云-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
