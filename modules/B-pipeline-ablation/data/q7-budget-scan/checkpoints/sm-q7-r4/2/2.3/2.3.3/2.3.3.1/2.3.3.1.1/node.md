# N561: 阿里云 OSS 低频访问（IA）存储的数据取回（Retrieval）费用单价为 ¥0.03/GB，此费用仅在数据从 IA 层被读取时产生，不包含在月度存储费中。

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N185

## Claim

阿里云 OSS 低频访问（IA）存储的数据取回（Retrieval）费用单价为 ¥0.03/GB，此费用仅在数据从 IA 层被读取时产生，不包含在月度存储费中。

## Corrected Claim

阿里云 OSS 低频访问（IA）存储的数据取回（Retrieval）费用是独立于月度存储费的计费项，具体单价需查阅最新官方定价页（常见参考值约为 ¥0.03/GB，但可能因地域或时间而异）。

## Evidence

[质询]具体单价数值（¥0.03/GB）未在提供的参考来源摘要中直接体现，且阿里云OSS定价可能随时间或地域变化，存在数值过时或地域差异的风险。 | 来源[1]和[2]确认了‘低频访问数据取回’是独立的计费项（数据处理费用），逻辑上支持该费用独立于存储费；但所有来源均未提供具体的单价数值（¥0.03/GB），属于经验事实且缺乏直接来源支持。

## Search Query

Alibaba Cloud OSS Infrequent Access retrieval fee per GB

## Retrieval Sources

- {'url': 'https://www.alibabacloud.com/help/zh/oss/data-processing-fees&rut=e38d89eb046a353bd4e9a55687abdf1399762c59d4a426202d26b617b45e19d8', 'type': 'ddg', 'title': 'OSS数据处理费用说明 - 对象存储 OSS - 阿里云 - Alibaba Cloud'}
- {'url': 'https://help.aliyun.com/zh/oss/data-processing-fees&rut=b15fc372b173424fa68a60215fcb09f768069127a2cdba9742a8c1222e9ea8c8', 'type': 'ddg', 'title': 'Oss数据处理费用说明-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://cn.aliyun.com/price/detail/oss&rut=1f434cc06e03a6c94e43387f214943c4149c0bd9b33b5242d3f1909f00e0309e', 'type': 'ddg', 'title': '阿里云定价_oss价格详情_对象存储'}
