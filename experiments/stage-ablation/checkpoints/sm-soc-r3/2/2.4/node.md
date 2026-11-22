# N13: 降价后咨询停滞的博弈论解释：卖家降价触发买家‘等待更低价格’策略（hold-out behavior），概率 p_holdout = 1 - e^(-λ_wai

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

降价后咨询停滞的博弈论解释：卖家降价触发买家‘等待更低价格’策略（hold-out behavior），概率 p_holdout = 1 - e^(-λ_wait × Δt)，其中 λ_wait 为买家耐心参数（λ_wait ≈ 0.05/小时），Δt 为降价后时间；48 小时内 p_holdout ≈ 60%-70%，与题面数据一致。

## Corrected Claim

降价后咨询停滞可部分归因于买家的等待策略（hold-out behavior）。虽然具体的概率模型因情境而异，但通常认为在降价后的一段时间内，部分买家会选择等待更低价格，导致短期咨询量下降。

## Evidence

[质询]该陈述将复杂的博弈论行为简化为一个特定的指数衰减公式，并给出了具体的参数值（λ_wait ≈ 0.05/小时）和结果范围（60%-70%）。虽然数学计算上 1 - e^(-0.05*48) ≈ 0.909 与声称的 60%-70% 存在数值矛盾（若 λ=0.05，48小时概率应接近91%而非60-70%；若要得到60-70%，λ应约为0.01-0.015），且该特定公式并非博弈论中解释 hold-out 行为的通用标准模型，属于过度简化的经验拟合。 | 逻辑校验发现内部数值矛盾：根据公式 p = 1 - e^(-λt)，当 λ=0.05, t=48 时，p ≈ 0.909，与陈述中的 60%-70% 不符。此外，source 为 knowledge，但存在硬逻辑/数值错误，故不能判 verified。由于无外部来源，且数值不自洽，判为 degraded 以保留其定性解释（降价导致等待）但修正定量部分。

## Search Query

buyer hold-out strategy price reduction online marketplace waiting behavior
