# N129: 从乌鲁木齐/拉萨/呼和浩特到最近主流 CDN POP 点（如西安/成都/北京）的光纤物理距离 d_max 及理论传播延迟 t_propagation = d_m

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

从乌鲁木齐/拉萨/呼和浩特到最近主流 CDN POP 点（如西安/成都/北京）的光纤物理距离 d_max 及理论传播延迟 t_propagation = d_max / (200,000 km/s)，其中 d_max 约为 1,500-2,500km，t_propagation ≈ 7.5-12.5ms（单程），往返 RTT_propagation ≈ 15-25ms

## Corrected Claim

从乌鲁木齐/拉萨/呼和浩特到最近主流 CDN POP 点（如西安/成都/北京）的光纤物理距离 d_max 及理论传播延迟 t_propagation = d_max / (200,000 km/s)，其中 d_max 约为 1,500-2,500km，t_propagation ≈ 7.5-12.5ms（单程），往返 RTT_propagation ≈ 15-25ms

## Evidence

先验知识/题面给定，逻辑校验通过：光在光纤中的传播速度约为200,000 km/s，距离1,500-2,500km对应的单程延迟计算正确（7.5-12.5ms），往返RTT为15-25ms，符合物理规律及地理常识。
