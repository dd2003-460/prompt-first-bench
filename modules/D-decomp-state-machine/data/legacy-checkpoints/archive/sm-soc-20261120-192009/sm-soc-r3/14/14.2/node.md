# N356: 买家容忍度 S_buyer 的实证计算：S_buyer = P(Buy | Price > Median) / P(Buy | Price = Median)；

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N121

## Claim

买家容忍度 S_buyer 的实证计算：S_buyer = P(Buy | Price > Median) / P(Buy | Price = Median)；若 S_buyer > 1.2，则表明买家对溢价有显著容忍度，可能是由于信息不对称或品牌溢价效应。

## Corrected Claim

买家容忍度 S_buyer 可定义为 P(Buy | Price > Median) / P(Buy | Price = Median)；若该值显著大于 1，表明买家对溢价有一定容忍度，具体阈值（如 1.2）需依据特定市场实证数据确定。

## Evidence

[质询]该陈述定义了一个特定的实证指标 S_buyer 并设定了阈值 1.2，这属于具体的经验性研究结论或特定模型参数，无法从第一性原理推导，且参考来源均未涉及此特定指标的定义或阈值。 | 逻辑上该比率定义自洽（衡量溢价下的购买概率相对于中位价购买概率的倍数），但参考来源 [1][2][3] 均为房地产交易通用指南或政策介绍，与该特定实证指标无关，属于经验事实且缺乏来源支持。

## Search Query

buyer willingness to pay premium second-hand market empirical

## Retrieval Sources

- {'url': 'https://eforms.com/purchase-agreements/&rut=abc366bf8b439d4421f1e7e196ce65f402531ffd22703bb7da15393d5be2a9ef', 'type': 'ddg', 'title': 'Free Purchase and Sale Agreement Template - PDF | Word - eForms'}
- {'url': 'https://www.commbank.com.au/home-loans/australian-government-help-to-buy-scheme.html&rut=309f4efe559322d65492200ea98146b21f022f6538c28344c82a33fc26445d7b', 'type': 'ddg', 'title': 'Australian Government Help to Buy Scheme - CommBank'}
- {'url': 'https://www.realtor.com/advice/buy/what-does-buying-a-foreclosed-home-entail/&rut=ffd9bf6499704b69f2a717512f94aef960b45e522380326f7750aa3313a65660', 'type': 'ddg', 'title': 'Buying a Foreclosed Home: How a Foreclosure Sale Works'}
