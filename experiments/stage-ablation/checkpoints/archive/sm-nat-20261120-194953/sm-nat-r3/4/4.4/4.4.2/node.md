# N60: 整体命中率折损的精确值为 P_inval_hot * S_hot + P_inval_cold * W_cold ≈ 0.01 * 0.28 + 1 * 0.0

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19

## Claim

整体命中率折损的精确值为 P_inval_hot * S_hot + P_inval_cold * W_cold ≈ 0.01 * 0.28 + 1 * 0.04 = 0.0428，即 4.28 个百分点，主要由冷对象失效主导，而非热门对象。

## Corrected Claim

整体命中率折损的精确值为 P_inval_hot * S_hot + P_inval_cold * W_cold ≈ 0.01 * 0.28 + 1 * 0.04 = 0.0428，即 4.28 个百分点，主要由冷对象失效主导，而非热门对象。

## Evidence

父节点级核验未通过：非正交, 不完备（子节点1和子节点2存在逻辑重叠且相互矛盾。子节点1通过修正概率值（P_inval_cold < 0.05）直接推翻结论；子节点2通过边界条件分析（K_cap >> 10^5）也得出相同结论。两者都在论证'冷对象失效并非主导'，属于同一论据的不同表达，违反了正交性。此外，父节点的核心是'精确值计算'，但子节点主要聚焦于'定性结论的修正'，未覆盖父节点中'热门对象项'的验证或整体公式的重新推导，完备性不足。）
