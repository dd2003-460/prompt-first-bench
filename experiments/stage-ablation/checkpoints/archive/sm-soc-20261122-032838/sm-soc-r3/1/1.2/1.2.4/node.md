# N40: 高挂价区间 $[1.15, 1.25]P_{ref}$ 对应的 $z$ 值范围：当 $P_{ask} = 1.15 P_{ref}$ 时，$z = \frac{

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

高挂价区间 $[1.15, 1.25]P_{ref}$ 对应的 $z$ 值范围：当 $P_{ask} = 1.15 P_{ref}$ 时，$z = \frac{\mu_v - 1.15 P_{ref}}{\sigma_v}$；需计算该区间内 $\phi(z)$ 的具体数值范围，以验证是否足以支撑高咨询率。

## Corrected Claim

高挂价区间 $[1.15, 1.25]P_{ref}$ 对应的 $z$ 值范围：当 $P_{ask} = 1.15 P_{ref}$ 时，$z = \frac{\mu_v - 1.15 P_{ref}}{\sigma_v}$；需计算该区间内 $\phi(z)$ 的具体数值范围，以验证是否足以支撑高咨询率。

## Evidence

父节点级核验未通过：有冗余（子节点1和2本质上是同一公式在不同边界值（1.15和1.25）下的实例化，属于参数取值的重复，而非正交的独立概念；子节点3是对前两者的汇总，存在信息冗余。）
