# N181: 工作点1（低成本/低功能）：仅实现基础数据展示，C_dev_low = 5000元, C_maintenance_low = 500元/月, C_support

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

工作点1（低成本/低功能）：仅实现基础数据展示，C_dev_low = 5000元, C_maintenance_low = 500元/月, C_support_low = 0.1% of GMV，则首年总成本 ΔC_low = 5000 + 500*12 + 0.001 * GMV_yearly = 11000 + 0.001 * GMV_yearly，此工作点下透明化效果 α_low = 0.1（最低提升率），需验证 ΔRev_low = (Rev_post_low - Rev_pre) 是否覆盖 ΔC_low。

## Corrected Claim

工作点1（低成本/低功能）：仅实现基础数据展示，C_dev_low = 5000元, C_maintenance_low = 500元/月, C_support_low = 0.1% of GMV，则首年总成本 ΔC_low = 5000 + 500*12 + 0.001 * GMV_yearly = 11000 + 0.001 * GMV_yearly，此工作点下透明化效果 α_low = 0.1（最低提升率），需验证 ΔRev_low = (Rev_post_low - Rev_pre) 是否覆盖 ΔC_low。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 5000 + 500*12 = 11000 正确，公式结构符合成本定义，参数为假设值且内部自洽。

## Search Query

minimal viable product cost for price transparency feature e-commerce platform
