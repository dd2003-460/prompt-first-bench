# N102: 价格分布右偏度检验：计算成交均价 P_deal 的偏度系数 Skewness(P_deal)，若 Skewness > 0.5 且伴随 T_cycle 缩短，则

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27, N28, N29

## Claim

价格分布右偏度检验：计算成交均价 P_deal 的偏度系数 Skewness(P_deal)，若 Skewness > 0.5 且伴随 T_cycle 缩短，则支持随机偏好噪声假设；需给出具体偏度阈值及样本量要求。

## Corrected Claim

价格分布右偏度检验：计算成交均价 P_deal 的偏度系数 Skewness(P_deal)。若 Skewness 显著大于 0（需结合样本量进行显著性检验，如 Jarque-Bera 检验），且伴随 T_cycle 缩短，可作为支持随机偏好噪声假设的辅助证据；具体阈值需根据样本量分布特性确定，而非固定为 0.5。

## Evidence

[质询]将偏度系数（Skewness）与周期缩短（T_cycle）简单关联以支持“随机偏好噪声”假设缺乏严格的统计因果推导，且未指定具体的统计检验方法（如Jarque-Bera检验）和显著性水平，仅凭偏度>0.5这一经验阈值不足以构成严谨的假设检验结论。 | 先验知识/题面给定，逻辑校验通过，但作为经验性统计规则，缺乏通用理论支持其特定阈值与因果关系的必然性，故降级为定性表述。
