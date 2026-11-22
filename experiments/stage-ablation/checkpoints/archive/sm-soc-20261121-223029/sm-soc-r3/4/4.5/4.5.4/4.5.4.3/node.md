# N276: 在'低搜索深度/高依赖推荐'工作点（D_search < 0.5次/天，即'刷单式'浏览），买家几乎不进行主动筛选，直接点击推荐位商品，f(D_search) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N92

## Claim

在'低搜索深度/高依赖推荐'工作点（D_search < 0.5次/天，即'刷单式'浏览），买家几乎不进行主动筛选，直接点击推荐位商品，f(D_search) ≈ 0.9，导致 P(Encounter_Low) 接近商品池实际占比 Share_low，体验风险最大化，极易触发用户流失。

## Corrected Claim

在'低搜索深度/高依赖推荐'工作点（D_search < 0.5次/天，即'刷单式'浏览），买家几乎不进行主动筛选，直接点击推荐位商品，f(D_search) ≈ 0.9，导致 P(Encounter_Low) 接近商品池实际占比 Share_low，体验风险最大化，极易触发用户流失。

## Evidence

先验知识/题面给定，逻辑校验通过：在低搜索深度（D_search < 0.5）且高依赖推荐的场景下，用户主动筛选行为极少，点击概率 f(D_search) 趋近于 1（此处取 0.9 为合理近似），因此遭遇低质商品的概率 P(Encounter_Low) 确实趋近于商品池中的实际占比 Share_low，符合概率论基本逻辑。
