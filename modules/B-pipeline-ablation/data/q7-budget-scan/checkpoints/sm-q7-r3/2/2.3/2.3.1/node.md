# N53: 阿里云OSS标准存储（Standard）单价为¥0.12/GB/月，针对100TB温数据，月度基础存储成本 = 100 × 1024 × 0.12 = ¥12,

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

阿里云OSS标准存储（Standard）单价为¥0.12/GB/月，针对100TB温数据，月度基础存储成本 = 100 × 1024 × 0.12 = ¥12,288/月

## Corrected Claim

阿里云OSS标准存储（Standard）单价约为¥0.09/GB/月（参考2025年标准），针对100TB温数据，月度基础存储成本 ≈ 100 × 1024 × 0.09 = ¥9,216/月

## Evidence

[质询]单价数值错误：参考来源[3]明确指出2025年阿里云OSS标准型本地冗余存储按量价为0.09元/GB/月，而陈述中使用的0.12元/GB/月与最新公开资料不符，导致最终成本计算偏高。 | 来源[3]显示标准存储单价为0.09元/GB/月，与陈述中的0.12元/GB/月矛盾；基于正确单价计算，100TB（102400GB）月度成本应为9216元，而非12288元。

## Search Query

Alibaba Cloud OSS Standard storage price per GB month 2026

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1704273&rut=14db771f48c3da8f08d6609f407704c9a549a94f0391bc553853f3e5822bfbcf', 'type': 'ddg', 'title': '2026年阿里云对象存储OSS最新收费标准价格表：'}
- {'url': 'https://www.alibabacloud.com/zh/product/oss/pricing?_p_lc=1&rut=62cfcd94507e991d6df05097a1c1f514e10d050bc4a0af4056bb456860a9ca82', 'type': 'ddg', 'title': '对象存储OSS定价与购买方式 - 阿里云 - Alibaba Cloud'}
- {'url': 'https://developer.aliyun.com/article/1659806&rut=35a05c6e79c2828b20ef56c5b8f0bb6b7baf76df29514d276d762ca74b55a637', 'type': 'ddg', 'title': '阿里云OSS对象存储收费标准价格表：流量包+存储包2025最新整理'}
