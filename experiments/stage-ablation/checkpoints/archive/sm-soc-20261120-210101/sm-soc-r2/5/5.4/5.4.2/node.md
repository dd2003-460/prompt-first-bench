# N101: 干预效果显著性判定：若模拟得到的成交周期T的95%置信区间[T_0.025, T_0.975]不包含0，则'能打破均衡'置信度为高；若包含0但区间宽度<20%，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

干预效果显著性判定：若模拟得到的成交周期T的95%置信区间[T_0.025, T_0.975]不包含0，则'能打破均衡'置信度为高；若包含0但区间宽度<20%，置信度为中；若区间宽度>20%且包含0，置信度为低

## Corrected Claim

干预效果显著性判定：若模拟得到的成交周期T的95%置信区间[T_0.025, T_0.975]不包含0，则'能打破均衡'置信度为高；若包含0但区间宽度<20%，置信度为中；若区间宽度>20%且包含0，置信度为低

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

confidence interval zero inclusion effect size significance judgment
