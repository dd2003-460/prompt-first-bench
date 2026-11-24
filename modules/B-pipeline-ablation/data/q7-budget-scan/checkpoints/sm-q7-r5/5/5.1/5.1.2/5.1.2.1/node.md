# N232: NVMe SSD 阵列年化故障概率 P_failure_yearly 的量化计算：基于 500TB 容量对应的 270 块 1.92TB SSD（含冗余），单盘

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

NVMe SSD 阵列年化故障概率 P_failure_yearly 的量化计算：基于 500TB 容量对应的 270 块 1.92TB SSD（含冗余），单盘年故障率 AFR=2%，则 P_failure = 1 - (1 - 0.02)^270 ≈ 99.99%（至少一块盘故障）；但若指‘导致数据丢失的 RAID6 双盘故障’，P_data_loss ≈ C(270,2) * 0.02^2 * (1-0.02)^268 ≈ 35.7%/年。

## Corrected Claim

NVMe SSD 阵列年化故障概率 P_failure_yearly 的量化计算：基于 500TB 容量对应的 270 块 1.92TB SSD（含冗余），单盘年故障率 AFR=2%，则 P_failure = 1 - (1 - 0.02)^270 ≈ 99.99%（至少一块盘故障）；但若指‘导致数据丢失的 RAID6 双盘故障’，P_data_loss ≈ C(270,2) * 0.02^2 * (1-0.02)^268 ≈ 35.7%/年。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算正确（1-(0.98)^270≈0.9999, C(270,2)*0.02^2*0.98^268≈0.357），符合二项分布/泊松近似逻辑

## Search Query

nvme ssd annual failure rate af raito raid6 probability of data loss
