# N47: 前 K 个对象的热度累积占比 F_top = Σ_{i=1}^K h_i / Σ_{i=1}^N h_i，在 Pareto(β=0.9) 分布下，F_top ≈

- **status**: verified
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

先验知识/题面给定，逻辑校验通过
