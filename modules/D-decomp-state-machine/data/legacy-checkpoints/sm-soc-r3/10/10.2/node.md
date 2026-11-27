# N322: 方差分解的回归实现：Var(T_close) = β_noise * Var(Impulse_Buy_Rate) + β_liquidity * Var(Mar

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N111

## Claim

方差分解的回归实现：Var(T_close) = β_noise * Var(Impulse_Buy_Rate) + β_liquidity * Var(Market_Depth) + Residual；通过多元回归系数 β_noise / (β_noise + β_liquidity) 估算随机噪声的贡献率，验证其是否确实落在 35%-40% 区间。

## Corrected Claim

方差分解的回归实现：Var(T_close) = β_noise * Var(Impulse_Buy_Rate) + β_liquidity * Var(Market_Depth) + Residual；通过多元回归系数 β_noise / (β_noise + β_liquidity) 估算随机噪声的贡献率，具体数值需根据特定市场和时间窗口实证确定，而非固定为35%-40%。

## Evidence

[质询]该陈述将特定的经验性数值区间（35%-40%）作为既定事实进行验证，但缺乏具体的市场背景、时间窗口或资产类别限定。不同市场（如美股、A股、加密货币）和不同时间尺度下的噪声贡献率差异巨大，直接断言其落在该区间缺乏普适性依据，且参考来源缺失无法证实该特定数值范围。 | 逻辑上多元回归分解方差的数学框架自洽，但35%-40%属于特定经验事实，非第一性原理可推导，且本轮检索无可用来源支持该具体数值区间，故降级。

## Search Query

variance decomposition of transaction time impulse buying vs market liquidity e-commerce
