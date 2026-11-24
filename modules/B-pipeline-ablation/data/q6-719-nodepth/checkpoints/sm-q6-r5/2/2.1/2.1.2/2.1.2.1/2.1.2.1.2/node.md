# N493: 各 POP 对应的用户流量权重 w_i，基于 N133 的用户地理分布数据（如各省/市 DAU 占比），用于加权平均计算全局平均传播延迟 L_propagati

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N158

## Claim

各 POP 对应的用户流量权重 w_i，基于 N133 的用户地理分布数据（如各省/市 DAU 占比），用于加权平均计算全局平均传播延迟 L_propagation_avg = Σ(w_i * D_i / 300,000 km/s * 1000)。

## Corrected Claim

各 POP 对应的用户流量权重 w_i，基于 N133 的用户地理分布数据（如各省/市 DAU 占比），用于加权平均计算全局平均传播延迟 L_propagation_avg = Σ(w_i * D_i / 300,000 km/s * 1000)。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合加权平均定义，光速量级（300,000 km/s）正确，单位换算（km/s * 1000 转为 ms 或类似时间单位）逻辑自洽。
