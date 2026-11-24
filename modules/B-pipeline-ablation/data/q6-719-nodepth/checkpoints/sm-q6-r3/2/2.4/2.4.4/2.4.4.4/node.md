# N240: 公有云 CDN 回源流量成本 Cloud_Origin_Fetch_Cost = Origin_Fetch_Traffic_GB × Unit_Price_Or

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N71

## Claim

公有云 CDN 回源流量成本 Cloud_Origin_Fetch_Cost = Origin_Fetch_Traffic_GB × Unit_Price_Origin_Fetch_GB，其中 Origin_Fetch_Traffic_GB 为缓存未命中导致的回源流量（= Tail_Monthly_Traffic_GB × (1 - Hit_Rate_Cloud)），Unit_Price_Origin_Fetch_GB 为回源流量单价（阿里云 CDN 回源流量约 ¥0.15/GB，低于下行流量单价），需结合缓存命中率计算。

## Corrected Claim

公有云 CDN 回源流量成本 Cloud_Origin_Fetch_Cost = Origin_Fetch_Traffic_GB × Unit_Price_Origin_Fetch_GB，其中 Origin_Fetch_Traffic_GB 为缓存未命中导致的回源流量（= Tail_Monthly_Traffic_GB × (1 - Hit_Rate_Cloud)），Unit_Price_Origin_Fetch_GB 为回源流量单价（具体数值需查询阿里云最新价目表，通常低于下行流量单价），需结合缓存命中率计算。

## Evidence

[质询]具体数值（¥0.15/GB）属于经验事实，参考来源仅涉及计费逻辑和独立性，未提供具体单价，无法直接验证该数值是否准确或是否为最新价格。 | 逻辑推导成立（成本=流量×单价），但具体单价为经验事实，参考来源[1][2][3]仅说明CDN与其他产品独立计费，未提供具体回源流量单价，缺乏直接来源支持。

## Search Query

Alibaba Cloud CDN origin fetch traffic pricing per GB cost

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-of-data-transfer-when-alibaba-cloud-cdn-is-used-with-other-alibaba-cloud-services&rut=9de4f007814d52bc72cd7eec17e0df310c5ba189e08f4eee53d03181777bd698', 'type': 'ddg', 'title': 'Cdn与阿里云其他产品配合使用时流量如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://www.alibabacloud.com/help/zh/cdn/product-overview/billing-of-data-transfer-when-alibaba-cloud-cdn-is-used-with-other-alibaba-cloud-services&rut=1a3d74acf32503b4c02b909e4a65c84d67a9145c4b49273f3178837bdbfa03fd', 'type': 'ddg', 'title': 'Cdn与阿里云其他产品配合使用时流量如何计费 - Cdn - 阿里云'}
