# N207: 阈值 P_active > 0.8 的统计检验：需对 P_active 进行单样本比例检验，H0: P_active = 0.5, H1: P_active >

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N66

## Claim

阈值 P_active > 0.8 的统计检验：需对 P_active 进行单样本比例检验，H0: P_active = 0.5, H1: P_active > 0.8，计算 Z 统计量 Z = (p_hat - 0.5) / sqrt(0.5*0.5/n)，若 Z > 2.33 (α=0.01) 则拒绝 H0，支持高主动降价率。

## Corrected Claim

若需检验 P_active 是否显著高于 0.8，应设定 H0: P_active <= 0.8, H1: P_active > 0.8，计算 Z = (p_hat - 0.8) / sqrt(0.8*0.2/n)；若需检验是否显著高于 0.5，则 H0: P_active <= 0.5, H1: P_active > 0.5，Z = (p_hat - 0.5) / sqrt(0.5*0.5/n)。

## Evidence

[质询]假设设定存在逻辑矛盾：H0: P_active = 0.5 与 H1: P_active > 0.8 之间未包含 0.5 < P <= 0.8 的区间，导致检验逻辑不严谨（通常 H0 应设为 P <= 0.8 或 P = 0.8 以检验是否显著高于阈值，或者 H0: P=0.5 仅用于检验是否显著高于 0.5，而非直接支持 >0.8 的结论）。此外，若目的是检验 P > 0.8，标准做法是 H0: P <= 0.8 vs H1: P > 0.8，此时 Z 统计量分母应基于 0.8 计算，而非 0.5。 | 先验知识/题面给定，逻辑校验发现假设设定与检验目标不匹配，存在统计逻辑错误。

## Search Query

one-sample proportion hypothesis test z-statistic
