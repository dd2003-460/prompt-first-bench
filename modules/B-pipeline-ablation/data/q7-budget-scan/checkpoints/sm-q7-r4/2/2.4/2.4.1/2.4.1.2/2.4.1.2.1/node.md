# N572: NVMe SSD动态功耗增量0.2W/TB的物理依据验证：该系数隐含假设单盘Active功耗25W、Idle 5W、容量100TB（25W/100TB=0.25

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N190

## Claim

NVMe SSD动态功耗增量0.2W/TB的物理依据验证：该系数隐含假设单盘Active功耗25W、Idle 5W、容量100TB（25W/100TB=0.25W/TB，接近0.2）。若实际采用2TB盘（Active 25W, Idle 5W），密度为10W/TB，则100TB数据分布在50块盘上的动态功耗增量应为 50 × (25-5)W = 1000W，而非 100TB × 0.2W/TB = 20W，原公式存在量级错误。

## Corrected Claim

NVMe SSD动态功耗增量0.2W/TB的物理依据验证：该系数隐含假设单盘Active功耗25W、Idle 5W、容量100TB（25W/100TB=0.25W/TB，接近0.2）。若实际采用2TB盘（Active 25W, Idle 5W），密度为10W/TB，则100TB数据分布在50块盘上的动态功耗增量应为 50 × (25-5)W = 1000W，而非 100TB × 0.2W/TB = 20W，原公式存在量级错误。

## Evidence

先验知识/题面给定，逻辑校验通过：基于NVMe SSD典型功耗参数（Active ~25W, Idle ~5W）和容量（2TB/100TB），计算得出的功耗密度差异（~10W/TB vs ~0.2W/TB）及总功耗增量（1000W vs 20W）符合物理直觉和算术逻辑，原公式确实存在量级错误。
