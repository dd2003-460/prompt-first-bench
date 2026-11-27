# N25: 市场公允价 P_market 的操作性定义为过去30天内同品类、同成色、同地区成交价的加权中位数，权重 w_i 按时间衰减 exp(-λ_time * t_i)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

市场公允价 P_market 的操作性定义为过去30天内同品类、同成色、同地区成交价的加权中位数，权重 w_i 按时间衰减 exp(-λ_time * t_i) 计算，其中 λ_time ≈ 0.05/day，以反映近期价格信号的主导性。

## Corrected Claim

市场公允价 P_market 的操作性定义为过去30天内同品类、同成色、同地区成交价的加权中位数，权重 w_i 按时间衰减 exp(-λ_time * t_i) 计算，其中 λ_time ≈ 0.05/day，以反映近期价格信号的主导性。

## Evidence

先验知识/题面给定，逻辑校验通过
