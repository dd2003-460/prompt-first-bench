# N18: 公有云 CDN 带宽峰值计费单价：按 95th 百分位带宽计费模式下的单价（¥/Mbps/月）及折算到日均 2TB 下载量下的月度成本。

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

公有云 CDN 带宽峰值计费单价：按 95th 百分位带宽计费模式下的单价（¥/Mbps/月）及折算到日均 2TB 下载量下的月度成本。

## Corrected Claim

公有云 CDN 支持按 95th 百分位带宽计费模式（如阿里云、华为云均提供此选项），适用于月消费金额较大的用户；具体单价及日均 2TB 下载量下的月度成本需依据各厂商最新价格表及实际带宽峰值计算，参考来源未提供具体数值。

## Evidence

[质询]参考来源仅提供了计费模式的定义和适用场景，未提供具体的单价数值（¥/Mbps/月），也未提供针对“日均2TB下载量”这一特定负载下的月度成本计算结果或具体单价数据，导致无法从来源中直接提取或验证具体的金额数值。 | 来源[2]和[3]确认了“月结95带宽峰值计费”是公有云CDN（阿里云、华为云）的标准计费模式之一，逻辑上该模式存在且适用于大流量场景；但所有来源均未包含具体的单价数值或针对日均2TB流量的成本估算，属于经验事实且缺乏直接数据支持。

## Search Query

CDN 95th percentile bandwidth pricing Alibaba Cloud Cloudflare Mbps cost

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1712489&rut=9ac11fc059ec63ddd1ce104c3b0e7d9ac1b1e8c3823c8a667dafda6ca3e1bda1', 'type': 'ddg', 'title': '2026阿里云cdn 计费全攻略：按流量 / 带宽 / 95 峰值 + 基础服务费 + 增值服务价格表'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-rules-of-basic-services&rut=8ac269fc0fd33361b507140bc77f95e7de5882f95004416a424fe1397b02bd86', 'type': 'ddg', 'title': '基础服务计费方式定价规则-cdn-阿里云-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://support.huaweicloud.com/price-cdn/cdn_01_0160.html&rut=609f695d31cc553ef8d2a657ce4f3f016d670da0774fbd1d8764f0f5dc20d3be', 'type': 'ddg', 'title': '月结95峰值带宽计费_基础服务计费_计费说明_内容分发网络 Cdn-华为云'}
