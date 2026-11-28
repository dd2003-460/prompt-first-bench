# N23: 时间尺度外推误差（Prediction Horizon）：现有衰减速率统计基于 0-24h 登陆后窗口，超过 48h 的预测中，由于环境场演变（如冷舌形成）的非

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

时间尺度外推误差（Prediction Horizon）：现有衰减速率统计基于 0-24h 登陆后窗口，超过 48h 的预测中，由于环境场演变（如冷舌形成）的非线性反馈，衰减速率估计的不确定度（RMSE）从 ~5 kt/h 上升至 >10 kt/h，需明确标注适用时间窗口限制。

## Corrected Claim

时间尺度外推误差（Prediction Horizon）：现有衰减速率统计通常基于较短的时间窗口（如0-24h），随着预测时间延长（如超过48h），由于环境场演变（如冷舌形成）的非线性反馈，衰减速率估计的不确定度通常会显著增加，需明确标注适用时间窗口限制。

## Evidence

[质询]具体数值（RMSE从~5 kt/h上升至>10 kt/h）及特定时间窗口（0-24h vs >48h）缺乏通用文献支持，属于特定研究或模型的经验性结论，易被质疑为过度精确或特定场景下的局部最优解而非普遍规律。 | 参考来源[1]讨论的是控制理论中的移动视界观测器，与台风衰减预测的具体气象统计数值完全无关，无可用外部证据；该陈述作为经验事实，逻辑上符合非线性系统预测误差随时间增加而放大的直觉，但缺乏来源直接支持具体数值，故降级。

## Search Query

tropical cyclone post-landfall forecast error growth time horizon 48h

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/621671145&rut=fd5b49dd8cf548d9f768fefddee208aee5d7f7f590411c1b0b8664e5d9315fb3', 'type': 'ddg', 'title': '模型预测观测器moving horizon observer - 知乎'}
