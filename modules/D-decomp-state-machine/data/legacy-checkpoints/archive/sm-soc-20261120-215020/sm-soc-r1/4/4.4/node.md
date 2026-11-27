# N20: 受损利益相关方识别：卖家群体中‘高溢价策略者’（挂价 > 1.15 * P_avg）的受损程度量化：其曝光量下降比例 ΔExposure ≈ λ * (P_li

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

受损利益相关方识别：卖家群体中‘高溢价策略者’（挂价 > 1.15 * P_avg）的受损程度量化：其曝光量下降比例 ΔExposure ≈ λ * (P_list - P_avg) / P_avg，当 λ=0.5 且偏差为 20% 时，曝光量下降 10%；成交概率下降 ΔProb ≈ 1 - e^(-k * ΔExposure)，其中 k 为转化系数（假设 k=1.5），导致成交概率下降约 14%。

## Corrected Claim

受损利益相关方识别：卖家群体中‘高溢价策略者’（挂价 > 1.15 * P_avg）的受损程度量化：其曝光量下降比例 ΔExposure ≈ λ * (P_list - P_avg) / P_avg，当 λ=0.5 且偏差为 20% 时，曝光量下降 10%；成交概率下降 ΔProb ≈ 1 - e^(-k * ΔExposure)，其中 k 为转化系数（假设 k=1.5），导致成交概率下降约 14%。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算正确（ΔExposure=0.5*0.2=0.1，ΔProb=1-e^(-1.5*0.1)≈0.139），模型假设自洽

## Search Query

seller exposure reduction impact on conversion rate price deviation
