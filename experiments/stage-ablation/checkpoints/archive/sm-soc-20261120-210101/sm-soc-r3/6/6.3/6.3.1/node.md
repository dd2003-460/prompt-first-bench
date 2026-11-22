# N357: 曝光重置效应 W_reset 的机制分解：W_reset = f(算法衰减率, 降价幅度, 用户记忆效应)。具体地，若平台采用指数衰减推荐算法，降价后曝光权重 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N105

## Claim

曝光重置效应 W_reset 的机制分解：W_reset = f(算法衰减率, 降价幅度, 用户记忆效应)。具体地，若平台采用指数衰减推荐算法，降价后曝光权重 W(t) = W_0 * exp(-λ_decay * t)，其中 λ_decay 为衰减率。W_reset 可近似为降价后24小时平均曝光权重与降价前24小时平均曝光权重的比值，即 W_reset = (1/24)∫_0^24 W(t)dt / W_pre。需量化 λ_decay 对 W_reset 的敏感度 ∂W_reset/∂λ_decay。

## Corrected Claim

曝光重置效应 W_reset 的机制分解：W_reset = f(算法衰减率, 降价幅度, 用户记忆效应)。具体地，若平台采用指数衰减推荐算法，降价后曝光权重 W(t) = W_0 * exp(-λ_decay * t)，其中 λ_decay 为衰减率。W_reset 可近似为降价后24小时平均曝光权重与降价前24小时平均曝光权重的比值，即 W_reset = (1/24)∫_0^24 W(t)dt / W_pre。需量化 λ_decay 对 W_reset 的敏感度 ∂W_reset/∂λ_decay。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

recommendation algorithm exposure decay rate price drop reset effect
