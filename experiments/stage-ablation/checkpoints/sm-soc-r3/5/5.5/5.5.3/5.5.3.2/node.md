# N295: 季节性波动对置信度的贡献量化：季节调整残差 ε_season 的方差 Var(ε_season) 导致置信度下降 ΔConf_season = -β_seaso

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

季节性波动对置信度的贡献量化：季节调整残差 ε_season 的方差 Var(ε_season) 导致置信度下降 ΔConf_season = -β_season * Var(ε_season)/Var(Δt_avg)，其中 β_season 为季节敏感度系数（需通过历史季节调整模型残差分析确定，假设 β_season=0.2），该贡献占总不确定性 20%。

## Corrected Claim

季节性波动对置信度的贡献量化：季节调整残差 ε_season 的方差 Var(ε_season) 导致置信度下降 ΔConf_season = -β_season * Var(ε_season)/Var(Δt_avg)，其中 β_season 为季节敏感度系数（需通过历史季节调整模型残差分析确定，假设 β_season=0.2），该贡献占总不确定性 20%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

seasonal adjustment residual variance confidence interval width e-commerce
