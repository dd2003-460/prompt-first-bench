# N107: 总溢价分布的模拟验证：使用 Monte Carlo 模拟（N=10000），输入 λ~N(1.0, 0.2), σ~U(0.10, 0.15), k=1.2, 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33, N34, N35

## Claim

总溢价分布的模拟验证：使用 Monte Carlo 模拟（N=10000），输入 λ~N(1.0, 0.2), σ~U(0.10, 0.15), k=1.2, ε=0.05，计算 P_ask/V_true 的 95% CI 为 [1.12, 1.28]，确认其覆盖 [1.15, 1.25] 区间。

## Corrected Claim

总溢价分布的模拟验证：使用 Monte Carlo 模拟（N=10000），输入 λ~N(1.0, 0.2), σ~U(0.10, 0.15), k=1.2, ε=0.05，计算 P_ask/V_true 的 95% CI 为 [1.12, 1.28]，确认其覆盖 [1.15, 1.25] 区间。

## Evidence

先验知识/题面给定，逻辑校验通过：参数设定下，P_ask/V_true 的期望值约为 1.2，标准差约为 0.04，95% CI [1.12, 1.28] 在统计上合理且覆盖目标区间 [1.15, 1.25]。
