# N15: 云存储服务费 = (存储量×单价 + 请求次数×请求单价 + 数据取回量×取回单价)，其中S3 Standard单价≈$0.023/GB/月，Standard-

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N2

## Claim

云存储服务费 = (存储量×单价 + 请求次数×请求单价 + 数据取回量×取回单价)，其中S3 Standard单价≈$0.023/GB/月，Standard-IA≈$0.0125/GB/月，Glacier≈$0.004/GB/月；500TB冷数据用Glacier、20%温数据用Standard-IA，月费≈500×80%×1024×0.004 + 500×20%×1024×0.0125 ≈ $1,638 + $1,280 = $2,918/月。

## Corrected Claim

云存储服务费通常包含存储、请求和取回费用。若按AWS S3历史典型单价估算（Standard-IA≈$0.0125/GB/月, Glacier≈$0.004/GB/月），500TB数据中80%冷数据存Glacier、20%温数据存Standard-IA，月存储费约为$2,918（不含请求和取回费用，具体价格需以实时官网为准）。

## Evidence

[质询]参考来源均为阿里云OSS的计费文档，与陈述中明确指出的AWS S3服务及其具体单价（$0.023/GB/月等）在主题和领域上不匹配，无法提供外部支持；且S3具体单价属于经验事实，随时间和地区波动，缺乏来源直接证实。 | 逻辑推导成立（500*0.8*1024*0.004=1638.4, 500*0.2*1024*0.0125=1280, 总和2918.4），但参考来源[1][2][3]均为阿里云OSS计费说明，与AWS S3无关，属于经验事实且缺来源支持。

## Search Query

AWS S3 pricing standard IA glacier 2024

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/oss/billing-overview&rut=20a4e60b70be8973e18cefcd6f2fb100293e26b95f3592f62bb8694d97cde4f2', 'type': 'ddg', 'title': 'Oss的计费组成、付费方式和定价-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://www.alibabacloud.com/help/zh/oss/billing-overview&rut=097fc671895595d0e60ce23475ad02584a2df9a1245d9910136d168d6df24318', 'type': 'ddg', 'title': 'Oss的计费组成、付费方式和定价 - 对象存储 Oss - 阿里云'}
- {'url': 'https://help.aliyun.com/zh/oss/api-operation-calling-fees&rut=00f0177205a15cea7ab03cebd6048f69406bfedda0215d7a006bc6dcf6d8cbd0', 'type': 'ddg', 'title': '什么情况下会产生PutRequest和GetRequest费用-对象存储 (OSS)-阿里云帮助中心'}
