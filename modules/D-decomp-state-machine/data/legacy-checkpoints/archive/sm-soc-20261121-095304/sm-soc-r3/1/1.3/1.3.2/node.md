# N29: 剩余买家平均成交转化率 p_conv 的提高幅度：Δp_conv = p_conv_high - p_conv_low，其中 p_conv_high 为高定价下

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

剩余买家平均成交转化率 p_conv 的提高幅度：Δp_conv = p_conv_high - p_conv_low，其中 p_conv_high 为高定价下的转化率（通常 15%-25%），p_conv_low 为低定价下的转化率（通常 5%-10%），Δp_conv 通常达到 10%-15 个百分点，是成交周期缩短的主要驱动力。

## Corrected Claim

剩余买家平均成交转化率 p_conv 的变化幅度 Δp_conv 取决于具体的定价策略和市场环境，不同行业和产品类别的转化率区间差异巨大，无法给出通用的 10%-15 个百分点的固定范围。

## Evidence

[质询]该陈述包含具体的经验数值（高定价转化率15%-25%，低定价5%-10%，差值10-15个百分点），这些数值高度依赖于行业、产品类别及具体市场情境，并非普适的物理或数学定律。此外，通常高定价可能伴随更长的决策周期或更低的即时转化率，此处假设高定价下转化率显著高于低定价（或反之，取决于'高/低'指代的是价格高低还是转化高低，语境中'高定价下的转化率'通常指价格高时的转化，但逻辑上价格高通常转化低，这里可能存在因果倒置或特定语境下的反直觉假设，需具体业务背景支持），且参考来源中无相关数据支持。 | 来源[1][2]为计算机视觉卷积算法，与商业转化率无关；来源[3]仅定义转化率概念，未提供具体数值范围或定价与转化率的关系数据。该事实属于特定业务场景下的经验数据，缺乏通用来源支持，且数值范围具有高度情境依赖性。

## Search Query

conversion rate difference high priced vs low priced second hand items

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/9434297458&rut=51d32c9dc3ecea57aed5e895fdfd821231f71a96e0de6353757d35143b165fae', 'type': 'ddg', 'title': '(即插即用模块-Convolution部分) 二、(CVPR 2023) PConv 部分卷积'}
- {'url': 'https://zhuanlan.zhihu.com/p/1966886806768301957&rut=5ce37b3451458cf3fd03a43a3022ca94f219394f587ee3e6892550736df1a00c', 'type': 'ddg', 'title': 'CVPR 即插即用 | PConv：重新定义高效卷积，一个让模型"跑"得更快、更省的新范式 - 知乎'}
- {'url': 'https://baike.baidu.com/item/%E9%94%80%E5%94%AE%E8%BD%AC%E5%8C%96%E7%8E%87/67946148&rut=f0a9e97d2370167888f86dd9627ecf934ec70be158a3768da8c495256ff1c0ca', 'type': 'ddg', 'title': '销售转化率_百度百科'}
