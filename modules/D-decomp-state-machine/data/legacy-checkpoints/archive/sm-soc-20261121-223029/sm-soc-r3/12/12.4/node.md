# N374: 曝光边际贡献系数 β_exp 的回归控制变量集：模型设定为 Impression_i = β_0 + β_exp * δ_i + β_1 * Quality_S

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N125, N126, N127

## Claim

曝光边际贡献系数 β_exp 的回归控制变量集：模型设定为 Impression_i = β_0 + β_exp * δ_i + β_1 * Quality_Score_i + β_2 * Image_Quality_i + β_3 * Seller_Rating_i + ε，其中 δ_i 为溢价率；需报告 β_exp 的标准误及 t 统计量，且要求所有控制变量的 VIF < 5，以确保 β_exp 的估计不受商品质量混杂效应干扰。

## Corrected Claim

曝光边际贡献系数 β_exp 的回归控制变量集：模型设定为 Impression_i = β_0 + β_exp * δ_i + β_1 * Quality_Score_i + β_2 * Image_Quality_i + β_3 * Seller_Rating_i + ε，其中 δ_i 为溢价率；需报告 β_exp 的标准误及 t 统计量，且要求所有控制变量的 VIF < 5，以确保 β_exp 的估计不受商品质量混杂效应干扰。

## Evidence

先验知识/题面给定，逻辑校验通过：回归模型设定符合计量经济学规范，VIF<5是控制多重共线性的标准阈值，逻辑自洽。
