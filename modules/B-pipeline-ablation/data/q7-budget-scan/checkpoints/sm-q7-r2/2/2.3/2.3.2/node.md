# N54: 阿里云OSS低频访问（IA）存储单价为¥0.08/GB/月，针对400TB冷数据，月度基础存储成本 = 400 × 1024 × 0.08 = ¥32,768/

- **status**: degraded
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

[质询]参考来源中未包含具体的单价数值（¥0.08/GB/月），无法从提供的文本中直接验证该价格参数的准确性，存在价格随时间或地域变动的风险。 | 逻辑推导成立（400 * 1024 * 0.08 = 32768），但经验事实（具体单价）缺乏来源直接支持，来源[1][2][3]仅确认了计费单位和存储类型，未提供具体价格。

## Search Query

Alibaba Cloud OSS Infrequent Access storage price per GB month 2026

## Retrieval Sources

- {'url': 'https://www.alibabacloud.com/zh/product/oss/pricing?_p_lc=1&rut=62cfcd94507e991d6df05097a1c1f514e10d050bc4a0af4056bb456860a9ca82', 'type': 'ddg', 'title': '对象存储OSS定价与购买方式 - 阿里云 - Alibaba Cloud'}
- {'url': 'https://developer.aliyun.com/article/1771961&rut=8e79c56d88e646addef7e53c126caa5989effcbd6dc03b9ca79a27f07978d9a5', 'type': 'ddg', 'title': '阿里云 Oss 对象存储服务租用价格表（一年 / 按月 / 按小时报价明细）'}
- {'url': 'https://www.alibabacloud.com/en/product/oss-pricing-list/zh?_p_lc=1&rut=1b0528f855f4541bba72a22aac8bea9cdcaa867dec6734f9e9a8a0460c1487cc', 'type': 'ddg', 'title': 'OSS 价格详情 - Alibaba Cloud'}
