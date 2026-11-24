# N410: 西部长尾用户到最近自建 POP 的平均单程传播延迟 L_prop_tail = D_avg / (c * n_fiber)，其中 D_avg ≈ 1500 km

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N136

## Claim

西部长尾用户到最近自建 POP 的平均单程传播延迟 L_prop_tail = D_avg / (c * n_fiber)，其中 D_avg ≈ 1500 km，c = 3×10^8 m/s，n_fiber ≈ 1.5，计算得 L_prop_tail ≈ 7.5 ms；对比东部用户 L_prop_east ≈ 3 ms，差值 ΔL_prop = 4.5 ms 是硬件物理下限。

## Corrected Claim

西部长尾用户到最近自建 POP 的平均单程传播延迟 L_prop_tail = D_avg / (c * n_fiber)，其中 D_avg ≈ 1500 km，c = 3×10^8 m/s，n_fiber ≈ 1.5，计算得 L_prop_tail ≈ 7.5 ms；对比东部用户 L_prop_east ≈ 3 ms，差值 ΔL_prop = 4.5 ms 是硬件物理下限。

## Evidence

先验知识/题面给定，逻辑校验通过：光速在光纤中约为 2×10^8 m/s，1500km 距离对应延迟约 7.5ms，计算无误且符合物理直觉。
