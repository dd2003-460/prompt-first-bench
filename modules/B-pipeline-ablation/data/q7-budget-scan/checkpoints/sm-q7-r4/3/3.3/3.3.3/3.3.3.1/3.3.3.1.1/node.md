# N632: 云对象存储S3 Standard-IA的单价参数：存储费 $0.0125/GB/月 ≈ ¥0.09/GB/月 ≈ ¥1.08/TB/月。请求费（GET/PUT）

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N219

## Claim

云对象存储S3 Standard-IA的单价参数：存储费 $0.0125/GB/月 ≈ ¥0.09/GB/月 ≈ ¥1.08/TB/月。请求费（GET/PUT） $0.0004/1000 requests ≈ ¥0.0029/千次。数据取回费（Retrieval） $0.01/GB。对于500TB数据，年存储基础费 = 500 * 1024 GB * 12 * $0.0125 * 7.2 ≈ $552,960 ≈ ¥3,981,312/年（未考虑生命周期优化）。

## Corrected Claim

云对象存储S3 Standard-IA的单价参数需以AWS官网实时报价为准（通常约为$0.0125/GB/月，具体视区域而定）。基于该估算单价及$1≈¥7.2的汇率假设，500TB数据的年存储基础费估算约为$552,960（约¥3,981,312），实际费用取决于实时汇率及具体区域定价。

## Evidence

[质询]汇率假设（$1≈¥7.2）及具体单价（如S3 Standard-IA存储费$0.0125/GB/月）属于随时间波动的经验事实，参考来源仅提供了定价页面链接或通用描述，未包含具体的实时数值或汇率，无法直接验证这些具体数字的准确性。 | 逻辑推导自洽（500*1024*12*0.0125*7.2 ≈ 552,960 USD ≈ 3,981,312 CNY），但作为search节点，具体单价和汇率属于经验事实，参考来源[1][2][3]仅指向定价页面无具体数值支持，符合degraded判定条件。

## Search Query

AWS S3 Standard-Infrequent Access pricing per GB month retrieval cost 2024

## Retrieval Sources

- {'url': 'https://aws.amazon.com/cn/s3/pricing/&rut=76ca5b0ccc400c66eabd71d747989025406fd64f0a96d6b6b228107e58d4b242', 'type': 'ddg', 'title': 'S3 Pricing - aws.amazon.com'}
- {'url': 'https://www.amazonaws.cn/s3/pricing/&rut=effbb9e0e2bb283b012daf4dd6d07702dd07cc46a57f8d03036200587b93f0f3', 'type': 'ddg', 'title': 'Amazon S3 定价'}
- {'url': 'https://costgoat.com/pricing/amazon-s3&rut=85a9fbf5d8e3c93731df3916135d393aa3faee42c6d2e1337971c2dca987bb44', 'type': 'ddg', 'title': 'S3 Cost Calculator: Amazon S3 Pricing per GB (Nov 2026)'}
