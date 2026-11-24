# N558: 阿里云 OSS 低频访问（IA）存储的单价为 ¥0.03/GB/月（华东1等主流区域），注意：N183 中引用的 ¥0.08/GB/月 疑似为错误值或混淆了标准

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N183

## Claim

阿里云 OSS 低频访问（IA）存储的单价为 ¥0.03/GB/月（华东1等主流区域），注意：N183 中引用的 ¥0.08/GB/月 疑似为错误值或混淆了标准存储/归档存储价格，需以 ¥0.03 为基准进行后续成本计算。

## Corrected Claim

阿里云 OSS 低频访问（IA）存储的单价约为 ¥0.03/GB/月（华东1等主流区域），具体价格请以阿里云官网实时报价为准。

## Evidence

[质询]参考来源摘要中均未直接列出“¥0.03/GB/月”这一具体数值，无法从提供的文本片段中直接证实该精确价格，存在来源覆盖不足的风险。 | 来源[1][2][3]确认了阿里云OSS存在低频访问（IA）存储类型及计费模式，但未在摘要中提供具体单价数值；该价格符合行业常识量级，但缺乏直接文本支持，故降级。

## Search Query

Alibaba Cloud OSS Infrequent Access storage price per GB month

## Retrieval Sources

- {'url': 'https://www.aliyun.com/price/detail/oss&rut=59aa80ead5ae689831da534376c0ad98e79a1c3a8fe6b265f8fdffc7f59fc1c6', 'type': 'ddg', 'title': '阿里云定价_oss价格详情_对象存储'}
- {'url': 'https://developer.aliyun.com/article/1704273&rut=14db771f48c3da8f08d6609f407704c9a549a94f0391bc553853f3e5822bfbcf', 'type': 'ddg', 'title': '2026年阿里云对象存储OSS最新收费标准价格表：'}
- {'url': 'https://www.alibabacloud.com/zh/product/oss-pricing-list/zh?_p_lc=1&rut=40e63ec8dc12993212614bb84e64edc64b1e7aed8d9838ac1d72daf64144f112', 'type': 'ddg', 'title': 'OSS 价格详情 - Alibaba Cloud'}
