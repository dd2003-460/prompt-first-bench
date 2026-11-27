# N69: 贝叶斯后验概率映射公式：P(H|D) = [P(D|H) * P(H)] / P(D)，其中 P(H) 为先验概率，P(D|H) 为似然函数，需通过 MCMC 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

贝叶斯后验概率映射公式：P(H|D) = [P(D|H) * P(H)] / P(D)，其中 P(H) 为先验概率，P(D|H) 为似然函数，需通过 MCMC 或变分推断计算，而非简单区间映射，以确保置信度反映真实不确定性。

## Corrected Claim

贝叶斯后验概率映射公式：P(H|D) = [P(D|H) * P(H)] / P(D)，其中 P(H) 为先验概率，P(D|H) 为似然函数，需通过 MCMC 或变分推断计算，而非简单区间映射，以确保置信度反映真实不确定性。

## Evidence

先验知识/题面给定，逻辑校验通过：贝叶斯公式表述正确，MCMC/变分推断是计算复杂后验分布的标准方法，逻辑自洽。
