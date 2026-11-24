# N207: 阿里云CDN阶梯价格断点验证：2024年最新价目表显示，中国内地下行流量0-10TB/月单价为¥0.24/GB，10-50TB/月单价为¥0.22/GB，50T

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N67

## Claim

阿里云CDN阶梯价格断点验证：2024年最新价目表显示，中国内地下行流量0-10TB/月单价为¥0.24/GB，10-50TB/月单价为¥0.22/GB，50TB以上单价为¥0.20/GB；需核实日均2TB（月均60TB）是否跨越第二、三档断点，实际加权单价需按分段计算

## Corrected Claim

阿里云CDN采用阶梯价格计费，需根据最新官方价目表核实具体断点及单价；日均2TB（月均60TB）通常跨越多个计费档位，实际成本需按分段流量分别计算后加权。

## Evidence

[质询]具体价格数值（¥0.24/GB, ¥0.22/GB, ¥0.20/GB）及断点（10TB, 50TB）属于经验事实，参考来源摘要中未包含具体价目表数据，无法直接验证数值准确性，且阿里云价格可能随时间或区域调整，存在口径混淆风险。 | 逻辑上分段计费计算方式自洽，但参考来源[1][2]仅涉及计费规则和日志说明，未提供具体阶梯价格数值，属于经验事实且缺乏直接来源支持。

## Search Query

Alibaba Cloud CDN pricing 2024 China mainland traffic tier 0-10TB 10-50TB 50TB

## Retrieval Sources

- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
