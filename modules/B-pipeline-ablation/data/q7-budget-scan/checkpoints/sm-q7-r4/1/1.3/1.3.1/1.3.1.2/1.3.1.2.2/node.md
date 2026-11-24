# N462: 工作点2（高碎片/小对象）：平均对象大小 <64KB 且碎片率 >20% 时，XFS 元数据开销升至 2.5%（inode 1.5% + extent 0.8%

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N171

## Claim

工作点2（高碎片/小对象）：平均对象大小 <64KB 且碎片率 >20% 时，XFS 元数据开销升至 2.5%（inode 1.5% + extent 0.8% + journal 0.2%），有效容量因子 = 0.975，单位成本增加系数 = 1/0.975 ≈ 1.0256。

## Corrected Claim

工作点2（高碎片/小对象）：平均对象大小 <64KB 且碎片率 >20% 时，XFS 元数据开销升至 2.5%（inode 1.5% + extent 0.8% + journal 0.2%），有效容量因子 = 0.975，单位成本增加系数 = 1/0.975 ≈ 1.0256。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 1/(1-0.025) ≈ 1.0256 正确，各分项开销之和等于总开销，符合文件系统元数据开销的一般量级逻辑。
