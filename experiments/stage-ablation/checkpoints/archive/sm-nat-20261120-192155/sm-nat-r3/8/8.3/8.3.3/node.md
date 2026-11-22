# N133: 工作点3（字节加权/负相关耦合）：有效命中率折扣的字节加权项 D_loss = Σ_{i=1}^k (p_evict_i * r_i * s_i) / Σ_{i

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N49

## Claim

工作点3（字节加权/负相关耦合）：有效命中率折扣的字节加权项 D_loss = Σ_{i=1}^k (p_evict_i * r_i * s_i) / Σ_{i=1}^k (r_i * s_i)。由于 s_i ∝ i^{-1.1} 且 r_i ∝ i^{-0.9}，r_i s_i ∝ i^{-2.0}，头部对象字节流量占比极高（>98%）。尽管中尾部 p_evict 高，但其 r_i s_i 权重极低，导致整体折扣 D ≈ 1 - O(10^{-6})，即折扣极小。

## Corrected Claim

工作点3（字节加权/负相关耦合）：有效命中率折扣的字节加权项 D_loss = Σ_{i=1}^k (p_evict_i * r_i * s_i) / Σ_{i=1}^k (r_i * s_i)。由于 s_i ∝ i^{-1.1} 且 r_i ∝ i^{-0.9}，r_i s_i ∝ i^{-2.0}，头部对象字节流量占比极高（>98%）。尽管中尾部 p_evict 高，但其 r_i s_i 权重极低，导致整体折扣 D ≈ 1 - O(10^{-6})，即折扣极小。

## Evidence

先验知识/题面给定，逻辑校验通过：基于幂律分布 i^{-2.0} 的收敛性，头部权重占比极高，尾部贡献可忽略，推导出的 D ≈ 1 - O(10^{-6}) 在量级和逻辑上自洽。
