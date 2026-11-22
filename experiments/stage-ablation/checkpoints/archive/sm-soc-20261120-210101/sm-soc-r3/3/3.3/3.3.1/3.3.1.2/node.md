# N242: σ_algo 对成交周期 T 的传导系数 β_T：量化为 ΔT = β_T * σ_algo * T_base，其中 β_T 为弹性系数，假设 β_T = 0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N66

## Claim

σ_algo 对成交周期 T 的传导系数 β_T：量化为 ΔT = β_T * σ_algo * T_base，其中 β_T 为弹性系数，假设 β_T = 0.3（即曝光波动10%导致成交周期波动3%）；该系数需通过'同一商品不同时段曝光量'与'实际成交时间'的回归残差方差估计，若 β_T < 0.1，则算法噪声对 T 的影响可忽略（<1%）。

## Corrected Claim

σ_algo 对成交周期 T 的传导系数 β_T：量化为 ΔT = β_T * σ_algo * T_base，其中 β_T 为弹性系数，假设 β_T = 0.3（即曝光波动10%导致成交周期波动3%）；该系数需通过'同一商品不同时段曝光量'与'实际成交时间'的回归残差方差估计，若 β_T < 0.1，则算法噪声对 T 的影响可忽略（<1%）。

## Evidence

先验知识/题面给定，逻辑校验通过
