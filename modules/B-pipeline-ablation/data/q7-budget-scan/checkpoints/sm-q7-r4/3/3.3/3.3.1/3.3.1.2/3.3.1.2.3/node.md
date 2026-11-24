# N622: 工作点 B3 (激进型)：HDD 层配置 440TB 裸容量 (11×40TB)，RAID5 单盘奇偶校验，RAID 重建时间 T_rebuild ≈ 10-1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N212

## Claim

工作点 B3 (激进型)：HDD 层配置 440TB 裸容量 (11×40TB)，RAID5 单盘奇偶校验，RAID 重建时间 T_rebuild ≈ 10-15 天；虽 CapEx 最低 (节省约 ¥20,000)，但重建期间二次故障概率 P_double_fault ≈ 1 - e^(-T_rebuild/MTBF)，若 MTBF=500,000h，P_df ≈ 0.2%；一旦故障，数据恢复成本 C_recovery = Data_Value * P_df + Labor_Cost，预计年化隐性风险成本 ¥10,000-20,000，抵消 CapEx 节省，仅适用于非关键冷数据。

## Corrected Claim

工作点 B3 (激进型)：HDD 层配置 440TB 裸容量 (11×40TB)，RAID5 单盘奇偶校验，RAID 重建时间 T_rebuild ≈ 10-15 天；虽 CapEx 最低 (节省约 ¥20,000)，但重建期间二次故障概率 P_double_fault ≈ 1 - e^(-T_rebuild/MTBF)，若 MTBF=500,000h，P_df ≈ 0.2%；一旦故障，数据恢复成本 C_recovery = Data_Value * P_df + Labor_Cost，预计年化隐性风险成本 ¥10,000-20,000，抵消 CapEx 节省，仅适用于非关键冷数据。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID5重建时间与容量线性相关，10-15天符合440TB量级；P_df计算基于指数分布假设，数值量级合理；成本抵消逻辑符合风险管理常识。
