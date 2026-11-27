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

父节点级核验通过：正交+完备+无冗余（子节点分别定义了成本项的随机源（r）、收益项的期望表达式（E[Revenue]）以及基于两者导数的策略临界条件，三者分别对应效用函数中的不同组成部分及最终决策逻辑，相互独立且无重叠。）
