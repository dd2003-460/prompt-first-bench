# N247: Zipf(α=1.0) 分布下的最大 POP 峰值流量：基于 N10 的 geo_share 先验，最大省份占比 p_max ≈ 0.15-0.18，对应 B_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

Zipf(α=1.0) 分布下的最大 POP 峰值流量：基于 N10 的 geo_share 先验，最大省份占比 p_max ≈ 0.15-0.18，对应 B_peak_pop_max = 79.2 Mbps × p_max ≈ 11.9-14.3 Mbps，该值决定单点硬件选型上限。

## Corrected Claim

Zipf(α=1.0) 分布下的最大 POP 峰值流量：基于 N10 的 geo_share 先验，最大省份占比 p_max ≈ 0.15-0.18，对应 B_peak_pop_max = 79.2 Mbps × p_max ≈ 11.9-14.3 Mbps，该值决定单点硬件选型上限。

## Evidence

先验知识/题面给定，逻辑校验通过：79.2 * 0.15 = 11.88，79.2 * 0.18 = 14.256，数值计算准确，量级合理。

## Search Query

Zipf distribution geographic traffic concentration max node load
