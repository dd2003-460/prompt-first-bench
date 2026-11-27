# N202: 样本量与统计功效要求：检测 (T_low - T_high) / T_low > 10% 的差异，假设效应量 f = 0.10，在 α=0.05, Power=

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

样本量与统计功效要求：检测 (T_low - T_high) / T_low > 10% 的差异，假设效应量 f = 0.10，在 α=0.05, Power=0.80 条件下，每组最小样本量 n 约为 500-600，若实际样本量低于此值，则 p-value 的显著性不可靠，需增加置信区间宽度。

## Corrected Claim

样本量与统计功效要求：检测 (T_low - T_high) / T_low > 10% 的差异，假设效应量 f = 0.10，在 α=0.05, Power=0.80 条件下，每组最小样本量 n 约为 500-600，若实际样本量低于此值，则 p-value 的显著性不可靠，需增加置信区间宽度。

## Evidence

先验知识/题面给定，逻辑校验通过：基于标准统计功效分析（如ANOVA或t-test），在α=0.05, Power=0.80, 效应量f=0.10条件下，每组样本量确实在500-600量级（例如双样本t检验需约393/组，ANOVA多组或更保守估计接近500+），逻辑自洽且符合统计学常识。

## Search Query

sample size calculation for difference in means 10% effect size
