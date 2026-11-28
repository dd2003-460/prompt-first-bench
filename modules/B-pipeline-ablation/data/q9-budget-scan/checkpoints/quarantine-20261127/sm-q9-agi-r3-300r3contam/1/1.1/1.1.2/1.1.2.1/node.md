# N92: 首尾一致性偏差率的统计检验：采用配对t-test检验Head/Tail答案差异，H0: μ_diff = 0，n=100样本对，若p-value < 0.05且

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

首尾一致性偏差率的统计检验：采用配对t-test检验Head/Tail答案差异，H0: μ_diff = 0，n=100样本对，若p-value < 0.05且|μ_diff|/GT_std > 0.1，则判定偏差显著，需启用分块策略。

## Corrected Claim

首尾一致性偏差率的统计检验：采用配对t-test检验Head/Tail答案差异，H0: μ_diff = 0，n=100样本对，若p-value < 0.05且|μ_diff|/GT_std > 0.1，则判定偏差显著，需启用分块策略。

## Evidence

先验知识/题面给定，逻辑校验通过：配对t-test适用于比较同一组样本在两种条件下的差异，H0设定及显著性阈值符合统计学常规，效应量阈值0.1亦属合理经验范围。
