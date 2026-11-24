# N184: 阿里云OSS低频访问（IA）存储的单对象最小计费单位为64KB，小于64KB的对象按64KB计费；假设400TB冷数据由平均大小1MB的对象组成，对象数量 = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

阿里云OSS低频访问（IA）存储的单对象最小计费单位为64KB，小于64KB的对象按64KB计费；假设400TB冷数据由平均大小1MB的对象组成，对象数量 = 400 * 1024 * 1024 / 1 = 4.19亿个，由于1MB > 64KB，无额外小文件计费惩罚，成本维持 ¥32,768/月；若对象平均大小降至32KB，则有效计费容量翻倍至800TB，成本升至 ¥65,536/月。

## Corrected Claim

阿里云OSS低频访问（IA）存储的单对象最小计费单位为64KB，小于64KB的对象按64KB计费；假设400TB冷数据由平均大小1MB的对象组成，对象数量 = 400 * 1024 * 1024 / 1 = 4.19亿个，由于1MB > 64KB，无额外小文件计费惩罚，成本维持 ¥32,768/月；若对象平均大小降至32KB，则有效计费容量翻倍至800TB，成本升至 ¥65,536/月。

## Evidence

先验知识/题面给定，逻辑校验通过：阿里云OSS IA存储最小计费单位确为64KB，数学计算（400TB/1MB=4.19亿对象，32KB对象导致计费容量翻倍）及成本线性推导均正确。

## Search Query

Alibaba Cloud OSS minimum object size billing 64KB
