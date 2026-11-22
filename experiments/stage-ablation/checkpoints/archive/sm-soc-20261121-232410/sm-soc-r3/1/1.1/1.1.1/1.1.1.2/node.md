# N93: P_max（历史最高成交价）的检索逻辑：P_max = Max(P_deal_i | i ∈ SameCategory, T < 30d)，即同类目近30天最高

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

P_max（历史最高成交价）的检索逻辑：P_max = Max(P_deal_i | i ∈ SameCategory, T < 30d)，即同类目近30天最高成交价；该值受极端值影响大，需通过Winsorize处理（如截断至99分位数）以稳定参考点。

## Corrected Claim

P_max（历史最高成交价）的检索逻辑：P_max = Max(P_deal_i | i ∈ SameCategory, T < 30d)，即同类目近30天最高成交价；该值受极端值影响大，需通过Winsorize处理（如截断至99分位数）以稳定参考点。

## Evidence

先验知识/题面给定，逻辑校验通过：P_max定义为同类目近30天最高成交价符合市场数据检索逻辑，且最高价作为极端值确实易受异常值影响，采用Winsorize（如99分位数截断）是统计学中处理极端值以稳定参考点的标准且合理的方法。

## Search Query

outlier handling price anchor max transaction
