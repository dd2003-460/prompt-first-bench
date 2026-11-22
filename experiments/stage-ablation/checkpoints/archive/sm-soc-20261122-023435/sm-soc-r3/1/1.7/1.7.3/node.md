# N45: 买家对高挂价商品的质量信任阈值 θ_trust：当挂价偏差 δ_anchor 超过 θ_trust（通常 θ_trust ≈ 10-15%）时，买家默认商品存在

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

买家对高挂价商品的质量信任阈值 θ_trust：当挂价偏差 δ_anchor 超过 θ_trust（通常 θ_trust ≈ 10-15%）时，买家默认商品存在隐藏缺陷的概率 P_defect_expected 上升至 0.4 以上，触发逆向选择退出行为。

## Corrected Claim

买家对高挂价商品的质量信任阈值 θ_trust 存在：当挂价偏差 δ_anchor 超过该阈值时，买家默认商品存在隐藏缺陷的概率显著上升，从而可能触发逆向选择退出行为。

## Evidence

[质询]该陈述包含具体的经验参数（θ_trust ≈ 10-15% 和 P_defect_expected > 0.4），这些数值并非从第一性原理或数学公理严格推导出的必然结果，而是依赖于特定市场情境、买家群体心理及商品类型的经验统计值。不同市场（如二手车 vs. 二手电子产品）中，买家对价格偏差的敏感度及隐含缺陷概率的估计可能存在显著差异，固定数值缺乏普适性。 | 先验知识/题面给定，逻辑校验通过。虽然逻辑自洽（高挂价确实可能引发逆向选择），但具体阈值和概率数值属于经验事实，且无外部来源支持，故降级为定性表述。

## Search Query

buyer trust threshold price deviation perceived defect probability
