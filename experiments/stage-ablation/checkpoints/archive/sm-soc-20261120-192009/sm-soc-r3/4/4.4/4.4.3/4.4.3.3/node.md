# N260: 弱工具变量偏差量化：若 F-statistic 介于 5-10 之间，2SLS 估计量 β_IV 的偏差近似为 Bias(β_IV) ≈ (1 - 1/F) *

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N88

## Claim

弱工具变量偏差量化：若 F-statistic 介于 5-10 之间，2SLS 估计量 β_IV 的偏差近似为 Bias(β_IV) ≈ (1 - 1/F) * β_OLS - (1 - 1/F) * β_true，需通过 Jackknife 方法计算偏差校正后的置信区间宽度，若校正后区间仍包含 0 则结论不稳健。

## Corrected Claim

弱工具变量偏差量化：若 F-statistic 介于 5-10 之间，2SLS 估计量 β_IV 存在显著偏差。偏差近似可表示为 Bias(β_IV) ≈ (1 - 1/F) * (β_OLS - β_true)，其中 β_OLS 为 OLS 估计量的期望（即内生性下的伪真值）。由于标准误估计失效，需使用 Anderson-Rubin 区间或 Cragg-Donald 检验来评估结论的稳健性，而非简单的 Jackknife 偏差校正。

## Evidence

[质询]公式中的符号定义存在严重歧义且逻辑不自洽：通常 β_OLS 指代 OLS 估计量（随机变量），而 β_true 指代真实参数（常数）。若 β_OLS 为估计量，则 Bias(β_IV) 不应包含另一个随机变量 β_OLS 作为确定性偏差项的一部分；若 β_OLS 指代 OLS 的总体期望（即内生性下的伪真值），则公式结构虽在代数上可能成立，但表述极易误导，且未明确区分估计量与参数。此外，Jackknife 方法用于计算偏差校正置信区间并非标准做法，通常使用 Anderson-Rubin 区间或 Cragg-Donald 检验，Jackknife 更多用于稳健标准误或特定偏差估计，此处应用略显牵强。 | 先验知识/题面给定，逻辑校验未通过：公式中混淆了估计量与参数符号，且 Jackknife 用于弱工具变量偏差校正置信区间非标准主流方法，存在逻辑与术语使用错误。
