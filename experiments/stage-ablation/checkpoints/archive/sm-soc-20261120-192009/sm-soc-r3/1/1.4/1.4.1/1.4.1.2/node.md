# N151: 买家异质性维度量化：σ_buyer² 可分解为专业程度（Expertise_level）和信息获取能力（Info_access）两个子维度的方差和；Expert

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N45

## Claim

买家异质性维度量化：σ_buyer² 可分解为专业程度（Expertise_level）和信息获取能力（Info_access）两个子维度的方差和；Expertise_level 可用历史交易成功率或品类浏览深度代理，Info_access 可用设备类型和网络稳定性代理；需通过因子分析确定两个维度的载荷系数。

## Corrected Claim

买家异质性维度量化：σ_buyer² 可分解为多个子维度的方差和；在具体模型中，可考虑将专业程度（Expertise_level）和信息获取能力（Info_access）作为潜在维度，并分别使用历史交易成功率/品类浏览深度、设备类型/网络稳定性作为代理变量；需通过因子分析或主成分分析确定各维度的载荷系数及解释力。

## Evidence

[质询]该陈述将买家异质性方差分解为‘专业程度’和‘信息获取能力’两个特定子维度，并指定了具体的代理变量（如历史交易成功率、设备类型），这属于特定的模型设定或经验假设，而非通用的统计事实或第一性原理推导。参考来源仅讨论了异质性分析的一般方法论（如分组回归、交互项），并未支持这一特定的二维分解结构或代理变量选择。 | 逻辑上自洽（方差分解在数学上可行，代理变量在经济学中常见），但参考来源[1][2][3]仅涉及异质性分析的一般方法，未直接支持该特定的维度分解和代理变量设定，属于经验事实且缺乏直接来源支持。

## Search Query

buyer heterogeneity factor analysis expertise information access second hand trading

## Retrieval Sources

- {'url': 'https://newetds.lib.tsinghua.edu.cn/qh/paper/summary?dbCode=ETDQH&sysId=277199&rut=375e002c04c5c0ee6ee1907f20b25f4c78d179c1539f277639df0795d008e9ad', 'type': 'ddg', 'title': '清华大学学位论文服务系统'}
- {'url': 'https://zhuanlan.zhihu.com/p/1916813112276935509&rut=20433bd849d88a945faffdbac43e1a31859760dee88c539f8ba06afa7d395f0f', 'type': 'ddg', 'title': '硬核干货丨《数量经济技术经济研究》最新异质性分析方法汇总'}
- {'url': 'https://zhuanlan.zhihu.com/p/1918684785267671854&rut=9e5757437ed24d7deed4d2288d6b5e218353e33f965673897e134afa1f15c628', 'type': 'ddg', 'title': '最新更新丨《经济研究》异质性分析方法汇总 - 知乎'}
