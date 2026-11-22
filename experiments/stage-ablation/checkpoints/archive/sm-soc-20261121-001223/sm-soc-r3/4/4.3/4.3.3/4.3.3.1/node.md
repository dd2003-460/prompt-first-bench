# N178: 针对‘最小干预打破均衡’的具体断言，计算 Cohen's d 需明确分子 ΔEquilibrium 的统计量：若干预为价格透明度展示，ΔEquilibrium 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

针对‘最小干预打破均衡’的具体断言，计算 Cohen's d 需明确分子 ΔEquilibrium 的统计量：若干预为价格透明度展示，ΔEquilibrium 定义为干预组与对照组在 T_deal（成交周期，天）或 ΔP/P（溢价率，%）上的均值差，标准差 σ 取自对照组基线数据；若 σ 未知，使用合并标准差 s_pooled 计算 d = (M1 - M2) / s_pooled。

## Corrected Claim

针对‘最小干预打破均衡’的具体断言，计算 Cohen's d 需明确分子 ΔEquilibrium 的统计量：若干预为价格透明度展示，ΔEquilibrium 定义为干预组与对照组在 T_deal（成交周期，天）或 ΔP/P（溢价率，%）上的均值差，标准差 σ 取自对照组基线数据；若 σ 未知，使用合并标准差 s_pooled 计算 d = (M1 - M2) / s_pooled。

## Evidence

先验知识/题面给定，逻辑校验通过：Cohen's d 的标准定义即为均值差除以标准差，当总体标准差未知时使用合并标准差（pooled standard deviation）是统计学标准做法，量纲与逻辑自洽。
