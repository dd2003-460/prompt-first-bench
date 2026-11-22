# N306: 曝光权重函数 α 和 β 的逆向工程方法：构建回归模型 Rank_Score = α*ln(CTR) + β*ln(Speed) + γ*Price + ε，利

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

曝光权重函数 α 和 β 的逆向工程方法：构建回归模型 Rank_Score = α*ln(CTR) + β*ln(Speed) + γ*Price + ε，利用平台历史排名数据（Rank_Score 可观测）对 α/β 进行最小二乘估计，需假设其他因子正交。

## Corrected Claim

曝光权重函数 α 和 β 的逆向工程方法：构建回归模型 Rank_Score = α*ln(CTR) + β*ln(Speed) + γ*Price + ε，利用平台历史排名数据（Rank_Score 可观测）对 α/β 进行最小二乘估计，需假设其他因子正交。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述描述了一种标准的线性回归逆向工程方法，数学逻辑自洽，且明确指出了‘需假设其他因子正交’这一关键前提条件，符合计量经济学基本原理。

## Search Query

reverse engineering recommendation algorithm weights regression rank score
