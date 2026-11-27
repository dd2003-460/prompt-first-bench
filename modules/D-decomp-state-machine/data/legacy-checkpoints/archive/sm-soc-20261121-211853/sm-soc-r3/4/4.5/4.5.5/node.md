# N50: 供给端流动性下降的量化：ΔSupply = -δ * N_high_premium，其中 δ = P_exit * (1 - P_return)，P_exit 

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N18, N19, N20

## Claim

供给端流动性下降的量化：ΔSupply = -δ * N_high_premium，其中 δ = P_exit * (1 - P_return)，P_exit 为退出概率，P_return 为退出后回归概率。P_exit 可通过逻辑回归模型估计，自变量包括 ΔT、ΔE、平台满意度评分，目标变量为是否退出。

## Corrected Claim

供给端流动性下降可量化为 ΔSupply = -δ * N_high_premium，其中 δ 由退出概率 P_exit 和回归概率 P_return 决定；P_exit 可通过统计模型（如逻辑回归）基于市场指标（如 ΔT、ΔE）及用户满意度等变量进行估计。

## Evidence

父节点级核验通过：正交+完备+无冗余（两个子节点分别对应父节点公式中的两个独立参数 P_exit 和 P_return，内容无重叠且无矛盾，完整覆盖了量化模型所需的两个核心概率组件。）

## Search Query

logistic regression model seller exit probability platform intervention
