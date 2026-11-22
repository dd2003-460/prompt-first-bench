# N62: 平台信号放大机制投影1：平台算法将‘快速成交’信号转化为买家效用加成的权重 w_signal，使得 E[U_buyer]_adjusted = E[U_buye

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N13

## Claim

平台信号放大机制投影1：平台算法将‘快速成交’信号转化为买家效用加成的权重 w_signal，使得 E[U_buyer]_adjusted = E[U_buyer] + w_signal * (1/T)。若 w_signal > 0.3，则平台显著放大了短周期的吸引力，间接鼓励卖家维持高挂价以换取快速成交标签。

## Corrected Claim

平台算法可能通过赋予‘快速成交’信号正权重（w_signal > 0）来增加买家效用，从而间接鼓励卖家策略调整，但具体权重阈值及效用函数形式需依据特定平台数据或研究确定。

## Evidence

[质询]该陈述包含具体的经验性阈值（w_signal > 0.3）和特定的效用函数形式（线性加成 1/T），这属于平台内部算法的具体实现细节或特定研究结论，无法从第一性原理或通用逻辑中严格推导出来，且缺乏外部来源支持该特定数值阈值的有效性。 | source=knowledge，逻辑结构自洽（效用加成机制在理论上可行），但具体阈值 0.3 及线性关系属于经验事实/特定模型假设，缺乏来源直接支持，依据经验事实排除条款降级。
