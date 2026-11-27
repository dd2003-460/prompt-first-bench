# N109: λ_loss_used 的参考点漂移修正项 δ_ref：当商品持有时间 T_hold > 30天 时，卖家心理参考点从 P_cost 上移至 P_listed_

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

λ_loss_used 的参考点漂移修正项 δ_ref：当商品持有时间 T_hold > 30天 时，卖家心理参考点从 P_cost 上移至 P_listed_initial，导致有效 λ_eff = λ_loss_used * (1 + δ_ref * T_hold/30)，其中 δ_ref ≈ 0.15，解释了长期未成交卖家溢价率进一步扩大的现象。

## Corrected Claim

当商品持有时间 T_hold > 30天 时，卖家心理参考点可能从 P_cost 上移至 P_listed_initial，导致有效损失厌恶系数 λ_eff 发生变化（如 λ_eff = λ_loss_used * (1 + δ_ref * T_hold/30)），其中 δ_ref 为经验估计值（约0.15），用于解释长期未成交卖家溢价率扩大的现象。

## Evidence

[质询]该陈述包含具体的经验参数（δ_ref ≈ 0.15）和特定的行为经济学机制（参考点漂移导致λ线性增加），这属于经验事实而非第一性原理可推导的数学或物理定律。虽然逻辑上自洽（长期持有导致心理账户变化从而降低损失厌恶敏感度或提高溢价容忍度是合理的经济学假设），但缺乏外部来源支持该具体数值和线性关系模型。 | 经验事实，逻辑自洽但缺来源支持。该模型描述了行为经济学中常见的参考点适应性现象，但具体系数0.15及线性修正公式属于特定模型假设，无检索来源验证。
