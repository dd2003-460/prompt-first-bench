# N139: 投影3：分布宽度 W 的数值计算：代入 W = sqrt(Var(ε_s) + Var(ε_b) - 2ρ_ε*sqrt(Var(ε_s)*Var(ε_b)))

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N34

## Claim

投影3：分布宽度 W 的数值计算：代入 W = sqrt(Var(ε_s) + Var(ε_b) - 2ρ_ε*sqrt(Var(ε_s)*Var(ε_b)))。若 Var(ε_s)=0.05², Var(ε_b)=0.08², ρ_ε=0.5，则 W ≈ sqrt(0.0025 + 0.0064 - 2*0.5*0.004) ≈ 0.074，即 7.4%，与 15-25% 区间不符，提示需修正 ρ_ε 或方差假设。

## Corrected Claim

投影3：分布宽度 W 的数值计算：代入 W = sqrt(Var(ε_s) + Var(ε_b) - 2ρ_ε*sqrt(Var(ε_s)*Var(ε_b)))。若 Var(ε_s)=0.05², Var(ε_b)=0.08², ρ_ε=0.5，则 W ≈ sqrt(0.0025 + 0.0064 - 2*0.5*0.004) ≈ 0.074，即 7.4%，与 15-25% 区间不符，提示需修正 ρ_ε 或方差假设。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（sqrt(0.0049)≈0.07），结论推导符合逻辑
