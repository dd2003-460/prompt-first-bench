# N22: 缓存失效机制的字节加权影响（工作点：大对象主导）：由于对象大小服从Pareto(α=1.1)，大对象数量少但字节占比高。更新惩罚对命中率的最终影响需按字节加权：

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

缓存失效机制的字节加权影响（工作点：大对象主导）：由于对象大小服从Pareto(α=1.1)，大对象数量少但字节占比高。更新惩罚对命中率的最终影响需按字节加权：ΔH = Σ (P_invalidate_i * L_i * λ_i) / R_total。大对象（L_i 大）的更新失效对字节命中率的影响远大于小对象，即使其请求频率低。

## Corrected Claim

缓存失效机制的字节加权影响（工作点：大对象主导）：由于对象大小服从Pareto(α=1.1)，大对象数量少但字节占比高。更新惩罚对命中率的最终影响需按字节加权：ΔH = Σ (P_invalidate_i * L_i * λ_i) / R_total。大对象（L_i 大）的更新失效对字节命中率的影响远大于小对象，即使其请求频率低。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

byte weighted cache invalidation impact large objects Pareto size distribution
