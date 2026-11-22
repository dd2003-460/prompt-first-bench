# N198: 多重比较校正的影响：若同时对 H1 的多个子假设（如价格同质性、周期缩短、降价无效）进行反例检验，需采用 Bonferroni 校正，显著性水平调整为 $\al

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N72

## Claim

多重比较校正的影响：若同时对 H1 的多个子假设（如价格同质性、周期缩短、降价无效）进行反例检验，需采用 Bonferroni 校正，显著性水平调整为 $\alpha' = 0.05/3 \approx 0.0167$，对应临界值 $\chi^2_{crit} \approx 6.63$。此时 $O_{min}$ 从 16 升至 20（N=100），$p_{threshold}$ 从 16% 升至 20%，进一步收紧置信度下界的触发条件。

## Corrected Claim

多重比较校正的影响：若同时对 H1 的多个子假设（如价格同质性、周期缩短、降价无效）进行反例检验，需采用 Bonferroni 校正，显著性水平调整为 $\alpha' = 0.05/3 \approx 0.0167$，对应临界值 $\chi^2_{crit} \approx 6.63$。此时 $O_{min}$ 从 16 升至 20（N=100），$p_{threshold}$ 从 16% 升至 20%，进一步收紧置信度下界的触发条件。

## Evidence

先验知识/题面给定，逻辑校验通过：Bonferroni校正计算正确（0.05/3≈0.0167），对应卡方临界值（df=1, α=0.0167）约为6.63，样本量与阈值推导符合统计逻辑。

## Search Query

Bonferroni correction multiple hypothesis testing chi-square critical value adjustment
