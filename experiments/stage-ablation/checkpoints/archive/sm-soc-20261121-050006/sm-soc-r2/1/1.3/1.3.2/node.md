# N41: 匹配概率 p_match 的修正公式：引入买家决策摩擦系数 δ_friction，p_match_corrected = Φ((P_max - P_ask)/σ

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

匹配概率 p_match 的修正公式：引入买家决策摩擦系数 δ_friction，p_match_corrected = Φ((P_max - P_ask)/σ_pref) * (1 - δ_friction)，其中 δ_friction 随 P_ask/P_median 比率非线性增加

## Corrected Claim

在特定市场微观结构模型中，匹配概率 p_match 的修正公式可定义为：p_match_corrected = Φ((P_max - P_ask)/σ_pref) * (1 - δ_friction)，其中 δ_friction 为买家决策摩擦系数，且随 P_ask/P_median 比率非线性增加。

## Evidence

[质询]该公式属于特定领域（如二手交易、拍卖或特定市场微观结构）的自定义模型假设，并非通用的经济学或统计学标准公式。参考来源[1]讨论的是心理学/决策论中的概率匹配策略，来源[2]讨论的是法医学中的匹配概率，两者均与该陈述中的“买家决策摩擦系数”及具体公式形式完全无关，无法提供外部支持。 | 逻辑上自洽（Φ函数输出0-1，乘以(1-δ)保持概率范围，δ随价格比率增加符合直觉），但参考来源[1][2]均与该事实主题无关，无可用外部证据支持该特定公式的存在或正确性，属于经验事实/模型假设，故降级。

## Search Query

buyer decision friction coefficient matching probability high price listing nonlinear effect

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Probability_matching&rut=4cc0f9109fd48231b329b9b06f3bd9da45dad4b6ce448a6fab449a1c4065cbf9', 'type': 'ddg', 'title': 'Probability matching - Wikipedia'}
- {'url': 'https://baike.baidu.com/item/%E5%8C%B9%E9%85%8D%E6%A6%82%E7%8E%87/997681&rut=0057a1e84aad13ce5595e6d34621ccdaed09efdf4f7bdec51e6bfe08461de8c9', 'type': 'ddg', 'title': '匹配概率_百度百科'}
