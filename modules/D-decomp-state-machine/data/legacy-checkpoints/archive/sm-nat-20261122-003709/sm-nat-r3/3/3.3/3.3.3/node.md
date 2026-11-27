# N57: 线性折扣效应的近似条件：D_eff ≈ 1 - λ_update * T_resident 仅在 λ_update * T_resident << 1 时成立。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

线性折扣效应的近似条件：D_eff ≈ 1 - λ_update * T_resident 仅在 λ_update * T_resident << 1 时成立。若 T_resident 较大（如 > 100 天），需使用精确指数公式 1 - exp(-λ*T)，线性近似误差超过 5%。

## Corrected Claim

线性折扣效应的近似条件：D_eff ≈ 1 - λ_update * T_resident 仅在 λ_update * T_resident << 1 时成立。若 T_resident 较大（如 > 100 天），需使用精确指数公式 1 - exp(-λ*T)，线性近似误差超过 5%。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点逻辑的三个不同维度：1. 误差机理与极端情况验证（解析推导）；2. 实际参数下的适用性验证（自洽解计算）；3. 边界条件确定（临界阈值）。三者互为补充，无内容重叠或矛盾，且共同覆盖了‘近似条件’、‘失效阈值’及‘实际有效性’的关键方面。）
