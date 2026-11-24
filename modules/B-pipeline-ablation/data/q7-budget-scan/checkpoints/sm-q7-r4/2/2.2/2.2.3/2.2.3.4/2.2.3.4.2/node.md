# N546: HDD RAID-5 有效容量修正：450TB 裸容量，RAID-5 可用率 92%（假设 13 盘阵列或近似 12/13），实际可用 HDD 容量 = 450

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N179

## Claim

HDD RAID-5 有效容量修正：450TB 裸容量，RAID-5 可用率 92%（假设 13 盘阵列或近似 12/13），实际可用 HDD 容量 = 450 * 0.92 = 414TB。

## Corrected Claim

HDD RAID-5 有效容量修正：450TB 裸容量，RAID-5 可用率 92%（假设 13 盘阵列或近似 12/13），实际可用 HDD 容量 = 450 * 0.92 = 414TB。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-5 在 N 盘阵列中损失 1 盘容量，13 盘阵列可用率为 12/13 ≈ 92.3%，与 92% 近似相符；450 * 0.92 = 414 计算正确。
