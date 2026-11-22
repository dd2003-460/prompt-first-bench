# N173: 曝光量本身对点击率的边际效应 β_exposure = ∂CTR/∂ln(Exposure)，在控制商品价格溢价率后，需验证其是否为正且显著；若 β_expos

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

曝光量本身对点击率的边际效应 β_exposure = ∂CTR/∂ln(Exposure)，在控制商品价格溢价率后，需验证其是否为正且显著；若 β_exposure 在高溢价组显著高于低溢价组，则说明算法对高溢价商品存在额外的曝光倾斜（即平台驱动）。

## Corrected Claim

曝光量对点击率的边际效应（β_exposure）及其在不同价格溢价组间的差异，需通过控制变量法进行实证检验，以判断是否存在平台驱动的曝光倾斜；当前缺乏具体实证数据支持该效应显著为正或存在组间差异。

## Evidence

[质询]该陈述描述的是一个特定的实证研究假设或分析框架（涉及具体的回归系数β_exposure及其在不同溢价组间的差异），属于经验事实或特定研究结论，而非通用的数学或物理定律。参考来源仅解释了CTR和曝光率的定义区别，完全未涉及曝光量对CTR的边际效应、价格溢价控制或算法倾斜的实证验证，因此缺乏直接支持。 | 逻辑上，定义边际效应并比较不同组别的系数以推断算法行为是合理的计量经济学方法；但参考来源[1]仅定义CTR和曝光率，与该具体实证假设无关，无法提供外部证据支持，故降级。

## Search Query

e-commerce algorithm exposure bias high price items click rate elasticity

## Retrieval Sources

- {'url': 'https://www.zhihu.com/question/594493227&rut=bea07bd720a2c0a578f5ac71205378a36d229bbe19b7eabd06957bd0e7ce0cb7', 'type': 'ddg', 'title': '点击率和曝光率的区别是什么？ - 知乎'}
