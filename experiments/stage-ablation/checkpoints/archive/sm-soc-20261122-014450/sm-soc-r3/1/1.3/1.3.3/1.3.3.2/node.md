# N160: 成交周期 T 与匹配概率 P(Match) 的非线性关系修正：T = T_base / (P(Match) * (1 + ε_density))，其中 ε_de

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

成交周期 T 与匹配概率 P(Match) 的非线性关系修正：T = T_base / (P(Match) * (1 + ε_density))，其中 ε_density 为需求密度修正项（如 0.2），表示高匹配概率还带来了额外的搜索效率提升；需计算 ε_density 对 T 缩短幅度的贡献占比。

## Corrected Claim

成交周期 T 与匹配概率 P(Match) 的非线性关系修正：T = T_base / (P(Match) * (1 + ε_density))，其中 ε_density 为需求密度修正项（如 0.2），表示高匹配概率还带来了额外的搜索效率提升；需计算 ε_density 对 T 缩短幅度的贡献占比。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

non-linear relationship between matching probability and transaction time
