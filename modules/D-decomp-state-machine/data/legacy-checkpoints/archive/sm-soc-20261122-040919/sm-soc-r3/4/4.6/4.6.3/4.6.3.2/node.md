# N327: 混杂变量控制：若 r > 0.7，需引入需求激增指标（如搜索量 ΔS）作为控制变量，计算偏相关系数 r_partial = (r_pk - r_pS * r_k

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

混杂变量控制：若 r > 0.7，需引入需求激增指标（如搜索量 ΔS）作为控制变量，计算偏相关系数 r_partial = (r_pk - r_pS * r_kS) / sqrt((1-r_pS^2)(1-r_kS^2))；若 r_partial < 0.3，则混杂效应显著。

## Corrected Claim

混杂变量控制：若 r > 0.7，需引入需求激增指标（如搜索量 ΔS）作为控制变量，计算偏相关系数 r_partial = (r_pk - r_pS * r_kS) / sqrt((1-r_pS^2)(1-r_kS^2))；若 r_partial < 0.3，则混杂效应显著。

## Evidence

先验知识/题面给定，逻辑校验通过：偏相关系数公式正确，阈值设定符合统计学常规经验。

## Search Query

partial correlation coefficient formula controlling for confounding variable
