# N148: 共享随机源定义：买家对特定二手商品质量状态 Q 的贝叶斯后验分布 p(Q|Signal) 由先验 N(μ_prior, σ_prior²) 与观测信号 (价格 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N48, N49, N50

## Claim

共享随机源定义：买家对特定二手商品质量状态 Q 的贝叶斯后验分布 p(Q|Signal) 由先验 N(μ_prior, σ_prior²) 与观测信号 (价格 P_ask, 降价幅度 ΔP, 卖家历史) 共同决定，其核心随机变量为后验均值 μ_posterior 及其不确定性 σ_posterior，该随机源是所有买家决策概率的底层输入。

## Corrected Claim

共享随机源定义：买家对特定二手商品质量状态 Q 的贝叶斯后验分布 p(Q|Signal) 由先验 N(μ_prior, σ_prior²) 与观测信号 (价格 P_ask, 降价幅度 ΔP, 卖家历史) 共同决定，其核心随机变量为后验均值 μ_posterior 及其不确定性 σ_posterior，该随机源是所有买家决策概率的底层输入。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述准确描述了贝叶斯推断在二手商品质量评估中的标准应用框架，先验、似然（信号）与后验的关系符合概率论基本原理，且作为模型定义逻辑自洽。

## Search Query

Bayesian updating model second-hand goods quality uncertainty prior distribution
