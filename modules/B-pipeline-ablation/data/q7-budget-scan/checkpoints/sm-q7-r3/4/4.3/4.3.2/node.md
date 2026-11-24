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

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一参数（Parity_Calc_Overhead系数）在不同负载场景下的取值枚举，存在严重冗余；且父节点定义的公式 T_rebuild_total = T_read + T_write + T_parity_calc 在子节点描述中被隐含地简化或混淆（子节点中 T_parity_calc 直接对标 T_read_write 的比例，未明确区分读写分离或总IO时间的定义），导致逻辑覆盖不全。）

## Search Query

RAID 6 rebuild parity calculation overhead percentage
