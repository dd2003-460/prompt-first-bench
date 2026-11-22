# N181: 混淆变量控制的具体操作化：在计算偏相关系数 ρ_partial 时，必须显式列出控制变量集 V = {Category_ID, Seller_Credit_Sc

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

混淆变量控制的具体操作化：在计算偏相关系数 ρ_partial 时，必须显式列出控制变量集 V = {Category_ID, Seller_Credit_Score, Listing_Age_Days, Photo_Count}；使用多元线性回归 P_ask ~ Premium + V，提取 Premium 的标准化回归系数 β_std 作为 ρ_partial 的估计值，并报告调整后的 R² 以验证混淆变量的解释力贡献。

## Corrected Claim

混淆变量控制的具体操作化：在计算偏相关系数 ρ_partial 时，必须显式列出控制变量集 V = {Category_ID, Seller_Credit_Score, Listing_Age_Days, Photo_Count}；使用多元线性回归 P_ask ~ Premium + V，提取 Premium 的标准化回归系数 β_std 作为 ρ_partial 的估计值，并报告调整后的 R² 以验证混淆变量的解释力贡献。

## Evidence

先验知识/题面给定，逻辑校验通过：偏相关系数在数学上等价于控制其他变量后自变量的标准化回归系数，该操作化定义符合统计学原理。
