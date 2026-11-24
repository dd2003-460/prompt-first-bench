# N104: HDD 功耗修正：企业级 HDD（如 Seagate Exos, WD Gold）典型功耗 6-8W（读写），但 400TB 冷数据若使用 16TB 盘，需 2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

HDD 功耗修正：企业级 HDD（如 Seagate Exos, WD Gold）典型功耗 6-8W（读写），但 400TB 冷数据若使用 16TB 盘，需 25 块盘；若使用 8TB 盘，需 50 块盘。假设 16TB 盘，25 块 * 7W = 175W。SSD 热层 100TB，使用 7.68TB NVMe，需 14 块，14 * 12W = 168W。总磁盘功耗 ≈ 343W。

## Corrected Claim

HDD 功耗修正：企业级 HDD（如 Seagate Exos, WD Gold）典型功耗 6-8W（读写），但 400TB 冷数据若使用 16TB 盘，需 25 块盘；若使用 8TB 盘，需 50 块盘。假设 16TB 盘，25 块 * 7W = 175W。SSD 热层 100TB，使用 7.68TB NVMe，需 14 块，14 * 12W = 168W。总磁盘功耗 ≈ 343W。

## Evidence

先验知识/题面给定，逻辑校验通过：400TB/16TB=25块，25*7W=175W；100TB/7.68TB≈13.02，向上取整为14块，14*12W=168W；总功耗175+168=343W，计算无误且符合企业级HDD/NVMe典型功耗量级。
