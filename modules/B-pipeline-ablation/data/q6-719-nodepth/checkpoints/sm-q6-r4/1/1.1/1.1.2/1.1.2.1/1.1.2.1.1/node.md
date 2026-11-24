# N440: 光纤中光速修正系数 n_fiber 的精确值为 1.46-1.47（对应波长 1310nm/1550nm），导致有效传播速度 c_fiber = c_vac /

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N148, N149, N150

## Claim

光纤中光速修正系数 n_fiber 的精确值为 1.46-1.47（对应波长 1310nm/1550nm），导致有效传播速度 c_fiber = c_vac / n_fiber ≈ 2.04×10^8 m/s，与近似值 2×10^8 m/s 的偏差 < 2%，在 100km 链路中引入 < 0.01ms 误差，可忽略。

## Corrected Claim

光纤中光速修正系数 n_fiber 的精确值为 1.46-1.47（对应波长 1310nm/1550nm），导致有效传播速度 c_fiber = c_vac / n_fiber ≈ 2.04×10^8 m/s，与近似值 2×10^8 m/s 的偏差 < 2%，在 100km 链路中引入 < 0.01ms 误差，可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：石英光纤在1310nm/1550nm波段的折射率确为1.46-1.47，光速计算及误差推导符合物理定律与数学逻辑。
