# N166: 在 Top 10% 对象工作点，阈值 S_10% 需通过数值积分计算，假设截断 Pareto 分布，B_top_10% = [∫_{S_10%}^{S_max}

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

在 Top 10% 对象工作点，阈值 S_10% 需通过数值积分计算，假设截断 Pareto 分布，B_top_10% = [∫_{S_10%}^{S_max} s f(s) ds] / [∫_{S_min}^{S_max} s f(s) ds]，由于 α=1.1 < 2，字节占比高度集中于头部，预计 B_top_10% > 50%

## Corrected Claim

在 Top 10% 对象工作点，阈值 S_10% 需通过数值积分计算，假设截断 Pareto 分布，B_top_10% = [∫_{S_10%}^{S_max} s f(s) ds] / [∫_{S_min}^{S_max} s f(s) ds]，由于 α=1.1 < 2，字节占比倾向于集中于头部，具体 B_top_10% 数值需根据 S_min 和 S_max 确定，通常显著高于 10%。

## Evidence

[质询]参考来源均讨论分类模型阈值调优（Precision-Recall/ROC），与对象存储/数据分布的Pareto字节占比计算完全无关，无法提供外部支持；且'预计 B_top_10% > 50%'为经验性预测，缺乏具体分布参数（如S_min, S_max）下的严格数学证明，仅凭α=1.1<2不能在所有截断区间下保证该不等式恒成立（取决于截断点位置）。 | 逻辑上，Pareto分布(α=1.1)具有重尾特性，头部对象确实占据大部分字节，公式定义正确；但参考来源[1][2]均与主题无关，无法提供直接支持，且具体数值结论(>50%)依赖于未给出的截断参数，属于经验事实且缺来源支持。

## Search Query

truncated Pareto distribution cumulative byte share top 10 percent

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/564987291&rut=9f3592870e39a4d8cf4f608f7517b85f8ed623cc0b647c7ba97c83f28f6cb587', 'type': 'ddg', 'title': '使用阈值调优改进分类模型性能 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/712241812&rut=d49e44f11611dfd7bda2a6d330d3a588edf54d750eba2fa00ebfb4be23eaa0a4', 'type': 'ddg', 'title': '如何确定数据分析指标的阈值 - 知乎'}
