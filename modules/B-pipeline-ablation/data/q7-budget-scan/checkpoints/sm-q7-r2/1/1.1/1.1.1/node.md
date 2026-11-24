# N47: NVMe SSD 阵列推荐 RAID 级别选择：对于大容量（>500TB）NVMe 阵列，RAID-6（N≥4）通常优于 RAID-10，因 RAID-6 在 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N7

## Claim

NVMe SSD 阵列推荐 RAID 级别选择：对于大容量（>500TB）NVMe 阵列，RAID-6（N≥4）通常优于 RAID-10，因 RAID-6 在 N=12 时系数为 83.3%，而 RAID-10 恒为 50%，需根据单盘故障重建时间与容量利用率权衡选择。

## Corrected Claim

NVMe SSD 阵列推荐 RAID 级别选择：对于大容量（>500TB）NVMe 阵列，RAID-6（N≥4）通常优于 RAID-10，因 RAID-6 在 N=12 时系数为 83.3%，而 RAID-10 恒为 50%，需根据单盘故障重建时间与容量利用率权衡选择。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-6 容量利用率公式为 (N-2)/N，当 N=12 时为 10/12 ≈ 83.3%；RAID-10 容量利用率恒为 50%。数值计算准确，逻辑自洽。
