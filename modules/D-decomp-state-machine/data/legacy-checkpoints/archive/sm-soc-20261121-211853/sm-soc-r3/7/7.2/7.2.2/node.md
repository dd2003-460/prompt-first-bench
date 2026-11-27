# N152: 定义‘高溢价组’需设定偏离度下限 $D_{min} = 15\%$ 且上限 $D_{max} = P_{95}$（第95百分位），以避免将 $D > P_{95

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

定义‘高溢价组’需设定偏离度下限 $D_{min} = 15\%$ 且上限 $D_{max} = P_{95}$（第95百分位），以避免将 $D > P_{95}$ 的极端异常值（如标错价）纳入分母计算，导致 $\Delta P_{high}$ 被高估从而低估 $\eta$。

## Corrected Claim

定义‘高溢价组’需设定偏离度下限 $D_{min} = 15\%$ 且上限 $D_{max} = P_{95}$（第95百分位），以避免将 $D > P_{95}$ 的极端异常值（如标错价）纳入分母计算，导致 $\Delta P_{high}$ 被高估从而低估 $\eta$。

## Evidence

先验知识/题面给定，逻辑校验通过：截断极端异常值（Winsorization/Trimming）是统计处理中防止离群点扭曲均值/分母的标准做法，逻辑自洽且量级合理。
