# N66: 下游投影 2（买家边际贡献度）：买家对均衡的边际贡献度 M_buyer 定义为 ∂ΔQ/∂P_drop * (P_drop / ΔQ)，量化为：当 P_drop

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N13

## Claim

下游投影 2（买家边际贡献度）：买家对均衡的边际贡献度 M_buyer 定义为 ∂ΔQ/∂P_drop * (P_drop / ΔQ)，量化为：当 P_drop 增加 1% 时，ΔQ 变化 -0.3%（基于 N8 的柠檬市场效应）；M_buyer 的负值且绝对值较大（> 0.5）证明买家的负面反应机制是维持均衡的关键，其低咨询率抑制了卖家降价的激励。

## Corrected Claim

下游投影 2（买家边际贡献度）：买家对均衡的边际贡献度 M_buyer 定义为 ∂ΔQ/∂P_drop * (P_drop / ΔQ)。基于 N8 的柠檬市场效应，当 P_drop 增加 1% 时，ΔQ 变化 -0.3%，即 M_buyer ≈ -0.3。该负值表明买家对价格下降存在负面反应（如质量怀疑），这种反应机制在维持均衡中起一定作用，但需进一步验证其与卖家降价激励之间的具体传导路径。

## Evidence

[质询]数值量级与逻辑推导存在矛盾：若 M_buyer = ∂ΔQ/∂P_drop * (P_drop / ΔQ) 且 P_drop 增加 1% 导致 ΔQ 变化 -0.3%，则弹性系数为 -0.3，绝对值 0.3 < 0.5，与陈述中“绝对值较大（> 0.5）”直接矛盾；此外，将“低咨询率”直接归因为“抑制卖家降价激励”缺乏微观机制支撑，属于过度推断。 | 先验知识/题面给定，逻辑校验发现内部数值矛盾（弹性计算结果与阈值描述不符）及因果链条薄弱，故降级。

## Search Query

buyer marginal contribution inquiry rate price drop lemons market effect
