# N131: 卖家经验（历史交易次数 N_exp）与噪声 ε_seller 的相关性系数 ρ_exp：预期 ρ_exp ∈ [-0.3, -0.1]（负相关，经验越多噪声越小

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

卖家经验（历史交易次数 N_exp）与噪声 ε_seller 的相关性系数 ρ_exp：预期 ρ_exp ∈ [-0.3, -0.1]（负相关，经验越多噪声越小），需通过 OLS 回归 ε_seller ~ N_exp 的 t 统计量检验显著性（p<0.05）。

## Corrected Claim

卖家经验（历史交易次数 N_exp）与噪声 ε_seller 预期呈负相关（经验越多噪声越小），需通过 OLS 回归 ε_seller ~ N_exp 的 t 统计量检验显著性（p<0.05）。具体相关系数范围需根据实际数据回归结果确定。

## Evidence

[质询]该陈述包含具体的经验性数值预期（ρ_exp ∈ [-0.3, -0.1]），这属于特定市场或模型设定下的经验事实，无法从第一性原理或通用统计逻辑中严格推导得出，且参考来源未提供该具体数值范围的支持。 | 逻辑上，经验增加导致噪声降低（负相关）符合直觉，OLS t检验也是标准方法；但参考来源[1][2][3]仅涉及时间序列基础、假设检验通用原理及白噪声模型，均未覆盖‘卖家经验与噪声相关性’这一具体业务场景或提供[-0.3, -0.1]的数值依据，属于经验事实缺来源支持。

## Search Query

correlation between seller experience and pricing noise reduction C2C platform

## Retrieval Sources

- {'url': 'https://qihongruan.github.io/tsay-time-series/chapters/ch02.html&rut=f6e13900fc1c3f0f99822f43d6ae4a59de479d698a6a420a2d894ba2a250b28a', 'type': 'ddg', 'title': '第2章 线性时间序列分析及其应用 — 金融时间序列分析笔记'}
- {'url': 'https://si-xiaoming.github.io/quant-trade-tutorial/01_financial_concepts/06_statistics_fundamentals/&rut=232a3e714eb729c2079d4496797add4247cb60e34a1db8a333ce583a8786beb8', 'type': 'ddg', 'title': '1.6 统计学基础与假设检验 - 量化交易从零到一'}
- {'url': 'https://quant.10jqka.com.cn/view/article/1516&rut=a0faccaac54d88b505dee7e35299577fc94a182edd2148be56bcb4fe759769ff', 'type': 'ddg', 'title': '时间序列分析：白噪声模型与随机漫步模型 - 10jqka.com.cn'}
