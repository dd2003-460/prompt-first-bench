# N170: 卖家信用分 (Seller_Credit) 对成交周期 T_close 的偏回归系数 β_credit 的估计值：在控制 ΔQ 后，每增加 10 分信用分，T_

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

卖家信用分 (Seller_Credit) 对成交周期 T_close 的偏回归系数 β_credit 的估计值：在控制 ΔQ 后，每增加 10 分信用分，T_close 预期减少 0.5-1.5 天；该系数需通过平台历史数据回归验证，若 |β_credit| < 0.1 则信用分非主要混杂变量。

## Corrected Claim

卖家信用分 (Seller_Credit) 对成交周期 T_close 的偏回归系数 β_credit 需通过平台历史数据回归验证；若 |β_credit| < 0.1，则信用分非主要混杂变量。具体系数值（如每10分对应减少的天数）需依据实际回归结果确定，通常预期为负值。

## Evidence

[质询]该陈述包含具体的经验性数值范围（0.5-1.5天）和阈值（0.1），属于特定平台数据下的统计结论，无法从第一性原理或通用逻辑中严格推导得出，且缺乏外部数据支持其具体量级。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

C2C marketplace seller credit score impact on transaction time regression coefficient
