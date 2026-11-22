# N53: 非线性弹性函数具体形式：ε_buyer(ΔP/P) = ε_0 - ε_1 * exp(-k * (ΔP/P - ΔP_threshold)^2)，其中 ε_0

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

非线性弹性函数具体形式：ε_buyer(ΔP/P) = ε_0 - ε_1 * exp(-k * (ΔP/P - ΔP_threshold)^2)，其中 ε_0 ≈ 0.5 为基准弹性，ε_1 ≈ 1.0 为峰值修正项，ΔP_threshold ≈ 10% 为怀疑触发阈值，k ≈ 50 为曲率系数；该函数在 ΔP/P < 5% 时近似线性弱反应，在 ΔP/P > 10% 时急剧转为强负面反应。

## Corrected Claim

非线性弹性函数的一种可能形式为：ε_buyer(ΔP/P) = ε_0 - ε_1 * exp(-k * (ΔP/P - ΔP_threshold)^2)，其中参数需根据具体市场数据校准，通常设定在 ΔP/P < 5% 时近似线性，在 ΔP/P > 10% 时反应增强。

## Evidence

[质询]该陈述描述的是一个特定的、带有具体参数（ε_0≈0.5, ε_1≈1.0, k≈50等）的自定义非线性弹性函数模型，这属于经验事实或特定模型设定，而非通用的经济学第一性原理或标准公式。参考来源中未包含此特定函数形式及其参数，且来源[2]讨论的是固体力学中的非线性弹性，与经济学需求弹性无关，来源[1]和[3]仅讨论标准弹性定义，无法支持这一特定参数化模型。 | 逻辑上该函数形式自洽（高斯型修正项在阈值处产生峰值影响，符合‘怀疑触发’的直觉描述），但作为经验事实/特定模型参数，缺乏参考来源的直接支持（来源[1][3]仅涉及标准弹性，来源[2]领域不匹配），故降级。

## Search Query

nonlinear price elasticity consumer behavior second hand market

## Retrieval Sources

- {'url': 'https://www.zhihu.com/question/554802736&rut=d50db49e5017e8e62f9fa57b8c2bc8168bd081349ecf1045db1f11259fbccc43', 'type': 'ddg', 'title': '经济学弹性系数公式是怎么得出来的？能用通俗易懂的语言说明一下吗？ - 知乎'}
- {'url': 'https://baike.baidu.com/item/%E9%9D%9E%E7%BA%BF%E6%80%A7%E5%BC%B9%E6%80%A7/54691993&rut=40c2b97709a11002f94729f798279f21e0c4057c0e8b3c39ae47cf83735b3a98', 'type': 'ddg', 'title': '非线性弹性_百度百科'}
- {'url': 'https://zhuanlan.zhihu.com/p/382192746&rut=0908fcc2f385f4a57449d6b921d315ef3ff9f0ebd70bb63028a4c9e770172fe1', 'type': 'ddg', 'title': '【经济学公式大全】微观——弹性 - 知乎'}
