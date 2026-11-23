# N18: 功耗与散热不确定性量化：GPU TDP（热设计功耗）标称值与实际满载功耗（P_actual）的偏差率 δ_power = (P_actual - TDP) / 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

功耗与散热不确定性量化：GPU TDP（热设计功耗）标称值与实际满载功耗（P_actual）的偏差率 δ_power = (P_actual - TDP) / TDP；对于消费级卡（如RTX 4090），δ_power通常在-5%到+10%之间，需根据具体散热环境（风冷/水冷）修正；数据中心卡（A100/H100）δ_power通常<2%，可视为恒定。此偏差影响电力成本计算中的有效功耗系数。

## Corrected Claim

功耗与散热不确定性量化：GPU TDP（热设计功耗）标称值与实际满载功耗（P_actual）的偏差率 δ_power = (P_actual - TDP) / TDP；对于消费级卡（如RTX 4090），δ_power通常在-5%到+10%之间，需根据具体散热环境（风冷/水冷）修正；数据中心卡（A100/H100）δ_power通常<2%，可视为恒定。此偏差影响电力成本计算中的有效功耗系数。

## Evidence

先验知识/题面给定，逻辑校验通过
