# N296: 单POP人力成本 C_eng_pop = N_eng_pop * C_eng * (1 + Overtime_Factor)，其中 C_eng = ¥40,00

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N97

## Claim

单POP人力成本 C_eng_pop = N_eng_pop * C_eng * (1 + Overtime_Factor)，其中 C_eng = ¥40,000/月，Overtime_Factor 为加班/值班补贴系数（10%-20%），计算得 C_eng_pop ≈ ¥20,000-22,000/月/POP。

## Corrected Claim

若 C_eng = ¥40,000/月 且 N_eng_pop = 1，则 C_eng_pop 应约为 ¥44,000-48,000/月/POP；若目标成本为 ¥20,000-22,000/月/POP，则需 N_eng_pop ≈ 0.5 或 C_eng ≈ ¥20,000/月。

## Evidence

[质询]数值量级与公式逻辑存在严重矛盾：若 C_eng 为 ¥40,000/月，且 N_eng_pop 为整数（通常至少为1），则基础成本至少为 ¥40,000，乘以 (1+10%~20%) 后结果应在 ¥44,000-48,000 之间，不可能得出 ¥20,000-22,000 的结论。除非 N_eng_pop 小于 0.5（即半个工程师），但这在常规人力成本模型中不符合常理，或者 C_eng 的定义并非单人月薪而是其他口径（如日均成本误标为月均，或 N_eng_pop 代表的是某种分摊系数而非人数）。 | 逻辑校验失败：公式 C_eng_pop = N_eng_pop * C_eng * (1 + Overtime_Factor) 中，若 C_eng=40000，即使 N_eng_pop=1，结果也远大于 22000。数值推导与给定参数不符，存在内部矛盾。
