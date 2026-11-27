# N139: 最低补贴率 r_min 的敏感性分析：当 P_initial - P_equilibrium 的差值扩大时，r_min 线性增加。若溢价从 15% 升至 25%

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

最低补贴率 r_min 的敏感性分析：当 P_initial - P_equilibrium 的差值扩大时，r_min 线性增加。若溢价从 15% 升至 25%，r_min 从 0.15 升至 0.25。需验证平台预算约束下，r_min > 0.2 时补贴成本是否超过短期 GMV 损失，从而判断干预的财务可行性。

## Corrected Claim

最低补贴率 r_min 的敏感性分析：当 P_initial - P_equilibrium 的差值扩大时，r_min 线性增加。若溢价从 15% 升至 25%，r_min 从 0.15 升至 0.25。需验证平台预算约束下，r_min > 0.2 时补贴成本是否超过短期 GMV 损失，从而判断干预的财务可行性。

## Evidence

先验知识/题面给定，逻辑校验通过：在简单的线性补贴模型中，若补贴率 r 与溢价比例 (P_initial - P_equilibrium)/P_equilibrium 成正比且系数为1，则 r_min 随溢价线性增加是数学自洽的；财务可行性判断属于定性逻辑推导，无硬逻辑错误。
