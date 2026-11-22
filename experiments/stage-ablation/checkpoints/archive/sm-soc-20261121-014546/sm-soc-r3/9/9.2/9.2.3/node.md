# N367: 买家感知噪声标准差 σ_buyer 的分解式为 σ_buyer = sqrt(σ_info_asym^2 + σ_hetero_pref^2)，其中 σ_inf

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N121

## Claim

买家感知噪声标准差 σ_buyer 的分解式为 σ_buyer = sqrt(σ_info_asym^2 + σ_hetero_pref^2)，其中 σ_info_asym 为信息不对称导致的估值误差，σ_hetero_pref 为买家异质性偏好导致的离散度，两者需独立量化以判断噪声来源。

## Corrected Claim

买家感知噪声标准差 σ_buyer 的分解式为 σ_buyer = sqrt(σ_info_asym^2 + σ_hetero_pref^2)，其中 σ_info_asym 为信息不对称导致的估值误差，σ_hetero_pref 为买家异质性偏好导致的离散度，两者需独立量化以判断噪声来源。

## Evidence

先验知识/题面给定，逻辑校验通过：方差分解公式符合正交分量叠加原理，量纲一致，无内部矛盾。
