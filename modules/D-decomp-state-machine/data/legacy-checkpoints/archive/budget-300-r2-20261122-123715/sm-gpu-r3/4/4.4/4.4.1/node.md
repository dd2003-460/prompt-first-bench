# N94: 条件分支表-分支1：Budget_B < $3000 且 Quality_Sensitivity=Low 且 Electricity_Rate < $0.15/

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

条件分支表-分支1：Budget_B < $3000 且 Quality_Sensitivity=Low 且 Electricity_Rate < $0.15/kWh → 推荐 1x RTX 4090 + INT8 (AWQ)；此时 3 年 TCO ≈ $5600，但需注意 24GB 显存不足以完整加载 27B INT8 模型 (需 27GB)，实际需依赖部分 Offload 或降低上下文至 24K，若必须 32K 则此分支无可行解，需升级预算至 $4000+ 购买 2x 3090/4090 或二手 A6000。

## Corrected Claim

条件分支表-分支1：Budget_B < $3000 且 Quality_Sensitivity=Low 且 Electricity_Rate < $0.15/kWh → 推荐 1x RTX 4090 + INT8 (AWQ)；此时 3 年 TCO ≈ $5600，但需注意 24GB 显存不足以完整加载 27B INT8 模型 (需 27GB)，实际需依赖部分 Offload 或降低上下文至 24K，若必须 32K 则此分支无可行解，需升级预算至 $4000+ 购买 2x 3090/4090 或二手 A6000。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数INT8模型权重约27GB，超过RTX 4090的24GB显存，需Offload或降低上下文，逻辑自洽且数值量级合理。
