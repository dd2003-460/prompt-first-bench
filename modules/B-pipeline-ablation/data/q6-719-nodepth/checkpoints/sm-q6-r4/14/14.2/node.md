# N414: 硬件折旧分摊 F_depreciation 计算：F_depreciation = Total_Hardware_CapEx / Depreciation_Mo

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N144

## Claim

硬件折旧分摊 F_depreciation 计算：F_depreciation = Total_Hardware_CapEx / Depreciation_Months，假设单POP服务器+存储CapEx为¥100k，10个POP总CapEx为¥1000k，按36个月直线折旧，则 F_depreciation = 1000000 / 36 ≈ ¥27.8k/月。

## Corrected Claim

硬件折旧分摊 F_depreciation 计算：F_depreciation = Total_Hardware_CapEx / Depreciation_Months，假设单POP服务器+存储CapEx为¥100k，10个POP总CapEx为¥1000k，按36个月直线折旧，则 F_depreciation = 1000000 / 36 ≈ ¥27.8k/月。

## Evidence

先验知识/题面给定，逻辑校验通过：1,000,000 / 36 ≈ 27,777.78，即约 ¥27.8k/月，计算无误且符合直线折旧定义。
