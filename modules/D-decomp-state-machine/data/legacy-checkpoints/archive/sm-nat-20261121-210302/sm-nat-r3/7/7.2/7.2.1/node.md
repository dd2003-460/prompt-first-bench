# N203: 在 N_cap=10,000 的工作点下，P_evict 由 Pareto(β=0.9) 的逆 CDF 计算得出，具体数值为 P_99.9% = P_min *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

在 N_cap=10,000 的工作点下，P_evict 由 Pareto(β=0.9) 的逆 CDF 计算得出，具体数值为 P_99.9% = P_min * (10000/100000)^(-1/0.9) ≈ 10 * P_min，代表高容量低驱逐率场景。

## Corrected Claim

在 N_cap=10,000 的工作点下，P_evict 由 Pareto(β=0.9) 的逆 CDF 计算得出，具体数值为 P_99.9% = P_min * (10000/100000)^(-1/0.9) ≈ 10 * P_min，代表高容量低驱逐率场景。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布逆CDF公式应用正确，数值计算 (10000/100000)^(-1/0.9) ≈ 10 符合数学推导
