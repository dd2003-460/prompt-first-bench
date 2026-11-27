# N40: 投影2（低曝光池降权机制）：降价后落入低曝光池的曝光衰减率 Decay_low = 1 - β_low * max(0, 1.15 - P_ask/P_mark

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N9

## Claim

投影2（低曝光池降权机制）：降价后落入低曝光池的曝光衰减率 Decay_low = 1 - β_low * max(0, 1.15 - P_ask/P_market)，其中 β_low 为降权系数，需验证 β_low 是否大于 0.5 以解释 60% 无咨询现象中的曝光缺失部分。

## Corrected Claim

投影2（低曝光池降权机制）：假设存在降价后落入低曝光池的曝光衰减机制，其衰减率可能由降权系数β_low及价格相对市场价的偏离程度决定，需进一步实证验证β_low的具体数值及其对曝光缺失的解释力。

## Evidence

[质询]该陈述包含具体的经验性参数（如阈值1.15、系数β_low>0.5）和特定的业务现象解释（60%无咨询），属于经验事实而非第一性原理可推导内容，且参考来源完全无关，无法验证其数值合理性和因果解释的有效性。 | 参考来源[1]主题为AI写作降重，与电商曝光机制完全无关，无可用外部证据；该事实为经验性模型假设，逻辑自洽但缺乏来源支持，依据经验事实排除条款降级。

## Search Query

marketplace price drop algorithm penalty exposure reduction beta coefficient

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2018325997737485417&rut=aa5ea07aa78bef25f79a7d34106416748a3b588f02d97343e3a02f034ae0ac67', 'type': 'ddg', 'title': '降ai率90%→7%，DeepSeek 4大免费降ai率指令+3款降ai率工具实测（保姆级教程） - 知乎'}
