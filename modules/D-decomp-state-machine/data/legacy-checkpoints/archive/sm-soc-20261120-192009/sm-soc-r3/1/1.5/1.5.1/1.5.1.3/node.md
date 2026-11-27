# N164: 异质性量化指标：不同商品的信息更新速度异质性可用变异系数 CV_speed = σ_speed / μ_speed 衡量，若 CV_speed > 0.5，则需

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N49

## Claim

异质性量化指标：不同商品的信息更新速度异质性可用变异系数 CV_speed = σ_speed / μ_speed 衡量，若 CV_speed > 0.5，则需引入商品类别特征作为协变量修正 info_quality(t) 曲线，而非使用统一随机源。

## Corrected Claim

异质性量化指标：不同商品的信息更新速度异质性可用变异系数 CV_speed = σ_speed / μ_speed 衡量。当 CV_speed 较高（如超过特定经验阈值）时，建议引入商品类别特征作为协变量以修正 info_quality(t) 曲线，而非使用统一随机源。

## Evidence

[质询]该陈述中的具体阈值（CV_speed > 0.5）及后续处理策略（引入商品类别特征作为协变量修正 info_quality(t) 曲线）属于特定领域（如金融时间序列或推荐系统）的经验性建模规则，并非通用的统计学第一性原理或数学公理。参考来源仅提供了变异系数的通用定义和异质性检验的背景，未提供该特定阈值或特定修正方法的直接支持。 | 逻辑自洽（变异系数用于衡量离散程度合理），但属于经验事实，参考来源[1][2]仅间接支持变异系数的概念，未直接支持具体的阈值0.5及特定的协变量修正策略，故降级。

## Search Query

information diffusion heterogeneity variance coefficient

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/660482823&rut=2e6b1e9f08a2b40705d56001c0e61f93aec6e2bbf1cfc7fc81a4529bb8e64988', 'type': 'ddg', 'title': 'meta分析中异质性检验指标如何计算？ - 知乎'}
- {'url': 'https://wenku.baidu.com/noteview/ea0b77cb22fff705cc1755270722192e45365812.html&rut=a82956ab97f46a8abf9cc9e9a20f15947d7d843fe05281d909a90aec256cfa1d', 'type': 'ddg', 'title': '变异系数范围标准解读：通用标准与应用指南'}
