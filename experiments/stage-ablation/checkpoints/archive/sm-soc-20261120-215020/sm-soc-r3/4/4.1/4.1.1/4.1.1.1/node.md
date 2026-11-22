# N144: 线性惩罚模型下，偏差 $\delta=25\%$ 的得分保留率为 $S_{linear} = 1 - \lambda \times \delta = 1 - 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

线性惩罚模型下，偏差 $\delta=25\%$ 的得分保留率为 $S_{linear} = 1 - \lambda \times \delta = 1 - 0.5 \times 0.25 = 0.875$，即惩罚幅度为 12.5%，而非 50%。

## Corrected Claim

线性惩罚模型下，偏差 $\delta=25\%$ 的得分保留率为 $S_{linear} = 1 - \lambda \times \delta = 1 - 0.5 \times 0.25 = 0.875$，即惩罚幅度为 12.5%，而非 50%。

## Evidence

先验知识/题面给定，逻辑校验通过：线性惩罚模型定义下，得分保留率 S = 1 - λδ，代入 λ=0.5, δ=0.25 计算得 0.875，惩罚幅度为 1-0.875=0.125 (12.5%)，数学推导自洽且无逻辑错误。
