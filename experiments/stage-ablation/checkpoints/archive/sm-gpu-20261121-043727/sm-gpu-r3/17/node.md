# N293: 性价比最优判据量化公式定义：在缺乏硬性延迟指标前提下，定义综合性价比指数 $V = \frac{Throughput_{eff} \times Quality_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比最优判据量化公式定义：在缺乏硬性延迟指标前提下，定义综合性价比指数 $V = \frac{Throughput_{eff} \times Quality_{score}}{TCO_{3yr} + Initial\_Investment \times DiscountRate}$。其中 $Throughput_{eff}$ 为有效 tokens/s，$Quality_{score}$ 为归一化质量得分（基于 N263-N265），$TCO_{3yr}$ 为 3 年总拥有成本。需明确当 $Quality_{score} < 0.95$ 时，$V$ 值应乘以惩罚系数 0.5，以反映质量不可接受的隐性成本。

## Corrected Claim

在缺乏硬性延迟指标前提下，可定义综合性价比指数 V 为有效吞吐与归一化质量得分的乘积除以总拥有成本（含初始投资折现）。具体惩罚机制（如质量低于某阈值时的系数调整）需根据业务场景自定义，无通用标准值。

## Evidence

[质询]该公式为特定场景下的自定义经验公式，缺乏通用标准支持；特别是'Quality_score < 0.95 时乘以 0.5'这一惩罚系数属于任意设定的经验参数，无理论依据或行业共识支持，且来源中未提及此具体阈值和系数。 | 来源[1]和[3]支持性价比评估需综合吞吐、质量/性能与成本（TCO）的多维逻辑，但均未提供该特定公式结构及具体的0.95阈值/0.5惩罚系数，属于间接支持。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/QuickDebug/article/details/163273866&rut=b208b2189d8b46a5c3ae9f2217422284d116683648e10add3cb7c4d9eeb7c210', 'type': 'ddg', 'title': '【Ai模型性价比黄金公式】：20年实战总结的7大评估维度与3类企业选型避坑指南-csdn博客'}
- {'url': 'https://blog.csdn.net/m0_62281625/article/details/159884469&rut=ea1a81b919837c1742ac25e2c352a84b8a41cc35939326042bb2508d086bcf71', 'type': 'ddg', 'title': '多目标优化中的常用评价指标：定义、公式、区别_多目标优化算法评价指标spread-CSDN博客'}
- {'url': 'https://shufe_wechat.xml-journal.net/weixin/article/20245916&rut=e3590eb644ab50801812cd0704d988d59415d9c95c899a85b0116cd507c761df', 'type': 'ddg', 'title': '选择Pareto非劣解最优方案的量化方法:性价比法'}
