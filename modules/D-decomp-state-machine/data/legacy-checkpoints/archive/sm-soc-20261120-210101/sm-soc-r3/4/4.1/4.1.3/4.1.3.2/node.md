# N274: 窗口扩展对偏离度偏差 ΔD_window 的量化：计算近7天均价 P_7d 与近30天加权均价 P_30d 的相对差异分布。ΔD_window = |P_7d 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75

## Claim

窗口扩展对偏离度偏差 ΔD_window 的量化：计算近7天均价 P_7d 与近30天加权均价 P_30d 的相对差异分布。ΔD_window = |P_7d - P_30d| / P_30d。若 ΔD_window 的 90 分位数 > 5%，则使用 7 天窗口会导致 CTR' 预测误差增加约 5% * k。

## Corrected Claim

窗口扩展对偏离度偏差 ΔD_window 的量化：计算近7天均价 P_7d 与近30天加权均价 P_30d 的相对差异分布。ΔD_window = |P_7d - P_30d| / P_30d。若 ΔD_window 的 90 分位数 > 5%，则表明近期价格波动显著，可能影响基于近期数据的预测模型稳定性，具体对 CTR' 预测误差的影响需结合具体模型系数评估。

## Evidence

[质询]陈述中声称'CTR'预测误差增加约 5% * k'，但前文仅定义了价格偏离度 ΔD_window，未提供价格偏离度与 CTR（点击率）预测误差之间的因果机制或经验系数 k 的定义。将价格波动直接等同于 CTR 预测误差缺乏逻辑推导支持，且 k 为未定义变量，属于经验事实且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持；检索无可用来源，且价格偏离度与 CTR 误差间的定量关系无法从第一性原理推出。

## Search Query

price reference window sensitivity 7 days vs 30 days deviation error
