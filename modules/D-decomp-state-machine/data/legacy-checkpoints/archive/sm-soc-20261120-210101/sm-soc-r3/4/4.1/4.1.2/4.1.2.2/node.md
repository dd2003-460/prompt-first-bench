# N271: 稀缺性溢价系数 λ_rarity 的估计方法：在 D > 25% 的子样本中，回归 ln(CTR') = β0 + β1*D + β2*ln(1 + D) + 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N74

## Claim

稀缺性溢价系数 λ_rarity 的估计方法：在 D > 25% 的子样本中，回归 ln(CTR') = β0 + β1*D + β2*ln(1 + D) + ε，其中 β2 即为 λ_rarity 的近似值。需报告 β2 的点估计值及标准误，若 p-value > 0.1 则假设 λ_rarity = 0。

## Corrected Claim

在 D > 25% 的子样本中，可通过回归 ln(CTR') = β0 + β1*D + β2*ln(1 + D) + ε 来估计稀缺性相关参数，其中 β2 可作为 λ_rarity 的近似值；若 β2 不显著（p > 0.1），则假设 λ_rarity = 0。

## Evidence

[质询]该陈述描述了一个具体的统计估计方法（回归模型设定、子样本筛选条件、显著性阈值），属于经验性方法论或特定研究/模型的设计细节，无法从第一性原理或数学公理中严格推导出来。此外，将 ln(1+D) 的系数直接等同于“稀缺性溢价系数”在经济学直觉上可能存在混淆（通常稀缺性溢价与供给/库存负相关，而此处 D 若代表某种需求或展示指标，其正系数含义需具体定义支持），且缺乏外部来源验证该特定回归设定是否为行业标准或公认有效方法。 | 经验事实/方法论细节，逻辑自洽（回归设定在数学上可行），但无来源支持且不可从第一性原理推出，依据经验事实排除条款降级。

## Search Query

rarity premium coefficient high price deviation CTR regression second hand
