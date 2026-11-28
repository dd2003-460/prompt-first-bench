# N376: Safety_Margin 的确定依据：模型版本间性能波动标准差 σ_version 通常为 2-5%，取 Safety_Margin = max(10%, 2

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N120

## Claim

Safety_Margin 的确定依据：模型版本间性能波动标准差 σ_version 通常为 2-5%，取 Safety_Margin = max(10%, 2 * σ_version) 以确保覆盖 95% 置信区间，若 σ_version=3%，则 Margin=10%

## Corrected Claim

Safety_Margin 的确定依据：模型版本间性能波动标准差 σ_version 通常为 2-5%，取 Safety_Margin = max(10%, 2 * σ_version) 以确保覆盖 95% 置信区间，若 σ_version=3%，则 Margin=10%

## Evidence

先验知识/题面给定，逻辑校验通过：正态分布下2σ覆盖约95%置信区间，max(10%, 2*3%)=10%计算正确，符合工程安全边际设定惯例。
