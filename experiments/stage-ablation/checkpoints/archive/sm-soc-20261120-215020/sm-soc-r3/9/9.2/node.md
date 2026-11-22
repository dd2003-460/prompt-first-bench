# N235: 成交概率在容忍阈值处的连续性检验：当 $\delta = \tau_{tolerance} = 2b$ 时，验证基准成交概率 $p_0$ 与指数衰减函数 $Pr

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

成交概率在容忍阈值处的连续性检验：当 $\delta = \tau_{tolerance} = 2b$ 时，验证基准成交概率 $p_0$ 与指数衰减函数 $Pr(Sale) = p_0 \times e^{-k(\delta - 2b)}$ 在 $\delta = 2b$ 处是否连续（即 $Pr(Sale) = p_0$）。若存在跳变，需引入平滑函数（如 Sigmoid）并量化跳变幅度对整体成交率的影响。

## Corrected Claim

成交概率在容忍阈值处的连续性检验：当 $\delta = \tau_{tolerance} = 2b$ 时，验证基准成交概率 $p_0$ 与指数衰减函数 $Pr(Sale) = p_0 \times e^{-k(\delta - 2b)}$ 在 $\delta = 2b$ 处是否连续（即 $Pr(Sale) = p_0$）。若存在跳变，需引入平滑函数（如 Sigmoid）并量化跳变幅度对整体成交率的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：指数函数 e^0=1，代入 δ=2b 时 Pr(Sale)=p0，数学上严格连续，无跳变。
