# N545: SSD RAID-5 有效容量修正：50TB 裸容量，RAID-5 可用率 92%（(N-1)/N，假设 13 盘阵列或近似 12/13），实际可用 SSD 容

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N179

## Claim

SSD RAID-5 有效容量修正：50TB 裸容量，RAID-5 可用率 92%（(N-1)/N，假设 13 盘阵列或近似 12/13），实际可用 SSD 容量 = 50 * 0.92 = 46TB。

## Corrected Claim

SSD RAID-5 有效容量修正：50TB 裸容量，RAID-5 可用率 92%（(N-1)/N，假设 13 盘阵列或近似 12/13），实际可用 SSD 容量 = 50 * 0.92 = 46TB。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-5 可用率公式 (N-1)/N 正确，12/13 ≈ 0.923 与 92% 近似相符，计算 50 * 0.92 = 46TB 无误。
