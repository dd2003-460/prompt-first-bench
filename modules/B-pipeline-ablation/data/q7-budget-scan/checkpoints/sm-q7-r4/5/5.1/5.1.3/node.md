# N119: HDD+SSD 分层聚合 IOPS 供给 = SSD 层 IOPS (100,000 × 42) + HDD 层 IOPS (200 × 40 × 并行度修正)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

HDD+SSD 分层聚合 IOPS 供给 = SSD 层 IOPS (100,000 × 42) + HDD 层 IOPS (200 × 40 × 并行度修正) ≈ 4,200,000 + 8,000 = 4,208,000 IOPS，满足 IOPS_peak 需求

## Corrected Claim

HDD+SSD 分层聚合 IOPS 供给 = SSD 层 IOPS (100,000 × 42) + HDD 层 IOPS (200 × 40 × 并行度修正) ≈ 4,200,000 + 8,000 = 4,208,000 IOPS，满足 IOPS_peak 需求

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别聚焦于公式中的三个独立组成部分：SSD层贡献、HDD层基础计算及并行度修正系数。它们互不重叠（正交），共同构成了父节点IOPS总和的完整推导逻辑（完备）。虽然HDD部分涉及参数敏感性分析，但这是针对单一组件的深度展开，而非多个子节点重复定义同一参数，因此不存在结构性冗余。）
