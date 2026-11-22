# N112: σ_ε 的绝对值估算：基于 N36 的 5-10% 设定，若平台单次曝光池总权重 W_total 为 1000 单位，则 σ_ε ∈ [50, 100]；需验证

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N36

## Claim

σ_ε 的绝对值估算：基于 N36 的 5-10% 设定，若平台单次曝光池总权重 W_total 为 1000 单位，则 σ_ε ∈ [50, 100]；需验证该量级是否足以使高挂价商品（W_rec 高 20%）在排序中产生 >1 个名次的随机波动，即 |ε_traffic| > ΔW_ranking_threshold。

## Corrected Claim

σ_ε 的绝对值估算：基于 N36 的 5-10% 设定，若平台单次曝光池总权重 W_total 为 1000 单位，则 σ_ε ∈ [50, 100]；需验证该量级是否足以使高挂价商品（W_rec 高 20%）在排序中产生 >1 个名次的随机波动，即 |ε_traffic| > ΔW_ranking_threshold。

## Evidence

先验知识/题面给定，逻辑校验通过：基于 N36 的 5-10% 设定及 W_total=1000 的假设，σ_ε ∈ [50, 100] 的数值推导在算术上完全自洽；关于该量级是否足以产生 >1 名次波动的验证属于后续仿真或具体阈值设定的范畴，不构成本陈述内部逻辑矛盾。

## Search Query

platform traffic allocation random exploration epsilon standard deviation ranking variance
