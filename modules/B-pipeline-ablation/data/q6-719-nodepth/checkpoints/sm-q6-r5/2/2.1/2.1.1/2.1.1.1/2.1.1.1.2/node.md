# N484: SSD 查找延迟 L_ssd 的 IOPS 依赖模型：L_ssd = (1 / IOPS_effective) * 1000 ms，其中 IOPS_effect

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N155

## Claim

SSD 查找延迟 L_ssd 的 IOPS 依赖模型：L_ssd = (1 / IOPS_effective) * 1000 ms，其中 IOPS_effective = IOPS_max / (1 + Queue_Length / IOPS_max)；典型 NVMe SSD IOPS_max ≈ 100,000-500,000，在低负载下 L_ssd ≈ 0.002-0.01 ms，但在高并发队列下可上升至 0.1-1 ms，需结合 N156 的 L_queue_wait 进行叠加计算。

## Corrected Claim

SSD 查找延迟 L_ssd 的 IOPS 依赖模型：L_ssd = (1 / IOPS_effective) * 1000 ms，其中 IOPS_effective = IOPS_max / (1 + Queue_Length / IOPS_max)；典型 NVMe SSD IOPS_max ≈ 100,000-500,000，在低负载下 L_ssd ≈ 0.002-0.01 ms，但在高并发队列下可上升至 0.1-1 ms，需结合 N156 的 L_queue_wait 进行叠加计算。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（1/IOPS * 1000ms），数值量级符合NVMe SSD典型性能特征（低延迟微秒级，高负载毫秒级），且source为knowledge，无需外部来源支持。
