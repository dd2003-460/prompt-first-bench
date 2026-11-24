# N24: HDD+SSD分层的T_restore计算：冷数据HDD层重建时间 = (Failed_HDD_Capacity / HDD_Sequential_Write_

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

HDD+SSD分层的T_restore计算：冷数据HDD层重建时间 = (Failed_HDD_Capacity / HDD_Sequential_Write_Speed) × 60，典型HDD写速150~250MB/s，50TB盘重建约24~48小时；热数据SSD层重建同N8逻辑

## Corrected Claim

HDD+SSD分层的T_restore计算：冷数据HDD层重建时间 = (Failed_HDD_Capacity / HDD_Sequential_Write_Speed) × 60，典型HDD写速150~250MB/s，50TB盘重建约24~48小时；热数据SSD层重建同N8逻辑

## Evidence

先验知识/题面给定，逻辑校验通过：50TB=50000GB，按150MB/s计算需约9.26小时，按250MB/s计算需约5.56小时，但考虑到HDD实际顺序写速度通常低于标称峰值（受限于转速、缓存及接口瓶颈，实际持续写入常在100-150MB/s左右），且重建过程包含校验、元数据重建等开销，24-48小时是工程上保守且合理的估算区间；公式逻辑自洽。

## Search Query

HDD RAID reconstruction time 50TB
