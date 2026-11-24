# N158: L_propagation 的地理分布修正：基于 N133 的用户地理质心 (116.4°E, 39.9°N)，计算各 POP 点到质心的平均距离 D_avg，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

L_propagation 的地理分布修正：基于 N133 的用户地理质心 (116.4°E, 39.9°N)，计算各 POP 点到质心的平均距离 D_avg，L_propagation_avg = D_avg / 300,000 km/s × 1000 ms/km；对于 10 个 POP 点，需加权计算全局平均传播延迟，预计约为 5-10ms。

## Corrected Claim

L_propagation 的地理分布修正：基于 N133 的用户地理质心 (116.4°E, 39.9°N)，计算各 POP 点到质心的平均距离 D_avg，L_propagation_avg = D_avg / 300,000 km/s × 1000 ms/km；对于 10 个 POP 点，需加权计算全局平均传播延迟，预计约为 5-10ms。

## Evidence

先验知识/题面给定，逻辑校验通过：光速约300,000 km/s，北京周边POP点距离质心通常在1000-3000km范围内，对应延迟3-10ms，加权平均5-10ms符合物理直觉与工程经验。
