# N53: 云存储温数据（标准层）存储费：100TB × 1024GB × 12月 × ¥0.12/GB/月 ≈ ¥14,745,600/年（基于阿里云OSS标准存储中国区

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

云存储温数据（标准层）存储费：100TB × 1024GB × 12月 × ¥0.12/GB/月 ≈ ¥14,745,600/年（基于阿里云OSS标准存储中国区域定价，需核实最新价目表）

## Corrected Claim

云存储温数据（标准层）存储费估算：若单价为¥0.12/GB/月，则100TB年费约为¥14,745,600；具体费用需依据阿里云OSS最新官方价目表（区分LRS/ZRS及地域）核实。

## Evidence

[质询]来源未提供阿里云OSS标准存储的具体单价（¥0.12/GB/月），无法直接验证该经验参数；且不同冗余类型（LRS/ZRS）及地域价格存在差异，单一数值可能不准确。 | 逻辑计算正确（100*1024*12*0.12=147456），但参考来源[1][2]仅提及OSS收费模式及示例（如500GB包年价），未直接给出标准存储按量付费单价，属于经验事实缺直接来源支持。

## Search Query

Alibaba Cloud OSS Standard Storage pricing per GB per month China region 2024

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1784976&rut=295779d2181eed34de7844ba47687317c9974ee3e361abbe691827e614feeef8', 'type': 'ddg', 'title': '阿里云存储收费标准：2026年11月最新oss对象存储、Nas及块存储费用价格表-阿里云开发者社区'}
- {'url': 'https://developer.aliyun.com/article/1704273&rut=14db771f48c3da8f08d6609f407704c9a549a94f0391bc553853f3e5822bfbcf', 'type': 'ddg', 'title': '2026年阿里云对象存储OSS最新收费标准价格表：'}
- {'url': 'https://learn.microsoft.com/zh-cn/azure/storage/blobs/archive-cost-estimation&rut=62ccfc31d83ead67a577a3f4b6b30d014cbefb8df14f2aaebda67de8c70e8668', 'type': 'ddg', 'title': '估算存档数据的成本（Azure Blob 存储） - Azure Storage | Microsoft Learn'}
