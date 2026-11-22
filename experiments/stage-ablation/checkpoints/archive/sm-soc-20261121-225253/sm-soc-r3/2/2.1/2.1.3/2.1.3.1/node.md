# N72: 平台算法中'高挂价'权重系数 $\omega_{high}$ 的代理指标量化：通过回归 $\ln(Exposure) = \beta_0 + \omega_{h

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27

## Claim

平台算法中'高挂价'权重系数 $\omega_{high}$ 的代理指标量化：通过回归 $\ln(Exposure) = \beta_0 + \omega_{high} \cdot \ln(P_{ask}/P_{mkt}) + \epsilon$，估计 $\omega_{high}$ 的点估计值及置信区间；若 $\omega_{high} > 0.1$ 且 p < 0.05，则证实高挂价具有正向曝光加权效应。

## Corrected Claim

平台算法中'高挂价'权重系数可通过回归模型进行代理指标量化，但具体系数阈值（如0.1）及显著性判定需基于特定数据集的实证结果，当前缺乏通用来源支持该特定阈值的有效性。

## Evidence

[质询]该陈述描述的是一个具体的实证研究方法论（回归模型设定及阈值判定），属于经验事实/研究设计范畴，无法从第一性原理推导。参考来源仅讨论通用的权重计算方法（主观/客观赋权），未涉及具体的平台算法曝光回归模型或特定系数阈值，因此缺乏直接来源支持。 | 逻辑上回归模型设定自洽，但参考来源[1]仅介绍通用权重计算理论，与该具体实证节点主题不匹配，无可用外部证据支持该特定量化方法的有效性或阈值合理性。

## Search Query

platform algorithm exposure weighting price premium regression coefficient beta estimation

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1941441784258492406&rut=638020e18d01be5938bd8711f631cd772340ccd4e5d25e2c79f82140b01b89d6', 'type': 'ddg', 'title': '评价指标体系 | 15种权重计算与综合评价方法汇总 - 知乎'}
