# N59: NVMe SSD 阵列在 10GbE 网络约束下的恢复工作点：Restore_Throughput=4.5TB/h, Data_Size=100TB(温), T

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

NVMe SSD 阵列在 10GbE 网络约束下的恢复工作点：Restore_Throughput=4.5TB/h, Data_Size=100TB(温), T_restore=23.2h (含1h overhead)

## Corrected Claim

NVMe SSD 阵列在 10GbE 网络约束下的恢复工作点：Restore_Throughput=4.5TB/h, Data_Size=100TB(温), T_restore=23.2h (含1h overhead)

## Evidence

先验知识/题面给定，逻辑校验通过：100TB / 4.5TB/h ≈ 22.22h，加上1h overhead 为 23.22h，与 23.2h 一致；4.5TB/h 在 10GbE (理论上限 ~1.25GB/s ≈ 4.5TB/h) 约束下合理。
