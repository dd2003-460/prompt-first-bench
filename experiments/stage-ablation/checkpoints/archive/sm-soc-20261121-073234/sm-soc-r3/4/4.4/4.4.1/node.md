# N89: 平台排序算法中'标价/成交中位数比'（Price Ratio）对商品曝光量（Exposure）的敏感度系数 β_exposure，即 Exposure = f(

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

平台排序算法中'标价/成交中位数比'（Price Ratio）对商品曝光量（Exposure）的敏感度系数 β_exposure，即 Exposure = f(β_exposure * Price_Ratio)，需通过反事实推断或A/B测试数据确定 β_exposure 的具体数值。

## Corrected Claim

在部分电商平台的内部排序模型中，价格因素（如标价与历史成交价的比值）可能作为特征之一影响商品曝光，但其具体敏感度系数（β_exposure）及函数形式因平台而异，通常需通过内部 A/B 测试或因果推断确定，并非通用公开标准。

## Evidence

[质询]该陈述将‘标价/成交中位数比’（Price Ratio）直接定义为平台排序算法中影响曝光量的核心敏感度系数 β_exposure 的输入变量，并断言 Exposure = f(β_exposure * Price_Ratio)。然而，主流电商或广告平台的排序算法（如参考来源[1]提到的 eCPM 机制）通常基于预估点击率（pCTR）、预估转化率（pCVR）、出价（Bid）或综合质量分进行排序，‘标价/成交中位数比’并非通用的标准排序因子，且其具体数值 β_exposure 通常不公开，属于黑盒参数。该陈述可能混淆了特定内部实验指标与通用平台算法逻辑，或者将相关性（价格影响曝光）错误地具体化为一个未经验证的线性/函数关系模型。 | 参考来源[1]仅描述了海外广告平台基于 eCPM 的竞价原理，未提及‘标价/成交中位数比’作为排序因子，也未提供 β_exposure 的具体数值或确定方法，属于无关来源；该陈述为经验性假设，缺乏直接来源支持，且具体算法参数属于黑盒经验事实，无法从第一性原理推导，故降级。

## Search Query

platform algorithm exposure sensitivity price to median ratio coefficient

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1986800026312267022&rut=57f83c0230ebf7da325d219e685a1320a72af39d8525554584ded93235eff057', 'type': 'ddg', 'title': '海外广告平台竞价原理 - 知乎专栏'}
