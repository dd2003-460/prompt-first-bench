# N545: 基准情景下，500TB 有效容量对应的物理采购总量 C_phys_base 为 500TB * (1 + RAID6_Overhead + Spare_Rati

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N235

## Claim

基准情景下，500TB 有效容量对应的物理采购总量 C_phys_base 为 500TB * (1 + RAID6_Overhead + Spare_Ratio)，其中 RAID6_Overhead=0.25 (1/4盘冗余)，Spare_Ratio=0.1 (10%热备)，计算得 C_phys_base = 500 * 1.35 = 675TB；若按 1.92TB 单盘折算，需 352 块（ceil(675/1.92)），修正 N235 中 270 块（仅含 25% 冗余）的低估，基准硬件成本 C_base_corrected = 675TB * ¥3,000/TB = ¥2,025,000。

## Corrected Claim

基准情景下，500TB 有效容量对应的物理采购总量 C_phys_base 为 500TB * (1 + RAID6_Overhead + Spare_Ratio)，其中 RAID6_Overhead=0.25 (1/4盘冗余)，Spare_Ratio=0.1 (10%热备)，计算得 C_phys_base = 500 * 1.35 = 675TB；若按 1.92TB 单盘折算，需 352 块（ceil(675/1.92)），修正 N235 中 270 块（仅含 25% 冗余）的低估，基准硬件成本 C_base_corrected = 675TB * ¥3,000/TB = ¥2,025,000。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 500 * (1 + 0.25 + 0.1) = 675 正确，ceil(675/1.92) = 352 正确，675 * 3000 = 2,025,000 正确，且符合存储容量规划的基本逻辑。
