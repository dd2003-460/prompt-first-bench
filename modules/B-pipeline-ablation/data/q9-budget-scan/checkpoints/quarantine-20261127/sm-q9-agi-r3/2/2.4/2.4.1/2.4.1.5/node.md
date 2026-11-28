# N139: 失败案例选取的加权得分 Score_failure = Σ (W_type * Recency_Decay * Severity_Score)，其中Recenc

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47, N48, N49

## Claim

失败案例选取的加权得分 Score_failure = Σ (W_type * Recency_Decay * Severity_Score)，其中Recency_Decay = exp(-λ * Δt)，λ=0.05/day，Severity_Score为1-5分；在1k tokens限制下，选取Score_failure最高的Top-3案例，若Top-3中存在相同错误类型，则替换为次高异类型案例。

## Corrected Claim

失败案例选取的加权得分 Score_failure = Σ (W_type * Recency_Decay * Severity_Score)，其中Recency_Decay = exp(-λ * Δt)，λ=0.05/day，Severity_Score为1-5分；在1k tokens限制下，选取Score_failure最高的Top-3案例，若Top-3中存在相同错误类型，则替换为次高异类型案例。

## Evidence

先验知识/题面给定，逻辑校验通过
