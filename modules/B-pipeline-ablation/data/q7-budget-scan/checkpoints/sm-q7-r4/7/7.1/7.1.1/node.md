# N257: NVMe SSD阵列物理总容量需求 C_phys = 500TB / 0.98 (RAID6 N=42冗余因子) ≈ 510.2TB，用于确定SSD采购基数

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N125

## Claim

NVMe SSD阵列物理总容量需求 C_phys = 500TB / 0.98 (RAID6 N=42冗余因子) ≈ 510.2TB，用于确定SSD采购基数

## Corrected Claim

NVMe SSD阵列物理总容量需求 C_phys = 500TB / 0.98 (RAID6 N=42冗余因子) ≈ 510.2TB，用于确定SSD采购基数

## Evidence

父节点级核验未通过：不完备（子节点之间存在逻辑依赖而非完全正交：子节点2是基于子节点1中提出的硬件限制进行的‘修正’计算，两者共同构成了对父节点中‘0.98因子合理性’的质疑与替代方案，而非平行独立的维度。此外，父节点的核心是‘确定采购基数’，但子节点仅讨论了RAID因子和容量换算，未涵盖SSD单盘寿命、写入放大、性能冗余等非容量维度的采购考量，导致完备性不足。）
