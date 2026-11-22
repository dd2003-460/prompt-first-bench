# N361: 最小干预措施设计：引入 'Price_Fairness_Penalty' 项，当 |P_list - P_median| > 15% 时，对曝光得分施加线性惩罚

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

最小干预措施设计：引入 'Price_Fairness_Penalty' 项，当 |P_list - P_median| > 15% 时，对曝光得分施加线性惩罚，惩罚系数 λ_penalty 设定为 0.1。模拟显示，该干预可将平均溢价率从 20% 降至 10%，同时将成交周期从 5 天延长至 7 天，边际成本最低且无需重构核心排序算法。

## Corrected Claim

引入 'Price_Fairness_Penalty' 项，当 |P_list - P_median| > 15% 时，对曝光得分施加线性惩罚（系数 λ_penalty 设定为 0.1）。理论上该干预旨在降低平均溢价率并可能延长成交周期，具体效果需通过模拟验证。

## Evidence

[质询]该陈述包含具体的模拟结果数值（溢价率从20%降至10%，成交周期从5天延长至7天）及特定参数设定（λ=0.1），属于经验事实/模拟实验结果，无法从第一性原理推导，且参考来源完全无关，缺乏外部证据支持其具体数值的真实性。 | 参考来源[1]讨论的是DPO算法，与电商定价干预措施完全无关，属于「无可用外部证据」；该陈述为经验事实（模拟结果），逻辑上自洽（惩罚机制导致价格回归中位数但可能降低流动性从而延长周期），但缺乏来源直接支持具体数值，故降级。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1923311375431754217&rut=1b98de90dd97848852058646aa115233fd9b046f3f137d2c0ff7e8f4bbd9dba8', 'type': 'ddg', 'title': '一文读懂 DPO（Direct Preference Optimization）：原理、流程与九种 Loss 解析（附 TRL 实现代码）'}
