# N50: 算法偏差的激励机制：平台算法优化目标函数 J = α * GMV + β * User_Retention + γ * Ad_Revenue，若 γ (广告收入

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

算法偏差的激励机制：平台算法优化目标函数 J = α * GMV + β * User_Retention + γ * Ad_Revenue，若 γ (广告收入权重) > 0.5 且高价商品广告单价更高，则算法倾向于展示高价商品，导致 B_algo 上升，需量化 γ 的具体数值 [待核验]。

## Corrected Claim

平台算法通常以最大化综合收益为目标，若广告收入在目标函数中占据较高权重，且高价商品具有更高的广告变现效率（eCPM），算法倾向于展示高价商品，从而导致算法偏差（B_algo）上升。具体权重数值因平台而异，需通过逆向工程或内部数据量化。

## Evidence

[质询]该陈述将复杂的平台算法优化目标简化为线性加权求和（J = α*GMV + β*Retention + γ*AdRev），并设定具体的阈值（γ > 0.5）作为因果触发条件，这属于对黑盒算法机制的过度简化假设，缺乏普遍适用的理论或实证支持；不同平台的目标函数结构、权重动态调整机制及广告竞价逻辑差异巨大，无法一概而论。 | 先验知识/题面给定，逻辑校验通过（在假设线性加权模型成立的前提下，高广告权重确实会引导流量向高eCPM商品倾斜，逻辑自洽），但具体阈值0.5及线性模型假设缺乏通用性，故降级为定性表述。

## Search Query

e-commerce platform algorithm objective function ad revenue weight
