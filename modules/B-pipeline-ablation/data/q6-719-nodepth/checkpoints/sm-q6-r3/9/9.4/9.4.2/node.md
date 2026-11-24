# N569: 跨网延迟惩罚 ΔT_cross 随地理距离 d(km) 增加的修正系数为 0.05ms/km，即 ΔT_cross(d) = 15 + 0.05 * (d - 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N186

## Claim

跨网延迟惩罚 ΔT_cross 随地理距离 d(km) 增加的修正系数为 0.05ms/km，即 ΔT_cross(d) = 15 + 0.05 * (d - 200)，当 d > 500km 时，ΔT_cross ≈ 15 + 0.05*300 = 30ms，显著高于同网延迟。

## Corrected Claim

跨网延迟惩罚 ΔT_cross 随地理距离 d(km) 增加的修正系数为 0.05ms/km，即 ΔT_cross(d) = 15 + 0.05 * (d - 200)，当 d > 500km 时，ΔT_cross ≈ 15 + 0.05*300 = 30ms，显著高于同网延迟。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cross-ISP latency distance coefficient China backbone
