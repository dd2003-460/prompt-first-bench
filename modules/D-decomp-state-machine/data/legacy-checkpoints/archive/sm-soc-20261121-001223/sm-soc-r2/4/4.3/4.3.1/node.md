# N64: 反事实均衡偏移量的计算：ΔEquilibrium = E[Outcome | Treat=1] - E[Outcome | Treat=0]，其中 Outcom

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

反事实均衡偏移量的计算：ΔEquilibrium = E[Outcome | Treat=1] - E[Outcome | Treat=0]，其中 Outcome 为成交周期 T_deal 或溢价率 ΔP/P；使用倾向得分匹配 (PSM) 估计反事实均值，标准误 SE 用于构建置信区间。

## Corrected Claim

反事实均衡偏移量的计算：ΔEquilibrium = E[Outcome | Treat=1] - E[Outcome | Treat=0]，其中 Outcome 为成交周期 T_deal 或溢价率 ΔP/P；使用倾向得分匹配 (PSM) 估计反事实均值，标准误 SE 用于构建置信区间。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义符合因果推断中平均处理效应（ATE）的标准定义，PSM是估计反事实均值的常用方法，逻辑自洽且量纲合理。

## Search Query

Propensity score matching counterfactual equilibrium shift calculation
