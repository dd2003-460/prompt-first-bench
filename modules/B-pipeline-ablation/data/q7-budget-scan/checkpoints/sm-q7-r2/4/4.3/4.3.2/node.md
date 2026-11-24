# N80: RAID 6 重建时的奇偶校验计算开销 Parity_Calc_Overhead 约为重建时间的 10%-20%，即 T_rebuild_total = T_r

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

RAID 6 重建时的奇偶校验计算开销 Parity_Calc_Overhead 约为重建时间的 10%-20%，即 T_rebuild_total = T_read + T_write + T_parity_calc，需将校验开销纳入总重建时长估算

## Corrected Claim

RAID 6 重建时的奇偶校验计算开销 Parity_Calc_Overhead 约为重建时间的 10%-20%，即 T_rebuild_total = T_read + T_write + T_parity_calc，需将校验开销纳入总重建时长估算

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

RAID 6 rebuild parity calculation overhead percentage
