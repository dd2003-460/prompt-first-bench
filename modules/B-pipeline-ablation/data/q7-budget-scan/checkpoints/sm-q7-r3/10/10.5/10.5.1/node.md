# N409: 云存储出口流量单价：S3 标准出口流量单价为 $0.09/GB（前100TB/月免费额度后），阿里云 OSS 外网流出单价约为 ¥0.5/GB（具体依区域和带宽

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N155

## Claim

云存储出口流量单价：S3 标准出口流量单价为 $0.09/GB（前100TB/月免费额度后），阿里云 OSS 外网流出单价约为 ¥0.5/GB（具体依区域和带宽峰值而定），需根据实际云服务商定价表确定。

## Corrected Claim

云存储出口流量单价因区域和服务商而异：AWS S3 在美国东部区域的标准出口流量单价约为 $0.09/GB（具体依区域和流量阶梯而定，无统一全球免费额度）；阿里云 OSS 外网流出单价约为 ¥0.5/GB（具体依区域和带宽峰值而定），需根据实际云服务商定价表确定。

## Evidence

[质询]S3 出口流量单价 $0.09/GB 是 AWS 美国东部（us-east-1）等特定区域的典型价格，并非全球统一标准，且“前100TB/月免费额度”表述不准确（AWS 通常无此固定免费额度，而是通过 Data Transfer Out 的阶梯计价或特定合作伙伴/计划提供优惠，不同区域价格差异显著，如欧洲或亚太区域通常高于 $0.09/GB）；阿里云 OSS 价格同样随区域和带宽峰值波动，具体数值需实时查询。 | 来源 [1] 仅提及 S3 账单包含流量费用，未提供具体单价数值，无法直接支持 $0.09/GB 或 ¥0.5/GB 的具体数值；该事实属于经验性价格数据，逻辑上量级合理（云存储出口流量通常在 $0.05-$0.12/GB 区间），但缺乏直接来源支持具体数值，且存在区域差异导致的表述不严谨。

## Search Query

AWS S3 data transfer out pricing per GB 2024 Aliyun OSS outbound traffic price

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2084002793988400423&rut=2998f78e920c90c680a14b372a14126e67fd6de52261eedd7fa931a7d9ecfdec', 'type': 'ddg', 'title': '2026年亚马逊s3多少钱？存储、请求和流量费用怎么算？ - 知乎'}
