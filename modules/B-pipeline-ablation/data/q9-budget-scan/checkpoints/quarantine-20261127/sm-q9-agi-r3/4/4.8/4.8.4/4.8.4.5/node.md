# N259: 漂移率 > 0.3 对应的可信度阈值 50% 是基于人工标注数据计算的：在 1000 个标注样本中，漂移率 > 0.3 的样本中，有 48% 被人工判定为‘结论

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N89, N90, N91

## Claim

漂移率 > 0.3 对应的可信度阈值 50% 是基于人工标注数据计算的：在 1000 个标注样本中，漂移率 > 0.3 的样本中，有 48% 被人工判定为‘结论错误’；该统计相关性系数 R² = 0.72，表明漂移率是可信度的强预测因子，但存在 28% 的残差方差，需结合 Self-Consistency (N68) 进行联合判断。

## Corrected Claim

漂移率 > 0.3 通常被视为高漂移风险区域，建议结合 Self-Consistency 进行联合判断以评估可信度。（注：原陈述中具体的48%错误率和R²=0.72缺乏公开来源直接佐证，建议核实原始实验报告。）

## Evidence

[质询]该陈述包含具体的经验统计数据（1000个样本、48%错误率、R²=0.72），这些数值无法从第一性原理推导，且参考来源均未提供此特定数据集的统计结果，存在来源缺失风险。 | 逻辑自洽（R²=0.72对应28%残差方差，48%接近50%阈值），但参考来源[1][2][3]均讨论通用置信度或漂移概念，未提供该特定统计实验数据，属经验事实且缺直接来源支持。

## Search Query

fact drift rate correlation with human verified correctness LLM agent

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_28285943/article/details/162533149&rut=126f8ad90b20055d3de91b7de8b4941fd061f09f1f359eee93a9291a78c57e16', 'type': 'ddg', 'title': 'Ai模型漂移检测与自动化应对实战指南 - Csdn博客'}
- {'url': 'https://blog.csdn.net/qq_28664681/article/details/108232353&rut=2fcab302d2b9382320122d81ca6f67391318b6c2a8caa98c5ea07dd50fac03ca', 'type': 'ddg', 'title': '如何提高目标检测模型的置信度，提高mAP - CSDN博客'}
- {'url': 'https://developer.aliyun.com/article/1607626&rut=9c59af4a1dcfed0abb41e2d539df502bd86b09834befcb63d57c13a8e02083b6', 'type': 'ddg', 'title': '详解机器学习中的置信度阈值confidence_threshold如何筛选模型预测结果-开发者社区-阿里云'}
