# N145: 若要求偏差 25% 时惩罚幅度达到 50%（即 $S=0.5$），线性模型所需系数为 $\lambda_{req} = (1 - S_{target}) / \

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

若要求偏差 25% 时惩罚幅度达到 50%（即 $S=0.5$），线性模型所需系数为 $\lambda_{req} = (1 - S_{target}) / \delta = 0.5 / 0.25 = 2.0$，远高于当前假设的 0.5。

## Corrected Claim

若要求偏差 25% 时惩罚幅度达到 50%（即 $S=0.5$），线性模型所需系数为 $\lambda_{req} = (1 - S_{target}) / \delta = 0.5 / 0.25 = 2.0$，远高于当前假设的 0.5。

## Evidence

先验知识/题面给定，逻辑校验通过：根据线性惩罚模型定义，若偏差 δ 对应惩罚 S，则系数 λ = S/δ。代入 S=0.5, δ=0.25 得 λ=2.0，计算无误且量级合理。
