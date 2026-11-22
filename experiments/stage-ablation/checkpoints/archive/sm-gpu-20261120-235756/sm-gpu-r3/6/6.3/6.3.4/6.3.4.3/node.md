# N326: 使用频率（Utilization Rate）对单位 Token 成本上升幅度的修正系数，定义为：Cost_Increase = D_Perf * (1 / Ut

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N120

## Claim

使用频率（Utilization Rate）对单位 Token 成本上升幅度的修正系数，定义为：Cost_Increase = D_Perf * (1 / Utilization)；其中 D_Perf 为性能贬值幅度（如 N146/N147），Utilization 为实际使用频率（如 24/7 为 1.0，仅工作日为 0.4）；该公式用于将'性能贬值'转化为'单位 Token 成本上升'，高使用频率场景下成本上升幅度被放大，低使用频率场景下影响较小。

## Corrected Claim

使用频率（Utilization Rate）对单位 Token 成本上升幅度的修正系数，定义为：Cost_Increase = D_Perf * (1 / Utilization)；其中 D_Perf 为性能贬值幅度（如 N146/N147），Utilization 为实际使用频率（如 24/7 为 1.0，仅工作日为 0.4）；该公式用于将'性能贬值'转化为'单位 Token 成本上升'，高使用频率场景下成本上升幅度被放大，低使用频率场景下影响较小。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 Cost_Increase = D_Perf * (1 / Utilization) 在数学上自洽，符合‘总成本固定，使用量减少导致单位成本上升’的经济直觉（利用率越低，分母越小，系数越大，成本上升幅度越大），且作为定义性公式无内部矛盾。

## Search Query

GPU utilization rate impact on token cost inflation performance depreciation
