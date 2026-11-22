# N111: T_res 与更新率 λ_update 的耦合效应：当对象更新率 λ_update=1%/天 时，T_res 需修正为 T_res_eff = 1 / (λ_o

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

T_res 与更新率 λ_update 的耦合效应：当对象更新率 λ_update=1%/天 时，T_res 需修正为 T_res_eff = 1 / (λ_out + λ_update)，因为对象可能因更新而失效，而非仅因 LRU 驱逐；该修正项直接导致 N57 中衰减因子 exp(-λ_update * T_res_eff) 的指数项变化。

## Corrected Claim

T_res 与更新率 λ_update 的耦合效应：当对象更新率 λ_update=1%/天 时，T_res 需修正为 T_res_eff = 1 / (λ_out + λ_update)，因为对象可能因更新而失效，而非仅因 LRU 驱逐；该修正项直接导致 N57 中衰减因子 exp(-λ_update * T_res_eff) 的指数项变化。

## Evidence

先验知识/题面给定，逻辑校验通过：在连续时间马尔可夫过程或指数分布假设下，对象失效的总速率确实是各独立失效机制速率之和（λ_total = λ_out + λ_update），因此平均存活时间（即有效保留时间 T_res_eff）为总速率的倒数 1/(λ_out + λ_update)。该推导符合概率论基本公理，逻辑自洽且量纲正确（1/速率 = 时间）。
