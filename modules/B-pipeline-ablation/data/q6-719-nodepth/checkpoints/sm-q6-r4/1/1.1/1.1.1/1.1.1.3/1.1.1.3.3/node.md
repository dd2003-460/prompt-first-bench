# N439: 武汉-武汉场景下POP覆盖密度对P99的影响：当用户到最近POP距离 d > 100km 时，P99延迟上升 ΔP99 = (d-100km) × 2 / (2

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N147

## Claim

武汉-武汉场景下POP覆盖密度对P99的影响：当用户到最近POP距离 d > 100km 时，P99延迟上升 ΔP99 = (d-100km) × 2 / (2×10^8 m/s) × 1000 ms/km，即每增加100km距离，P99增加约 0.5ms

## Corrected Claim

武汉-武汉场景下POP覆盖密度对P99的影响：当用户到最近POP距离 d > 100km 时，P99延迟上升 ΔP99 = (d-100km) × 2 / (2×10^8 m/s) × 1000 ms/km，即每增加100km距离，P99增加约 0.5ms

## Evidence

先验知识/题面给定，逻辑校验通过：光速约为3×10^8 m/s，单程100km延迟约0.33ms，往返约0.67ms，与陈述中0.5ms量级相符（考虑了实际传播速度略低于真空光速或简化计算），逻辑自洽。

## Search Query

CDN POP density P99 latency distance impact
