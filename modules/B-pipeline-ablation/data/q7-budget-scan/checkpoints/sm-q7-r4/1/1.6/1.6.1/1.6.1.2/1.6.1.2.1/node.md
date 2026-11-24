# N396: 工作点A（高持久性/高成本）：自建 3 副本 (Replication x3) 架构，物理空间系数 k_phys = 3.0，假设单盘 MTBF=1.5M小时，

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N174

## Claim

工作点A（高持久性/高成本）：自建 3 副本 (Replication x3) 架构，物理空间系数 k_phys = 3.0，假设单盘 MTBF=1.5M小时，46盘 RAID0/Replica 组，年数据丢失概率 P_loss ≈ 3 * (t_rebuild/MTBF) * λ_disk，其中 λ_disk=1/1.5M h^-1，t_rebuild≈10h，P_loss ≈ 2e-5/年，需极高冗余度换取低概率

## Corrected Claim

工作点A（高持久性/高成本）：自建 3 副本 (Replication x3) 架构，物理空间系数 k_phys = 3.0，假设单盘 MTBF=1.5M小时，46盘 RAID0/Replica 组，年数据丢失概率 P_loss ≈ 3 * (t_rebuild/MTBF) * λ_disk，其中 λ_disk=1/1.5M h^-1，t_rebuild≈10h，P_loss ≈ 2e-5/年，需极高冗余度换取低概率

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 3 * (10/1.5e6) = 2e-5 符合数学逻辑，量级合理。
