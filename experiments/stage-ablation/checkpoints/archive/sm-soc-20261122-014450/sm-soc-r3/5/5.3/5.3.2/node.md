# N95: 选择偏差量化：'主动降价'卖家群体可能存在自选择偏差，即只有预期需求低或商品缺陷概率高的卖家才主动降价。定义偏差系数 B = P(Defective | Act

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N29

## Claim

选择偏差量化：'主动降价'卖家群体可能存在自选择偏差，即只有预期需求低或商品缺陷概率高的卖家才主动降价。定义偏差系数 B = P(Defective | Active_Decrease) / P(Defective | Passive_Decrease)。若 B > 1.5，则 60% 无咨询数据不能直接推广到所有卖家，需修正为 P(No_Inquiry | All_Sellers) = P(No_Inquiry | Active) * P(Active) + P(No_Inquiry | Passive) * P(Passive)。

## Corrected Claim

选择偏差量化：'主动降价'卖家群体可能存在自选择偏差。若存在显著偏差（如偏差系数 B 显著大于 1），则 60% 无咨询数据不能直接推广到所有卖家，需利用全概率公式进行修正：P(No_Inquiry | All_Sellers) = P(No_Inquiry | Active) * P(Active) + P(No_Inquiry | Passive) * P(Passive)。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上是正交的（分别处理分子、分母、权重和敏感性分析），但存在明显的完备性缺失。父节点的核心定义是 B = P(Defective|Active)/P(Defective|Passive)。子节点1和2通过贝叶斯公式展开，引入了 P(Defective) 先验概率。然而，没有子节点明确说明如何获取或估计 P(Defective)（缺陷商品的总体基础概率），也没有说明如何获取 P(Active|Defective) 和 P(Passive|Defective) 这两个关键的条件概率参数。此外，父节点提到的 '60% 无咨询数据' 在子节点中未得到具体的数据映射或验证，子节点4仅讨论了下界计算，未覆盖中间值或完整分布的估计。）

## Search Query

self-selection bias price decrease seller behavior used goods market

## Retrieval Sources

- {'url': 'https://jmsc.tju.edu.cn/jmsc/article/abstract/20260707&rut=75591112eae78b46635a92a71d5cd813e1c04c4045f5b09e53255793727ac9d8', 'type': 'ddg', 'title': '考虑在线评论和自选择偏差的产品线策略研究'}
- {'url': 'https://blog.csdn.net/xiedelong/article/details/110392184&rut=38b224f79be507ee385846e7722f983a2617a1ee65f7530aec4de83f0ffeb5c9', 'type': 'ddg', 'title': '推荐系统中的选择偏差及处理_样本选择偏差-csdn博客'}
- {'url': 'https://jmsc.tju.edu.cn/jmsc/article/pdf/20260707&rut=771071a9db7ee5f3ee1e98d540d3ead8cf1aab9add03071d88ba62d723103563', 'type': 'ddg', 'title': '考虑在线评论和自选择偏差的产品线策略研究'}
