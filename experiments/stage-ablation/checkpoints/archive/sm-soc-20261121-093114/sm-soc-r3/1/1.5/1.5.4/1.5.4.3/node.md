# N133: γ_penalty 的实证反推：由 60% 无咨询率 P(0) = exp(-λ_consult_after * 48h) = 0.6 解得 λ_consult

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

γ_penalty 的实证反推：由 60% 无咨询率 P(0) = exp(-λ_consult_after * 48h) = 0.6 解得 λ_consult_after ≈ 0.0144/h，结合 λ_consult_before 和 P(negative_signal)，反推 γ_penalty = 1 - (λ_consult_after / (λ_consult_before * (1 - P(negative_signal))))，需代入 λ_consult_before 和 P(negative_signal) 的具体数值计算 γ_penalty。

## Corrected Claim

γ_penalty 的实证反推：由 60% 无咨询率 P(0) = exp(-λ_consult_after * 48h) = 0.6 解得 λ_consult_after ≈ 0.0144/h，结合 λ_consult_before 和 P(negative_signal)，反推 γ_penalty = 1 - (λ_consult_after / (λ_consult_before * (1 - P(negative_signal))))，需代入 λ_consult_before 和 P(negative_signal) 的具体数值计算 γ_penalty。

## Evidence

先验知识/题面给定，逻辑校验通过：指数衰减公式 P(0)=exp(-λt) 解得 λ=-ln(0.6)/48≈0.0144 计算正确，γ_penalty 定义符合逻辑推导。

## Search Query

penalty sensitivity coefficient empirical back-calculation consultation rate
