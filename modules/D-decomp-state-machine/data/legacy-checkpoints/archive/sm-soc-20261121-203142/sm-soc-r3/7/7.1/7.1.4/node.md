# N281: 咨询量增加函数 h(x) 的线性近似斜率 k_linear：假设在 ΔP 刚超过 ε 的区间内，咨询量增加与降价幅度呈线性关系 Increase = k_lin

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N95, N96, N97

## Claim

咨询量增加函数 h(x) 的线性近似斜率 k_linear：假设在 ΔP 刚超过 ε 的区间内，咨询量增加与降价幅度呈线性关系 Increase = k_linear * (ΔP - ε)，需通过 A/B 测试数据拟合 k_linear 的具体数值（如每降价1%带来的咨询量增量）。

## Corrected Claim

在ΔP刚超过ε的区间内，咨询量增加与降价幅度呈线性关系 Increase = k_linear * (ΔP - ε) 是一种常用的线性近似假设，k_linear 的具体数值需通过 A/B 测试数据拟合确定。

## Evidence

[质询]该陈述描述的是一个特定业务场景下的经验性模型假设（咨询量与降价幅度的线性关系及阈值效应），属于经验事实而非第一性原理可推导的数学或物理定律。参考来源[1]讨论的是公务员考试资料分析中的数学计算技巧（假设法求增量），与电商/咨询业务中的价格弹性或A/B测试拟合完全无关，无法提供外部支持。 | 逻辑上，在阈值附近使用线性近似是常见的工程简化方法，量纲和逻辑自洽；但参考来源[1]与该事实主题无关，且该事实属于经验性业务假设，缺乏直接来源支持，故降级。

## Search Query

price discount impact on inquiry volume linear elasticity A/B test

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/144472919&rut=a4202e5a1196ae292d6bac32efbb6c7dfe80e42b10b9ba800fa232bb7b86e727', 'type': 'ddg', 'title': '资料分析技巧之假设法求增量 - 知乎'}
