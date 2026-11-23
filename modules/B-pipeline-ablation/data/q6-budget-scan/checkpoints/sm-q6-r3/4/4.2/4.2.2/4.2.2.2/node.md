# N240: 阿里云 CDN 95th 带宽计费的阶梯单价结构：当承诺带宽低于 100Gbps 时，单价约为 0.04-0.06 元/Mbps/天；超过 100Gbps 后单

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82

## Claim

阿里云 CDN 95th 带宽计费的阶梯单价结构：当承诺带宽低于 100Gbps 时，单价约为 0.04-0.06 元/Mbps/天；超过 100Gbps 后单价阶梯下降，具体阶梯区间需查阅最新价目表以确定 $B_{95th}=0.35\text{Gbps}$ 所属档位。

## Corrected Claim

阿里云 CDN 支持月结 95 带宽峰值计费，其单价通常随承诺带宽增加呈阶梯式下降，具体阶梯区间及单价需查阅最新官方价目表以确定 $B_{95th}=0.35\text{Gbps}$ 所属档位。

## Evidence

[质询]具体单价数值（0.04-0.06 元/Mbps/天）及阶梯阈值（100Gbps）属于经验事实，参考来源摘要中未包含具体的价格表数据，无法直接验证该数值量级是否准确，存在价格随时间波动或地域差异导致数值偏差的风险。 | 来源[1][2][3]确认了阿里云CDN存在'月结95带宽峰值计费'模式，但摘要未提供具体阶梯单价数值，属于间接支持计费模式存在，无法直接支持具体价格数值；经验事实缺直接来源支持，降级为定性表述。

## Search Query

Alibaba Cloud CDN 95th percentile bandwidth pricing tiers 2024

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-rules-of-basic-services&rut=8ac269fc0fd33361b507140bc77f95e7de5882f95004416a424fe1397b02bd86', 'type': 'ddg', 'title': '基础服务计费方式定价规则-cdn-阿里云-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1712489&rut=9ac11fc059ec63ddd1ce104c3b0e7d9ac1b1e8c3823c8a667dafda6ca3e1bda1', 'type': 'ddg', 'title': '2026阿里云cdn 计费全攻略：按流量 / 带宽 / 95 峰值 + 基础服务费 + 增值服务价格表'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
