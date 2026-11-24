# N746: 公有云 CDN 存储费用 C_storage_cloud 的计算公式：C_storage_cloud = S_total * P_storage_per_TB_

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N249

## Claim

公有云 CDN 存储费用 C_storage_cloud 的计算公式：C_storage_cloud = S_total * P_storage_per_TB_day * 30，其中 P_storage_per_TB_day 为公有云 CDN 存储单价（如阿里云 ¥0.0001/TB/小时），需查询最新定价表。

## Corrected Claim

公有云 CDN 存储费用通常取决于后端存储服务的定价，不同厂商计费模式各异。若采用按量付费模式，费用可估算为：存储总量 * 单位存储单价 * 计费时长。具体单价需查询各云厂商（如阿里云、AWS）最新定价表，不同厂商及区域价格差异较大。

## Evidence

[质询]该陈述将“公有云 CDN 存储费用”作为一个通用公式，并引用阿里云的具体单价作为示例，但忽略了不同云厂商（如 AWS CloudFront, Google Cloud CDN）的计费模式差异（部分厂商 CDN 本身不直接收取存储费，而是依赖后端对象存储；或计费单位不同），且“¥0.0001/TB/小时”这一具体数值属于易变动的经验事实，缺乏当前有效来源的直接支持。 | 逻辑上公式结构自洽（总量*单价*时间），但参考来源[1][2][3]均未提供阿里云 CDN 存储的具体单价或确认该通用公式适用于所有公有云 CDN，属于经验事实且缺来源直接支持。

## Search Query

Alibaba Cloud CDN storage price per TB per hour 2024

## Retrieval Sources

- {'url': 'https://cloud.google.com/cdn/pricing?hl=zh-cn&rut=6fdb2a8c5d1d9c2a49300e07a7fc6296b0bd29ae6ca463b088f9a27677cbc822', 'type': 'ddg', 'title': 'Cloud CDN 价格 | Google Cloud'}
- {'url': 'https://docsv4.qingcloud.com/user_guide/network/cdn/billing/price/&rut=05ac04f5d186ad8e92f3d2e8f2762407455c1cffda18011825d069f9de68624f', 'type': 'ddg', 'title': 'Cdn 计费 - 公有云文档中心'}
- {'url': 'https://cloudinsight.cc/zh/blog/cdn-pricing&rut=223d7b5a7e8cf251dc18e1452aa16b0c1b80d449d42dc92d774c430d0fd287b8', 'type': 'ddg', 'title': 'CDN 費用完整指南：2026 各大廠商定價比較與省錢技巧 | CloudInsight'}
