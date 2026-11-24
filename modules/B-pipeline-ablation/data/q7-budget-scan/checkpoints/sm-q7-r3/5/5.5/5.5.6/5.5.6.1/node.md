# N290: 48.8 TB NVMe SSD 缓存的物理功耗构成 = 静态功耗 (W) + 动态功耗 (W)；其中静态功耗取决于 SSD 控制器待机状态（典型值 1-5W/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

48.8 TB NVMe SSD 缓存的物理功耗构成 = 静态功耗 (W) + 动态功耗 (W)；其中静态功耗取决于 SSD 控制器待机状态（典型值 1-5W/盘，取决于是否启用 NVMe Idle），动态功耗取决于读写负载（典型值 5-15W/盘，取决于 NAND 类型和控制器效率）

## Corrected Claim

48.8 TB NVMe SSD 缓存的物理功耗构成 = 静态功耗 (W) + 动态功耗 (W)；其中静态功耗取决于 SSD 控制器待机状态（典型值 1-5W/盘，取决于是否启用 NVMe Idle），动态功耗取决于读写负载（典型值 5-15W/盘，取决于 NAND 类型和控制器效率）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVMe SSD idle power consumption watts typical enterprise drive
