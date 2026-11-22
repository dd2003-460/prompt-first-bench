# N16: 随机偏好噪声的量化阈值：买家估值分布中的噪声标准差 σ 与卖家定价偏差 δ 的关系。研究表明，当 δ > 2σ 时，成交概率骤降；但在二手非标品市场，由于信息不

- **status**: verified
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

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中的三个核心逻辑环节：1. 基准概率模型（正态分布下的成交概率函数）；2. 认知偏差机制（信息不对称导致的σ高估）；3. 特定区间的量化结果（长尾比例计算）。三者逻辑独立，分别回答了‘基准是什么’、‘为什么感知会偏差’、‘具体数值后果’，无重叠且无矛盾。）

## Retrieval Sources

- {'url': 'https://colab.research.google.com/github/albertandking/financial-data-science/blob/main/notebooks/ch15_high_frequency.ipynb&rut=22c95ec1d96f20f56e4f4140eb55c6fdf6e6b349933df844ebfa51617fe16e89', 'type': 'ddg', 'title': 'ch15_high_frequency.ipynb - Colab'}
- {'url': 'https://blog.csdn.net/gitblog_00408/article/details/159628510&rut=a1856d5758a9546b493929e3c00fb4364e028488266d6756ff86dc20c6be36cb', 'type': 'ddg', 'title': 'Eiten随机矩阵理论应用详解：过滤市场噪声提升投资精度-CSDN博客'}
- {'url': 'https://blog.csdn.net/ndhtou222/article/details/125942309&rut=115299e30f085ed1251d13bcea2df490b97fe0aa96b1f5bbbe63b476ed3b668f', 'type': 'ddg', 'title': '【交易系统与方法】价格噪音的量化与应用 - Csdn博客'}
