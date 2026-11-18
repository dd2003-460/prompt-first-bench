# N113: 驻留时间投影 W_i = E[D_i] / λ_i，对于热度排名 i 的对象，λ_i = R_total * i^{-β} / Z_β，代入 W_i 得到 W_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N41

## Claim

驻留时间投影 W_i = E[D_i] / λ_i，对于热度排名 i 的对象，λ_i = R_total * i^{-β} / Z_β，代入 W_i 得到 W_i = (Z_β / (R_total * i^{-β})) * (1/p_i)。

## Corrected Claim

驻留时间投影 W_i = E[D_i] / λ_i，对于热度排名 i 的对象，λ_i = R_total * i^{-β} / Z_β，代入 W_i 得到 W_i = (Z_β / (R_total * i^{-β})) * (1/p_i)。

## Evidence

先验知识/题面给定，逻辑校验通过：根据利特尔法则（Little's Law）驻留时间 W = E[D]/λ，代入给定的 λ_i 表达式，代数推导结果与陈述一致。

## Search Query

LRU residence time calculation based on request rate and rank
