# N31: 云对象存储（S3/OSS）500TB数据全量存储的年服务费估算：假设500TB全部存入标准存储（Standard），单价约¥0.12/GB/月，年成本 = 50

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

云对象存储（S3/OSS）500TB数据全量存储的年服务费估算：假设500TB全部存入标准存储（Standard），单价约¥0.12/GB/月，年成本 = 500 * 1024 * 1024 GB * 0.12 * 12 ≈ ¥73.4M；若采用智能分层（80%冷数据转IA/Archive），平均单价降至¥0.05/GB/月，年成本约¥30.2M，但需计入请求费和取回费。

## Corrected Claim

云对象存储（S3/OSS）500TB数据全量存储的年服务费估算：假设500TB全部存入标准存储，若单价约为¥0.12/GB/月，则年成本约为¥73.4M；若采用智能分层（80%冷数据转IA/Archive），平均单价可能降低，年成本可能降至¥30M左右，但需额外计入请求费和取回费。（注：具体单价需以实时官网报价为准）

## Evidence

[质询]单价数值（¥0.12/GB/月）属于具体经验参数，参考来源虽确认了计费结构（存储+流量+请求）和存储类型（标准/低频/归档等），但未提供具体的单价数值，无法直接验证该特定价格是否准确或是否为当前最新价格。 | 逻辑计算正确（500*1024*1024*0.12*12 ≈ 73.4M），来源[1][2][3]证实了OSS计费包含存储、流量、请求费及多种存储类型，支持了‘需计入请求费和取回费’及‘智能分层’的逻辑，但未直接提供¥0.12/GB/月的具体单价，属经验事实缺直接来源支持。

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/oss/billing-overview&rut=20a4e60b70be8973e18cefcd6f2fb100293e26b95f3592f62bb8694d97cde4f2', 'type': 'ddg', 'title': 'Oss的计费组成、付费方式和定价-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1704273&rut=14db771f48c3da8f08d6609f407704c9a549a94f0391bc553853f3e5822bfbcf', 'type': 'ddg', 'title': '2026年阿里云对象存储OSS最新收费标准价格表：'}
- {'url': 'https://developer.aliyun.com/article/1771961&rut=8e79c56d88e646addef7e53c126caa5989effcbd6dc03b9ca79a27f07978d9a5', 'type': 'ddg', 'title': '阿里云 Oss 对象存储服务租用价格表（一年 / 按月 / 按小时报价明细）'}
