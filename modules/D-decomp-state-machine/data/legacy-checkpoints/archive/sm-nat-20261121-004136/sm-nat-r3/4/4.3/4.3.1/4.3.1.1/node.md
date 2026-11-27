# N136: 修正 Hit_Rate_Original 输入值：由于 N70 指出容量约束非绑定，静态命中率 H_LRU_original 应趋近于 1 (100%)，而非 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N56

## Claim

修正 Hit_Rate_Original 输入值：由于 N70 指出容量约束非绑定，静态命中率 H_LRU_original 应趋近于 1 (100%)，而非 N56 中假设的 0.85；修正后的 Discount_Factor = 1 - P_invalid * (1 - 1.0) = 1.0，表明在理想无更新假设下无折损。

## Corrected Claim

修正 Hit_Rate_Original 输入值：由于 N70 指出容量约束非绑定，静态命中率 H_LRU_original 应趋近于 1 (100%)，而非 N56 中假设的 0.85；修正后的 Discount_Factor = 1 - P_invalid * (1 - 1.0) = 1.0，表明在理想无更新假设下无折损。

## Evidence

先验知识/题面给定，逻辑校验通过：若容量约束非绑定（N70），LRU缓存命中率理论上趋近于1，代入公式 Discount_Factor = 1 - P_invalid * (1 - 1.0) 确实等于 1.0，推导自洽。
