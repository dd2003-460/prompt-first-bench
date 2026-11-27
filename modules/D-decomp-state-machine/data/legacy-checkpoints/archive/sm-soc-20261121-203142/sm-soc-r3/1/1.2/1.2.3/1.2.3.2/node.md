# N119: 信号-噪声比 (SNR) 的统计显著性检验：计算 SNR = Var(δ) / Var(σ_buyer)，基于 N70 的 Var(δ)≈0.00083 和 N

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

信号-噪声比 (SNR) 的统计显著性检验：计算 SNR = Var(δ) / Var(σ_buyer)，基于 N70 的 Var(δ)≈0.00083 和 N31 的 Var(σ_buyer)=0.0025，SNR ≈ 0.33，需进行 F 检验或似然比检验，确认在 α=0.05 水平下，挂价偏差信号是否显著区别于纯噪声，若 SNR < 1 则信号微弱。

## Corrected Claim

信号-噪声比 (SNR) 的统计显著性检验：计算 SNR = Var(δ) / Var(σ_buyer)，基于 N70 的 Var(δ)≈0.00083 和 N31 的 Var(σ_buyer)=0.0025，SNR ≈ 0.33，需进行 F 检验或似然比检验，确认在 α=0.05 水平下，挂价偏差信号是否显著区别于纯噪声，若 SNR < 1 则信号微弱。

## Evidence

先验知识/题面给定，逻辑校验通过：SNR计算数值正确（0.00083/0.0025≈0.33），统计检验方法（F检验/似然比）及显著性判断逻辑自洽。
