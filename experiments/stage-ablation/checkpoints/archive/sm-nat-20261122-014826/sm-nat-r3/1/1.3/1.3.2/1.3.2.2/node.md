# N84: 非线性修正项的推导：引入二次项或分位数回归修正，计算修正后的条件均值 E[Size|Top-1%]_corrected = E[Size] * (1 + ρ *

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N31

## Claim

非线性修正项的推导：引入二次项或分位数回归修正，计算修正后的条件均值 E[Size|Top-1%]_corrected = E[Size] * (1 + ρ * z_heat * (σ_size/σ_heat) + k * (z_heat^2 - 1))，其中 k 为拟合系数。

## Corrected Claim

在特定非线性修正模型假设下，引入二次项或分位数回归修正，修正后的条件均值可表示为 E[Size|Top-1%]_corrected = E[Size] * (1 + ρ * z_heat * (σ_size/σ_heat) + k * (z_heat^2 - 1))，其中 k 为拟合系数。

## Evidence

[质询]该公式将条件均值表示为全局均值乘以包含线性项和二次项的修正因子，这在数学上隐含了修正项与基础均值成比例的关系，且未明确说明 z_heat 和 σ 的具体定义及 k 的拟合背景，属于特定模型假设下的经验公式，缺乏通用理论推导支持。 | 经验事实/特定模型公式，逻辑自洽但缺来源支持

## Search Query

nonlinear correction conditional mean skewed distribution regression
