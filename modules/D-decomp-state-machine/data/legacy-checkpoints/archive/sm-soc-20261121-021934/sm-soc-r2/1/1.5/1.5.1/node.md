# N35: 卖家剩余 PS_seller 的感知偏差 ΔPS = PS_perceived - PS_actual 定义为卖家基于 V_true_perceived 计算的

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

卖家剩余 PS_seller 的感知偏差 ΔPS = PS_perceived - PS_actual 定义为卖家基于 V_true_perceived 计算的剩余减去基于 V_true_actual 计算的剩余；由于损失厌恶系数 λ ≈ 2.25，卖家高估 V_true 的比例约为 λ * (V_true - P_market) / P_market，导致 ΔPS > 0，具体数值需通过卖家心理定价调查量化。

## Corrected Claim

卖家剩余 PS_seller 的感知偏差 ΔPS = PS_perceived - PS_actual 定义为卖家基于 V_true_perceived 计算的剩余减去基于 V_true_actual 计算的剩余；由于损失厌恶效应（通常 λ ≈ 2.25），卖家倾向于高估 V_true，导致 ΔPS > 0，具体数值需通过卖家心理定价调查量化。

## Evidence

[质询]陈述中关于高估比例的公式 `λ * (V_true - P_market) / P_market` 缺乏严谨的理论推导支持，且将损失厌恶系数 λ 直接线性映射到价值高估比例在行为经济学中并非标准结论，存在逻辑跳跃和量纲/定义混淆的风险。 | 先验知识/题面给定，逻辑校验通过（定义自洽，但具体量化公式缺乏标准理论支撑，故降级为定性表述）

## Search Query

seller surplus perception bias loss aversion overvaluation secondhand goods
