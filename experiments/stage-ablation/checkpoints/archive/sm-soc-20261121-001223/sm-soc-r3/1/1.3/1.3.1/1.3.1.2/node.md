# N102: 系数 k 的品类异质性修正项：k_category = k_base * (1 + γ_category)，其中 γ_category 为品类特定调整因子（如电

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33, N34, N35

## Claim

系数 k 的品类异质性修正项：k_category = k_base * (1 + γ_category)，其中 γ_category 为品类特定调整因子（如电子产品 γ=-0.1，奢侈品 γ=+0.2），需通过分类别回归验证 γ 的显著性（t>2）。

## Corrected Claim

系数 k 的品类异质性修正项可采用 k_category = k_base * (1 + γ_category) 的形式，其中 γ_category 为品类特定调整因子，需通过分类别回归或交互项模型验证 γ 的统计显著性。

## Evidence

[质询]该陈述包含具体的经验参数（如电子产品γ=-0.1，奢侈品γ=+0.2）和特定的统计阈值（t>2），这些属于经验事实或具体模型设定，无法从第一性原理推导，且参考来源仅讨论异质性分析的一般方法论（分组回归、交互项），未提供具体的品类系数数值或验证标准。 | 逻辑自洽，但参考来源[1][2]仅支持异质性分析的方法论框架（如交互项/分组回归），未直接支持具体的γ数值或t值阈值，属于经验事实缺来源支持。

## Search Query

category heterogeneity pricing coefficient used electronics luxury goods regression gamma

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1971974865654359133&rut=1d7dcc665930edc824089ef8ac1a693c99bc997af2487ba3bd3a76e1c770e7b2', 'type': 'ddg', 'title': '【原理到实战】实验异质性分析 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/1918684785267671854&rut=9e5757437ed24d7deed4d2288d6b5e218353e33f965673897e134afa1f15c628', 'type': 'ddg', 'title': '最新更新丨《经济研究》异质性分析方法汇总 - 知乎'}
