# N46: NVMe SSD 单盘标准容量选择：主流企业级 NVMe SSD 单盘容量通常为 3.84TB 或 7.68TB，选择 7.68TB 可最小化盘数从而降低 RA

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

NVMe SSD 单盘标准容量选择：主流企业级 NVMe SSD 单盘容量通常为 3.84TB 或 7.68TB，选择 7.68TB 可最小化盘数从而降低 RAID 6 中 (N-2)/N 的冗余损耗率

## Corrected Claim

NVMe SSD 单盘标准容量选择：主流企业级 NVMe SSD 单盘容量通常为 3.84TB 或 7.68TB，选择 7.68TB 可最小化盘数从而降低 RAID 6 中 (N-2)/N 的冗余损耗率

## Evidence

先验知识/题面给定，逻辑校验通过：3.84TB和7.68TB确实是当前主流企业级NVMe SSD的标准容量档位；RAID 6冗余损耗率公式(N-2)/N随N增大而减小，因此选择更大容量单盘减少总盘数N，确实能降低相对冗余损耗率。

## Search Query

enterprise nvme ssd standard capacity 3.84TB 7.68TB
