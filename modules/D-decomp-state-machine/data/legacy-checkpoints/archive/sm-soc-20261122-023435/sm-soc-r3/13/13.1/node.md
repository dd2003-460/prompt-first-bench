# N260: 定向压力项 P_dir 的具体形式：P_dir(t) = k_t * t * (SP - 1)，其中 k_t 为压力转化系数，SP 为生存压力指数。当 SP >

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N85

## Claim

定向压力项 P_dir 的具体形式：P_dir(t) = k_t * t * (SP - 1)，其中 k_t 为压力转化系数，SP 为生存压力指数。当 SP > 1 时，P_dir 为正，推动挂价向均值回归；当 SP < 1 时，P_dir 为负或零，卖家维持高价策略。k_t 的估计值通常在 0.05-0.15 /天 之间，取决于市场流动性。

## Corrected Claim

定向压力项 P_dir 的形式可表示为 P_dir(t) = k_t * t * (SP - 1)，其中 k_t 为压力转化系数，SP 为生存压力指数。当 SP > 1 时，P_dir 为正，推动挂价向均值回归；当 SP < 1 时，P_dir 为负或零，卖家维持高价策略。k_t 的具体数值取决于市场流动性及模型设定，常见估计值在 0.05-0.15 /天 之间。

## Evidence

[质询]该公式及参数范围（k_t 0.05-0.15 /天）属于特定模型假设或经验拟合值，缺乏通用理论推导支持，且不同市场环境下系数可能差异巨大，存在将特定场景参数泛化为通用规律的风险。 | source=knowledge，逻辑自洽（SP>1时P_dir>0推动回归，SP<1时P_dir<=0维持高价，量纲与方向合理），但无外部来源支持具体数值范围，依据经验事实排除条款降级。

## Search Query

dynamic pricing pressure coefficient inventory holding time
