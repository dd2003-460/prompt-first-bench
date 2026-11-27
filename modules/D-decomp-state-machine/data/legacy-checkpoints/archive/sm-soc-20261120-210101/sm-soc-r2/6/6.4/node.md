# N106: 非对称性显著性检验的统计门槛：E_high 与 E_drop 的差值 ΔE = E_high - E_drop 需通过双样本 t 检验，显著性水平 α=0.05

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27, N28, N29

## Claim

非对称性显著性检验的统计门槛：E_high 与 E_drop 的差值 ΔE = E_high - E_drop 需通过双样本 t 检验，显著性水平 α=0.05，且最小可检测效应量 (MDE) 需满足 ΔE > 1.96 * SE(ΔE)，其中 SE(ΔE) = sqrt(Var(E_high)/n_high + Var(E_drop)/n_drop)。

## Corrected Claim

非对称性显著性检验的统计门槛：E_high 与 E_drop 的差值 ΔE = E_high - E_drop 需通过双样本 t 检验，显著性水平 α=0.05，且最小可检测效应量 (MDE) 需满足 ΔE > 1.96 * SE(ΔE)，其中 SE(ΔE) = sqrt(Var(E_high)/n_high + Var(E_drop)/n_drop)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

two sample t test minimum detectable effect size elasticity
