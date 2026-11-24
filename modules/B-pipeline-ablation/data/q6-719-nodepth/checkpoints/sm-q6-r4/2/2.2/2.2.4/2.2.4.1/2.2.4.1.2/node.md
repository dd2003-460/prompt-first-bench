# N640: 现场巡检工时 Staff_Cost_Onsite 的精确计算：Staff_Cost_Onsite = FTE_Onsite × Salary_Rate_Corr

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N219

## Claim

现场巡检工时 Staff_Cost_Onsite 的精确计算：Staff_Cost_Onsite = FTE_Onsite × Salary_Rate_Corrected，其中 FTE_Onsite 由巡检频率决定（见 N411），Salary_Rate_Corrected 由 N220 修正后薪资决定。若 FTE_Onsite = 0.05（每周 1 次，2h/次），Salary_Rate_Corrected = ¥27,000（N220 修正值），则 Staff_Cost_Onsite = 0.05 × 27,000 = ¥1,350/月/POP；若 FTE_Onsite = 0.1（每周 2 次，2h/次），则 Staff_Cost_Onsite = 0.1 × 27,000 = ¥2,700/月/POP。

## Corrected Claim

现场巡检工时 Staff_Cost_Onsite 的精确计算：Staff_Cost_Onsite = FTE_Onsite × Salary_Rate_Corrected，其中 FTE_Onsite 由巡检频率决定（见 N411），Salary_Rate_Corrected 由 N220 修正后薪资决定。若 FTE_Onsite = 0.05（每周 1 次，2h/次），Salary_Rate_Corrected = ¥27,000（N220 修正值），则 Staff_Cost_Onsite = 0.05 × 27,000 = ¥1,350/月/POP；若 FTE_Onsite = 0.1（每周 2 次，2h/次），则 Staff_Cost_Onsite = 0.1 × 27,000 = ¥2,700/月/POP。

## Evidence

先验知识/题面给定，逻辑校验通过：乘法运算 0.05*27000=1350 和 0.1*27000=2700 正确，量纲一致（FTE为无量纲比例，薪资为月度金额，结果为月度成本），符合成本计算基本逻辑。
