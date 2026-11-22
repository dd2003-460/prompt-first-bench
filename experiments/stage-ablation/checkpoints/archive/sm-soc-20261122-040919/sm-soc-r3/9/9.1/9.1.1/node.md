# N388: 逻辑回归模型中 price_drop 的标准化系数 β1_std = β1 * SD(price_drop)，若 β1=0.4 且 SD(price_drop)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N118

## Claim

逻辑回归模型中 price_drop 的标准化系数 β1_std = β1 * SD(price_drop)，若 β1=0.4 且 SD(price_drop)=0.2，则 β1_std=0.08。

## Corrected Claim

逻辑回归模型中 price_drop 的标准化系数 β1_std = β1 * SD(price_drop)，若 β1=0.4 且 SD(price_drop)=0.2，则 β1_std=0.08。

## Evidence

先验知识/题面给定，逻辑校验通过：标准化系数计算公式为 β_std = β * SD，代入数值 0.4 * 0.2 = 0.08，计算正确且逻辑自洽。
