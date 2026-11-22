# N60: 共享随机源：用户行为波动性 σ_behavior，定义为活跃用户数 N_users 的日度波动标准差与平均值的比值（变异系数）；该随机源驱动 GMV 与广告收入

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N12

## Claim

共享随机源：用户行为波动性 σ_behavior，定义为活跃用户数 N_users 的日度波动标准差与平均值的比值（变异系数）；该随机源驱动 GMV 与广告收入 eCPM 的联合波动，假设 N_users ~ N(μ_users, σ_users²)，且 eCPM 与 N_users 存在正相关（ρ_eCPM_users > 0），是平台收益函数 R_platform 的主要内生扰动项。

## Corrected Claim

共享随机源：用户行为波动性 σ_behavior，定义为活跃用户数 N_users 的日度波动标准差与平均值的比值（变异系数）；该随机源驱动 GMV 与广告收入 eCPM 的联合波动，假设 N_users ~ N(μ_users, σ_users²)，且 eCPM 与 N_users 存在正相关（ρ_eCPM_users > 0），是平台收益函数 R_platform 的主要内生扰动项。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别描述了随机源在GMV、eCPM两个主要收益组件上的传导机制（弹性分解），以及最终在平台总收益层面的方差聚合公式。三者分别对应“分量1传导”、“分量2传导”和“系统级聚合”，逻辑层次清晰，互不重叠且无矛盾。虽然第三个子节点引用了前两个子节点隐含的协方差关系，但这是从微观传导到宏观波动的必要推导步骤，不构成冗余。）

## Search Query

user engagement volatility eCPM correlation active users standard deviation
