# N216: 商品类别因子 f(C) 的量化：不同类别（如电子产品 vs 服饰）的基准咨询率差异，需通过历史数据统计各类别的 λ_base_median，例如电子产品 λ_b

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N77

## Claim

商品类别因子 f(C) 的量化：不同类别（如电子产品 vs 服饰）的基准咨询率差异，需通过历史数据统计各类别的 λ_base_median，例如电子产品 λ_base ≈ 0.03/h，服饰 λ_base ≈ 0.01/h。

## Corrected Claim

商品类别因子 f(C) 的量化：不同类别（如电子产品 vs 服饰）的基准咨询率存在差异，需通过历史数据统计各类别的 λ_base_median，通常电子产品的基准咨询率高于服饰。

## Evidence

[质询]具体数值（0.03/h 和 0.01/h）属于经验事实，缺乏来源支持，且不同平台/时间段的基准咨询率波动较大，固定数值可能不准确。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

category specific consultation rate second hand platform electronics vs clothing
