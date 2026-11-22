# N21: 负相关修正因子K的线性近似误差：K = 1 + ρ(1-C) 是ρ的一阶泰勒展开，当ρ=-0.3时，二阶项 ρ²(1-C)²/2 ≈ 0.03 不可忽略，精确修

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

负相关修正因子K的线性近似误差：K = 1 + ρ(1-C) 是ρ的一阶泰勒展开，当ρ=-0.3时，二阶项 ρ²(1-C)²/2 ≈ 0.03 不可忽略，精确修正因子应为 K_exact ≈ 1 + ρ(1-C) + 0.5ρ²(1-C)²，需计算二阶项对H_corrected的影响幅度（约0.3-0.5个百分点）。

## Corrected Claim

负相关修正因子K的线性近似误差：K = 1 + ρ(1-C) 是ρ的一阶泰勒展开，当ρ=-0.3时，二阶项 ρ²(1-C)²/2 ≈ 0.03 不可忽略，精确修正因子应为 K_exact ≈ 1 + ρ(1-C) + 0.5ρ²(1-C)²，需计算二阶项对H_corrected的影响幅度（约0.3-0.5个百分点）。

## Evidence

父节点级核验未通过：有冗余（子节点本质上是同一计算公式（K = 1 + ρ(1-C) + 0.5ρ²(1-C)² 及其对 H 的影响）在不同参数点（C, ρ）下的具体数值实例。虽然它们在参数空间上不重叠（正交），且覆盖了低、中、高误差范围（完备），但存在高度冗余，因为它们共享完全相同的逻辑结构和公式，仅数值不同。）

## Search Query

correlation coefficient second order correction cache eviction cost
