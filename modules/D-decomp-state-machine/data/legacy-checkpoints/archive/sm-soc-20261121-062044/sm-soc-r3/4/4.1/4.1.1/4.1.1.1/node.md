# N191: 共享随机源：市场活跃度波动 σ²_market，定义为月度 GMV 的变异系数，作为 P(D|H) 中观测数据 D 的噪声源；需估计 σ_market 的分布，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

共享随机源：市场活跃度波动 σ²_market，定义为月度 GMV 的变异系数，作为 P(D|H) 中观测数据 D 的噪声源；需估计 σ_market 的分布，若 σ_market > 0.2 则似然函数需加入重尾修正项，否则假设正态分布。

## Corrected Claim

共享随机源：市场活跃度波动 σ²_market，定义为月度 GMV 的变异系数，作为 P(D|H) 中观测数据 D 的噪声源；需估计 σ_market 的分布，若 σ_market > 0.2 则似然函数需加入重尾修正项，否则假设正态分布。

## Evidence

先验知识/题面给定，逻辑校验通过
