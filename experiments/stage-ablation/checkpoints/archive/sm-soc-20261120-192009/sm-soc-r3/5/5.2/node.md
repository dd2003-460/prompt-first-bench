# N101: 年化持有成本率 r_holding 的具体构成包括资金机会成本（无风险利率 r_f）、仓储/物流成本（C_storage）及折旧损耗（Depreciation）

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

年化持有成本率 r_holding 的具体构成包括资金机会成本（无风险利率 r_f）、仓储/物流成本（C_storage）及折旧损耗（Depreciation）；r_holding = r_f + (C_storage + Depreciation) / Value，不同品类的 C_storage 差异导致 k_evolve 阈值不同。

## Corrected Claim

年化持有成本率 r_holding 的具体构成包括资金机会成本（无风险利率 r_f）、仓储/物流成本（C_storage）及折旧损耗（Depreciation）；r_holding = r_f + (C_storage + Depreciation) / Value，不同品类的 C_storage 差异导致 k_evolve 阈值不同。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的 r_f、C_storage、Depreciation 三个独立分量，以及整体公式的边界条件（失效场景）。各子节点在概念维度上互斥（资金成本 vs 物理成本 vs 时间价值衰减 vs 逻辑边界），无内容重叠或矛盾，且完整覆盖了父节点定义的所有构成要素及特殊情形。）
