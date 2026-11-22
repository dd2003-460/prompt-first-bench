# N37: 均衡稳定性指标 Quantified Definition：Equilibrium Stability S_eq = 1 / (1 + Var(ΔP_ask) 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

均衡稳定性指标 Quantified Definition：Equilibrium Stability S_eq = 1 / (1 + Var(ΔP_ask) + Var(ΔT_deal))，其中 Var(ΔP_ask) 和 Var(ΔT_deal) 分别为均衡状态下价格偏差和成交周期的方差，S_eq ∈ (0, 1]，S_eq 越接近 1 表示均衡越稳定，该定义将抽象的‘稳定性’转化为可计算的统计量。

## Corrected Claim

均衡稳定性指标 Quantified Definition：Equilibrium Stability S_eq = 1 / (1 + Var(ΔP_ask) + Var(ΔT_deal))，其中 Var(ΔP_ask) 和 Var(ΔT_deal) 分别为均衡状态下价格偏差和成交周期的方差，S_eq ∈ (0, 1]，S_eq 越接近 1 表示均衡越稳定，该定义将抽象的‘稳定性’转化为可计算的统计量。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的两个独立变量（价格方差、时间方差）以及最终的计算结果，三者逻辑上互不重叠且无矛盾。虽然第三个子节点依赖于前两个，但在学术分解中，将‘参数估计’与‘最终指标计算’分开是合理的结构，不属于冗余。完备性方面，覆盖了公式定义所需的所有核心组成部分。）
