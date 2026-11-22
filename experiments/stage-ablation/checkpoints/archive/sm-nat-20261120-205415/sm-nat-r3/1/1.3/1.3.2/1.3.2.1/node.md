# N103: 条件期望 E[S|H=h] 在 Gaussian Copula 下的数值计算路径：先计算 h 的分位数 u=Φ⁻¹(h)，再通过逆 Copula 变换 v = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

条件期望 E[S|H=h] 在 Gaussian Copula 下的数值计算路径：先计算 h 的分位数 u=Φ⁻¹(h)，再通过逆 Copula 变换 v = Φ⁻¹(Φ(u|v) + ρ) 得到 S 的条件分位数，最后对 v 求期望，需通过 1D 数值积分实现

## Corrected Claim

条件期望 E[S|H=h] 在 Gaussian Copula 下的数值计算路径：先计算 h 的分位数 u=Φ⁻¹(h)，再通过逆 Copula 变换 v = Φ⁻¹(Φ(u|v) + ρ) 得到 S 的条件分位数，最后对 v 求期望，需通过 1D 数值积分实现

## Evidence

先验知识/题面给定，逻辑校验通过
