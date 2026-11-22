# N321: 预测偏差量化：计算在典型参数组合（如v=1, D=1）下，线性模型N29预测的成交周期 T_lin 与包含交互项模型 T_int 的相对偏差 (T_lin - 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N103

## Claim

预测偏差量化：计算在典型参数组合（如v=1, D=1）下，线性模型N29预测的成交周期 T_lin 与包含交互项模型 T_int 的相对偏差 (T_lin - T_int)/T_int，以评估公式的准确性上限。

## Corrected Claim

在典型参数组合（如v=1, D=1）下，通过计算线性模型N29预测的成交周期 T_lin 与包含交互项模型 T_int 的相对偏差 (T_lin - T_int)/T_int，可以量化特定参数下的模型预测差异，但需结合具体模型定义和数据分布来评估其作为准确性上限的适用性。

## Evidence

[质询]该陈述描述的是一个具体的计算任务或实验结果，而非一个普遍成立的物理/数学定律。在缺乏具体模型定义（N29的具体形式）和交互项模型具体形式的情况下，无法从第一性原理推导出特定的相对偏差数值或结论。此外，'典型参数组合'的定义模糊，不同参数下偏差可能差异巨大，直接断言以此评估'准确性上限'在逻辑上略显牵强，因为线性模型与交互项模型的偏差取决于数据分布和具体参数，而非固定的公式属性。 | 经验事实/具体计算任务，逻辑自洽但缺来源支持，且无法从第一性原理严格推出特定数值结论。

## Search Query

prediction error linear vs interaction model transaction time seller behavior
