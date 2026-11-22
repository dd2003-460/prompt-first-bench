# N100: 蒙特卡洛模拟参数分布：价格弹性α服从正态分布α~N(μ_α, σ_α²)，其中μ_α=0.8, σ_α=0.2（基于历史A/B测试数据）；成交周期T的分布通过1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

蒙特卡洛模拟参数分布：价格弹性α服从正态分布α~N(μ_α, σ_α²)，其中μ_α=0.8, σ_α=0.2（基于历史A/B测试数据）；成交周期T的分布通过10000次迭代模拟得到，每次迭代随机抽样α值

## Corrected Claim

蒙特卡洛模拟参数分布：价格弹性α服从正态分布α~N(μ_α, σ_α²)，其中μ_α=0.8, σ_α=0.2（基于历史A/B测试数据）；成交周期T的分布通过10000次迭代模拟得到，每次迭代随机抽样α值

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

monte carlo simulation price elasticity normal distribution 10000 iterations
