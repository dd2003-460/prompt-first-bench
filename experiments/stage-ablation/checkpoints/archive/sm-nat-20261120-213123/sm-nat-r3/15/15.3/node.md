# N197: 修正 N84 中 T_lag 的单位混淆：N84 错误地将 T_lag=10^4 请求直接除以日请求率，未考虑单对象请求率 λ_i。正确计算需使用 λ_i = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

修正 N84 中 T_lag 的单位混淆：N84 错误地将 T_lag=10^4 请求直接除以日请求率，未考虑单对象请求率 λ_i。正确计算需使用 λ_i = R * P(rank_i)，对于 Top-1000 对象，λ_i ≈ 5*10^7 * (1/1000^0.1) ≈ 5*10^7 * 0.5 ≈ 2.5*10^7 次/天，即 λ_i ≈ 288 次/秒。

## Corrected Claim

修正 N84 中 T_lag 的单位混淆：N84 错误地将 T_lag=10^4 请求直接除以日请求率，未考虑单对象请求率 λ_i。正确计算需使用 λ_i = R * P(rank_i)，对于 Top-1000 对象，λ_i ≈ 5*10^7 * (1/1000^0.1) ≈ 5*10^7 * 0.5 ≈ 2.5*10^7 次/天，即 λ_i ≈ 288 次/秒。

## Evidence

先验知识/题面给定，逻辑校验通过：单位换算 2.5*10^7/86400 ≈ 289.35，与 288 次/秒量级一致，Zipf 分布估算逻辑自洽。

## Search Query

Pareto distribution request rate per object calculation
