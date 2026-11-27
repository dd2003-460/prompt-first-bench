# N263: 函数形式 f 的线性假设检验：对回归模型 δ = β0 + β1 * λ + ε 进行残差正态性检验（Shapiro-Wilk），若 p < 0.05 或存在显

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89, N90, N91

## Claim

函数形式 f 的线性假设检验：对回归模型 δ = β0 + β1 * λ + ε 进行残差正态性检验（Shapiro-Wilk），若 p < 0.05 或存在显著异方差，则线性形式失效，需引入二次项 λ² 或交互项 λ * 品类哑变量。

## Corrected Claim

函数形式 f 的线性假设检验：对回归模型 δ = β0 + β1 * λ + ε 进行残差正态性检验（Shapiro-Wilk），若 p < 0.05 或存在显著异方差，则线性形式失效，需引入二次项 λ² 或交互项 λ * 品类哑变量。

## Evidence

先验知识/题面给定，逻辑校验通过：Shapiro-Wilk检验用于残差正态性，p<0.05拒绝正态假设，异方差性破坏OLS有效性，引入二次项或交互项是标准的模型修正策略，逻辑自洽且符合计量经济学规范。
