# N47: 前 K 个对象的热度累积占比 F_top = Σ_{i=1}^K h_i / Σ_{i=1}^N h_i，在 Pareto(β=0.9) 分布下，F_top ≈

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

前 K 个对象的热度累积占比 F_top = Σ_{i=1}^K h_i / Σ_{i=1}^N h_i，在 Pareto(β=0.9) 分布下，F_top ≈ 1 - (K/N)^(1-β) = 1 - (K/N)^0.1

## Corrected Claim

前 K 个对象的热度累积占比 F_top = Σ_{i=1}^K h_i / Σ_{i=1}^N h_i，在 Pareto(β=0.9) 分布下，F_top ≈ 1 - (K/N)^(1-β) = 1 - (K/N)^0.1

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点仅是公式 F_top = 1 - (K/N)^0.1 在不同 K/N 比值下的数值实例化，属于同一维度的参数扫描，而非对父节点概念（如分布特性、边界条件、物理意义）的结构性分解。虽然计算互不重叠（正交），但存在严重冗余，且未涵盖该公式的推导前提、适用范围或与其他分布的对比等关键方面（不完备）。）
