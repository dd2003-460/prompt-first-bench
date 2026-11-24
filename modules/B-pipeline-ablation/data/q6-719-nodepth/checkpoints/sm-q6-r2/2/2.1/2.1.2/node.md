# N69: 阿里云CDN的请求计费单价 P_request_ali，根据阿里云最新价目表，静态HTTPS请求约为 ¥0.045/1000 requests，动态请求约为 ¥

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

阿里云CDN的请求计费单价 P_request_ali，根据阿里云最新价目表，静态HTTPS请求约为 ¥0.045/1000 requests，动态请求约为 ¥0.05/1000 requests。[时效待核：2024-2025价格变动]

## Corrected Claim

阿里云CDN主要采用按下行流量或带宽峰值计费，部分场景或增值服务可能涉及请求数计费，具体单价需查阅最新官方价目表，静态/动态请求单价约为¥0.045-0.05/1000 requests（需以实时官网为准）。

## Evidence

[质询]阿里云CDN的标准计费模式通常基于“下行流量”（GB）或“带宽峰值”（Mbps），而非直接按“请求次数”（Requests）计费。虽然存在“请求数”作为增值服务或特定场景（如全站加速DCDN的某些计费项）的计费维度，但将其作为基础CDN的核心计费单价（且区分静态/动态HTTPS请求的具体单价）缺乏普遍性，且具体数值（0.045/0.05元/千次）极易随区域、套餐及时间变动，属于高度易变的经验事实。 | 参考来源[1]和[3]主要描述的是按流量（GB）或带宽计费的阶梯价格，未直接提供按“请求次数”计费的具体单价表；来源[2]为计费概览，未列出具体数值。该陈述属于经验事实，逻辑上虽无硬伤（存在按请求计费的可能性），但缺乏来源直接支持具体数值，且与主流按流量计费的描述存在口径差异风险。

## Search Query

Alibaba Cloud CDN request pricing 2024 static dynamic

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}
