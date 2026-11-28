# N61: 检索Hook的边际收益递减效应：当τ从0.5降低到0.3时，FP_rate从~20%增加到~45%，但拦截的FN（漏报）数量增加有限（因为高置信度错误占比低），

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N21

## Claim

检索Hook的边际收益递减效应：当τ从0.5降低到0.3时，FP_rate从~20%增加到~45%，但拦截的FN（漏报）数量增加有限（因为高置信度错误占比低），导致C_total在τ<0.35后开始上升。转折点τ_min_cost可通过求导dC_total/dτ=0获得，需实测FP(τ)和FN(τ)的经验曲线。

## Corrected Claim

检索Hook的边际收益递减效应：当阈值τ降低时，FP_rate通常会显著增加，而拦截的FN数量增加有限（取决于错误分布），导致C_total在τ低于某临界值后开始上升。转折点τ_min_cost可通过求导dC_total/dτ=0获得，需实测FP(τ)和FN(τ)的经验曲线确定具体数值。

## Evidence

[质询]陈述中包含具体的经验数值（τ从0.5降至0.3时，FP_rate从~20%增至~45%），这些具体参数值属于经验事实，无法从第一性原理推导，且参考来源中完全未提及Hook检测的具体阈值与误报率数据，存在来源缺失风险。 | 逻辑上，降低阈值τ通常会导致召回率提升（FN减少）但精确率下降（FP增加），总成本C_total存在最优平衡点是符合检测理论的基本直觉；但具体数值缺乏来源支持，且参考来源[1]讨论的是用户习惯模型而非安全Hook，[2][3]讨论的是强化学习与经济学一般规律，均与该特定技术场景的具体参数无关。

## Search Query

fact checking hook threshold optimization false positive rate cost minimization llm agent

## Retrieval Sources

- {'url': 'https://baike.baidu.com/item/Hook%E6%A8%A1%E5%9E%8B/50912732&rut=054a2309e8b6b8270fa4ac3137a80cc0542a3669d18e1ee90af3c4733f3fa49a', 'type': 'ddg', 'title': 'Hook模型 - 百度百科'}
- {'url': 'https://zhuanlan.zhihu.com/p/2048061989923165953&rut=f63fbfe5528b79f849deb22c0fb9b80474fc5341da9ff39385bdad52db6657fb', 'type': 'ddg', 'title': '强化学习入门（五）：回报与折扣因子——如何衡量长期收益'}
- {'url': 'https://zhuanlan.zhihu.com/p/409418782&rut=0991fd10db05c90ce547200c3ec6ab5af7ebe79b8896fd8c1c82a8b128c1bcf9', 'type': 'ddg', 'title': '8.边际收益递减规律（law of diminishing marginal returns）'}
