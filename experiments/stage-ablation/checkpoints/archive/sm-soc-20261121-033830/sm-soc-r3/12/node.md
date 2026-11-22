# N113: 随机偏好噪声（Stochastic Noise）的强度 σ_noise 通过卖家定价偏离最优策略 ε* 的标准差衡量：σ_noise = std(P_i - P

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

随机偏好噪声（Stochastic Noise）的强度 σ_noise 通过卖家定价偏离最优策略 ε* 的标准差衡量：σ_noise = std(P_i - P*_i)，若 σ_noise < D_p 的 50%，则假设链成立，即定向压力主导均衡；需检索二手市场中卖家定价离散度的实证分布。

## Corrected Claim

随机偏好噪声（Stochastic Noise）的强度 σ_noise 通过卖家定价偏离最优策略 ε* 的标准差衡量：σ_noise = std(P_i - P*_i)，若 σ_noise < D_p 的 50%，则假设链成立，即定向压力主导均衡；需检索二手市场中卖家定价离散度的实证分布。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别关注噪声分布特性（形状/稳健性）、测量误差分离（信号与噪声解耦）以及阈值基准定义（分母校准），三者逻辑独立且互补，共同构成了计算和验证 σ_noise 的完整方法论链条，无重叠或矛盾。）
