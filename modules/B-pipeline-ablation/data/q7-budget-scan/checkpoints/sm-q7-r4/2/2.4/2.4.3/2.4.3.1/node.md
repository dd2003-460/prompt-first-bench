# N223: 阿里云 OSS 标准存储（Standard）的 GET 请求单价为 ¥0.01/万次（即 ¥1 \times 10^{-6}$/次），基于 N71 计算的年请求

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

阿里云 OSS 标准存储（Standard）的 GET 请求单价为 ¥0.01/万次（即 ¥1 \times 10^{-6}$/次），基于 N71 计算的年请求量 $7.65 \times 10^{10}$ 次，年请求成本为 $7.65 \times 10^{10} \times 1 \times 10^{-6} \approx ¥76,500$/年。

## Corrected Claim

阿里云 OSS 标准存储（Standard）的 GET 请求单价为 ¥0.01/万次（即 ¥1 \times 10^{-6}$/次），基于 N71 计算的年请求量 $7.65 \times 10^{10}$ 次，年请求成本为 $7.65 \times 10^{10} \times 1 \times 10^{-6} \approx ¥76,500$/年。

## Evidence

先验知识/题面给定，逻辑校验通过：阿里云OSS标准存储GET请求单价确为0.01元/万次（即1e-6元/次），计算过程 7.65e10 * 1e-6 = 76500 元，数值量级与逻辑均正确。

## Search Query

Alibaba Cloud OSS Standard storage GET request pricing per 10000 requests
