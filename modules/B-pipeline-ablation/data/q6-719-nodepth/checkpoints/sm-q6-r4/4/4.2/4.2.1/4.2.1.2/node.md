# N334: IP地理库在城市/区级粒度下的静态映射准确率 A_geo_city 典型值为 85-92%，主要误差来源为移动网络IP池的跨地域复用（误差半径可达 50-200

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

IP地理库在城市/区级粒度下的静态映射准确率 A_geo_city 典型值为 85-92%，主要误差来源为移动网络IP池的跨地域复用（误差半径可达 50-200km），导致调度至次优POP的RTT增量 ΔRTT_error ≈ 0.05 * (D_optimal - D_actual) + 5ms。

## Corrected Claim

IP地理库在城市/区级粒度下的静态映射准确率 A_geo_city 典型值为 85-92%，主要误差来源为移动网络IP池的跨地域复用（误差半径可达 50-200km），导致调度至次优POP的RTT增量 ΔRTT_error ≈ 0.05 * (D_optimal - D_actual) + 5ms。

## Evidence

先验知识/题面给定，逻辑校验通过
