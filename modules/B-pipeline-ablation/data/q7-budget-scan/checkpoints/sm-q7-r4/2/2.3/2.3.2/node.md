# N54: 阿里云OSS低频访问（IA）存储单价为¥0.08/GB/月，针对400TB冷数据，月度基础存储成本 = 400 × 1024 × 0.08 = ¥32,768/

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

阿里云OSS低频访问（IA）存储单价为¥0.08/GB/月，针对400TB冷数据，月度基础存储成本 = 400 × 1024 × 0.08 = ¥32,768/月

## Corrected Claim

阿里云OSS低频访问（IA）存储单价需以官网实时报价为准（通常约为¥0.08/GB/月），针对400TB冷数据，若单价为¥0.08/GB/月，则月度基础存储成本约为¥32,768/月。

## Evidence

父节点级核验未通过：不完备（子节点分别讨论了‘最短存储时长’和‘最小对象大小’两个不同的计费维度，彼此正且不重复，因此正交性成立；但父节点仅包含基础存储成本计算，未涵盖低频访问存储的其他关键成本项（如请求费用、数据取回费用），导致完备性不足；两个子节点描述的是独立的计费规则，并非同一参数的不同取值，故无冗余。）

## Search Query

Alibaba Cloud OSS Infrequent Access storage price per GB month 2026

## Retrieval Sources

- {'url': 'https://www.alibabacloud.com/zh/product/oss/pricing?_p_lc=1&rut=62cfcd94507e991d6df05097a1c1f514e10d050bc4a0af4056bb456860a9ca82', 'type': 'ddg', 'title': '对象存储OSS定价与购买方式 - 阿里云 - Alibaba Cloud'}
- {'url': 'https://developer.aliyun.com/article/1771961&rut=8e79c56d88e646addef7e53c126caa5989effcbd6dc03b9ca79a27f07978d9a5', 'type': 'ddg', 'title': '阿里云 Oss 对象存储服务租用价格表（一年 / 按月 / 按小时报价明细）'}
- {'url': 'https://www.alibabacloud.com/en/product/oss-pricing-list/zh?_p_lc=1&rut=1b0528f855f4541bba72a22aac8bea9cdcaa867dec6734f9e9a8a0460c1487cc', 'type': 'ddg', 'title': 'OSS 价格详情 - Alibaba Cloud'}
