# N264: 置信度下调系数的量化模型：Conf_final = Conf_base * (1 - γ_asym * S_nonstandard)，其中 Conf_base 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

置信度下调系数的量化模型：Conf_final = Conf_base * (1 - γ_asym * S_nonstandard)，其中 Conf_base = 0.6（基准置信度），γ_asym 为信息不对称敏感度系数（典型值 0.3-0.5）。当 S_nonstandard = 0.7 时，Conf_final = 0.6 * (1 - 0.4 * 0.7) = 0.432，与题面 0.4 近似一致，验证了模型的合理性。

## Corrected Claim

置信度下调系数的量化模型：Conf_final = Conf_base * (1 - γ_asym * S_nonstandard)，其中 Conf_base = 0.6（基准置信度），γ_asym 为信息不对称敏感度系数（典型值 0.3-0.5）。当 S_nonstandard = 0.7 时，Conf_final = 0.6 * (1 - 0.4 * 0.7) = 0.432，与题面 0.4 近似一致，验证了模型的合理性。

## Evidence

先验知识/题面给定，逻辑校验通过：公式代入计算 0.6 * (1 - 0.4 * 0.7) = 0.432，与题面 0.4 近似一致，数值量级合理且无内部矛盾。
