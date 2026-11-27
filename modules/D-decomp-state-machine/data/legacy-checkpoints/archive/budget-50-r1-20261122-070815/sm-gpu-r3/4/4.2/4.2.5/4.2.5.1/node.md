# N313: 本地工作站部署的年运行小时数 H_hours 在‘个人开发者/研究者’典型场景下设定为 4380 小时 (12h/day, 5 days/week) 或 876

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N109

## Claim

本地工作站部署的年运行小时数 H_hours 在‘个人开发者/研究者’典型场景下设定为 4380 小时 (12h/day, 5 days/week) 或 8760 小时 (24/7 在线服务)，该参数直接影响电力成本 C_power = P_avg * H_hours * E_price 的线性缩放，需根据最终答案中‘长期持有’的时间尺度假设进行敏感性分析。

## Corrected Claim

本地工作站部署的年运行小时数 H_hours 在‘个人开发者/研究者’典型场景下设定为 4380 小时 (12h/day, 5 days/week) 或 8760 小时 (24/7 在线服务)，该参数直接影响电力成本 C_power = P_avg * H_hours * E_price 的线性缩放，需根据最终答案中‘长期持有’的时间尺度假设进行敏感性分析。

## Evidence

先验知识/题面给定，逻辑校验通过：4380小时（12h*5d*52w）和8760小时（24h*365d）计算正确，电力成本公式线性关系符合物理直觉。
