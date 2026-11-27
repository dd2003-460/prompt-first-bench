# N12: 信息结构 I1：平台显示的历史成交价分布为右偏分布，均值 μ_hist = P_ask_avg / 1.2，标准差 σ_hist = 0.1·P_ask_avg

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N2

## Claim

信息结构 I1：平台显示的历史成交价分布为右偏分布，均值 μ_hist = P_ask_avg / 1.2，标准差 σ_hist = 0.1·P_ask_avg，买家基于此分布更新信念，高挂价落在分布上尾 90% 分位以上时，买家信任度下降 30%。

## Corrected Claim

信息结构 I1：平台显示的历史成交价分布为右偏分布，其均值与标准差及买家信任度变化系数需依据具体市场数据或模型假设确定，而非固定为 P_ask_avg/1.2、0.1·P_ask_avg 及 30% 下降。

## Evidence

[质询]该陈述包含具体的经验性参数（如均值与问价的比例1.2、标准差系数0.1、信任度下降30%），这些并非数学公理或第一性原理可推导的必然结论，而是依赖于特定市场行为或模型假设的经验事实。参考来源仅涉及Python数据分析工具和量化交易的一般性理论，未提供该特定信息结构I1的参数支持或验证。 | 逻辑上自洽（右偏分布、均值与标准差定义清晰），但属于经验事实，参考来源[1][2]仅涉及数据分析方法，未直接支持该特定参数设定，故降级。

## Search Query

historical price distribution skewness buyer trust threshold online marketplace

## Retrieval Sources

- {'url': 'https://developer.baidu.com/article/detail.html?id=3716548&rut=fa2d723ae86cf3751c6504230f1722ace62ed89e843556b9e196db538f6ef45b', 'type': 'ddg', 'title': 'Python数据分析实战：价格分布可视化与总额计算指南-百度开发者中心'}
- {'url': 'https://developer.baidu.com/article/detail.html?id=6067905&rut=f5bc9e45353eb1ca798d1a00c9df623b3ac8f0a67a16c390d35f74c33b3701c6', 'type': 'ddg', 'title': 'Python量化交易：单因子有效性分析之信息分析全解析-百度开发者中心'}
