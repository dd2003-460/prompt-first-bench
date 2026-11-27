# N154: β1 的品类异质性检验：将样本按商品品类（如电子、服饰、家具）分组，分别估计 β1_cat；若组间 β1 差异的 F 检验 p < 0.05，则需使用交互项模型

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N46

## Claim

β1 的品类异质性检验：将样本按商品品类（如电子、服饰、家具）分组，分别估计 β1_cat；若组间 β1 差异的 F 检验 p < 0.05，则需使用交互项模型 β1 = β1_base + Σ δ_cat * I_cat，其中 δ_cat 为品类特定调整系数，不可使用单一 β1。

## Corrected Claim

β1 的品类异质性检验：将样本按商品品类（如电子、服饰、家具）分组，分别估计 β1_cat；若组间 β1 差异的 F 检验 p < 0.05，则需使用交互项模型 β1 = β1_base + Σ δ_cat * I_cat，其中 δ_cat 为品类特定调整系数，不可使用单一 β1。

## Evidence

逻辑推导成立，来源未直接覆盖；来源[1][2]确认了异质性检验的基本原理（检验不同子样本间系数差异），支持该统计方法的适用性。

## Search Query

price sensitivity coefficient heterogeneity by category second hand goods logistic regression

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1911807513659151159&rut=84fb0b3cd460772d251612740ff17d7c7642941e4627a404279d489562c6ee75', 'type': 'ddg', 'title': '超级经典丨《管理世界》2025年异质性分析方法大汇总 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/2046240115438235865&rut=53780f8e73739fcd57542ec0c47c6aefcad6c2960319f57eadc7f41a9a0fcd5e', 'type': 'ddg', 'title': '异质性检验基本原理与软件操作教程 - 知乎'}
