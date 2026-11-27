# N130: 挂价 $P_{ask} = 1.15 P_{ref}$ 时的 $z$ 值计算：$z = \frac{\mu_v - 1.15 P_{ref}}{\sigma_v

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

挂价 $P_{ask} = 1.15 P_{ref}$ 时的 $z$ 值计算：$z = \frac{\mu_v - 1.15 P_{ref}}{\sigma_v}$。若 $\mu_v = P_{ref}$ 且 $\sigma_v = 0.15 P_{ref}$，则 $z = -1.0$，对应 $\Phi(z) \approx 0.159$。

## Corrected Claim

挂价 $P_{ask} = 1.15 P_{ref}$ 时的 $z$ 值计算：$z = \frac{\mu_v - 1.15 P_{ref}}{\sigma_v}$。若 $\mu_v = P_{ref}$ 且 $\sigma_v = 0.15 P_{ref}$，则 $z = -1.0$，对应 $\Phi(z) \approx 0.159$。

## Evidence

先验知识/题面给定，逻辑校验通过：代入数值计算 z = (1 - 1.15)/0.15 = -1.0，标准正态分布 Φ(-1.0) ≈ 0.1587，与陈述一致。
