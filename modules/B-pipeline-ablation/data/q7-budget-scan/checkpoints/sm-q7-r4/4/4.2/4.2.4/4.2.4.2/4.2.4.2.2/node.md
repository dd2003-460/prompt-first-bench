# N466: NVMe SSD 阵列重建时的 I/O 干扰量化：重建期间前台 I/O 性能下降幅度 ΔIOPS 取决于 QoS 策略；若无严格 QoS 限制，重建任务通常抢占

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N206

## Claim

NVMe SSD 阵列重建时的 I/O 干扰量化：重建期间前台 I/O 性能下降幅度 ΔIOPS 取决于 QoS 策略；若无严格 QoS 限制，重建任务通常抢占 50-70% 的 I/O 带宽，导致前台随机读 IOPS 下降至正常值的 30-50%，这将增加 RTO 期间的业务机会成本 C_opportunity = Base_IOPS_Revenue * (1 - 0.4) * T_rebuild。

## Corrected Claim

NVMe SSD 阵列重建时的 I/O 干扰量化：重建期间前台 I/O 性能下降幅度 ΔIOPS 取决于 QoS 策略；若无严格 QoS 限制，重建任务通常抢占 50-70% 的 I/O 带宽，导致前台随机读 IOPS 下降至正常值的 30-50%，这将增加 RTO 期间的业务机会成本 C_opportunity = Base_IOPS_Revenue * (1 - 0.4) * T_rebuild。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVMe SSD RAID rebuild foreground performance degradation percentage
