# N71: 公有云CDN的基础设施成本中，对象存储（OSS/S3）的存储费用 C_storage_public = S_total * P_storage_public，其

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

公有云CDN的基础设施成本中，对象存储（OSS/S3）的存储费用 C_storage_public = S_total * P_storage_public，其中 S_total 为存储总容量（GB），P_storage_public 为每GB月存储单价（¥/GB/月）。对于2TB日均下载量，假设存储容量为10TB，阿里云OSS标准存储约为 ¥0.12/GB/月。

## Corrected Claim

公有云CDN的基础设施成本中，对象存储（OSS/S3）的存储费用 C_storage_public = S_total * P_storage_public，其中 S_total 为存储总容量（GB），P_storage_public 为每GB月存储单价（¥/GB/月）。对于2TB日均下载量，假设存储容量为10TB，阿里云OSS标准存储单价需根据具体地域和当前官方定价确定（参考值约为 ¥0.12/GB/月）。

## Evidence

[质询]阿里云OSS标准存储的具体单价（¥0.12/GB/月）属于随时间、地域及促销活动变动的经验事实，参考来源仅提供了计费逻辑和框架，未提供该具体数值，存在价格过时或地域差异的风险。 | 来源[2]和[3]确认了OSS计费包含存储费用且按量付费，支持公式逻辑；但所有来源均未提供¥0.12/GB/月的具体数值，该数值为经验事实，逻辑自洽但缺来源直接支持。

## Search Query

Alibaba Cloud OSS storage pricing standard 2024

## Retrieval Sources

- {'url': 'https://blog.csdn.net/2601_95525647/article/details/160419380&rut=6fde7709ad36dad7be5291fba4bc38487f18dd151e6b7196cb3449c269919deb', 'type': 'ddg', 'title': '对象存储成本优化实战：Oss/Cdn费用构成分析与生命周期、批量api省钱配置指南-csdn博客'}
- {'url': 'https://help.aliyun.com/zh/oss/billing-overview&rut=29ddc4cd22dc9abc78484f47251fe39f99d8d8e977251b19615483e37b9a717c', 'type': 'ddg', 'title': 'Oss的计费组成、付费方式和定价-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-of-oss-content-acceleration&rut=d489a658be3e4f065943b8be8074ff4503e553f35415f3dd0264563cb68045cd', 'type': 'ddg', 'title': 'Cdn加速oss计费说明-cdn (Cdn)-阿里云帮助中心'}
