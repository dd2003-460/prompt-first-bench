# N244: S3 Standard 单价 $0.023/GB/月 的时效性校验：该价格为 2023-2024 年 AWS 官方标准定价，需确认 2026 年是否有调价或区域

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

S3 Standard 单价 $0.023/GB/月 的时效性校验：该价格为 2023-2024 年 AWS 官方标准定价，需确认 2026 年是否有调价或区域差异（如 us-east-1 vs eu-west-1），若价格变动 10%，年成本波动约 ¥10,860。

## Corrected Claim

S3 Standard 单价 $0.023/GB/月 的时效性校验：该价格为 2023-2024 年 AWS 官方标准定价，需确认 2026 年是否有调价或区域差异（如 us-east-1 vs eu-west-1），若价格变动 10%，年成本波动约 ¥10,860。

## Evidence

来源[2]明确列出2026年AWS S3标准存储价格为$0.023/GB/月，直接支持该单价在2026年依然有效；来源[1]为官方定价页，虽未直接列出数值但确认了定价结构，与来源[2]无矛盾。

## Search Query

AWS S3 Standard pricing per GB month 2026 current rate

## Retrieval Sources

- {'url': 'https://aws.amazon.com/cn/s3/pricing/&rut=76ca5b0ccc400c66eabd71d747989025406fd64f0a96d6b6b228107e58d4b242', 'type': 'ddg', 'title': 'S3 Pricing - aws.amazon.com'}
- {'url': 'https://sevencoloryun.com/blog/aws-s3-pricing-cost-comparison-2026/&rut=6609ebadebc3f4aafca58ad359704169f5453b31ec74842d79716a9f09b776e2', 'type': 'ddg', 'title': 'AWS S3 价格怎么算：存储/请求/流量三笔账+取回费陷阱+比官网便宜的路径 | SevenColorYun'}
- {'url': 'https://costgoat.com/pricing/amazon-s3&rut=85a9fbf5d8e3c93731df3916135d393aa3faee42c6d2e1337971c2dca987bb44', 'type': 'ddg', 'title': 'S3 Cost Calculator: Amazon S3 Pricing per GB (Nov 2026)'}
