# N82: 锚点效应强度 k_anchor：卖家挂价 P_ask = P_anchor + ε，其中 P_anchor 为展示的历史均价。价格锚定效应使 ε 的均值向 0 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N19

## Claim

锚点效应强度 k_anchor：卖家挂价 P_ask = P_anchor + ε，其中 P_anchor 为展示的历史均价。价格锚定效应使 ε 的均值向 0 收缩，收缩比例 k = 1 - (σ_new / σ_old)，预期偏离度从 20% 降至 7.5%，则 k = 0.625。

## Corrected Claim

锚点效应强度 k_anchor：卖家挂价 P_ask = P_anchor + ε，其中 P_anchor 为展示的历史均价。价格锚定效应使 ε 的均值向 0 收缩，收缩比例 k = 1 - (σ_new / σ_old)，预期偏离度从 20% 降至 7.5%，则 k = 0.625。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应锚点效应的随机微观基础（敏感度分布）、静态系统性偏差（展示误差）以及动态时间衰减（稳定性），三者维度正交且共同构成了计算 k_anchor 及其动态变化的完整逻辑链条，无冗余。）
