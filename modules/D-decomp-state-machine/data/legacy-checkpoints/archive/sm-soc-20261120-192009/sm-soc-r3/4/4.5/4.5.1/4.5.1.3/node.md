# N263: 方差膨胀系数（VIF）估计：在未成交商品占比 30% 的情况下，若假设未成交商品价格方差 Var(P_unsold) = k * Var(P_sold)，则总体

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

方差膨胀系数（VIF）估计：在未成交商品占比 30% 的情况下，若假设未成交商品价格方差 Var(P_unsold) = k * Var(P_sold)，则总体方差 Var(P_total) = 0.7*Var(P_sold) + 0.3*k*Var(P_sold)；通过样本内残差平方和比值估计 k，若 k > 1.5 则简单乘法因子 1.43 低估了标准误，需使用 Bootstrap 重抽样计算真实 SE。

## Corrected Claim

方差膨胀系数（VIF）估计：在未成交商品占比 30% 的情况下，若假设未成交商品价格方差 Var(P_unsold) = k * Var(P_sold)，则总体方差 Var(P_total) = 0.7*Var(P_sold) + 0.3*k*Var(P_sold)；通过样本内残差平方和比值估计 k，若 k > 1.5 则简单乘法因子 1.43 低估了标准误，需使用 Bootstrap 重抽样计算真实 SE。

## Evidence

先验知识/题面给定，逻辑校验通过：方差分解公式 Var(P_total) = 0.7*Var(P_sold) + 0.3*k*Var(P_sold) 符合混合分布方差定义（忽略均值差异或假设均值相同），且 k>1.5 时简单因子低估标准误的推断符合统计学直觉。
