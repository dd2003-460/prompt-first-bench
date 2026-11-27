# N99: 修正 N40/N77 矛盾：对于标准 Pareto 分布 $f(x) = \beta x_{min}^\beta x^{-(\beta+1)}$，对数变量 $Y

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

修正 N40/N77 矛盾：对于标准 Pareto 分布 $f(x) = \beta x_{min}^\beta x^{-(\beta+1)}$，对数变量 $Y=\ln(x/x_{min})$ 服从指数分布 $Exp(\beta)$，其方差为 $1/\beta^2$。因此 $\sigma_{\log H} = 1/\beta = 1/0.9 \approx 1.111$。N40 中的 $\pi/\beta$ 错误地引入了正态分布的 $\pi$ 因子，N77 中的 $\pi/\sqrt{6}$ 错误地引入了均匀分布的方差因子。

## Corrected Claim

修正 N40/N77 矛盾：对于标准 Pareto 分布 $f(x) = \beta x_{min}^\beta x^{-(\beta+1)}$，对数变量 $Y=\ln(x/x_{min})$ 服从指数分布 $Exp(\beta)$，其方差为 $1/\beta^2$。因此 $\sigma_{\log H} = 1/\beta = 1/0.9 \approx 1.111$。N40 中的 $\pi/\beta$ 错误地引入了正态分布的 $\pi$ 因子，N77 中的 $\pi/\sqrt{6}$ 错误地引入了均匀分布的方差因子。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的对数变换确实服从指数分布，其标准差为1/β，推导严谨且量纲正确。

## Search Query

variance of log of pareto distribution
