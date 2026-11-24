# N80: RAID 6 重建时的奇偶校验计算开销 Parity_Calc_Overhead 约为重建时间的 10%-20%，即 T_rebuild_total = T_r

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

RAID 6 重建时的奇偶校验计算开销 Parity_Calc_Overhead 约为重建时间的 10%-20%，即 T_rebuild_total = T_read + T_write + T_parity_calc，需将校验开销纳入总重建时长估算

## Corrected Claim

RAID 6 重建时的奇偶校验计算开销 Parity_Calc_Overhead 约为重建时间的 10%-20%，即 T_rebuild_total = T_read + T_write + T_parity_calc，需将校验开销纳入总重建时长估算

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点存在逻辑矛盾与定义冲突，且本质上是同一参数在不同场景下的取值，缺乏独立性。）

## Search Query

RAID 6 rebuild parity calculation overhead percentage
