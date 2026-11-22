# N184: 共享随机源 R_price：卖家降价幅度 ΔP 的原始分布为 TruncatedNormal(μ=0.1·P_ask, σ=0.05·P_ask, lower=

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N53

## Claim

共享随机源 R_price：卖家降价幅度 ΔP 的原始分布为 TruncatedNormal(μ=0.1·P_ask, σ=0.05·P_ask, lower=0, upper=0.3·P_ask)，该分布由损失厌恶系数 λ 和参考点 P_ref 共同决定，其中 μ 的偏移量受 λ 调节。

## Corrected Claim

共享随机源 R_price：卖家降价幅度 ΔP 的原始分布为 TruncatedNormal(μ=0.1·P_ask, σ=0.05·P_ask, lower=0, upper=0.3·P_ask)，该分布由损失厌恶系数 λ 和参考点 P_ref 共同决定，其中 μ 的偏移量受 λ 调节。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

truncated normal distribution seller price adjustment loss aversion parameter
