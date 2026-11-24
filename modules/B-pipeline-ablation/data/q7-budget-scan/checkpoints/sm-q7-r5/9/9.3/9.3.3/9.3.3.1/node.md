# N682: SSD缓存层总功耗P_SSD的敏感性分析：基于N303和N304修正后的W_SSD_avg（假设Active=11W, Idle=1.2W, 50%负载则W_a

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N283

## Claim

SSD缓存层总功耗P_SSD的敏感性分析：基于N303和N304修正后的W_SSD_avg（假设Active=11W, Idle=1.2W, 50%负载则W_avg=6.1W），若盘数为55块（1.92TB方案），P_SSD = 55 * 6.1W = 335.5W；若盘数为14块（7.68TB方案），P_SSD = 14 * 6.1W = 85.4W，两者差异巨大，需依据N301确定的规格选取对应值 [待核验]

## Corrected Claim

SSD缓存层总功耗P_SSD的敏感性分析：基于N303和N304修正后的W_SSD_avg（假设Active=11W, Idle=1.2W, 50%负载则W_avg=6.1W），若盘数为55块（1.92TB方案），P_SSD = 55 * 6.1W = 335.5W；若盘数为14块（7.68TB方案），P_SSD = 14 * 6.1W = 85.4W，两者差异巨大，需依据N301确定的规格选取对应值 [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（55*6.1=335.5, 14*6.1=85.4），功耗模型符合SSD典型能耗量级，内部逻辑自洽。
