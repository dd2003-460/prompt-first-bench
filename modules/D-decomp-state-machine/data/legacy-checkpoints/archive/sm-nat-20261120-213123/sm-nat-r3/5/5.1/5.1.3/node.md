# N61: 工作点 3（高成本低性）：大对象主导场景，T_resident ≈ 100 天，P_invalidate = 1 - e^(-100/100) ≈ 63.2%，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

工作点 3（高成本低性）：大对象主导场景，T_resident ≈ 100 天，P_invalidate = 1 - e^(-100/100) ≈ 63.2%，字节命中率折损 ΔH ≈ 63.2% * (S_hot/S_total ≈ 0.8) ≈ 50.6%。

## Corrected Claim

工作点 3（高成本低性）：大对象主导场景，T_resident ≈ 100 天，P_invalidate = 1 - e^(-100/100) ≈ 63.2%，字节命中率折损 ΔH ≈ 63.2% * (S_hot/S_total ≈ 0.8) ≈ 50.6%。

## Evidence

父节点级核验通过：正交+完备+无冗余（两个子节点分别针对父节点公式中的两个独立变量进行修正：子节点1修正失效概率 P_invalidate（基于更新率分布），子节点2修正热度占比 S_hot/S_total（基于Pareto分布积分）。两者在逻辑上相互独立，分别对应公式 ΔH ≈ P_invalidate * (S_hot/S_total) 中的两个因子，因此正交且完备，不存在冗余。）

## Search Query

LRU large object resident time invalidation probability byte hit rate loss
