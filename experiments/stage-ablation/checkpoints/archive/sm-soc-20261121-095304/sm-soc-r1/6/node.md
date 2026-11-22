# N16: 随机偏好噪声的量化阈值：买家估值分布中的噪声标准差 σ 与卖家定价偏差 δ 的关系。研究表明，当 δ > 2σ 时，成交概率骤降；但在二手非标品市场，由于信息不

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

随机偏好噪声的量化阈值：买家估值分布中的噪声标准差 σ 与卖家定价偏差 δ 的关系。研究表明，当 δ > 2σ 时，成交概率骤降；但在二手非标品市场，由于信息不对称，σ 通常被高估，导致卖家认为 δ=15-25% 仍在‘安全区’内。具体而言，若市场平均成交价 μ=1000元，标准差 σ=80元，则 15-25% 的溢价（1150-1250元）处于 1.875σ-3.125σ 区间，恰好落在‘高意愿买家’的长尾分布中。

## Corrected Claim

在二手非标品市场中，若假设买家估值噪声标准差 σ 与卖家定价偏差 δ 存在正态分布关系，且市场平均成交价 μ=1000元、σ=80元，则 15-25% 的溢价（1150-1250元）在数学上对应 1.875σ-3.125σ 区间。但关于‘δ > 2σ 时成交概率骤降’及‘σ 通常被高估’的具体市场行为结论，缺乏当前参考来源的直接实证支持，需进一步验证。

## Evidence

[质询]该陈述包含具体的经验性阈值（δ > 2σ 导致成交概率骤降）和特定市场参数（二手非标品 σ=80元），属于经验事实而非第一性原理可推导的数学/物理定律。参考来源均涉及高频金融数据或随机矩阵理论中的噪声过滤，与二手非标品市场的买家估值噪声及定价偏差无直接相关性，无法提供外部支持。 | 逻辑上数值计算自洽（150/80=1.875, 250/80=3.125），但作为经验事实，参考来源[1][2][3]均不相关，缺乏直接支持，依据经验事实排除条款降级。

## Retrieval Sources

- {'url': 'https://colab.research.google.com/github/albertandking/financial-data-science/blob/main/notebooks/ch15_high_frequency.ipynb&rut=22c95ec1d96f20f56e4f4140eb55c6fdf6e6b349933df844ebfa51617fe16e89', 'type': 'ddg', 'title': 'ch15_high_frequency.ipynb - Colab'}
- {'url': 'https://blog.csdn.net/gitblog_00408/article/details/159628510&rut=a1856d5758a9546b493929e3c00fb4364e028488266d6756ff86dc20c6be36cb', 'type': 'ddg', 'title': 'Eiten随机矩阵理论应用详解：过滤市场噪声提升投资精度-CSDN博客'}
- {'url': 'https://blog.csdn.net/ndhtou222/article/details/125942309&rut=115299e30f085ed1251d13bcea2df490b97fe0aa96b1f5bbbe63b476ed3b668f', 'type': 'ddg', 'title': '【交易系统与方法】价格噪音的量化与应用 - Csdn博客'}
