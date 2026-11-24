# N212: 阿里云 CDN 按带宽峰值计费（Pay-by-Bandwidth）的单价阶梯及峰值定义：通常以 5 分钟平均带宽的最大值为准，0-500Mbps 区间单价约为 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N61

## Claim

阿里云 CDN 按带宽峰值计费（Pay-by-Bandwidth）的单价阶梯及峰值定义：通常以 5 分钟平均带宽的最大值为准，0-500Mbps 区间单价约为 ¥0.066/GB/天（或 ¥1.6/Mbps/天），需将日均 2TB 流量转换为峰值带宽（假设峰值系数 3，平均带宽 ≈ 25.6Mbps，峰值 ≈ 77Mbps）以确定适用档位

## Corrected Claim

阿里云 CDN 支持按带宽峰值计费，通常以 5 分钟平均带宽的最大值为准。日均 2TB 流量在峰值系数为 3 的假设下，平均带宽约为 25.6Mbps，峰值约为 77Mbps。具体单价阶梯需查阅阿里云官方最新价目表，不同区域和带宽区间价格有所不同。

## Evidence

[质询]具体单价数值（¥0.066/GB/天 或 ¥1.6/Mbps/天）及峰值系数假设（3）属于经验事实，参考来源仅确认了计费模式的存在，未提供具体价格表或峰值定义细节，无法直接验证数值准确性。 | 来源[1][2][3]确认阿里云CDN支持按带宽峰值计费，但未提供具体单价阶梯和峰值定义细节；逻辑上2TB/天流量转换为平均25.6Mbps、峰值77Mbps的计算自洽，但具体价格需以官方最新价目表为准，故降级。

## Search Query

Aliyun CDN bandwidth peak pricing 5-minute average definition 2024

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-rules-of-basic-services&rut=8ac269fc0fd33361b507140bc77f95e7de5882f95004416a424fe1397b02bd86', 'type': 'ddg', 'title': '基础服务计费方式定价规则-cdn-阿里云-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
