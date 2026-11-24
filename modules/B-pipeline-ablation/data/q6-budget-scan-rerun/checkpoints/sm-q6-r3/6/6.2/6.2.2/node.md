# N357: 平均 RPS 低负载工作点：RPS_avg_low = 800,000 / 86,400 ≈ 9.26 RPS，对应 s=2.5MB 的高对象大小场景，影响带宽

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

平均 RPS 低负载工作点：RPS_avg_low = 800,000 / 86,400 ≈ 9.26 RPS，对应 s=2.5MB 的高对象大小场景，影响带宽包年计费档位

## Corrected Claim

平均 RPS 低负载工作点：RPS_avg_low = 800,000 / 86,400 ≈ 9.26 RPS，对应 s=2.5MB 的高对象大小场景，影响带宽包年计费档位

## Evidence

先验知识/题面给定，逻辑校验通过：800,000 / 86,400 ≈ 9.259，四舍五入为 9.26 RPS，计算准确；s=2.5MB 为典型大对象场景，低 RPS 高带宽场景影响计费档位符合云存储/CDN 计费逻辑。
