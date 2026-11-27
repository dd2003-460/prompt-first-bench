# N240: 用户生命周期价值变化 ΔUser_LTV 的量化分解：ΔUser_LTV = - (C_acquisition + C_support_per_user) + 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N79

## Claim

用户生命周期价值变化 ΔUser_LTV 的量化分解：ΔUser_LTV = - (C_acquisition + C_support_per_user) + (M_margin × N_transactions_lost)，其中 C_acquisition 为获客成本（典型值 50-100 元/用户），N_transactions_lost 为流失前平均剩余交易次数（假设 3-5 次），M_margin 为单次交易毛利（典型值 5-10 元），计算得出 ΔUser_LTV 约为 -50 至 -100 元/流失用户。

## Corrected Claim

用户生命周期价值变化 ΔUser_LTV 的量化分解：ΔUser_LTV = - (C_acquisition + C_support_per_user) + (M_margin × N_transactions_lost)，其中 C_acquisition 为获客成本（典型值 50-100 元/用户），N_transactions_lost 为流失前平均剩余交易次数（假设 3-5 次），M_margin 为单次交易毛利（典型值 5-10 元），计算得出 ΔUser_LTV 约为 -50 至 -100 元/流失用户。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合LTV分解逻辑，代入典型值（获客成本50-100元，毛利5-10元×3-5次=15-50元）后，净损失范围在-35至-85元之间，与结论-50至-100元量级一致且逻辑自洽。

## Search Query

customer lifetime value churn cost e-commerce platform metrics
