# N12: 信息结构 I1：平台显示的历史成交价分布为右偏分布，均值 μ_hist = P_ask_avg / 1.2，标准差 σ_hist = 0.1·P_ask_avg

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

信息结构 I1：平台显示的历史成交价分布为右偏分布，均值 μ_hist = P_ask_avg / 1.2，标准差 σ_hist = 0.1·P_ask_avg，买家基于此分布更新信念，高挂价落在分布上尾 90% 分位以上时，买家信任度下降 30%。

## Corrected Claim

信息结构 I1：平台显示的历史成交价分布为右偏分布，其均值与标准差及买家信任度变化系数需依据具体市场数据或模型假设确定，而非固定为 P_ask_avg/1.2、0.1·P_ask_avg 及 30% 下降。

## Evidence

父节点级核验未通过：不完备（子节点1定义了分布形状（偏度），子节点2定义了信任衰减函数，两者概念正交且不冗余。然而，父节点明确给出了均值和标准差的具体数值定义（μ_hist = P_ask_avg / 1.2, σ_hist = 0.1·P_ask_avg），这两个关键参数在子节点中完全缺失。子节点仅涵盖了分布形状和衰减逻辑，未涵盖分布的中心位置（均值）和离散程度（标准差）的具体定义，导致信息不完整。）

## Search Query

historical price distribution skewness buyer trust threshold online marketplace

## Retrieval Sources

- {'url': 'https://developer.baidu.com/article/detail.html?id=3716548&rut=fa2d723ae86cf3751c6504230f1722ace62ed89e843556b9e196db538f6ef45b', 'type': 'ddg', 'title': 'Python数据分析实战：价格分布可视化与总额计算指南-百度开发者中心'}
- {'url': 'https://developer.baidu.com/article/detail.html?id=6067905&rut=f5bc9e45353eb1ca798d1a00c9df623b3ac8f0a67a16c390d35f74c33b3701c6', 'type': 'ddg', 'title': 'Python量化交易：单因子有效性分析之信息分析全解析-百度开发者中心'}
