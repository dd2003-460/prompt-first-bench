# N129: β_anchor 在 [0.5, 1.0] 区间内的分位数分布：第25百分位 Q25 ≈ 0.65，中位数 Q50 ≈ 0.80，第75百分位 Q75 ≈ 0.

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

β_anchor 在 [0.5, 1.0] 区间内的分位数分布：第25百分位 Q25 ≈ 0.65，中位数 Q50 ≈ 0.80，第75百分位 Q75 ≈ 0.90，表明约50%的卖家锚定强度高于0.8，需通过核密度估计验证分布形态。

## Corrected Claim

β_anchor 在 [0.5, 1.0] 区间内呈现右偏或集中分布特征（具体分位数需依据实际数据集计算，如 Q50 可能接近 0.80），需通过核密度估计验证分布形态。

## Evidence

[质询]该陈述包含具体的经验统计数值（Q25≈0.65, Q50≈0.80, Q75≈0.90），属于特定数据集的实证结果，无法从第一性原理或数学公理推导得出，且参考来源中未包含任何关于卖家锚定强度分布的具体数据支持。 | 逻辑上分位数单调递增（0.65 < 0.80 < 0.90）且位于[0.5, 1.0]区间内，自洽；但参考来源[1]仅介绍Q-Q图概念，[2]介绍Beta分布定义，均与该具体经验事实无关，缺乏外部证据支持具体数值。

## Search Query

distribution of anchor bias coefficients quantiles C2C marketplace sellers

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/661198241&rut=3e00df68419baa5b71fad66538ee9f916c73ad7b4125eed02b442899825e2fd6', 'type': 'ddg', 'title': '统计基础：分位数-分位数图（Q-q图） - 知乎 - 知乎专栏'}
- {'url': 'https://zh.wikipedia.org/wiki/%CE%92%E5%88%86%E5%B8%83&rut=ae565a6ca0da3ce795d91e6340704305943c95951e95e18629c7568afe0a2866', 'type': 'ddg', 'title': 'Β分布 - 维基百科，自由的百科全书'}
