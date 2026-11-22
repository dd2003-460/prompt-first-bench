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

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于统计检验的分布假设、自由度及方差齐性处理（Welch校正），子节点2聚焦于MDE的具体数值计算与显著性判断实例。两者在内容上正交（一个侧重统计推断框架，一个侧重效应量计算与判定），且共同覆盖了父节点中关于t检验、显著性水平、MDE公式及标准误计算的所有关键要素，无冗余。）

## Search Query

two sample t test minimum detectable effect size elasticity
