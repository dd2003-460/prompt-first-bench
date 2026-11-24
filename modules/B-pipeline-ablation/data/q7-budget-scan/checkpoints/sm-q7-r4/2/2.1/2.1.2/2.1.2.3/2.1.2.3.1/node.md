# N490: NVMe SSD 静态功耗密度修正：N165 假设静态功耗 0.5W/TB，但现代 32TB U.2 NVMe SSD 在 Idle 状态下的功耗通常为 2-3

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N165

## Claim

NVMe SSD 静态功耗密度修正：N165 假设静态功耗 0.5W/TB，但现代 32TB U.2 NVMe SSD 在 Idle 状态下的功耗通常为 2-3W/盘，即 0.06-0.10W/TB；0.5W/TB 的假设过高，可能混淆了动态功耗或包含了控制器开销；修正后静态功耗 = 20 * 2.5W = 50W = 0.05kW。

## Corrected Claim

NVMe SSD 静态功耗密度修正：N165 假设静态功耗 0.5W/TB，但现代 32TB U.2 NVMe SSD 在 Idle 状态下的功耗通常为 2-3W/盘，即 0.06-0.10W/TB；0.5W/TB 的假设过高，可能混淆了动态功耗或包含了控制器开销；修正后静态功耗 = 20 * 2.5W = 50W = 0.05kW。

## Evidence

先验知识/题面给定，逻辑校验通过：现代大容量NVMe SSD（如32TB）Idle功耗通常在2-3W左右，换算密度约为0.06-0.10W/TB，远低于0.5W/TB；计算过程 20 * 2.5W = 50W = 0.05kW 准确无误。

## Search Query

32TB NVMe SSD idle power consumption watts
