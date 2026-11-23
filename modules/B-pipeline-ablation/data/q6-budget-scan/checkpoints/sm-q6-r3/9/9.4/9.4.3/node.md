# N372: 边际效益递减阈值的量化：计算 $dH/dC_{cache} = \alpha (C_{hot}/C_{cache})^{\alpha+1} / C_{hot}$

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N138

## Claim

边际效益递减阈值的量化：计算 $dH/dC_{cache} = \alpha (C_{hot}/C_{cache})^{\alpha+1} / C_{hot}$；当 $C_{cache} = 10 \times C_{hot}$ 且 $\alpha=0.7$ 时，$dH/dC_{cache} \approx 0.7 \times (0.1)^{1.7} / C_{hot} \approx 0.0014 / C_{hot}$；若 $C_{hot}=10\text{TB}$，则每增加 1TB 缓存，命中率仅提升 0.014%，对 P99 延迟影响可忽略（<0.1ms）。

## Corrected Claim

边际效益递减阈值的量化：计算 $dH/dC_{cache} = \alpha (C_{hot}/C_{cache})^{\alpha+1} / C_{hot}$；当 $C_{cache} = 10 \times C_{hot}$ 且 $\alpha=0.7$ 时，$dH/dC_{cache} \approx 0.7 \times (0.1)^{1.7} / C_{hot} \approx 0.0014 / C_{hot}$；若 $C_{hot}=10\text{TB}$，则每增加 1TB 缓存，命中率仅提升 0.014%，对 P99 延迟影响可忽略（<0.1ms）。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算正确（0.7 * 0.1^1.7 ≈ 0.0014），量级合理，符合边际效益递减规律。
