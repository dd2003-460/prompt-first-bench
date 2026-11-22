# N90: 尾部风险权重 λ 的实证校准：在二手交易场景中，卖家对‘交易失败’或‘商品瑕疵被拒收’的尾部风险厌恶系数 λ_tail 可通过反事实选择实验估计；假设卖家在 (

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

尾部风险权重 λ 的实证校准：在二手交易场景中，卖家对‘交易失败’或‘商品瑕疵被拒收’的尾部风险厌恶系数 λ_tail 可通过反事实选择实验估计；假设卖家在 (P_high, q_low) 和 (P_low, q_high) 之间选择，通过最大似然法估计 λ_tail，通常发现 λ_tail 显著高于一般风险厌恶系数（约为 2-3 倍），表明卖家对极端负面结果的惩罚权重更高。

## Corrected Claim

在二手交易场景中，卖家对‘交易失败’或‘商品瑕疵被拒收’的尾部风险厌恶系数 λ_tail 可通过反事实选择实验估计；理论及一般行为经济学证据表明，卖家对极端负面结果的惩罚权重通常高于一般风险厌恶系数，但具体倍数（如 2-3 倍）需依赖特定场景的实证数据支持。

## Evidence

[质询]该陈述包含具体的实证结论（λ_tail 约为一般风险厌恶系数的 2-3 倍）和特定的实验设计（二手交易场景下的反事实选择实验），属于经验事实。参考来源主要讨论金融风控模型和金融市场尾部风险管理，未涉及二手交易场景或提供该具体倍数关系的实证数据，存在领域不匹配和具体数值缺乏直接证据的风险。 | 逻辑上，行为经济学中损失厌恶（Loss Aversion）确实通常高于一般风险厌恶，且尾部风险厌恶在特定情境下可能更高，量级合理；但参考来源 [1][3] 仅讨论金融风控和金融市场，与二手交易场景无关，无法直接支持该具体实证结论，故降级。

## Search Query

empirical calibration of tail risk aversion lambda in consumer choice experiments second-hand market

## Retrieval Sources

- {'url': 'https://blog.csdn.net/FuncInk/article/details/155970196&rut=25b9ba16f0dd98eed6d4e423dc0f2b2c259c070351f159e03e40b3b90d788de2', 'type': 'ddg', 'title': '为什么90%的风控模型失败？R语言实证分析揭示被忽略的尾部风险-csdn博客'}
- {'url': 'https://d.wanfangdata.com.cn/thesis/D02602299&rut=6e62a0e676609e9a442cd5a276480920c17043f78f349bd5ef3aed56fb5bebcc', 'type': 'ddg', 'title': '万方数据知识服务平台'}
- {'url': 'https://blog.csdn.net/weixin_42602368/article/details/167860680&rut=b66502f5ccc118c7e194d50bb805f4f43e3ec2cac8858a9d01afce78904ce3da', 'type': 'ddg', 'title': '金融市场尾部风险管理：识别、量化与对冲策略-csdn博客'}
