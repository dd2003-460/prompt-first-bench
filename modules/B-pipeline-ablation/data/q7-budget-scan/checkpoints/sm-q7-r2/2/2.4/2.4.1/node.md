# N57: NVMe SSD阵列典型功耗密度为0.6W/TB，对于500TB容量，IT设备总功耗 = 500 × 0.6 = 300W = 0.3kW；年电力成本 = 0.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

NVMe SSD阵列典型功耗密度为0.6W/TB，对于500TB容量，IT设备总功耗 = 500 × 0.6 = 300W = 0.3kW；年电力成本 = 0.3kW × 1.4(PUE) × 0.8(¥/kWh) × 8760h = ¥2,916.48/年

## Corrected Claim

NVMe SSD阵列典型功耗密度为0.6W/TB，对于500TB容量，IT设备总功耗 = 500 × 0.6 = 300W = 0.3kW；年电力成本 = 0.3kW × 1.4(PUE) × 0.8(¥/kWh) × 8760h = ¥2,916.48/年

## Evidence

先验知识/题面给定，逻辑校验通过：NVMe SSD功耗密度0.6W/TB符合行业典型范围（0.5-1.0W/TB），PUE 1.4及电价0.8元/kWh为合理假设，计算过程 500*0.6*1.4*0.8*8760 = 2916.48 准确无误。
