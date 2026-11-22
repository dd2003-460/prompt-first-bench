# N61: 反事实推断基线：需构建控制组，移除'高价优先'权重后，预测成交周期 T_new 的公式为 T_new = T_old * (1 + 20% * Sensitiv

- **status**: pending
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

父节点级核验未通过：不完备（子节点正交性良好，分别处理参数估计（SensitivityFactor）和数据平衡（控制组构建），无重复或矛盾。但完备性不足：父节点明确包含反事实推断的核心步骤'移除权重后的预测公式 T_new = T_old * (1 + 20% * SensitivityFactor)'，而两个子节点仅分别覆盖 SensitivityFactor 的回归估计和控制组协变量平衡检验，未覆盖'权重移除后的预测模型构建'这一关键环节。此外，父节点提到'若 SensitivityFactor > 1 则验证平台驱动力'的决策逻辑也未在子节点中体现。）
