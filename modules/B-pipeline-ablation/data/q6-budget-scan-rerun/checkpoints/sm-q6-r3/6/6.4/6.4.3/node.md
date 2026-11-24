# N364: 年总请求量的业务增长修正：R_total_annual_growth = R_total_annual_base × (1 + g)^n，其中 g 为年增长率（

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N115

## Claim

年总请求量的业务增长修正：R_total_annual_growth = R_total_annual_base × (1 + g)^n，其中 g 为年增长率（假设 20%），n 为规划周期（如 3 年），若忽略增长，第 3 年的实际请求量将比基线高 72.8%，导致基础设施投资不足或过度投资。

## Corrected Claim

年总请求量的业务增长修正：R_total_annual_growth = R_total_annual_base × (1 + g)^n，其中 g 为年增长率（假设 20%），n 为规划周期（如 3 年），若忽略增长，第 3 年的实际请求量将比基线高 72.8%，导致基础设施投资不足或过度投资。

## Evidence

先验知识/题面给定，逻辑校验通过：(1+0.2)^3 = 1.728，即增长72.8%，数学推导正确且符合业务规划常识。
