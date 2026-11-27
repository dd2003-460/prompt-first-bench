# N102: 异常信号检测阈值 τ_anomaly 的实证估计方法：通过二元逻辑回归模型 P(NoInquiry | ΔP) = 1 / (1 + exp(-β_0 - β_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

异常信号检测阈值 τ_anomaly 的实证估计方法：通过二元逻辑回归模型 P(NoInquiry | ΔP) = 1 / (1 + exp(-β_0 - β_1 * ΔP)) 拟合历史数据，取 P(NoInquiry) = 0.5 时对应的 ΔP 值作为 τ_anomaly，预期 τ_anomaly ≈ 10%。

## Corrected Claim

异常信号检测阈值 τ_anomaly 的实证估计方法：通过二元逻辑回归模型 P(NoInquiry | ΔP) = 1 / (1 + exp(-β_0 - β_1 * ΔP)) 拟合历史数据，取 P(NoInquiry) = 0.5 时对应的 ΔP 值作为 τ_anomaly，预期 τ_anomaly ≈ 10%。

## Evidence

先验知识/题面给定，逻辑校验通过：二元逻辑回归中取概率为0.5对应的自变量值即为决策边界（阈值），数学定义自洽；10%作为价格变动异常阈值在金融/商业语境下量级合理。
