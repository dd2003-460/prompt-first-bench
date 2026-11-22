# N95: 选择偏差量化：'主动降价'卖家群体可能存在自选择偏差，即只有预期需求低或商品缺陷概率高的卖家才主动降价。定义偏差系数 B = P(Defective | Act

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29

## Claim

选择偏差量化：'主动降价'卖家群体可能存在自选择偏差，即只有预期需求低或商品缺陷概率高的卖家才主动降价。定义偏差系数 B = P(Defective | Active_Decrease) / P(Defective | Passive_Decrease)。若 B > 1.5，则 60% 无咨询数据不能直接推广到所有卖家，需修正为 P(No_Inquiry | All_Sellers) = P(No_Inquiry | Active) * P(Active) + P(No_Inquiry | Passive) * P(Passive)。

## Corrected Claim

选择偏差量化：'主动降价'卖家群体可能存在自选择偏差。若存在显著偏差（如偏差系数 B 显著大于 1），则 60% 无咨询数据不能直接推广到所有卖家，需利用全概率公式进行修正：P(No_Inquiry | All_Sellers) = P(No_Inquiry | Active) * P(Active) + P(No_Inquiry | Passive) * P(Passive)。

## Evidence

[质询]该陈述将‘主动降价’与‘商品缺陷概率高’直接关联，并设定具体的阈值 B > 1.5 作为修正条件，这属于特定的经验性假设或模型设定，而非普遍成立的逻辑真理或第一性原理。参考来源主要讨论消费者评论自选择偏差或推荐系统偏差，未涉及卖家定价行为与商品缺陷之间的具体量化关系，也未支持 B > 1.5 这一特定阈值。 | 逻辑上全概率公式修正方法自洽，但‘主动降价卖家更可能商品缺陷’及阈值 B>1.5 为经验假设，参考来源 [1][2][3] 仅涉及概念层面的选择偏差，未提供该特定场景下的直接支持或数值依据，故降级。

## Search Query

self-selection bias price decrease seller behavior used goods market

## Retrieval Sources

- {'url': 'https://jmsc.tju.edu.cn/jmsc/article/abstract/20260707&rut=75591112eae78b46635a92a71d5cd813e1c04c4045f5b09e53255793727ac9d8', 'type': 'ddg', 'title': '考虑在线评论和自选择偏差的产品线策略研究'}
- {'url': 'https://blog.csdn.net/xiedelong/article/details/110392184&rut=38b224f79be507ee385846e7722f983a2617a1ee65f7530aec4de83f0ffeb5c9', 'type': 'ddg', 'title': '推荐系统中的选择偏差及处理_样本选择偏差-csdn博客'}
- {'url': 'https://jmsc.tju.edu.cn/jmsc/article/pdf/20260707&rut=771071a9db7ee5f3ee1e98d540d3ead8cf1aab9add03071d88ba62d723103563', 'type': 'ddg', 'title': '考虑在线评论和自选择偏差的产品线策略研究'}
