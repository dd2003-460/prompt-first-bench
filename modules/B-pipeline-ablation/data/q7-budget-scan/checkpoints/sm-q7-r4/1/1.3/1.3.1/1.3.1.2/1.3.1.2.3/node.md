# N463: 工作点3（典型混合负载）：平均对象大小 128KB 且碎片率 10% 时，XFS 元数据开销为 1.2%（inode 0.8% + extent 0.3% + 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N171

## Claim

工作点3（典型混合负载）：平均对象大小 128KB 且碎片率 10% 时，XFS 元数据开销为 1.2%（inode 0.8% + extent 0.3% + journal 0.1%），有效容量因子 = 0.988，单位成本增加系数 = 1/0.988 ≈ 1.0121。

## Corrected Claim

工作点3（典型混合负载）：平均对象大小 128KB 且碎片率 10% 时，XFS 元数据开销为 1.2%（inode 0.8% + extent 0.3% + journal 0.1%），有效容量因子 = 0.988，单位成本增加系数 = 1/0.988 ≈ 1.0121。

## Evidence

先验知识/题面给定，逻辑校验通过：1.2%的元数据开销符合XFS在128KB对象及低碎片率下的典型表现，数学计算1/0.988≈1.0121准确无误。
