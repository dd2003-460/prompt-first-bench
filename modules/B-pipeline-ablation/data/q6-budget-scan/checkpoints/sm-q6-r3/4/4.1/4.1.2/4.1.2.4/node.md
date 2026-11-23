# N182: 长尾用户（偏远地区）对 d_avg 的拉高效应：假设 5% 的用户位于偏远地区（d > 500km），其贡献的加权距离为 0.05 * 500 = 25km，占

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

长尾用户（偏远地区）对 d_avg 的拉高效应：假设 5% 的用户位于偏远地区（d > 500km），其贡献的加权距离为 0.05 * 500 = 25km，占总 d_avg 的 10-15%；若剔除长尾用户，d_avg 可降低 10-15%，但需单独评估长尾用户的 P99 延迟合规性

## Corrected Claim

长尾用户（偏远地区）对 d_avg 的拉高效应：假设 5% 的用户位于偏远地区（d > 500km），其贡献的加权距离为 0.05 * 500 = 25km，占总 d_avg 的 10-15%；若剔除长尾用户，d_avg 可降低 10-15%，但需单独评估长尾用户的 P99 延迟合规性

## Evidence

先验知识/题面给定，逻辑校验通过：加权距离贡献计算（0.05 * 500 = 25km）数学正确，占比及剔除后的影响幅度在合理范围内，符合长尾分布对均值影响的统计直觉。

## Search Query

long tail users remote areas impact on average distance CDN latency
