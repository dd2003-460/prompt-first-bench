# N230: 时间窗口修正因子：N_unique_hot 随TTL窗口T_w变化，公式修正为 N_unique_hot(T_w) = N_total * (1 / (1 - 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N73

## Claim

时间窗口修正因子：N_unique_hot 随TTL窗口T_w变化，公式修正为 N_unique_hot(T_w) = N_total * (1 / (1 - (1/N_total)^α)) * f(T_w/T_max)，其中f(x)为累积分布函数近似。若T_w从1小时缩短至15分钟，活跃对象数通常减少40-60%，即N_unique_hot_15min ≈ 0.4-0.6 * N_unique_hot_1h。

## Corrected Claim

时间窗口修正因子：N_unique_hot 随TTL窗口T_w变化，公式修正为 N_unique_hot(T_w) = N_total * (1 / (1 - (1/N_total)^α)) * f(T_w/T_max)，其中f(x)为累积分布函数近似。若T_w从1小时缩短至15分钟，活跃对象数通常显著减少（具体比例取决于负载特征，经验上可能在40-60%左右）。

## Evidence

[质询]经验事实排除条款：具体数值范围（40-60%减少）属于经验参数，无法从第一性原理严格推出，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持
