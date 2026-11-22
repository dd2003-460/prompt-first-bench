# N66: GMV损失计算式：ΔGMV = Σ (GMV_baseline_t - GMV_intervention_t) * (1+r)^-t，需通过A/B测试获取干预组

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

GMV损失计算式：ΔGMV = Σ (GMV_baseline_t - GMV_intervention_t) * (1+r)^-t，需通过A/B测试获取干预组与对照组的GMV差值

## Corrected Claim

GMV损失计算式：ΔGMV = Σ (GMV_baseline_t - GMV_intervention_t) * (1+r)^-t，需通过A/B测试获取干预组与对照组的GMV差值

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式中的基准值（GMV_baseline_t）、折现率（r）和求和范围（Σ），三者逻辑独立且无重叠，共同构成了计算ΔGMV所需的全部核心参数定义，覆盖了父节点的关键方面。）
