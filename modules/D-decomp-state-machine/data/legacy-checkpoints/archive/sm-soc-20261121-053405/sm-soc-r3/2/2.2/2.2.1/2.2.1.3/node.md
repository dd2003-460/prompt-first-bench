# N118: 下游投影2：策略模仿对 $\sigma_{strat}$ 的衰减效应：若存在平台算法驱动的模仿（自相关系数 $\rho_{lag} > 0.2$），独立噪声假设

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N38

## Claim

下游投影2：策略模仿对 $\sigma_{strat}$ 的衰减效应：若存在平台算法驱动的模仿（自相关系数 $\rho_{lag} > 0.2$），独立噪声假设失效，有效变异系数需修正为 $CV_{eff} = CV_{independent} \times \sqrt{1 - \rho_{lag}}$。若 $\rho_{lag} = 0.3$，则 $CV_{eff} \approx 0.058 \times \sqrt{0.7} \approx 0.049$。这意味着模仿行为降低了群体定价的离散度，使得 $H_{obs}$ 更容易显著高于 $H_{null}$，从而支持策略模仿假设而非纯随机噪声。

## Corrected Claim

下游投影2：策略模仿对 $\sigma_{strat}$ 的衰减效应：若存在平台算法驱动的模仿（自相关系数 $\rho_{lag} > 0.2$），独立噪声假设失效，有效变异系数需修正为 $CV_{eff} = CV_{independent} \times \sqrt{1 - \rho_{lag}}$。若 $\rho_{lag} = 0.3$，则 $CV_{eff} \approx 0.058 \times \sqrt{0.7} \approx 0.049$。这意味着模仿行为降低了群体定价的离散度，使得 $H_{obs}$ 更容易显著高于 $H_{null}$，从而支持策略模仿假设而非纯随机噪声。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 0.058 * sqrt(0.7) ≈ 0.0488 ≈ 0.049 正确；统计逻辑上，正自相关（模仿）确实会降低有效变异系数，从而在均值不变时使观测熵/离散度指标相对于独立噪声假设更易显著，推导自洽。

## Search Query

autocorrelation reduction variance pricing strategy imitation coefficient
