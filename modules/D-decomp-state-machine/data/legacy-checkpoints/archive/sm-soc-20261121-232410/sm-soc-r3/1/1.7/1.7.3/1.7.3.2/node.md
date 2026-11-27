# N144: 噪声主导概率 P(Noise_Dominant) 的量化定义：P(Noise_Dominant) = P(σ_noise > |ΔP_signal| / 2)，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

噪声主导概率 P(Noise_Dominant) 的量化定义：P(Noise_Dominant) = P(σ_noise > |ΔP_signal| / 2)，其中 σ_noise 为买家主观价格容忍度标准差（基于N88，估算为市场价的10%），当降价幅度 ΔP 小于 2*σ_noise（即20%市场价）时，该概率接近 1.0，导致信号失效。

## Corrected Claim

噪声主导概率 P(Noise_Dominant) 的量化定义：P(Noise_Dominant) = P(σ_noise > |ΔP_signal| / 2)，其中 σ_noise 为买家主观价格容忍度标准差（基于N88，估算为市场价的10%），当降价幅度 ΔP 小于 2*σ_noise（即20%市场价）时，该概率接近 1.0，导致信号失效。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

price noise tolerance threshold second hand buyer behavior
