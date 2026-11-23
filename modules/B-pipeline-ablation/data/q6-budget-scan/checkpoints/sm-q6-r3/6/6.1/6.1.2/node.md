# N269: 阿里云CDN 10-50TB/月区间单价核验：官方价目表显示该区间标准价为¥0.22/GB，适用于中型平台（如日均2TB下载量对应月流量60TB，处于50TB以

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N87

## Claim

阿里云CDN 10-50TB/月区间单价核验：官方价目表显示该区间标准价为¥0.22/GB，适用于中型平台（如日均2TB下载量对应月流量60TB，处于50TB以上区间边缘）

## Corrected Claim

阿里云CDN采用阶梯计费模式，具体单价需查阅官方最新价目表；日均2TB下载量对应月流量约60TB，该流量规模通常处于较高计费阶梯。

## Evidence

[质询]具体数值（¥0.22/GB）及区间划分（10-50TB）属于经验事实，参考来源摘要中未包含具体价格表数据，无法直接验证该特定数值是否准确对应阿里云当前官方价目表；此外，日均2TB对应月60TB的计算虽逻辑正确，但60TB是否确实处于“50TB以上区间边缘”取决于具体的阶梯划分点，来源未提供阶梯细节。 | 来源[1][2][3]确认了阿里云CDN采用阶梯计费模式，但摘要中未包含具体价格数值（如¥0.22/GB）及具体阶梯区间（10-50TB），属于经验事实且缺乏直接来源支持，故降级。

## Search Query

阿里云 CDN 下行流量 阶梯计费 10-50TB 单价 2024

## Retrieval Sources

- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
