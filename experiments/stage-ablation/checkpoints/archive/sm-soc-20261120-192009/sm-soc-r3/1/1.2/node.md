# N6: 演化定向压力（逐利）：卖家效用函数 U_seller = E[Revenue] - C_holding，其中 C_holding = r * t_wait，r为

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

演化定向压力（逐利）：卖家效用函数 U_seller = E[Revenue] - C_holding，其中 C_holding = r * t_wait，r为持有成本率；理性策略是最大化 U_seller，导致初始挂价锚定在 μ 附近以测试市场上限。

## Corrected Claim

演化定向压力（逐利）：卖家效用函数 U_seller = E[Revenue] - C_holding，其中 C_holding = r * t_wait，r为持有成本率；理性策略是最大化 U_seller，导致初始挂价锚定在 μ 附近以测试市场上限。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别定义了效用函数中的随机参数来源（C_holding的随机性）、期望收益项的具体表达式（E[Revenue]）以及基于两项差值的策略优化条件（临界条件）。三者分别对应数学模型中的输入分布、函数定义和优化约束，逻辑上相互独立且无重叠，共同完整覆盖了父节点中关于效用函数构成及理性策略推导的核心内容。）
