# N12: “可发表级”研究的量化基准为：实验可复现性 (Reproducibility) >95%，统计显著性 p<0.05，且效应量 (Effect Size) Coh

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

“可发表级”研究的量化基准为：实验可复现性 (Reproducibility) >95%，统计显著性 p<0.05，且效应量 (Effect Size) Cohen's d >0.2，需在 Analysis 节点自动执行 t-test 或 chi-square 检验并生成报告。

## Corrected Claim

在采用传统频率学派的定量实证研究中，常见的初步统计筛查基准包括：实验可复现性高（如>95%一致性）、统计显著性 p<0.05，且效应量达到小至中等水平（如 Cohen's d >0.2），通常需根据数据类型选择适当的统计检验（如 t-test 或 chi-square）并生成报告，但这并非所有“可发表级”研究的唯一或绝对量化标准。

## Evidence

父节点级核验通过：正交+完备+无冗余（四个子节点分别对应父节点中的三个量化指标（Reproducibility, p-value, Effect Size）的具体操作定义，以及最终的输出规范（Report Generation）。各子节点关注点独立：节点1定义复现性，节点2定义统计检验逻辑，节点3定义效应量计算与阈值映射，节点4定义数据输出格式。它们之间没有重叠或矛盾，且共同构成了从指标定义到执行再到输出的完整闭环，无冗余。）
