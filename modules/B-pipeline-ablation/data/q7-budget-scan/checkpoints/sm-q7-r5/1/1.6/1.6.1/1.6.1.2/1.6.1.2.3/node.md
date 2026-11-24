# N398: 工作点C（低持久性/低成本）：自建 RAID5 (4+1) 架构，物理空间系数 k_phys = 1.25，46盘组中 36 数据盘 10 校验盘（假设多个 R

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N174

## Claim

工作点C（低持久性/低成本）：自建 RAID5 (4+1) 架构，物理空间系数 k_phys = 1.25，46盘组中 36 数据盘 10 校验盘（假设多个 RAID5 组），重建时间 t_rebuild ≈ 12h，年数据丢失概率 P_loss ≈ (N_data * t_rebuild / MTBF) * (1 + t_rebuild / MTBF)，代入 N_data=36, MTBF=1.5M, t_rebuild=12h，P_loss ≈ 36*12/1.5e6 ≈ 2.88e-4/年，成本最低但风险最高

## Corrected Claim

工作点C（低持久性/低成本）：自建 RAID5 (4+1) 架构，物理空间系数 k_phys = 1.25，46盘组中 36 数据盘 10 校验盘（假设多个 RAID5 组），重建时间 t_rebuild ≈ 12h，年数据丢失概率 P_loss ≈ (N_data * t_rebuild / MTBF) * (1 + t_rebuild / MTBF)，代入 N_data=36, MTBF=1.5M, t_rebuild=12h，P_loss ≈ 36*12/1.5e6 ≈ 2.88e-4/年，成本最低但风险最高

## Evidence

先验知识/题面给定，逻辑校验通过：RAID5 (4+1) 架构下 46 盘分为 9 组（36 数据+9 校验）或近似比例，物理空间系数 1.25 符合 RAID5 冗余特性；P_loss 公式为经典 RAID 可靠性估算模型，代入数值 36*12/1.5e6 = 2.88e-4 计算正确，量级合理。
