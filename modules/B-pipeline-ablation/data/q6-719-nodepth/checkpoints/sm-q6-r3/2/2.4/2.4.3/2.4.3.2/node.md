# N234: 单 POP 月度折旧成本 Depreciation_Per_POP = (CapEx_Per_POP / Useful_Life_Months) × (1 - 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

单 POP 月度折旧成本 Depreciation_Per_POP = (CapEx_Per_POP / Useful_Life_Months) × (1 - Residual_Value_Ratio)，其中 CapEx_Per_POP 包含服务器、存储、网络设备采购成本（典型值 ¥500k-1M/POP），Useful_Life_Months 为资产折旧年限（通常 36-60 个月），Residual_Value_Ratio 为残值率（通常 5%-10%）。

## Corrected Claim

单 POP 月度折旧成本 Depreciation_Per_POP = (CapEx_Per_POP / Useful_Life_Months) × (1 - Residual_Value_Ratio)，其中 CapEx_Per_POP 包含服务器、存储、网络设备采购成本（典型值 ¥500k-1M/POP），Useful_Life_Months 为资产折旧年限（通常 36-60 个月），Residual_Value_Ratio 为残值率（通常 5%-10%）。

## Evidence

先验知识/题面给定，逻辑校验通过：折旧公式符合直线折旧法标准定义，CapEx量级（¥500k-1M/POP）与典型边缘节点硬件配置相符，折旧年限（36-60个月）及残值率（5%-10%）均处于电信/IT行业常规财务参数范围内，无逻辑矛盾。

## Search Query

CDN edge node capex server storage network equipment cost depreciation useful life
