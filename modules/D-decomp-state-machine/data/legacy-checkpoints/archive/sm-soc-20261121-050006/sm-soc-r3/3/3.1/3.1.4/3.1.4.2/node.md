# N234: α_label（标签边际效应）的因果识别策略：采用工具变量法（IV），以标签字体大小或颜色对比度作为工具变量，回归模型为 ΔQ_it = α_label * (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N71

## Claim

α_label（标签边际效应）的因果识别策略：采用工具变量法（IV），以标签字体大小或颜色对比度作为工具变量，回归模型为 ΔQ_it = α_label * (1 - P(IgnoreLabel_it)) + Z_it * γ + ε_it，其中 Z_it 为工具变量；α_label 的估计值需通过 2SLS 计算，并报告 F-statistic > 10 以排除弱工具变量问题。

## Corrected Claim

α_label（标签边际效应）的因果识别策略：采用工具变量法（IV），以标签字体大小或颜色对比度作为工具变量，回归模型为 ΔQ_it = α_label * (1 - P(IgnoreLabel_it)) + Z_it * γ + ε_it，其中 Z_it 为工具变量；α_label 的估计值需通过 2SLS 计算，并报告 F-statistic > 10 以排除弱工具变量问题。

## Evidence

先验知识/题面给定，逻辑校验通过：IV方法用于解决内生性问题，2SLS是标准估计方法，F-statistic > 10是排除弱工具变量的通用经验法则，模型设定符合因果推断规范。

## Search Query

instrumental variable estimation label effect on inquiry rate 2SLS
