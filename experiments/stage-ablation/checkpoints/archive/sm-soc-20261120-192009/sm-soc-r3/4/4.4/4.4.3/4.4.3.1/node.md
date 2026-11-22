# N258: 工具变量相关性检验统计量：计算 F-statistic = (Cov(Push_t, Price_High)^2 / Var(Push_t)) / Var(Pr

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N88

## Claim

工具变量相关性检验统计量：计算 F-statistic = (Cov(Push_t, Price_High)^2 / Var(Push_t)) / Var(Price_High | Push_t)，若 F < 10 则判定为弱工具变量，此时需采用 Lim-Hansen 检验替代 Wald 检验以避免过度拒绝问题。

## Corrected Claim

工具变量相关性检验中，若第一阶段F统计量小于10，通常判定为弱工具变量。此时，标准的Wald检验可能失效（过度拒绝），建议采用对弱工具变量稳健的检验方法，如Anderson-Rubin检验或Kleibergen-Paap检验；Lim-Hansen检验也可用于处理内生性导致的过度拒绝问题，但需根据具体模型设定选择。

## Evidence

[质询]公式表述存在量纲与逻辑瑕疵：标准的第一阶段F统计量通常定义为 $F = \frac{\hat{\pi}^2}{\text{Var}(\hat{\pi})}$ 或基于回归系数的t统计量平方，而非陈述中复杂的协方差/方差比值形式（该形式在数学上可能等价于 $R^2$ 相关的统计量，但表述易引起歧义）；此外，Lim-Hansen检验主要用于处理内生性导致的过度拒绝，但通常是在工具变量有效（非弱）或特定条件下使用，若F<10判定为弱工具变量，标准做法是报告弱工具变量稳健性检验（如Anderson-Rubin, Kleibergen-Paap），直接替换为Lim-Hansen检验的表述不够严谨，因为Lim-Hansen检验本身对弱工具变量也有特定的渐近性质要求。 | 先验知识/题面给定，逻辑校验通过。虽然F<10是弱工具变量的经典经验法则（Stock & Yogo），且Lim-Hansen检验确实用于解决过度拒绝问题，但陈述中的F统计量公式非标准教科书形式，且弱工具变量下的检验替代方案表述略显绝对（通常需结合具体模型设定），故降级为定性表述。
