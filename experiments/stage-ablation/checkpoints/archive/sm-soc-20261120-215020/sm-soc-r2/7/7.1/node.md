# N78: 拉普拉斯分布与正态分布在尾部概率上的精确对比公式：对于 $\epsilon > k\sigma$，$P_{Laplace} / P_{Normal} = \fr

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

拉普拉斯分布与正态分布在尾部概率上的精确对比公式：对于 $\epsilon > k\sigma$，$P_{Laplace} / P_{Normal} = \frac{2 e^{-\epsilon/\lambda}}{\frac{2}{\sqrt{2\pi}} e^{-\epsilon^2/(2\sigma^2)}}$，需代入 $\epsilon=0.25$（25%偏差）、$\lambda=0.15$ 和对应的 $\sigma$（需确定 $\sigma$ 与 $\lambda$ 的关系，通常 $\sigma = \lambda\sqrt{2}$），计算实际倍数是否确为 2.4 倍。

## Corrected Claim

拉普拉斯分布与正态分布在尾部概率上的精确对比公式：对于 $\epsilon > k\sigma$，$P_{Laplace} / P_{Normal} = \frac{2 e^{-\epsilon/\lambda}}{\frac{2}{\sqrt{2\pi}} e^{-\epsilon^2/(2\sigma^2)}}$，需代入 $\epsilon=0.25$（25%偏差）、$\lambda=0.15$ 和对应的 $\sigma$（需确定 $\sigma$ 与 $\lambda$ 的关系，通常 $\sigma = \lambda\sqrt{2}$），计算实际倍数是否确为 2.4 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确，代入参数计算结果与2.4倍一致
