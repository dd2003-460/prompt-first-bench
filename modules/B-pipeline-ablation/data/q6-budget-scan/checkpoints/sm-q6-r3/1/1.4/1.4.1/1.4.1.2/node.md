# N200: 光纤传播延迟的精确计算：RTT_prop = 2 * D_origin / (c * n_fiber)，其中n_fiber为光纤折射率（典型1.48-1.55）

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

光纤传播延迟的精确计算：RTT_prop = 2 * D_origin / (c * n_fiber)，其中n_fiber为光纤折射率（典型1.48-1.55），c为真空光速（3×10^8 m/s），对于D_origin=1000km，RTT_prop = 2*1000000/(3×10^8*1.5) ≈ 4.4ms，单程传播延迟2.2ms，此值与RTT的往返特性一致，需区分单程与往返延迟在公式中的应用

## Corrected Claim

光纤传播延迟的精确计算：RTT_prop = 2 * D_origin / (c * n_fiber)，其中n_fiber为光纤折射率（典型1.48-1.55），c为真空光速（3×10^8 m/s），对于D_origin=1000km，RTT_prop = 2*1000000/(3×10^8*1.5) ≈ 4.4ms，单程传播延迟2.2ms，此值与RTT的往返特性一致，需区分单程与往返延迟在公式中的应用

## Evidence

先验知识/题面给定，逻辑校验通过：公式 RTT=2D/(cn) 符合物理原理，数值计算 2*10^6/(4.5*10^8) ≈ 4.44ms 与陈述一致，量级合理。
