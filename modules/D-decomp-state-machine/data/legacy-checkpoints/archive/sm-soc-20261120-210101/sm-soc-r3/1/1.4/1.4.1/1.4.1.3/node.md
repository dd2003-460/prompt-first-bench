# N166: 信息不对称估值偏差 σ_informational 的计算：σ_informational = β_I * I_asym * P_ref，其中 I_asym 为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N42

## Claim

信息不对称估值偏差 σ_informational 的计算：σ_informational = β_I * I_asym * P_ref，其中 I_asym 为信息不对称指数（定义为买家与卖家私有信息差的标准化值），β_I 为敏感度系数（假设 β_I=0.2），若 I_asym=0.5，则 σ_informational = 0.1 * P_ref

## Corrected Claim

信息不对称估值偏差 σ_informational 的计算：σ_informational = β_I * I_asym * P_ref，其中 I_asym 为信息不对称指数（定义为买家与卖家私有信息差的标准化值），β_I 为敏感度系数（假设 β_I=0.2），若 I_asym=0.5，则 σ_informational = 0.1 * P_ref

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义明确，代入数值 0.2 * 0.5 = 0.1 计算正确，量纲一致。
