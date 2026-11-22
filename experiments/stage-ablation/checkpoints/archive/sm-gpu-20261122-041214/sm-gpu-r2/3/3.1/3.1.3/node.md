# N102: CapEx 计算公式修正：多卡方案 CapEx = N * P_GPU + C_infra，其中 C_infra 包含主板、电源、机箱及潜在互联组件；单卡方案 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27

## Claim

CapEx 计算公式修正：多卡方案 CapEx = N * P_GPU + C_infra，其中 C_infra 包含主板、电源、机箱及潜在互联组件；单卡方案 CapEx = P_GPU + C_infra_min（通常 C_infra_min ≈ $0 若复用现有工作站，或 $200 若需新购基础外设）

## Corrected Claim

CapEx 计算公式修正：多卡方案 CapEx = N * P_GPU + C_infra，其中 C_infra 包含主板、电源、机箱及潜在互联组件；单卡方案 CapEx = P_GPU + C_infra_min（通常 C_infra_min ≈ $0 若复用现有工作站，或 $200 若需新购基础外设）

## Evidence

先验知识/题面给定，逻辑校验通过
