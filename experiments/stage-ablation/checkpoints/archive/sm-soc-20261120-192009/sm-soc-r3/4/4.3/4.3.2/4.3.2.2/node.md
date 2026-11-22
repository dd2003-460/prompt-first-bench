# N249: 零咨询概率的敏感性分析：若 ε 降至 0.8（低于单位弹性），则 λ = 0.8 * 0.05 * 10 = 0.4，P(ΔConsult=0) = e^{-0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

零咨询概率的敏感性分析：若 ε 降至 0.8（低于单位弹性），则 λ = 0.8 * 0.05 * 10 = 0.4，P(ΔConsult=0) = e^{-0.4} ≈ 0.67；若 ε 升至 1.5，则 λ = 0.75，P(ΔConsult=0) ≈ 0.47；观测值 0.6 落在 ε ∈ [0.9, 1.1] 区间内，表明 H2 的 ε > 1.0 假设需修正为 ε ≈ 1.0。

## Corrected Claim

零咨询概率的敏感性分析：若 ε 降至 0.8（低于单位弹性），则 λ = 0.8 * 0.05 * 10 = 0.4，P(ΔConsult=0) = e^{-0.4} ≈ 0.67；若 ε 升至 1.5，则 λ = 0.75，P(ΔConsult=0) ≈ 0.47；观测值 0.6 落在 ε ∈ [0.9, 1.1] 区间内，表明 H2 的 ε > 1.0 假设需修正为 ε ≈ 1.0。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松分布公式 P(0)=e^-λ 计算正确（e^-0.4≈0.67, e^-0.75≈0.47），观测值0.6对应的λ≈0.512，反推ε≈1.02，落在[0.9, 1.1]区间，结论自洽。

## Search Query

sensitivity analysis price elasticity zero inquiry probability
