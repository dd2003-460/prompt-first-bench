# N106: 回归系数 b 的估计值：在控制商品类别和卖家信用后，价格溢价率每增加 10%，决策时间 T_decision 平均减少 15%-20%（即 b ≈ 0.15-0

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

回归系数 b 的估计值：在控制商品类别和卖家信用后，价格溢价率每增加 10%，决策时间 T_decision 平均减少 15%-20%（即 b ≈ 0.15-0.20 天/10%溢价），前提是商品处于算法高曝光位；若移除曝光权重，b 值不显著

## Corrected Claim

在控制商品类别和卖家信用后，价格溢价率增加通常与决策时间减少相关（具体系数 b 需依据特定数据集回归结果确定，参考来源未提供具体数值）；若商品处于算法高曝光位，该效应可能更显著，但移除曝光权重后的显著性需具体统计检验支持。

## Evidence

[质询]该陈述包含具体的经验性数值（b ≈ 0.15-0.20）和特定的统计显著性结论（移除曝光权重后不显著），这属于特定数据集下的实证结果，无法从第一性原理或通用逻辑中推导出来。参考来源仅提供了回归系数的一般定义和解读方法，未包含任何关于“价格溢价率”与“决策时间”关系的具体实证数据或研究结论，因此缺乏直接的外部证据支持。 | 逻辑上自洽（负相关符合直觉，量纲合理），但参考来源[1][2]仅解释回归系数含义，未提供该具体实证结论的支持，属于经验事实且缺来源直接支持。

## Search Query

regression analysis price premium vs decision time e-commerce platform

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/656638077&rut=59a11c59e16a3a5221c7a032332bfb82881995911351ba48d32f561266d4538c', 'type': 'ddg', 'title': '（自学笔记5）线性回归模型回归系数的解读 - 知乎'}
- {'url': 'https://baike.baidu.com/item/%E5%9B%9E%E5%BD%92%E7%B3%BB%E6%95%B0/10840879&rut=0f7d03bb6f1706f31962a9056e3c45cb7bb5786fbd84fdba49e977db317b5012', 'type': 'ddg', 'title': '回归系数_百度百科'}
