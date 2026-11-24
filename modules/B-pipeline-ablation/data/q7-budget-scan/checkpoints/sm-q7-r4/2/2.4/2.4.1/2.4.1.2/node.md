# N190: NVMe SSD阵列动态功耗增量计算：温数据100TB日均2次全量扫描，每次扫描IO强度对应功耗增量0.2W/TB，年动态功耗成本 = 100TB × 0.2W

- **status**: pending
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

父节点级核验未通过：非正交（子节点1和子节点2存在严重的逻辑重叠与矛盾。子节点1指出原公式存在量级错误并给出了正确的物理推导（50块盘，1000W增量），子节点2紧接着基于同样的前提重复了相同的计算过程。这两个节点本应合并为一个“功耗修正”节点。此外，子节点1侧重于‘依据验证’（定性/纠错），子节点2侧重于‘正确计算’（定量），但内容高度重合，违反了正交性原则。）

## Search Query

NVMe SSD active read power consumption watts per terabyte
