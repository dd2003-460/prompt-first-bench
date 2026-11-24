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

父节点级核验未通过：非正交, 有冗余（子节点存在严重的数据矛盾（RAID6冗余开销计算错误且逻辑自相矛盾）和结构性冗余（两个工作点本质是同一决策变量的不同取值）。）

## Search Query

enterprise nvme ssd standard capacity 3.84TB 7.68TB
