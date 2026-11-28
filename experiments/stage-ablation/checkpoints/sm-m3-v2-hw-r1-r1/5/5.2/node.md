# N32: 逻辑一致性检查：使用形式化验证器（如 Z3 SMT Solver）将论证步骤转化为逻辑命题，检查推导链中是否存在矛盾（Contradiction Detecti

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

逻辑一致性检查：使用形式化验证器（如 Z3 SMT Solver）将论证步骤转化为逻辑命题，检查推导链中是否存在矛盾（Contradiction Detection），计算一致性得分 Consistency = Valid Steps / Total Steps，要求 ≥ 0.98；平均每篇论文含 20±5 个逻辑步骤

## Corrected Claim

逻辑一致性检查：使用形式化验证器（如 Z3 SMT Solver）将论证步骤转化为逻辑命题，检查推导链中是否存在矛盾（Contradiction Detection），计算一致性得分 Consistency = Valid Steps / Total Steps，要求 ≥ 0.98；平均每篇论文含 20±5 个逻辑步骤

## Evidence

先验知识/题面给定，逻辑校验通过：Z3 SMT Solver 是标准的逻辑一致性验证工具，Consistency 公式定义清晰且量纲合理（比率），20±5 步/篇符合学术论文论证密度的经验量级，无内部矛盾。

## Search Query

logical consistency check SMT solver argument validation research papers
