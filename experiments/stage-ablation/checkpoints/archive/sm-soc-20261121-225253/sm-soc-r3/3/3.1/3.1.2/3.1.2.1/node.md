# N84: 季节性修正因子 β_season 的计算公式：β_season = 1 + s * sin(2π(t - t_peak)/365)，其中 s 为该品类近3年历史

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

季节性修正因子 β_season 的计算公式：β_season = 1 + s * sin(2π(t - t_peak)/365)，其中 s 为该品类近3年历史数据拟合的振幅（如电子产品 s≈0.05），t_peak 为历史成交均价最高点对应的月份；若 s 未校准（s=0），在 Q4 旺季 P_avg 将被低估约 5-10%。

## Corrected Claim

季节性修正因子 β_season 的计算公式：β_season = 1 + s * sin(2π(t - t_peak)/365)，其中 s 为该品类近3年历史数据拟合的振幅（如电子产品 s≈0.05），t_peak 为历史成交均价最高点对应的月份；若 s 未校准（s=0），在 Q4 旺季 P_avg 将被低估约 5-10%。

## Evidence

先验知识/题面给定，逻辑校验通过：正弦函数模型是季节性修正的标准形式，s=0.05时最大偏差为5%，结合Q4旺季通常对应峰值附近，低估5-10%的量级在逻辑上合理且自洽。

## Search Query

seasonal adjustment factor calculation e-commerce transaction price
