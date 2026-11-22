# N317: 修正项量化：估计Cobb-Douglas模型中的指数项 ε 和 δ 的具体数值，以及当价格偏离基线20%时，线性近似与Cobb-Douglas预测的需求量相对误

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N102

## Claim

修正项量化：估计Cobb-Douglas模型中的指数项 ε 和 δ 的具体数值，以及当价格偏离基线20%时，线性近似与Cobb-Douglas预测的需求量相对误差（Error = |Q_lin - Q_CD| / Q_CD）。

## Corrected Claim

Cobb-Douglas模型中的指数项 ε 和 δ 需通过具体市场数据回归估计；当价格偏离基线20%时，线性近似与Cobb-Douglas预测的需求量相对误差取决于具体的指数值，通常随指数绝对值增大而增大，需代入具体参数计算。

## Evidence

[质询]该陈述要求提供具体的数值估计（ε, δ 的具体值及特定偏差下的误差值），但 Cobb-Douglas 模型的指数取决于具体商品的市场数据，且线性近似误差依赖于具体的函数形式和基线点，属于经验事实，无法仅从第一性原理推导得出唯一数值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值非数学恒等式或物理定律推论，属于需实证数据支持的经验参数）

## Search Query

Cobb-Douglas demand estimation coefficients price deviation error linear approximation
