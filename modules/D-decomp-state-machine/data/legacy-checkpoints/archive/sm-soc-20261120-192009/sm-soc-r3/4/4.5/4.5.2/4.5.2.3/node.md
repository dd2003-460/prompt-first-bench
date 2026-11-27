# N266: 匹配质量检验指标：计算匹配后协变量标准化均值差（SMD），若所有协变量的 |SMD| < 0.1 则匹配成功；若 V_remain 的 SMD > 0.1，则需

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

匹配质量检验指标：计算匹配后协变量标准化均值差（SMD），若所有协变量的 |SMD| < 0.1 则匹配成功；若 V_remain 的 SMD > 0.1，则需增加近邻匹配数量（从 1:1 增加到 1:3）或使用核匹配（Kernel Matching）以进一步平衡高/低价值商品的分布。

## Corrected Claim

匹配质量检验指标：计算匹配后协变量标准化均值差（SMD），若所有协变量的 |SMD| < 0.1 则匹配成功；若 V_remain 的 SMD > 0.1，则需增加近邻匹配数量（从 1:1 增加到 1:3）或使用核匹配（Kernel Matching）以进一步平衡高/低价值商品的分布。

## Evidence

先验知识/题面给定，逻辑校验通过：SMD<0.1是匹配平衡性的标准阈值，针对特定变量失衡增加近邻数或改用核匹配是标准的因果推断补救措施，符合计量经济学原理。
