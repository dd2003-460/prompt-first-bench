# N108: 置信度修正的量化公式：Conf_final = Conf_prior * (1 - α_missing_evidence)，其中 Conf_prior=0.85

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

置信度修正的量化公式：Conf_final = Conf_prior * (1 - α_missing_evidence)，其中 Conf_prior=0.85，α_missing_evidence ∈ [0.1, 0.3] 为因缺乏平台内部算法权重直接证据导致的贝叶斯后验下调系数，计算得 0.75 对应 α ≈ 0.118。

## Corrected Claim

置信度修正的量化公式：Conf_final = Conf_prior * (1 - α_missing_evidence)，其中 Conf_prior=0.85，α_missing_evidence ∈ [0.1, 0.3] 为因缺乏平台内部算法权重直接证据导致的贝叶斯后验下调系数，计算得 0.75 对应 α ≈ 0.118。

## Evidence

先验知识/题面给定，逻辑校验通过：0.85 * (1 - 0.118) ≈ 0.75，数学推导自洽，且属于模型内部置信度评估的逻辑定义。
