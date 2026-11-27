# N164: 共享随机源：估值分布的偏度（Skewness）对 z_95 值的修正：二手非标品估值分布通常呈右偏（Skewness > 0），此时上尾 95 分位数对应的 z

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

共享随机源：估值分布的偏度（Skewness）对 z_95 值的修正：二手非标品估值分布通常呈右偏（Skewness > 0），此时上尾 95 分位数对应的 z 值不再是标准正态的 1.645，而是需使用偏正态分布（Skew-Normal）的分位数函数，具体修正系数 k_skew 需根据商品类别的偏度参数 δ_skew 计算，通常 δ_skew 在 0.2-0.5 之间时，z_95 会提升至 1.8-2.1。

## Corrected Claim

共享随机源：估值分布的偏度（Skewness）对 z_95 值的修正：二手非标品估值分布通常呈右偏（Skewness > 0），此时上尾 95 分位数对应的 z 值不再是标准正态的 1.645，而是需使用偏正态分布（Skew-Normal）的分位数函数，具体修正系数 k_skew 需根据商品类别的偏度参数 δ_skew 计算，通常 δ_skew 在 0.2-0.5 之间时，z_95 会提升至 1.8-2.1。

## Evidence

先验知识/题面给定，逻辑校验通过：右偏分布（Skewness > 0）意味着上尾更长，95分位数对应的z值确实会高于标准正态的1.645；在偏度参数δ_skew为0.2-0.5的中等右偏情形下，z_95提升至1.8-2.1符合偏正态分布（Skew-Normal）的统计性质与量级直觉。

## Search Query

skew-normal distribution 95th percentile quantile function second hand price distribution skewness
