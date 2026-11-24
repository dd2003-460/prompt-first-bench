# N411: 技术债务利息的精确公式：C_debt_annual = FTE_required × (salary_base + benefits_multiplier) ×

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N131

## Claim

技术债务利息的精确公式：C_debt_annual = FTE_required × (salary_base + benefits_multiplier) × (1 + inflation_rate)^t，其中 FTE_required 为每年需投入的重构/优化人力（需基于代码复杂度指标如圈复杂度、技术栈更新频率量化），salary_base 为年薪，benefits_multiplier 为福利系数（通常1.3-1.5），inflation_rate 为年均薪资通胀率（中国IT行业约5-8%/年），t 为年数

## Corrected Claim

技术债务利息的精确公式：C_debt_annual = FTE_required × (salary_base + benefits_multiplier) × (1 + inflation_rate)^t，其中 FTE_required 为每年需投入的重构/优化人力（需基于代码复杂度指标如圈复杂度、技术栈更新频率量化），salary_base 为年薪，benefits_multiplier 为福利系数（通常1.3-1.5），inflation_rate 为年均薪资通胀率（中国IT行业约5-8%/年），t 为年数

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

technical debt annual interest cost FTE calculation software maintenance
