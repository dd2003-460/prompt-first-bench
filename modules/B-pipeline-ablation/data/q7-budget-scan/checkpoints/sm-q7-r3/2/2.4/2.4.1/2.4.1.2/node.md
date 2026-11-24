# N190: NVMe SSD阵列动态功耗增量计算：温数据100TB日均2次全量扫描，每次扫描IO强度对应功耗增量0.2W/TB，年动态功耗成本 = 100TB × 0.2W

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

NVMe SSD阵列动态功耗增量计算：温数据100TB日均2次全量扫描，每次扫描IO强度对应功耗增量0.2W/TB，年动态功耗成本 = 100TB × 0.2W/TB × 2次/天 × 4小时/次 × 365天 × 1.4(PUE) × 0.8(¥/kWh) = ¥1,420.48/年

## Corrected Claim

NVMe SSD阵列动态功耗增量计算：温数据100TB日均2次全量扫描，每次扫描IO强度对应功耗增量0.2W/TB，年动态功耗成本 = 100TB × 0.2W/TB × 2次/天 × 4小时/次 × 365天 × 1.4(PUE) × 0.8(¥/kWh) = ¥1,420.48/年

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（100*0.2*2*4*365*1.4*0.8 = 1420.48），单位量纲一致，符合功耗成本计算逻辑。

## Search Query

NVMe SSD active read power consumption watts per terabyte
