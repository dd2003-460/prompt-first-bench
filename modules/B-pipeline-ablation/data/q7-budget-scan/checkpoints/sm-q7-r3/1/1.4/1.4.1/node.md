# N46: NVMe SSD 单盘标准容量选择：主流企业级 NVMe SSD 单盘容量通常为 3.84TB 或 7.68TB，选择 7.68TB 可最小化盘数从而降低 RA

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

NVMe SSD 单盘标准容量选择：主流企业级 NVMe SSD 单盘容量通常为 3.84TB 或 7.68TB，选择 7.68TB 可最小化盘数从而降低 RAID 6 中 (N-2)/N 的冗余损耗率

## Corrected Claim

NVMe SSD 单盘标准容量选择：主流企业级 NVMe SSD 单盘容量通常为 3.84TB 或 7.68TB，选择 7.68TB 可最小化盘数从而降低 RAID 6 中 (N-2)/N 的冗余损耗率

## Evidence

父节点级核验未通过：非正交, 有冗余（1. 冗余：子节点1和子节点2本质上是同一决策维度（SSD容量选择）的两个互斥选项，属于‘多值参数’而非独立的正交知识点，应合并为一个包含对比数据的节点。2. 逻辑矛盾：子节点3声称‘RTO影响极低’，但RAID 6在发生双盘故障时需进行长时间的重建（Rebuild），这通常会导致I/O性能显著下降甚至服务中断，RTO（恢复时间目标）在此场景下主要受限于重建时间和数据量，而非简单的‘极低’，该结论与RAID机制常识相悖。3. 计算错误：子节点1中119块盘的年故障期望值计算有误（119 * 0.0000876 ≈ 0.0104，此处数值看似正确，但‘96年一次’是基于平均等待时间，对于RAID 6而言，需关注的是双盘同时故障的概率，单纯单盘故障率不能直接推导出系统安全性）。）

## Search Query

enterprise nvme ssd standard capacity 3.84TB 7.68TB
