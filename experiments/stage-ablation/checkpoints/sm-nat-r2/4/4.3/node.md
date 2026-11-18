# N18: 有效命中率 $H_{eff} = H_{LRU} \times (1 - R_{inv} \cdot \frac{C_{miss}}{C_{total}})$，

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

有效命中率 $H_{eff} = H_{LRU} \times (1 - R_{inv} \cdot \frac{C_{miss}}{C_{total}})$，其中 $C_{miss}$ 为因更新而导致的额外未命中成本占比，通常简化为 $H_{eff} \approx H_{LRU} \times (1 - R_{inv})$ 当更新均匀分布时。

## Corrected Claim

有效命中率 $H_{eff} = H_{LRU} \times (1 - R_{inv} \cdot \frac{C_{miss}}{C_{total}})$，其中 $C_{miss}$ 为因更新而导致的额外未命中成本占比，通常简化为 $H_{eff} \approx H_{LRU} \times (1 - R_{inv})$ 当更新均匀分布时。

## Evidence

父节点级核验未通过：不完备（子节点分别讨论了分布影响（非均匀性）和物理机制（边界条件），两者正交。但父节点核心是 H_eff 公式，子节点仅深入探讨了 C_miss/C_total 这一项，完全遗漏了 R_inv（失效率/更新率）和 H_LRU 的定义或计算逻辑，导致对父节点公式的分解不完备。）

## Search Query

cache hit rate reduction due to object updates uniform distribution
