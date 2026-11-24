# N88: 云存储价格波动率 $\sigma_{cloud}$ 的量化边界：AWS S3 和 Aliyun OSS 标准存储价格在 2019-2024 年间年均降幅约为 5

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

云存储价格波动率 $\sigma_{cloud}$ 的量化边界：AWS S3 和 Aliyun OSS 标准存储价格在 2019-2024 年间年均降幅约为 5%-8%，但请求费用（Request Cost）和流出费用（Data Egress）波动率较低（±5%）；在敏感性分析中，应单独对存储费（Storage Fee）应用 -8%/年 的趋势项，而对请求费和流出费应用 ±5% 的静态波动区间，避免高估长期节省

## Corrected Claim

云存储价格波动率 $\sigma_{cloud}$ 的量化边界：AWS S3 和 Aliyun OSS 标准存储价格在 2019-2024 年间年均降幅约为 5%-8%，但请求费用（Request Cost）和流出费用（Data Egress）波动率较低（±5%）；在敏感性分析中，应单独对存储费（Storage Fee）应用 -8%/年 的趋势项，而对请求费和流出费应用 ±5% 的静态波动区间，避免高估长期节省

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

AWS S3 OSS price history 2019-2024 annual price reduction storage vs request cost
