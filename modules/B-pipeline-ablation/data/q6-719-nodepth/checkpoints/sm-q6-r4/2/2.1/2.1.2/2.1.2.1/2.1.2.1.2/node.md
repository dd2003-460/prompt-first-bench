# N600: 企业级 NVMe SSD 的随机读 IOPS 基准为 1,000,000 IOPS (4K QD32)，而消费级约为 500,000 IOPS；根据 N140 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N206

## Claim

企业级 NVMe SSD 的随机读 IOPS 基准为 1,000,000 IOPS (4K QD32)，而消费级约为 500,000 IOPS；根据 N140 推导的单 POP 峰值读 IOPS 需求 35k (2TB/3600s/4h_peak / 4KB)，企业级 SSD 的单盘利用率仅为 3.5%，消费级为 7%，两者均远低于饱和阈值 (80%)，因此 IOPS 不是瓶颈，选型主要受限于成本与寿命，而非性能上限。

## Corrected Claim

企业级 NVMe SSD 的随机读 IOPS 基准为 1,000,000 IOPS (4K QD32)，而消费级约为 500,000 IOPS；根据 N140 推导的单 POP 峰值读 IOPS 需求 35k (2TB/3600s/4h_peak / 4KB)，企业级 SSD 的单盘利用率仅为 3.5%，消费级为 7%，两者均远低于饱和阈值 (80%)，因此 IOPS 不是瓶颈，选型主要受限于成本与寿命，而非性能上限。

## Evidence

先验知识/题面给定，逻辑校验通过：企业级NVMe SSD随机读IOPS通常在1M+，消费级在500k-1M之间，量级合理；35k IOPS需求相对于1M/500k容量，利用率3.5%/7%计算正确，远低于80%饱和阈值，结论自洽。

## Search Query

NVMe SSD random read IOPS 4K QD32 enterprise vs consumer benchmark
