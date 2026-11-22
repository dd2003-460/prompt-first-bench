# N357: 先验分布的参数校准：基于 N162-N164 的数据，设定 μ_prior = δc_mean，σ_prior = sqrt(Σ(δc_i - δc_mean)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N122

## Claim

先验分布的参数校准：基于 N162-N164 的数据，设定 μ_prior = δc_mean，σ_prior = sqrt(Σ(δc_i - δc_mean)^2 / (3-1))，该先验分布将用于 N120 中的贝叶斯更新计算

## Corrected Claim

先验分布的参数校准：基于 N162-N164 的数据，设定 μ_prior = δc_mean，σ_prior = sqrt(Σ(δc_i - δc_mean)^2 / (3-1))，该先验分布将用于 N120 中的贝叶斯更新计算

## Evidence

先验知识/题面给定，逻辑校验通过：基于样本数据计算均值和样本标准差（分母为 n-1）作为正态先验的参数是贝叶斯推断中的标准做法，公式定义清晰且量纲一致。
