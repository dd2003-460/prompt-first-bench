# N552: 3.84TB NVMe SSD 方案下的 RTO 时间 T_RTO_3.84TB = C_logical / B_agg，其中 C_logical = 500T

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N238

## Claim

3.84TB NVMe SSD 方案下的 RTO 时间 T_RTO_3.84TB = C_logical / B_agg，其中 C_logical = 500TB (假设全量重建或最大故障域)，B_agg = 40 GB/s (N247)，故 T_RTO_3.84TB = 500 * 1024 GB / 40 GB/s ≈ 12,800 s ≈ 3.56 小时

## Corrected Claim

3.84TB NVMe SSD 方案下的 RTO 时间 T_RTO_3.84TB = C_logical / B_agg，其中 C_logical = 500TB (假设全量重建或最大故障域)，B_agg = 40 GB/s (N247)，故 T_RTO_3.84TB = 500 * 1024 GB / 40 GB/s ≈ 12,800 s ≈ 3.56 小时

## Evidence

先验知识/题面给定，逻辑校验通过：500TB转换为GB后除以聚合带宽40GB/s，计算结果12800秒及换算的小时数均准确无误。
