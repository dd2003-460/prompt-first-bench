# N175: LFU 相对 LRU 的净增益公式分解：ΔH_net = ΔH_gain - ΔH_penalty。ΔH_gain 来源于 LRU 因时间局部性失效导致的 Mi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N62

## Claim

LFU 相对 LRU 的净增益公式分解：ΔH_net = ΔH_gain - ΔH_penalty。ΔH_gain 来源于 LRU 因时间局部性失效导致的 Miss 被 LFU 正确命中（基于 P[hot but cold]）；ΔH_penalty 来源于 LFU 因频率估计噪声或滞后导致的 Miss（基于 P[LFU_error]）。具体表达式：ΔH_net ≈ P[hot but cold] * (1 - P[LFU_error]) - P[LFU_error] * P[LRU_correct]。需分别计算两项的数值贡献，以确定 3-5 个百分点上限的构成。

## Corrected Claim

LFU 相对 LRU 的净增益公式分解：ΔH_net = ΔH_gain - ΔH_penalty。ΔH_gain 来源于 LRU 因时间局部性失效导致的 Miss 被 LFU 正确命中（基于 P[hot but cold]）；ΔH_penalty 来源于 LFU 因频率估计噪声或滞后导致的 Miss（基于 P[LFU_error]）。具体表达式：ΔH_net ≈ P[hot but cold] * (1 - P[LFU_error]) - P[LFU_error] * P[LRU_correct]。需分别计算两项的数值贡献，以确定 3-5 个百分点上限的构成。

## Evidence

先验知识/题面给定，逻辑校验通过
