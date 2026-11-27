# N238: 共享随机源：信息熵冲击 ΔH_info 的量化公式。ΔH_info = log(1 + Var(Noise_display) / Var(S_old))。其中 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N65

## Claim

共享随机源：信息熵冲击 ΔH_info 的量化公式。ΔH_info = log(1 + Var(Noise_display) / Var(S_old))。其中 Var(Noise_display) = σ²_p / n，σ_p 为同类商品近期成交价的标准差，n 为样本量。例如，若 σ_p = 100元, n=30, Var(S_old)=100，则 Var(Noise_display) = 33.3，ΔH_info = log(1.333) ≈ 0.287。

## Corrected Claim

共享随机源：信息熵冲击 ΔH_info 的量化公式。ΔH_info = log(1 + Var(Noise_display) / Var(S_old))。其中 Var(Noise_display) = σ²_p / n，σ_p 为同类商品近期成交价的标准差，n 为样本量。例如，若 σ_p = 100元, n=30, Var(S_old)=100，则 Var(Noise_display) = 33.3，ΔH_info = log(1.333) ≈ 0.287。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算正确（100²/30≈33.33，log(1+33.33/100)≈0.287），公式定义自洽。
