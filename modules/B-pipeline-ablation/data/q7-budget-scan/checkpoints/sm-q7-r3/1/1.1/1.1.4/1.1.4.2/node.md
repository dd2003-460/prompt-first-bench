# N121: NVMe RAID5 有效容量系数 f_raid(N) = (N-1)/N 的边际收益递减特性：当 N 从 8 增至 16，系数从 0.875 升至 0.937

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30

## Claim

NVMe RAID5 有效容量系数 f_raid(N) = (N-1)/N 的边际收益递减特性：当 N 从 8 增至 16，系数从 0.875 升至 0.9375，增益 6.25%；从 16 增至 32，系数从 0.9375 升至 0.96875，增益仅 3.125%；每增加 1 块盘带来的有效容量增量 ΔC = C_total * (1/N^2)，在 N=8 时 ΔC ≈ 0.0156*500TB=7.8TB，在 N=32 时 ΔC ≈ 0.00097*500TB=0.49TB，证明小规模阵列（N=8-16）的冗余开销对总成本影响显著。

## Corrected Claim

NVMe RAID5 有效容量系数 f_raid(N) = (N-1)/N 的边际收益递减特性：当 N 从 8 增至 16，系数从 0.875 升至 0.9375，增益 6.25%；从 16 增至 32，系数从 0.9375 升至 0.96875，增益仅 3.125%；每增加 1 块盘带来的有效容量增量 ΔC = C_total * (1/N^2)，在 N=8 时 ΔC ≈ 0.0156*500TB=7.8TB，在 N=32 时 ΔC ≈ 0.00097*500TB=0.49TB，证明小规模阵列（N=8-16）的冗余开销对总成本影响显著。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID5有效容量系数公式及数值计算（0.875, 0.9375, 0.96875）均正确，边际收益递减趋势符合数学规律。

## Search Query

RAID5 capacity efficiency ratio (N-1)/N marginal gain diminishing returns storage
