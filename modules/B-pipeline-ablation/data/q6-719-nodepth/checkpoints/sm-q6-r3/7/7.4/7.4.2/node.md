# N372: 有限对象总数 N_total 的截断效应修正项：当 N_total < 10^6 时，必须使用完整公式 Hit_Rate = 1 - (1 - (K/N_tot

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N129

## Claim

有限对象总数 N_total 的截断效应修正项：当 N_total < 10^6 时，必须使用完整公式 Hit_Rate = 1 - (1 - (K/N_total)^α) / (1 - (1/N_total)^α) × (1 - 1/N_total)，否则高估命中率，误差可达 5%-10%。

## Corrected Claim

当 N_total 较小时（具体阈值取决于 α 和 K/N 的比例），使用无限总体近似公式会高估命中率，需使用有限总体修正公式 Hit_Rate = 1 - (1 - (K/N_total)^α) / (1 - (1/N_total)^α) × (1 - 1/N_total) 以消除截断效应。

## Evidence

[质询]该陈述包含具体的经验性阈值（N_total < 10^6）和具体的误差范围（5%-10%），这些属于经验事实而非第一性原理可推导的数学恒等式。虽然公式结构符合有限总体修正的逻辑，但具体的截断阈值和误差量级缺乏通用理论支持，可能依赖于特定的α值或K/N比例，存在过度泛化的风险。 | source=knowledge，逻辑自洽（公式结构符合有限总体修正原理），但具体阈值和误差范围为经验参数，无外部来源支持，依据经验事实排除条款降级。

## Search Query

Zipf distribution finite population correction
