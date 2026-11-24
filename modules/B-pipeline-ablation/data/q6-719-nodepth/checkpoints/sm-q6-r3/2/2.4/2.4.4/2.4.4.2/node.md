# N238: 公有云 CDN 月度流量成本 Cloud_Traffic_Cost = Tail_Monthly_Traffic_GB × Unit_Price_GB_Tier

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N71

## Claim

公有云 CDN 月度流量成本 Cloud_Traffic_Cost = Tail_Monthly_Traffic_GB × Unit_Price_GB_Tier，其中 Tail_Monthly_Traffic_GB 为长尾区域月下载流量（日均 2TB × 30 × Tail_Traffic_Ratio），Unit_Price_GB_Tier 为阶梯定价下的单价（阿里云 CDN 下行流量 60TB/月以下约 ¥0.24/GB，60-150TB 约 ¥0.20/GB，>150TB 约 ¥0.15/GB），需根据总流量确定适用阶梯。

## Corrected Claim

公有云 CDN 月度流量成本 Cloud_Traffic_Cost = Tail_Monthly_Traffic_GB × Unit_Price_GB_Tier，其中 Tail_Monthly_Traffic_GB 为长尾区域月下载流量，Unit_Price_GB_Tier 为阶梯定价下的单价（阿里云 CDN 下行流量采用阶梯计费，具体单价需查询最新官方价格表，通常随流量增加而降低），需根据总流量确定适用阶梯。

## Evidence

[质询]具体单价数值（¥0.24/GB, ¥0.20/GB, ¥0.15/GB）及阶梯阈值（60TB, 150TB）属于经验事实，参考来源仅确认了“阶梯定价”和“按流量计费”的机制，未提供具体的2024-2026年最新价格表数值，无法排除价格波动或地区差异导致的数值偏差。 | 来源[1][2][3]证实阿里云CDN采用按流量计费且存在阶梯价格机制，逻辑自洽；但具体单价数值缺乏来源直接支持，属经验事实，故降级。

## Search Query

Alibaba Cloud CDN pricing tier traffic cost per GB monthly 2024

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://docsv4.qingcloud.com/user_guide/network/cdn/billing/price/&rut=5d61c86496841278c91ca524d0b4c5ad19e7808d0663d81deed8f9349d13e860', 'type': 'ddg', 'title': 'Cdn 计费 - 公有云文档中心'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
