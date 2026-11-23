# N162: 骨干网传输延迟 t_backbone 的基础值由源站到边缘POP点的地理距离 d_km 决定，经验公式 t_base ≈ d_km / 200 ms/km（光速

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

骨干网传输延迟 t_backbone 的基础值由源站到边缘POP点的地理距离 d_km 决定，经验公式 t_base ≈ d_km / 200 ms/km（光速在光纤中约 200,000 km/s，考虑路由开销系数 1.2-1.5），例如北京到上海 d≈1000km，t_base ≈ 5-6ms

## Corrected Claim

骨干网传输延迟 t_backbone 的基础值由源站到边缘POP点的地理距离 d_km 决定，经验公式 t_base ≈ d_km / 200 ms/km（光速在光纤中约 200,000 km/s，考虑路由开销系数 1.2-1.5），例如北京到上海 d≈1000km，t_base ≈ 5-6ms

## Evidence

先验知识/题面给定，逻辑校验通过：光速在光纤中约为200,000 km/s，单程延迟理论值为 d/200,000 s = d/200 ms。北京到上海1000km对应5ms，符合物理规律及工程经验。

## Search Query

fiber optic latency per km calculation networking
