# N119: 市场匹配速度常数 k 的估计公式：k = ΔT_observed / [(P_markup - P_market) * C_signal * ln(P_will

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N38

## Claim

市场匹配速度常数 k 的估计公式：k = ΔT_observed / [(P_markup - P_market) * C_signal * ln(P_willing_high)]，需基于至少 100 个成交样本计算，且 k 的 95% 置信区间需通过 Bootstrap 重抽样（B=1000）获得，标准误 SE_k = std(bootstrap_samples)。

## Corrected Claim

在特定市场匹配模型中，速度常数 k 可通过公式 k = ΔT_observed / [(P_markup - P_market) * C_signal * ln(P_willing_high)] 进行估计，建议基于至少 100 个成交样本计算，并通过 Bootstrap 重抽样（B=1000）获得 95% 置信区间，标准误 SE_k = std(bootstrap_samples)。

## Evidence

[质询]该公式缺乏明确的经济学或统计学理论推导支持，分母中各项（如 P_markup, C_signal, ln(P_willing_high)）的量纲与物理意义不明确，且将市场匹配速度常数 k 定义为观测时间差与价格/信号项的商，属于高度特定的经验模型假设，无法从第一性原理推出，存在将特定场景拟合公式泛化为通用定义的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该公式非通用公理，属特定模型参数估计方法）

## Search Query

market matching speed constant estimation bootstrap confidence interval second hand goods
