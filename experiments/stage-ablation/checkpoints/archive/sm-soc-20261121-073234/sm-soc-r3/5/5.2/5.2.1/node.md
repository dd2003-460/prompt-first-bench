# N306: 小幅降价（<10%）场景下的 CTR 衰减系数 δ_small：当降价幅度小于 10% 时，买家感知的‘捡漏’信号弱，CTR 衰减幅度较小，估计为 δ_smal

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

小幅降价（<10%）场景下的 CTR 衰减系数 δ_small：当降价幅度小于 10% 时，买家感知的‘捡漏’信号弱，CTR 衰减幅度较小，估计为 δ_small ∈ [0.1, 0.2]，即 CTR_new ≈ CTR_base * (1 - 0.15)，此时‘降价’标签与‘正常价’标签的点击率差异不显著，不足以解释 60% 无咨询现象。

## Corrected Claim

小幅降价（<10%）场景下的 CTR 衰减系数 δ_small：当降价幅度小于 10% 时，买家感知的‘捡漏’信号弱，CTR 衰减幅度较小，估计为 δ_small ∈ [0.1, 0.2]，即 CTR_new ≈ CTR_base * (1 - 0.15)，此时‘降价’标签与‘正常价’标签的点击率差异不显著，不足以解释 60% 无咨询现象。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

small price drop effect on click through rate second hand market
