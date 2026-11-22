# N134: 参数校准方程：基于观测数据 P_no_inquiry(observed_Δp) = 0.6，代入公式 1 - Φ((Δp - μ_pct) / σ_pct) =

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N41

## Claim

参数校准方程：基于观测数据 P_no_inquiry(observed_Δp) = 0.6，代入公式 1 - Φ((Δp - μ_pct) / σ_pct) = 0.6 求解 Φ((Δp - μ_pct) / σ_pct) = 0.4，对应 Z-score ≈ -0.253，建立约束方程 (Δp - μ_pct) / σ_pct = -0.253 用于反推参数。

## Corrected Claim

参数校准方程：基于观测数据 P_no_inquiry(observed_Δp) = 0.6，代入公式 1 - Φ((Δp - μ_pct) / σ_pct) = 0.6 求解 Φ((Δp - μ_pct) / σ_pct) = 0.4，对应 Z-score ≈ -0.253，建立约束方程 (Δp - μ_pct) / σ_pct = -0.253 用于反推参数。

## Evidence

先验知识/题面给定，逻辑校验通过：标准正态分布性质 Φ(-0.253) ≈ 0.40，推导链条 1-Φ(x)=0.6 → Φ(x)=0.4 → x≈-0.253 数学上自洽且数值准确。
