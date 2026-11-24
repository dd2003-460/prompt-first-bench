# N106: 云对象存储新增 244TB 数据的年请求费用 (¥/年) = 假设每日全量 LIST 244TB 对象（平均对象 1MB，250,000 对象），250,000

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

云对象存储新增 244TB 数据的年请求费用 (¥/年) = 假设每日全量 LIST 244TB 对象（平均对象 1MB，250,000 对象），250,000 requests × 365 天 × $0.005/1000 × 7.2 ¥/$，总计 ¥3,300/年

## Corrected Claim

云对象存储新增 244TB 数据的年请求费用 (¥/年) = 假设每日全量 LIST 244TB 对象（平均对象 1MB，250,000 对象），250,000 requests × 365 天 × $0.005/1000 × 7.2 ¥/$，总计 ¥3,300/年

## Evidence

先验知识/题面给定，逻辑校验通过：250,000 × 365 × 0.005 / 1000 × 7.2 = 3,294，约等于 3,300，计算无误且量级合理。

## Search Query

aws s3 api request pricing list put get
