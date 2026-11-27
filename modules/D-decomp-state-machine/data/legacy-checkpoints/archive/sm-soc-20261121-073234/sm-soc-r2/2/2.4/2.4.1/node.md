# N61: 反事实推断基线：需构建控制组，移除'高价优先'权重后，预测成交周期 T_new 的公式为 T_new = T_old * (1 + 20% * Sensitiv

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

反事实推断基线：需构建控制组，移除'高价优先'权重后，预测成交周期 T_new 的公式为 T_new = T_old * (1 + 20% * SensitivityFactor)，其中 SensitivityFactor 需通过历史 A/B 测试中类似权重调整的数据回归得出，若 SensitivityFactor > 1 则验证平台驱动力。

## Corrected Claim

反事实推断基线：需构建控制组，移除'高价优先'权重后，预测成交周期 T_new 的公式为 T_new = T_old * (1 + 20% * SensitivityFactor)，其中 SensitivityFactor 需通过历史 A/B 测试中类似权重调整的数据回归得出，若 SensitivityFactor > 1 则验证平台驱动力。

## Evidence

先验知识/题面给定，逻辑校验通过
