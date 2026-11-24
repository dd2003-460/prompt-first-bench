# N378: 基于校准单价的年化转换 API 费用对比：AWS (500M objects, 10% change) = 50M/1000 * $0.005 = $250 ≈

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N128

## Claim

基于校准单价的年化转换 API 费用对比：AWS (500M objects, 10% change) = 50M/1000 * $0.005 = $250 ≈ ¥1,800/年；Aliyun (500M objects, 10% change) = 50M/10000 * ¥0.01 = ¥50/年；表明 API 请求费用在总成本中占比极低 (<0.1%)，主要成本在于存储费率差异。

## Corrected Claim

基于校准单价的年化转换 API 费用对比：AWS (500M objects, 10% change) = 50M/1000 * $0.005 = $250 ≈ ¥1,800/年；Aliyun (500M objects, 10% change) = 50M/10000 * ¥0.01 = ¥50/年；表明 API 请求费用在总成本中占比极低 (<0.1%)，主要成本在于存储费率差异。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（AWS: 50,000 * 0.005 = 250 USD; Aliyun: 5,000 * 0.01 = 50 CNY），汇率换算合理（250 USD ≈ 1800 CNY），且符合云存储API费用远低于存储费用的常识。
