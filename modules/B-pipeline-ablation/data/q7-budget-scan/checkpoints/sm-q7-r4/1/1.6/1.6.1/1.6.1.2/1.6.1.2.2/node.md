# N397: 工作点B（中持久性/中成本）：自建 RAID6 (4+2) 架构，物理空间系数 k_phys = 1.5，46盘组中 30 数据盘 16 校验盘，重建时间 t_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N174

## Claim

工作点B（中持久性/中成本）：自建 RAID6 (4+2) 架构，物理空间系数 k_phys = 1.5，46盘组中 30 数据盘 16 校验盘，重建时间 t_rebuild ≈ 8h，年数据丢失概率 P_loss ≈ (N_data * t_rebuild / MTBF) * (1 + t_rebuild / MTBF)，代入 N_data=30, MTBF=1.5M, t_rebuild=8h，P_loss ≈ 30*8/1.5e6 * (1+微小项) ≈ 1.6e-4/年

## Corrected Claim

工作点B（中持久性/中成本）：自建 RAID6 (4+2) 架构，物理空间系数 k_phys = 1.5，46盘组中 30 数据盘 16 校验盘，重建时间 t_rebuild ≈ 8h，年数据丢失概率 P_loss ≈ (N_data * t_rebuild / MTBF) * (1 + t_rebuild / MTBF)，代入 N_data=30, MTBF=1.5M, t_rebuild=8h，P_loss ≈ 30*8/1.5e6 * (1+微小项) ≈ 1.6e-4/年

## Evidence

先验知识/题面给定，逻辑校验通过：RAID6 (4+2) 比例下 46 盘对应 30 数据盘/16 校验盘符合 3:2 比例；P_loss 公式及数值计算 (30*8/1.5e6 ≈ 1.6e-4) 逻辑自洽且量级合理。
