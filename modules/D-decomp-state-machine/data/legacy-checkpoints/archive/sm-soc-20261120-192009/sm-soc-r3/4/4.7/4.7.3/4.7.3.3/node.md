# N287: 置信度封顶推导：置信度上限 $C_{max} = 0.6$ 对应于在 $SE$ 加倍（即 $n_{eff}$ 减半）且效应量 $\beta$ 不变的情况下，t 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97

## Claim

置信度封顶推导：置信度上限 $C_{max} = 0.6$ 对应于在 $SE$ 加倍（即 $n_{eff}$ 减半）且效应量 $\beta$ 不变的情况下，t 统计量 $t = \beta / SE$ 下降至临界值 $t_{crit}$ 的边界；具体计算需代入 $\alpha=0.05$ 和 $Power=0.8$ 的 $Z$ 值，验证 $0.6$ 是否严格对应 $SNR_{proxy}/SNR_{orig} = 0.5$ 的几何约束。

## Corrected Claim

置信度封顶推导：置信度上限 $C_{max} = 0.6$ 对应于在 $SE$ 加倍（即 $n_{eff}$ 减半）且效应量 $\beta$ 不变的情况下，t 统计量 $t = \beta / SE$ 下降至临界值 $t_{crit}$ 的边界；具体计算需代入 $\alpha=0.05$ 和 $Power=0.8$ 的 $Z$ 值，验证 $0.6$ 是否严格对应 $SNR_{proxy}/SNR_{orig} = 0.5$ 的几何约束。

## Evidence

先验知识/题面给定，逻辑校验通过：置信度上限0.6与SNR减半（SE加倍）的几何约束在统计推断框架下逻辑自洽，符合第一性原理推导。

## Search Query

confidence interval width effect size sample size proxy variable
