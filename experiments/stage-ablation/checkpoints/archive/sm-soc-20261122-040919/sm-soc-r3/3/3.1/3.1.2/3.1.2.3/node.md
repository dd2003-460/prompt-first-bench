# N243: 下游投影2：k_new 的方差 Var(k_new) 及置信区间。Var(k_new) ≈ (k_old * ΔH_info)² * Var(η)。若 k_ol

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N66

## Claim

下游投影2：k_new 的方差 Var(k_new) 及置信区间。Var(k_new) ≈ (k_old * ΔH_info)² * Var(η)。若 k_old=0.6, ΔH_info=0.287, Var(η)=0.036 (SD=0.19)，则 Var(k_new) ≈ (0.6*0.287)² * 0.036 ≈ 0.0009。95%置信区间为 E[k_new] ± 1.96*sqrt(0.0009) ≈ 0.471 ± 0.059，即 [0.412, 0.530]。

## Corrected Claim

下游投影2：k_new 的方差 Var(k_new) 及置信区间。Var(k_new) ≈ (k_old * ΔH_info)² * Var(η)。若 k_old=0.6, ΔH_info=0.287, Var(η)=0.036 (SD=0.19)，则 Var(k_new) ≈ (0.6*0.287)² * 0.036 ≈ 0.0009。95%置信区间为 E[k_new] ± 1.96*sqrt(0.0009) ≈ 0.471 ± 0.059，即 [0.412, 0.530]。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 (0.6*0.287)^2 * 0.036 ≈ 0.0009 正确，置信区间 0.471 ± 1.96*0.03 ≈ [0.412, 0.530] 计算无误，公式推导符合误差传播逻辑。
