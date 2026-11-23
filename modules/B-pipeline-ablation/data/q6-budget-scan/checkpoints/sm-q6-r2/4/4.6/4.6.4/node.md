# N92: 公有云CDN单位流量成本 Price_cloud_CDN 在混合策略中通常采用阶梯定价或合约价，对于长尾小流量（0.4TB/日），单价通常高于大额流量包，需具体

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

公有云CDN单位流量成本 Price_cloud_CDN 在混合策略中通常采用阶梯定价或合约价，对于长尾小流量（0.4TB/日），单价通常高于大额流量包，需具体查询阿里云/Cloudflare小流量阶梯价

## Corrected Claim

公有云CDN通常采用阶梯定价或合约价，根据规模经济原理，长尾小流量的单位成本通常高于大额流量包，具体价格需查询阿里云/Cloudflare等厂商的最新阶梯价目表。

## Evidence

[质询]该陈述包含具体的经验性参数（0.4TB/日）和定性结论（小流量单价高于大额流量包），属于经验事实。虽然逻辑上符合规模经济原理，但参考来源仅提供了计费模式（按流量/带宽）和批量折扣的存在，并未直接提供“0.4TB/日”这一具体量级下的阶梯定价对比数据或明确证实该特定流量下的单价高低关系，缺乏直接来源支持。 | 来源[1]和[2]证实了CDN存在按流量计费及批量折扣机制，支持“阶梯/合约价”的逻辑基础，但未直接覆盖“0.4TB/日”具体场景下的单价对比，属经验事实缺直接来源支持。

## Search Query

Alibaba Cloud CDN traffic pricing tiers small volume 0.4TB daily

## Retrieval Sources

- {'url': 'https://cloud.google.com/cdn/pricing?hl=zh-cn&rut=74fac12a2c12ad0f3ff9712259e6fb7f4eb556c23cf368ae2dd79e79f2660348', 'type': 'ddg', 'title': 'Cloud CDN 价格 | Google Cloud'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://cloudinsight.cc/zh/blog/cdn-pricing&rut=654151bc9b88e9834d32418962ce2e5781eda8f0b377faa402e8a0c39a62ae38', 'type': 'ddg', 'title': 'CDN 費用完整指南：2026 各大廠商定價比較與省錢技巧 | CloudInsight'}
