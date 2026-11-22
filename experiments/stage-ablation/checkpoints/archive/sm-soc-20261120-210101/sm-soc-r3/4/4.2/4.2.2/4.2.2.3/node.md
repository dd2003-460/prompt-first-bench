# N280: T_save 的界面复杂度修正项：若干预措施导致搜索界面增加步骤（如增加筛选器），则实际 T_save_net = T_save_gross - T_extra

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N77

## Claim

T_save 的界面复杂度修正项：若干预措施导致搜索界面增加步骤（如增加筛选器），则实际 T_save_net = T_save_gross - T_extra_interface。假设 T_extra_interface = 3分钟/次（基于UI/UX测试标准），则净增益需扣除此值；若 T_save_gross < 3分钟，则干预导致福利负增长。

## Corrected Claim

T_save 的界面复杂度修正项：若干预措施导致搜索界面增加步骤（如增加筛选器），则实际 T_save_net = T_save_gross - T_extra_interface。假设 T_extra_interface = 3分钟/次（基于UI/UX测试标准），则净增益需扣除此值；若 T_save_gross < 3分钟，则干预导致福利负增长。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

ui complexity impact on search efficiency time cost
