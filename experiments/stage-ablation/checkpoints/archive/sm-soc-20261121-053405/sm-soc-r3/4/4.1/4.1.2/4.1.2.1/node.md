# N174: 共享随机源：定义残差标准差 $\sigma_{\epsilon}$ 为回归模型 $T_{cycle} = \beta_0 + \beta_1 P_{premiu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

共享随机源：定义残差标准差 $\sigma_{\epsilon}$ 为回归模型 $T_{cycle} = \beta_0 + \beta_1 P_{premium} + \epsilon$ 中误差项 $\epsilon$ 的标准差，其数值受 $T_{cycle}$ 测量噪声（$\sigma_{data}$）和未观测协变量（如商品质量异质性）影响，需通过 OLS 残差平方和 $RSS/(n-2)$ 估计。

## Corrected Claim

共享随机源：定义残差标准差 $\sigma_{\epsilon}$ 为回归模型 $T_{cycle} = \beta_0 + \beta_1 P_{premium} + \epsilon$ 中误差项 $\epsilon$ 的标准差，其数值受 $T_{cycle}$ 测量噪声（$\sigma_{data}$）和未观测协变量（如商品质量异质性）影响，需通过 OLS 残差平方和 $RSS/(n-2)$ 估计。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述准确描述了线性回归模型中残差标准差的定义、影响因素（测量噪声与遗漏变量）以及基于OLS残差平方和的自由度调整估计方法，符合统计学基本原理。

## Search Query

OLS residual standard error estimation formula
