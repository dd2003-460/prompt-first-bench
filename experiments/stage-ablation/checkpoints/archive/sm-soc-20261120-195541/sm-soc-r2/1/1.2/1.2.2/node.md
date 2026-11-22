# N27: 挂价分布 P_ask 的尾部修正：由于卖家存在‘高价试探’策略，ε 的分布并非严格正态，而是在右尾（ε > 0.3*σ_noise）存在截断或混合分布，即 P(

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

挂价分布 P_ask 的尾部修正：由于卖家存在‘高价试探’策略，ε 的分布并非严格正态，而是在右尾（ε > 0.3*σ_noise）存在截断或混合分布，即 P(ε > 0.3*σ_noise) 降低，导致实际挂价上限 P_ask_max ≈ P_reserve * (1 + 0.5*σ_noise)，超出此范围的挂价成交概率趋近于0。

## Corrected Claim

挂价分布 P_ask 的尾部修正：由于卖家存在‘高价试探’策略，ε 的分布并非严格正态，而是在右尾存在截断或混合分布特征，导致实际挂价上限 P_ask_max 显著高于保留价，且超出此范围的挂价成交概率趋近于0。

## Evidence

[质询]该陈述包含具体的经验性参数（如阈值 0.3*σ_noise 和系数 0.5*σ_noise），这些数值并非数学公理或第一性原理可推导的必然结果，而是依赖于特定市场微观结构或实证数据的经验假设。在缺乏来源支持的情况下，无法验证这些具体系数是否准确反映了真实的卖家行为分布。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体系数无法从第一性原理严格推出）

## Search Query

asking price distribution tail truncation high price probing strategy second-hand market
