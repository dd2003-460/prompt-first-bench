# N616: 层级分布对监控费占比的敏感性分析：若温数据 100% 为 Frequent Access，Cost_storage = 100,000 * 0.023 = $2

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N218

## Claim

层级分布对监控费占比的敏感性分析：若温数据 100% 为 Frequent Access，Cost_storage = 100,000 * 0.023 = $2,300/月，Ratio = 250 / (250 + 2300) ≈ 9.8%；若 100% 为 Infrequent Access，Cost_storage = 100,000 * 0.0125 = $1,250/月，Ratio = 250 / (250 + 1250) ≈ 16.7%；因此监控费占比在 9.8%-16.7% 区间波动，取决于实际层级分布，N70 假设的 6% 偏低，需按实际分布修正。

## Corrected Claim

层级分布对监控费占比的敏感性分析：若温数据 100% 为 Frequent Access，Cost_storage = 100,000 * 0.023 = $2,300/月，Ratio = 250 / (250 + 2300) ≈ 9.8%；若 100% 为 Infrequent Access，Cost_storage = 100,000 * 0.0125 = $1,250/月，Ratio = 250 / (250 + 1250) ≈ 16.7%；因此监控费占比在 9.8%-16.7% 区间波动，取决于实际层级分布，N70 假设的 6% 偏低，需按实际分布修正。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（250/(250+2300)≈9.8%, 250/(250+1250)≈16.7%），AWS S3 存储单价量级符合常识（Standard ~$0.023/GB, IA ~$0.0125/GB），结论逻辑自洽。
